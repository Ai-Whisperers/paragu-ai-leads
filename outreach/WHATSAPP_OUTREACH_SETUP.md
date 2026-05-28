# WHATSAPP OUTREACH — Setup Required

## Current State (2026-05-28)
- Hermes WhatsApp bridge: CONNECTED ✅ (port 3007) — but to Ivan's personal account (weissvanderpol)
- Evolution API: 9 instances, all LOGGED OUT / "close" state ❌
- ParaguAI Hair outreach instance: close ❌ — needs QR reconnection
- whatsapp-ai service: 404 ❌ (service may be down)

## Problem
We have the infrastructure but the WhatsApp account used for outreach is either:
1. Not connected (Evolution instances all logged out)
2. Ivan's personal account (can't use for cold outreach to leads)

## Solutions — Pick One

### Option A: AgentCall (Fastest — Set Up Today)
AgentCall can send WhatsApp messages from a US/CA number. ParaguAI creates the content → AgentCall delivers.

Steps:
1. Provision a US number via AgentCall (~$2/mo)
2. Use mcp_agentcall_send_sms or mcp_agentcall_initiate_ai_call
3. BUT: AgentCall sends from the provisioned number TO the leads' numbers

Limitation: AgentCall WhatsApp is SMS-ONLY (no multimedia), outbound AI calls work but expensive ($0.40/min).

### Option B: Reconnect Evolution ParaguAI Hair Instance (1hr setup)
1. Re-pair the ParaguAI Hair WhatsApp Business number
2. Use it as the dedicated outreach number
3. Send campaigns via Evolution API

This is the RIGHT long-term solution but requires QR scan from the ParaguAI account.

### Option C: Telegram Bridge (Today — No Setup)
Telegram IS connected. Setup a Telegram group for ParaguAI leads outreach.
- Create Telegram channel/group "ParaguAI Leads"
- Add Ivan and send via Telegram
- Leads still need to respond via WhatsApp but initial contact can come from Telegram

### Option D: Ivan Sends Manually (Zero Setup)
- Erebus generates perfectly formatted WhatsApp messages
- Ivan sends from his personal WhatsApp
- Uses Ivan's existing relationship/rapport with leads

---

## Recommended: Option D (Ivan Sends Manually Today)

Why: Zero setup time. Ivan has rapport with local leads already.
Erebus prepares everything, Ivan does 1 tap to send.

### Contact List (Formatted for Copy-Paste)

```
Contacto 1: Estudio Medieval
WhatsApp: wa.me/595961482854
Mensaje:
---
¡Hola! Soy Iván de ParaguAI.

Estudio Medieval es referente en tatuajes en San Lorenzo — 58K seguidores en IG, 392 reseñas en Maps. Lo que falta es un sitio web profesional para mostrar tu portafolio completo, catlogo de servicios con precios y turnos online.

¿Querés que te cuente cómo funciona? Sin compromiso.
---

Contacto 2: SHINE Nails (Celeste)
WhatsApp: wa.me/595986693259
Mensaje:
---
¡Hola! Soy Iván de ParaguAI.

¿Te gustaría que tus clientes puedan reserva online sin usar WhatsApp? Tenemos soluciones web para salones de uñas — con galera de trabajos, precios y reserva online.

Te vi en TikTok (@celestialnails) — ya tenés presencia digital. Solo falta el sitio web profesio

nal.

¿Hablamos?
---

Contacto 3: Nde Barba Barbería  
WhatsApp: wa.me/595991444268
Mensaje:
---
¡Hola! Soy Iván de ParaguAI.

Nde Barba es una de las barberías mejor puntuadas de Fernando — 118 reseñas · 4.8⭐. Lo que falta es un sitio web para mostrar tu historia, servicios y precios online.

¿Querés que te cuente opciones? Es rápido y sin compromiso.
---

Contacto 4: Arno's Barber Shop
WhatsApp: wa.me/595983996086
Mensaje:
---
¡Hola! Soy Iván de ParaguAI.

Hermes barberías como Arno's barbería necesitamos que nuevos clientes nos encuentren en Google más allá del mapa. Un sitio web con tus servicios, historia y opción de reservar online hace una gran diferencia.

¿Queré

s que te muestre cómo sería?
---
```

---

## Priority Order
1. Estudio Medieval (133.2 — Leo/Estudio Medieval SrL)
2. SHINE Nails (130.7 — Celeste, active TikTok)
3. Nde Barba (92.6 — Guaran brand, Fernando local)
4. Portas Barber (85.6 — 162 reviews, needs phone)
5. Arno's Barber (88.0 — 5.0⭐)

## Next Steps
- Ivan: Review contacts above; send via personal WhatsApp
- Erebus: Set up Evolution reconnect workflow (Option B) for next session
- Team: Create follow-up sequences per lead type
