"""
ParaguAI WhatsApp CRM - Backend API
FastAPI server for lead management and WhatsApp integration
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import os
import logging

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

# Initialize Supabase client
if SUPABASE_URL and SUPABASE_KEY:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    logger.info("✅ Supabase connected")
else:
    supabase = None
    logger.warning("⚠️  Supabase not configured — using demo mode")

# FastAPI app
app = FastAPI(
    title="ParaguAI WhatsApp CRM",
    description="CRM backend for WhatsApp outreach management",
    version="1.0.0"
)

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Pydantic Models ───────────────────────────────────────

class LeadCreate(BaseModel):
    business_name: str
    contact_name: Optional[str] = None
    whatsapp_number: str
    wa_chat_id: Optional[str] = None
    score: float = 0
    rating: float = 0
    reviews: int = 0
    source: Optional[str] = None
    location: Optional[str] = None
    notes: Optional[str] = None

class LeadUpdate(BaseModel):
    business_name: Optional[str] = None
    contact_name: Optional[str] = None
    whatsapp_number: Optional[str] = None
    status: Optional[str] = None
    last_contact: Optional[datetime] = None
    next_follow_up: Optional[datetime] = None
    notes: Optional[str] = None

class Lead(LeadCreate):
    id: str
    status: str
    last_contact: Optional[datetime]
    next_follow_up: Optional[datetime]
    created_at: datetime
    updated_at: datetime

class MessageCreate(BaseModel):
    lead_id: str
    direction: str  # 'outbound' or 'inbound'
    content: str
    wa_message_id: Optional[str] = None
    status: str = "sent"

class Message(BaseModel):
    id: str
    lead_id: str
    direction: str
    content: str
    wa_message_id: Optional[str]
    status: str
    created_at: datetime

class FollowUpCreate(BaseModel):
    lead_id: str
    due_date: datetime
    type: str = "whatsapp"
    notes: Optional[str] = None

class FollowUp(BaseModel):
    id: str
    lead_id: str
    due_date: datetime
    type: str
    notes: Optional[str]
    completed: bool
    completed_at: Optional[datetime]
    created_at: datetime

# ─── Health Check ──────────────────────────────────────────

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "supabase": "connected" if supabase else "not_configured",
        "bridge_url": WHATSAPP_BRIDGE_URL,
        "timestamp": datetime.utcnow().isoformat()
    }

# ─── Lead Endpoints ────────────────────────────────────────

@app.get("/api/leads", response_model=list[Lead])
async def get_leads(
    status: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    limit: int = Query(50, le=200)
):
    """Get all leads with optional filtering."""
    if not supabase:
        return get_demo_leads()
    
    query = supabase.table("leads").select("*").order("score", desc=True)
    
    if status:
        query = query.eq("status", status)
    
    if search:
        query = query.ilike("business_name", f"%{search}%")
    
    response = query.limit(limit).execute()
    return response.data

@app.get("/api/leads/{lead_id}", response_model=Lead)
async def get_lead(lead_id: str):
    """Get a single lead by ID."""
    if not supabase:
        demo = get_demo_leads()
        for l in demo:
            if l["id"] == lead_id:
                return l
        raise HTTPException(status_code=404, detail="Lead not found")
    
    response = supabase.table("leads").select("*").eq("id", lead_id).single().execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Lead not found")
    return response.data

@app.post("/api/leads", response_model=Lead)
async def create_lead(lead: LeadCreate):
    """Create a new lead."""
    if not supabase:
        return {"id": "demo-id", **lead.model_dump(), "status": "new", 
                "created_at": datetime.utcnow().isoformat(), "updated_at": datetime.utcnow().isoformat()}
    
    response = supabase.table("leads").insert(lead.model_dump()).execute()
    if not response.data:
        raise HTTPException(status_code=500, detail="Failed to create lead")
    return response.data[0]

@app.patch("/api/leads/{lead_id}", response_model=Lead)
async def update_lead(lead_id: str, update: LeadUpdate):
    """Update a lead."""
    if not supabase:
        return {"id": lead_id, **update.model_dump(exclude_none=True)}
    
    data = update.model_dump(exclude_none=True)
    if not data:
        raise HTTPException(status_code=400, detail="No fields to update")
    
    response = supabase.table("leads").update(data).eq("id", lead_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Lead not found")
    return response.data[0]

@app.delete("/api/leads/{lead_id}")
async def delete_lead(lead_id: str):
    """Delete a lead."""
    if not supabase:
        return {"deleted": True}
    
    supabase.table("leads").delete().eq("id", lead_id).execute()
    return {"deleted": True}

# ─── Message Endpoints ─────────────────────────────────────

@app.get("/api/leads/{lead_id}/messages", response_model=list[Message])
async def get_messages(lead_id: str, limit: int = Query(100, le=500)):
    """Get all messages for a lead."""
    if not supabase:
        return []
    
    response = (
        supabase.table("messages")
        .select("*")
        .eq("lead_id", lead_id)
        .order("created_at")
        .limit(limit)
        .execute()
    )
    return response.data

@app.post("/api/messages", response_model=Message)
async def create_message(msg: MessageCreate):
    """Create/save a message."""
    if not supabase:
        return {"id": "demo-msg-id", **msg.model_dump(), "created_at": datetime.utcnow().isoformat()}
    
    # Si es inbound, actualizar status del lead a 'responded'
    if msg.direction == "inbound":
        supabase.table("leads").update({
            "status": "responded",
            "last_contact": datetime.utcnow().isoformat()
        }).eq("id", msg.lead_id).execute()
        
        # Actualizar métricas de respuesta
        update_response_metrics(msg.lead_id)
    
    response = supabase.table("messages").insert(msg.model_dump()).execute()
    if not response.data:
        raise HTTPException(status_code=500, detail="Failed to save message")
    return response.data[0]

# ─── Follow-up Endpoints ──────────────────────────────────

@app.get("/api/leads/{lead_id}/follow-ups", response_model=list[FollowUp])
async def get_follow_ups(lead_id: str):
    """Get follow-ups for a lead."""
    if not supabase:
        return []
    
    response = (
        supabase.table("follow_ups")
        .select("*")
        .eq("lead_id", lead_id)
        .order("due_date")
        .execute()
    )
    return response.data

@app.post("/api/follow-ups", response_model=FollowUp)
async def create_follow_up(fu: FollowUpCreate):
    """Create a follow-up reminder."""
    if not supabase:
        return {"id": "demo-fu-id", **fu.model_dump(), "completed": False, 
                "completed_at": None, "created_at": datetime.utcnow().isoformat()}
    
    response = supabase.table("follow_ups").insert(fu.model_dump()).execute()
    if not response.data:
        raise HTTPException(status_code=500, detail="Failed to create follow-up")
    return response.data[0]

@app.patch("/api/follow-ups/{follow_up_id}/complete")
async def complete_follow_up(follow_up_id: str):
    """Mark a follow-up as completed."""
    if not supabase:
        return {"completed": True}
    
    response = supabase.table("follow_ups").update({
        "completed": True,
        "completed_at": datetime.utcnow().isoformat()
    }).eq("id", follow_up_id).execute()
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Follow-up not found")
    return response.data[0]

# ─── Metrics Endpoints ────────────────────────────────────

@app.get("/api/metrics/summary")
async def get_metrics_summary():
    """Get outreach metrics summary."""
    if not supabase:
        return {
            "total_leads": 11,
            "contacted": 11,
            "responded": 0,
            "converted": 0,
            "pending": 7
        }
    
    # Count by status
    response = supabase.table("leads").select("status").execute()
    statuses = [r["status"] for r in response.data]
    
    return {
        "total_leads": len(statuses),
        "new": statuses.count("new"),
        "contacted": statuses.count("contacted"),
        "responded": statuses.count("responded"),
        "qualified": statuses.count("qualified"),
        "proposal": statuses.count("proposal"),
        "negotiating": statuses.count("negotiating"),
        "converted": statuses.count("converted"),
        "closed": statuses.count("closed"),
        "disqualified": statuses.count("disqualified"),
    }

# ─── Helper Functions ──────────────────────────────────────

def update_response_metrics(lead_id: str):
    """Update response time metrics when a lead responds."""
    if not supabase:
        return
    
    # Get first sent message
    sent = (
        supabase.table("messages")
        .select("created_at")
        .eq("lead_id", lead_id)
        .eq("direction", "outbound")
        .order("created_at")
        .limit(1)
        .execute()
    )
    
    if not sent.data:
        return
    
    first_sent = sent.data[0]["created_at"]
    now = datetime.utcnow()
    
    # Get first response
    resp = (
        supabase.table("messages")
        .select("created_at")
        .eq("lead_id", lead_id)
        .eq("direction", "inbound")
        .order("created_at")
        .limit(1)
        .execute()
    )
    
    if resp.data:
        first_resp = resp.data[0]["created_at"]
        response_minutes = int((first_resp - first_sent).total_seconds() / 60)
    else:
        response_minutes = None
    
    # Count total messages
    msg_count = (
        supabase.table("messages")
        .select("id", count="exact")
        .eq("lead_id", lead_id)
        .execute()
    )
    total = msg_count.count if hasattr(msg_count, 'count') else 0
    
    # Upsert metrics
    supabase.table("response_metrics").upsert({
        "lead_id": lead_id,
        "first_sent_at": first_sent,
        "first_resp_at": resp.data[0]["created_at"] if resp.data else None,
        "response_time_minutes": response_minutes,
        "message_count": total,
    }, on_conflict="lead_id").execute()

def get_demo_leads():
    """Demo data when Supabase is not configured."""
    return [
        {"id": "1", "business_name": "Estudio Medieval", "contact_name": "Léo", 
         "whatsapp_number": "595961482854", "score": 133.2, "rating": 4.7, "reviews": 392,
         "status": "contacted", "location": "San Lorenzo", "source": "google",
         "created_at": "2026-05-27T00:00:00Z", "updated_at": "2026-05-27T00:00:00Z"},
        {"id": "2", "business_name": "SHINE Nails", "contact_name": "Celeste",
         "whatsapp_number": "595986693259", "score": 130.7, "rating": 4.8, "reviews": 287,
         "status": "contacted", "location": "Fernando", "source": "google",
         "created_at": "2026-05-27T00:00:00Z", "updated_at": "2026-05-27T00:00:00Z"},
    ]

# ─── Run Server ────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
    logger.info(f"🚀 CRM API running on port {PORT}")