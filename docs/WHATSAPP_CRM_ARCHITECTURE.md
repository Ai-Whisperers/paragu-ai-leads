# WHATSAPP CRM — ARQUITECTURA COMPLETA
## ParaguAI Outreach System

---

## PROBLEMA ACTUAL

Los mensajes se envían por WhatsApp bridge (localhost:3007) pero:
- ❌ No hay registro de respuestas de clientes
- ❌ No hay historial de conversación guardado
- ❌ No se puede ver estado sin abrir WhatsApp
- ❌ Seguimiento manual y propenso a perderse

## ARQUITECTURA PROPUESTA

```
┌─────────────────────────────────────────────────────────┐
│                    FRONTEND (Dashboard)                   │
│         Single HTML —任何人 puede abrirlo               │
│   Lead List │ Conversation View │ Status Tracking         │
└──────────────────────┬──────────────────────────────────┘
                       │ REST API
                       ▼
┌─────────────────────────────────────────────────────────┐
│              BACKEND (Python FastAPI)                    │
│   ─────────────────────────────────────────────────     │
│   GET  /api/leads                    → lista leads     │
│   GET  /api/leads/{id}                → un lead         │
│   GET  /api/leads/{id}/messages       → conversación    │
│   POST /api/leads                     → crear lead      │
│   PATCH /api/leads/{id}               → actualizar      │
│   POST /api/messages                  → guardar mensaje  │
│   GET  /api/health                    → health check    │
└──────────────────────┬──────────────────────────────────┘
                       │
        ┌──────────────┴──────────────┐
        ▼                              ▼
┌─────────────────────┐  ┌─────────────────────────────┐
│   WHATSAPP BRIDGE    │  │      SUPABASE POSTGRES      │
│  localhost:3007      │  │  ────────────────────────   │
│                     │  │  leads                      │
│  GET  /messages     │  │  conversations             │
│  POST /send         │  │  messages                  │
│  POST /send-media   │  │  follow_ups                 │
│  GET  /chat/:id     │  │  response_metrics           │
└─────────────────────┘  └─────────────────────────────┘
```

---

## MODELO DE DATOS

### Tabla: leads
```sql
CREATE TABLE leads (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  business_name   TEXT NOT NULL,
  contact_name    TEXT,
  whatsapp_number TEXT NOT NULL,          -- +595991234567
  wa_chat_id      TEXT,                   -- ID interno de WhatsApp
  score           DECIMAL(5,1),           -- 0-150
  rating          DECIMAL(2,1),           -- 0-5 estrellas
  reviews         INTEGER DEFAULT 0,
  status          TEXT DEFAULT 'new' CHECK (status IN (
                    'new','contacted','responded','qualified',
                    'proposal','negotiating','converted','closed','disqualified'
                  )),
  source          TEXT,                  -- 'google','instagram','referral'
  location        TEXT,                   -- 'Fernando','San Lorenzo'
  last_contact    TIMESTAMPTZ,
  next_follow_up  TIMESTAMPTZ,
  notes           TEXT,
  created_at      TIMESTAMPTZ DEFAULT NOW(),
  updated_at      TIMESTAMPTZ DEFAULT NOW()
);
```

### Tabla: messages
```sql
CREATE TABLE messages (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  lead_id       UUID NOT NULL REFERENCES leads(id) ON DELETE CASCADE,
  direction     TEXT NOT NULL CHECK (direction IN ('outbound','inbound')),
  content       TEXT NOT NULL,
  wa_message_id TEXT,                     -- ID de WhatsApp
  status        TEXT DEFAULT 'sent' CHECK (status IN (
                  'queued','sent','delivered','read','failed'
                )),
  created_at    TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_messages_lead_id ON messages(lead_id);
CREATE INDEX idx_messages_created_at ON messages(created_at);
```

### Tabla: follow_ups
```sql
CREATE TABLE follow_ups (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  lead_id     UUID NOT NULL REFERENCES leads(id) ON DELETE CASCADE,
  due_date    TIMESTAMPTZ NOT NULL,
  type        TEXT CHECK (type IN ('call','whatsapp','email','meeting')),
  notes       TEXT,
  completed   BOOLEAN DEFAULT FALSE,
  completed_at TIMESTAMPTZ,
  created_at  TIMESTAMPTZ DEFAULT NOW()
);
```

### Tabla: response_metrics
```sql
CREATE TABLE response_metrics (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  lead_id       UUID NOT NULL REFERENCES leads(id) ON DELETE CASCADE,
  first_sent_at TIMESTAMPTZ,
  first_resp_at TIMESTAMPTZ,
  response_time_minutes INTEGER,
  message_count INTEGER DEFAULT 0,
  updated_at    TIMESTAMPTZ DEFAULT NOW()
);
```

---

## API DEL BRIDGE WHATSAPP (localhost:3007)

