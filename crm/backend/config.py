"""Configuration for ParaguAI Messaging CRM Backend"""

import os
from dotenv import load_dotenv

load_dotenv()

# Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")  # Use service_role key for backend

# Messaging Bridge
MESSAGING_BRIDGE_URL = os.getenv("MESSAGING_BRIDGE_URL", "http://localhost:3007")

# Server
CRM_HOST = os.getenv("CRM_HOST", "0.0.0.0")
CRM_PORT = int(os.getenv("CRM_PORT", "3042"))

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = "/root/paragu-ai-leads/crm/logs/app.log"

# Lead scoring weights
SCORE_WEIGHTS = {
    "rating": 2,       # Points per 0.1 star
    "reviews": 0.1,    # Points per review
    "recency": 5,      # Points if reviewed < 6 months ago
    "location": 10,    # Points if near Politécnica
}

# Status lifecycle
STATUS_FLOW = [
    "new",
    "contacted",
    "responded",
    "qualified",
    "proposal",
    "negotiating",
    "converted",
    "closed",
]

# Follow-up defaults
FOLLOW_UP_HOURS = [24, 48, 72, 168]  # 1, 2, 3, 7 days