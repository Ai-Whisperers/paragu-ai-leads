"""
ParaguAI WhatsApp CRM - Backend API v1
FastAPI server for lead management and WhatsApp integration
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
import os, logging, re, csv
from pathlib import Path

from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
WHATSAPP_BRIDGE_URL = os.getenv("WHATSAPP_BRIDGE_URL", "http://localhost:3007")
PORT = int(os.getenv("CRM_PORT", "3042"))

# Supabase client
supabase: Optional[Client] = None
if SUPABASE_URL and SUPABASE_KEY:
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        logger.info(f"✅ Supabase connected")
    except Exception as e:
        logger.warning(f"⚠️  Supabase init failed: {e}")
else:
    logger.warning("⚠️  Supabase not configured — running in demo mode")

# FastAPI app
app = FastAPI(title="ParaguAI CRM API", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# Models
class MessageCreate(BaseModel):
    lead_id: str
    direction: str = Field(..., pattern="^(outbound|inbound)$")
    content: str
    status: str = "sent"
    external_id: Optional[str] = None

class LeadUpdate(BaseModel):
    status: Optional[str] = None
    notes: Optional[str] = None
    contact_name: Optional[str] = None

# CSV Loader
def load_csv_leads():
    csv_path = Path(__file__).parent.parent.parent / "outreach" / "OUTREACH_TRACKER.csv"
    if not csv_path.exists():
        logger.warning(f"CSV not found: {csv_path}")
        return []
    leads = []
    with open(csv_path, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            review_str = row.get("response", "") or ""
            review_match = re.search(r'(\d+)\s*(?:reviews|reseñas)', review_str, re.IGNORECASE)
            reviews = int(review_match.group(1)) if review_match else 0
            raw_status = (row.get("status", "") or "").strip().upper()
            status_map = {
                "OUTREACH SENT": "contacted",
                "RESPONDED": "responding",
                "CONVERTED": "converted",
                "NO RESPONSE": "new",
            }
            leads.append({
                "id": row.get("lead_id", ""),
                "business_name": row.get("business_name", ""),
                "contact_name": row.get("contact_name", ""),
                "whatsapp_number": (row.get("whatsapp", "") or "").replace("wa.me/", ""),
                "rating": None,
                "reviews": reviews,
                "score": float(row.get("score", 0) or 0),
                "status": status_map.get(raw_status, "contacted"),
                "address": row.get("location", ""),
                "last_contact": row.get("round_1_date", ""),
                "notes": row.get("notes", "") or row.get("response", "") or ""
            })
    return leads

# Routes
frontend_path = Path(__file__).parent.parent / "frontend"

@app.get("/")
async def root():
    p = frontend_path / "dashboard.html"
    if p.exists():
        with open(p, encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return {"message": "Go to /dashboard.html"}

@app.get("/dashboard.html")
async def dashboard():
    p = frontend_path / "dashboard.html"
    if p.exists():
        with open(p, encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse(content="<h1>Dashboard not found</h1>", status_code=404)

@app.options("/{full_path:path}")
async def options_handler(full_path: str):
    return {"ok": True}

@app.get("/health")
async def health():
    return {"status": "ok", "version": "1.0.0", "supabase": "connected" if supabase else "demo_mode"}

# Leads
@app.get("/api/v1/leads")
async def list_leads(status: Optional[str] = None, search: Optional[str] = None):
    if supabase:
        try:
            query = supabase.table("leads").select("*").order("score", desc=True)
            if status:
                query = query.eq("status", status)
            result = query.execute()
            leads = result.data or []
            if search:
                leads = [l for l in leads if search.lower() in (l.get("business_name") or "").lower()]
            return leads
        except Exception as e:
            logger.warning(f"Supabase error: {e}")
    leads = load_csv_leads()
    if status:
        leads = [l for l in leads if l.get("status") == status]
    if search:
        leads = [l for l in leads if search.lower() in (l.get("business_name") or "").lower()]
    return leads

@app.get("/api/v1/leads/{lead_id}")
async def get_lead(lead_id: str):
    if supabase:
        try:
            result = supabase.table("leads").select("*").eq("id", lead_id).execute()
            if result.data:
                return result.data[0]
        except Exception as e:
            logger.warning(f"Supabase error: {e}")
    leads = load_csv_leads()
    lead = next((l for l in leads if l["id"] == lead_id), None)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead

@app.patch("/api/v1/leads/{lead_id}")
async def update_lead(lead_id: str, update: LeadUpdate):
    if supabase:
        try:
            data = {k: v for k, v in update.model_dump().items() if v is not None}
            result = supabase.table("leads").update(data).eq("id", lead_id).execute()
            if result.data:
                return result.data[0]
        except Exception as e:
            logger.warning(f"Supabase error: {e}")
    return {"id": lead_id, **update.model_dump()}

# Messages
@app.get("/api/v1/leads/{lead_id}/messages")
async def get_lead_messages(lead_id: str, limit: int = Query(default=50, le=200)):
    if supabase:
        try:
            result = supabase.table("messages").select("*").eq("lead_id", lead_id).order("created_at").limit(limit).execute()
            return result.data or []
        except Exception as e:
            logger.warning(f"Supabase error: {e}")
    return []

@app.post("/api/v1/messages")
async def create_message(msg: MessageCreate):
    if supabase:
        try:
            data = msg.model_dump()
            data["created_at"] = datetime.now().isoformat()
            result = supabase.table("messages").insert(data).execute()
            if result.data:
                return result.data[0]
        except Exception as e:
            logger.warning(f"Supabase error: {e}")
    return {**msg.model_dump(), "created_at": datetime.now().isoformat()}

# Metrics
@app.get("/api/v1/metrics/summary")
async def get_metrics_summary():
    if supabase:
        try:
            leads_result = supabase.table("leads").select("status").execute()
            msgs_result = supabase.table("messages").select("direction").execute()
            leads_data = leads_result.data or []
            msgs_data = msgs_result.data or []
            return {
                "total_leads": len(leads_data),
                "contacted": sum(1 for l in leads_data if l.get("status") in ("contacted", "responding", "converted")),
                "responded": sum(1 for l in leads_data if l.get("status") in ("responding", "converted")),
                "converted": sum(1 for l in leads_data if l.get("status") == "converted"),
                "outbound_messages": sum(1 for m in msgs_data if m.get("direction") == "outbound"),
                "inbound_messages": sum(1 for m in msgs_data if m.get("direction") == "inbound"),
            }
        except Exception as e:
            logger.warning(f"Supabase error: {e}")
    leads = load_csv_leads()
    return {
        "total_leads": len(leads),
        "contacted": sum(1 for l in leads if l.get("status") in ("contacted", "responding", "converted")),
        "responded": sum(1 for l in leads if l.get("status") in ("responding", "converted")),
        "converted": sum(1 for l in leads if l.get("status") == "converted"),
        "outbound_messages": sum(1 for l in leads if l.get("status") in ("contacted", "responding")),
        "inbound_messages": 0
    }

if __name__ == "__main__":
    import uvicorn
    logger.info(f"🚀 ParaguAI CRM starting on port {PORT}")
    uvicorn.run(app, host="0.0.0.0", port=PORT)