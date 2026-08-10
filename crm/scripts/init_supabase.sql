-- ParaguAI Messaging CRM - Supabase Schema
-- Ejecutar en: Supabase SQL Editor

-- Tabla: leads
CREATE TABLE IF NOT EXISTS leads (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  business_name   TEXT NOT NULL,
  contact_name    TEXT,
  messaging_number TEXT NOT NULL,
  wa_chat_id      TEXT,
  score           DECIMAL(5,1) DEFAULT 0,
  rating          DECIMAL(2,1) DEFAULT 0,
  reviews         INTEGER DEFAULT 0,
  status          TEXT DEFAULT 'new' CHECK (status IN (
                    'new','contacted','responded','qualified',
                    'proposal','negotiating','converted','closed','disqualified'
                  )),
  source          TEXT,
  location        TEXT,
  last_contact    TIMESTAMPTZ,
  next_follow_up  TIMESTAMPTZ,
  notes           TEXT,
  created_at      TIMESTAMPTZ DEFAULT NOW(),
  updated_at      TIMESTAMPTZ DEFAULT NOW()
);

-- Tabla: messages
CREATE TABLE IF NOT EXISTS messages (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  lead_id       UUID NOT NULL REFERENCES leads(id) ON DELETE CASCADE,
  direction     TEXT NOT NULL CHECK (direction IN ('outbound','inbound')),
  content       TEXT NOT NULL,
  wa_message_id TEXT,
  status        TEXT DEFAULT 'sent' CHECK (status IN (
                  'queued','sent','delivered','read','failed'
                )),
  created_at    TIMESTAMPTZ DEFAULT NOW()
);

-- Tabla: follow_ups
CREATE TABLE IF NOT EXISTS follow_ups (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  lead_id      UUID NOT NULL REFERENCES leads(id) ON DELETE CASCADE,
  due_date     TIMESTAMPTZ NOT NULL,
  type         TEXT CHECK (type IN ('call','messaging','email','meeting')),
  notes        TEXT,
  completed    BOOLEAN DEFAULT FALSE,
  completed_at TIMESTAMPTZ,
  created_at   TIMESTAMPTZ DEFAULT NOW()
);

-- Tabla: response_metrics
CREATE TABLE IF NOT EXISTS response_metrics (
  id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  lead_id             UUID UNIQUE NOT NULL REFERENCES leads(id) ON DELETE CASCADE,
  first_sent_at       TIMESTAMPTZ,
  first_resp_at       TIMESTAMPTZ,
  response_time_minutes INTEGER,
  message_count       INTEGER DEFAULT 0,
  updated_at          TIMESTAMPTZ DEFAULT NOW()
);

-- Índices
CREATE INDEX IF NOT EXISTS idx_messages_lead_id ON messages(lead_id);
CREATE INDEX IF NOT EXISTS idx_messages_created_at ON messages(created_at);
CREATE INDEX IF NOT EXISTS idx_leads_status ON leads(status);
CREATE INDEX IF NOT EXISTS idx_leads_messaging ON leads(messaging_number);
CREATE INDEX IF NOT EXISTS idx_follow_ups_due ON follow_ups(due_date) WHERE completed = FALSE;

-- Trigger para updated_at automático
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER leads_updated_at
  BEFORE UPDATE ON leads
  FOR EACH ROW EXECUTE FUNCTION update_updated_at();

CREATE OR REPLACE TRIGGER response_metrics_updated_at
  BEFORE UPDATE ON response_metrics
  FOR EACH ROW EXECUTE FUNCTION update_updated_at();

-- Row Level Security
ALTER TABLE leads ENABLE ROW LEVEL SECURITY;
ALTER TABLE messages ENABLE ROW LEVEL SECURITY;
ALTER TABLE follow_ups ENABLE ROW LEVEL SECURITY;
ALTER TABLE response_metrics ENABLE ROW LEVEL SECURITY;

-- Políticas públicas (para el dashboard - ajustar según necesidad)
CREATE POLICY "Public read leads" ON leads FOR SELECT USING (true);
CREATE POLICY "Public insert leads" ON leads FOR INSERT WITH CHECK (true);
CREATE POLICY "Public update leads" ON leads FOR UPDATE USING (true);

CREATE POLICY "Public read messages" ON messages FOR SELECT USING (true);
CREATE POLICY "Public insert messages" ON messages FOR INSERT WITH CHECK (true);
CREATE POLICY "Public update messages" ON messages FOR UPDATE USING (true);

CREATE POLICY "Public read follow_ups" ON follow_ups FOR SELECT USING (true);
CREATE POLICY "Public insert follow_ups" ON follow_ups FOR INSERT WITH CHECK (true);
CREATE POLICY "Public update follow_ups" ON follow_ups FOR UPDATE USING (true);

CREATE POLICY "Public read metrics" ON response_metrics FOR SELECT USING (true);
CREATE POLICY "Public insert metrics" ON response_metrics FOR INSERT WITH CHECK (true);
CREATE POLICY "Public update metrics" ON response_metrics FOR UPDATE USING (true);