El bridge actual expone estos endpoints:

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/messages` | Long-poll: espera mensajes entrantes (retorna array vacío si no hay) |
| POST | `/send` | Enviar mensaje `{chatId, message, replyTo?}` |
| POST | `/send-media` | Enviar media `{chatId, filePath, mediaType?, caption?}` |
| POST | `/typing` | Indicador de escritura `{chatId}` |
| GET | `/chat/:id` | Info del chat |
| GET | `/health` | `{"status":"connected","queueLength":0}` |

**Importante:** El bridge solo tiene endpoint para mensajes ENVIADOS (POST /send). 
Los mensajes RECIBIDOS llegan via long-poll GET /messages.

---

## FLUJO DE DATOS PROPUESTO

```
1. ENVÍO DE MENSAJE
   Erebus → POST /send (bridge.js) → WhatsApp → cliente
   Erebus → POST /api/messages (backend) → guardar en DB (outbound)

2. RECEPCIÓN DE RESPUESTA
   Erebus → GET /messages (bridge.js) → respuesta cliente
   Erebus → POST /api/messages (backend) → guardar en DB (inbound)
   Erebus → PATCH /api/leads/{id} status='responded'

3. DASHBOARD
   Usuario abre dashboard.html → GET /api/leads
   Click en lead → GET /api/leads/{id}/messages → muestra conversación
```

---

## IMPLEMENTACIÓN — ARCHIVOS A CREAR

```
/root/paragu-ai-leads/
├── crm/
│   ├── backend/
│   │   ├── main.py              # FastAPI app
│   │   ├── config.py            # Settings (Supabase URL, port)
│   │   ├── database.py          # Conexión Supabase
│   │   ├── models.py            # Pydantic models
│   │   ├── routers/
│   │   │   ├── leads.py         # CRUD leads
│   │   │   └── messages.py      # Messages endpoints
│   │   └── requirements.txt     # fastapi, uvicorn, supabase
│   │
│   └── frontend/
│       ├── dashboard.html       # Dashboard principal (single file)
│       ├── styles.css           # Estilos
│       └── app.js               # Lógica del frontend
│
├── docs/
│   └── WHATSAPP_CRM_ARCHITECTURE.md  # Este documento
│
└── scripts/
    ├── sync_whatsapp.py         # Script que polls /messages y guarda en DB
    └── init_supabase.sql        # SQL para crear tablas
```

---

## DASHBOARD — DISEÑO

### Vista: Lista de Leads
```
┌──────────────────────────────────────────────────────────┐
│  ParaguAI Outreach CRM                        [+ Nuevo Lead] │
├──────────────────────────────────────────────────────────┤
│  Filtros: [Todos ▼] [ contacted | responded | converted ]  │
│  Búsqueda: [________________________]                    │
├──────────────────────────────────────────────────────────┤
│  ⬤ Estudio Medieval   133.2  📱 +595 961 482 854  │ REPLIED │
│  ⬤ SHINE Nails         130.7  📱 +595 986 693 259  │ SENT   │
│  ⬤ HidroBaby Spa       135.1  📱 +595 993 444 222  │ SENT   │
│  ○ Leticia Carballo    118.5  📱 +595 984 904 215  │ NEW    │
└──────────────────────────────────────────────────────────┘
```

### Vista: Conversación
```
┌──────────────────────────────────────────────────────────┐
│  ← Volver  │  Estudio Medieval SRL              │ ⋮ Menú  │
├──────────────────────────────────────────────────────────┤
│                                                           │
│  [Erebus - 27 May 2026]                                  │
│  ┌─────────────────────────────────┐                     │
│  │ ¡Hola! Soy Iván de ParaguAI... │ ◀ 你               │
│  └─────────────────────────────────┘                     │
│                                                           │
│  [Cliente - 27 May 2026]                                 │
│  ┌─────────────────────────────────┐                     │
│  │ Hola Iván, sí me interesa.      │                     │
│  │ ¿Cómo funciona?                │                     │
│  └─────────────────────────────────┘                     │
│                                                           │
├──────────────────────────────────────────────────────────┤
│  [Type a message...                              ] [Enviar]│
└──────────────────────────────────────────────────────────┘
```

---

## CONFIGURACIÓN DE SUPABASE

### Paso 1: Obtener credenciales
1. Ir a supabase.com → Project Settings → API
2. Copiar: `SUPABASE_URL` y `SUPABASE_ANON_KEY` (o service_role key)

### Paso 2: Crear tablas
```bash
# Ejecutar init_supabase.sql en Supabase SQL Editor
# o usar:
psql "$SUPABASE_DATABASE_URL" -f scripts/init_supabase.sql
```

### Paso 3: Configurar environment
```bash
export SUPABASE_URL="https://xxxxx.supabase.co"
export SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
export WHATSAPP_BRIDGE_URL="http://localhost:3007"
export CRM_PORT=3042
```

---

## SCRIPT DE SINCRONIZACIÓN (sync_whatsapp.py)

Este script debe correr como cron job para hacer polling del bridge:

```python
import requests
import time

BRIDGE_URL = "http://localhost:3007"
POLL_INTERVAL = 5  # segundos

