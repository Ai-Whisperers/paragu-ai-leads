"""
Messaging Bridge Sync Script
Polls the Messaging bridge for incoming messages and saves them to Supabase.
Run as a cron job: */1 * * * * /usr/bin/python3 /root/paragu-ai-leads/crm/scripts/sync_messaging.py
"""

import os
import sys
import time
import logging
import requests
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("/root/paragu-ai-leads/crm/logs/sync.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configuration
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
MESSAGING_BRIDGE_URL = os.getenv("MESSAGING_BRIDGE_URL", "http://localhost:3007")
POLL_TIMEOUT = 65  # seconds (bridge long-poll timeout)

def get_supabase():
    if not SUPABASE_URL or not SUPABASE_KEY:
        logger.warning("⚠️  Supabase not configured")
        return None
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def get_bridge_health():
    """Check if bridge is healthy."""
    try:
        resp = requests.get(f"{MESSAGING_BRIDGE_URL}/health", timeout=5)
        return resp.status_code == 200
    except:
        return False

def poll_incoming_messages():
    """Long-poll the bridge for new incoming messages."""
    try:
        resp = requests.get(
            f"{MESSAGING_BRIDGE_URL}/messages",
            timeout=POLL_TIMEOUT
        )
        if resp.status_code == 200:
            return resp.json()
        return []
    except requests.exceptions.Timeout:
        # Normal — no messages within timeout
        return []
    except Exception as e:
        logger.error(f"Error polling bridge: {e}")
        return []

def find_lead_by_phone(supabase, phone: str) -> dict | None:
    """Find a lead by Messaging number."""
    if not supabase:
        return None
    
    # Normalize phone: remove non-digits
    phone_clean = "".join(filter(str.isdigit, phone))
    
    response = supabase.table("leads").select("*").execute()
    for lead in response.data:
        lead_phone = "".join(filter(str.isdigit, lead.get("messaging_number", "")))
        if lead_phone and phone_clean.endswith(lead_phone[-9:]):  # Last 9 digits
            return lead
    
    return None

def save_message(supabase, message: dict):
    """Save an incoming message to the database."""
    if not supabase:
        logger.info(f"[DEMO] Message saved: {message.get('content', '')[:50]}")
        return
    
    # Extract sender and content
    sender = message.get("from", message.get("chatId", "unknown"))
    content = message.get("content", message.get("message", ""))
    wa_id = message.get("id", message.get("messageId", ""))
    
    if not content:
        return
    
    # Find the lead
    lead = find_lead_by_phone(supabase, sender)
    if not lead:
        logger.warning(f"No lead found for phone: {sender}")
        return
    
    # Check if message already exists (dedup by wa_message_id)
    if wa_id:
        existing = supabase.table("messages").select("id").eq("wa_message_id", wa_id).execute()
        if existing.data:
            logger.debug(f"Message {wa_id} already saved, skipping")
            return
    
    # Save message
    msg_data = {
        "lead_id": lead["id"],
        "direction": "inbound",
        "content": content,
        "wa_message_id": wa_id,
        "status": "read" if message.get("read") else "delivered",
        "created_at": message.get("timestamp", datetime.utcnow().isoformat())
    }
    
    try:
        supabase.table("messages").insert(msg_data).execute()
        logger.info(f"✅ Saved inbound message from {lead['business_name']}: {content[:50]}")
        
        # Update lead status to 'responded' if still 'contacted'
        if lead.get("status") == "contacted":
            supabase.table("leads").update({
                "status": "responded",
                "last_contact": datetime.utcnow().isoformat()
            }).eq("id", lead["id"]).execute()
            logger.info(f"📲 {lead['business_name']} → status: responded")
        
        # Schedule follow-up if not set
        if not lead.get("next_follow_up"):
            follow_up_date = datetime.utcnow().replace(
                hour=18, minute=0, second=0, microsecond=0
            )
            if follow_up_date <= datetime.utcnow():
                from datetime import timedelta
                follow_up_date += timedelta(days=1)
            
            supabase.table("follow_ups").insert({
                "lead_id": lead["id"],
                "due_date": follow_up_date.isoformat(),
                "type": "messaging",
                "notes": "Respuesta recibida — hacer seguimiento"
            }).execute()
    
    except Exception as e:
        logger.error(f"Error saving message: {e}")

def main():
    logger.info("🔄 Messaging Bridge Sync started")
    
    if not get_bridge_health():
        logger.error("❌ Bridge not healthy, aborting")
        return
    
    supabase = get_supabase()
    if not supabase:
        logger.warning("⚠️  Running in demo mode (no Supabase)")
    
    messages = poll_incoming_messages()
    
    if messages:
        logger.info(f"📬 Received {len(messages)} message(s)")
        for msg in messages:
            save_message(supabase, msg)
    else:
        logger.debug("No new messages")
    
    logger.info("✅ Sync completed")

if __name__ == "__main__":
    main()