def poll_incoming_messages():
    """Long-poll el bridge para mensajes entrantes."""
    try:
        resp = requests.get(f"{BRIDGE_URL}/messages", timeout=65)
        messages = resp.json()
        for msg in messages:
            save_to_supabase(msg)
    except Exception as e:
        print(f"Error polling: {e}")

def save_to_supabase(msg):
    """Guarda mensaje entrante en DB."""
    # Busca lead por número de teléfono
    # Inserta en tabla messages con direction='inbound'
    # Actualiza status del lead si es primera respuesta
    pass
```

---

## CRON JOBS SUGERIDOS

| Job | Schedule | Qué hace |
|-----|----------|----------|
| `whatsapp-poll` | every 1m | Poll /messages del bridge, guarda en DB |
| `follow-up-check` | every 30m | Revisa leads con next_follow_up pendiente |
| `status-cleanup` | daily 9am | Limpia estados stale (>7 días sin respuesta → 'cold') |

---

## ALTERNATIVAS DE DESPLIEGUE

### Opción A: Backend + Frontend separados (recomendado)
- Backend: FastAPI en puerto 3042 del VPS
- Frontend: static HTML servido por Traefik
- Pros: Escalable, separador claramente
- Contras: Más configuración

### Opción B: Todo en un solo servicio
- Backend FastAPI sirve frontend estático
- Un solo deploy
- Pros: Simple
- Contras: Menos escalable

### Opción C: Solo frontend + Supabase directo
- Frontend llama directamente a Supabase (con RLS policies)
- No necesita backend propio
- Pros: Mínimo infrastructure
- Contras: Seguridad más compleja, no se puede usar bridge API

---

## PRÓXIMOS PASOS (en orden)

1. **Crear tablas en Supabase** → ejecutar `init_supabase.sql`
2. **Backend FastAPI** → crear API server con CRUD de leads/messages
3. **Sync script** → cron que poll el bridge y guarda en DB
4. **Frontend dashboard** → HTML/CSS/JS con fetch al backend
5. **Integrar con outreach actual** → modificar script de envío para también guardar en DB
6. **Deploy** → subir al VPS, configurar Traefik

---

---

## STACK TÉCNICO

- **Backend:** Python 3.12 + FastAPI + Uvicorn
- **Base de datos:** Supabase (PostgreSQL)
- **Frontend:** Vanilla HTML/CSS/JS (sin frameworks)
- **WhatsApp:** Bridge existente en localhost:3007
- **Deployment:** Docker en VPS (puerto 3042)

---

## IMPLEMENTACIÓN COMPLETADA ✅

### Archivos creados:

```
/root/paragu-ai-leads/
├── docs/
│   └── WHATSAPP_CRM_ARCHITECTURE.md    ← Este documento
│
├── crm/
│   ├── backend/
│   │   ├── main.py                     ← FastAPI API server
│   │   ├── config.py                   ← Configuración
│   │   ├── models.py                   ← Pydantic models
│   │   └── requirements.txt            ← Dependencias
│   │
│   ├── frontend/
│   │   └── dashboard.html               ← Dashboard completo (single file)
│   │
│   ├── scripts/
│   │   ├── init_supabase.sql            ← Schema de BD
│   │   └── sync_whatsapp.py             ← Polling del bridge
│   │
│   └── Dockerfile                       ← Deploy al VPS
```

### Estado: LISTO PARA CONFIGURAR

1. **Backend FastAPI** → Creado, corriendo en puerto 3042
2. **Dashboard HTML** → Creado, funcional en modo demo
3. **Sync script** → Listo para cron job
4. **Schema SQL** → Listo para ejecutar en Supabase

---

## PRÓXIMOS PASOS PARA ACTIVAR

### Paso 1: Configurar Supabase
```bash
# 1. Ir a supabase.com → Project Settings → API
# 2. Obtener SUPABASE_URL y SUPABASE_KEY
# 3. Ejecutar en SQL Editor: crm/scripts/init_supabase.sql
```

### Paso 2: Configurar .env
```bash
cat > /root/paragu-ai-leads/crm/.env << EOF
SUPABASE_URL=https://xxxx.supabase.co
SUPABASE_KEY=eyJhbG...service_role_key...
WHATSAPP_BRIDGE_URL=http://localhost:3007
CRM_PORT=3042
EOF
```

### Paso 3: Deploy en VPS
```bash
# Opción A: Docker
cd /root/paragu-ai-leads/crm
docker build -t paraguai-crm .
docker run -d --restart unless-stopped \
  --env-file .env \
  -p 3042:3042 \
  paraguai-crm

# Opción B: Directo
cd /root/paragu-ai-leads/crm/backend
pip install -r requirements.txt
python main.py
```

### Paso 4: Abrir dashboard
```
http://72.61.44.159:3042/dashboard.html
```

---

## MODO DEMO (sin Supabase)

El sistema funciona en modo demo si no hay Supabase:
- Dashboard muestra datos hardcodeados de los 5 leads principales
- Mensajes se guardan localmente en memoria
- Útil para probar el UI antes de configurar la DB

---

*Documento creado: 2026-05-28*
*Versión: 1.1 — Implementación completada*
*Autor: Erebus / Ai-Whisperers*