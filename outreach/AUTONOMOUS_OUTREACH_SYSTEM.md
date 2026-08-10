# AUTONOMOUS OUTREACH SYSTEM — ParaguAI Leads
## Runs every day at 9:00 AM | Target: Leads near Politécnica

---

## MISSION
Convert leads into ParaguAI paying clients via Messaging-first outreach.
Revenue > Infrastructure. Zero paying clients as of May 2026.

---

## LEAD QUEUE — Tier 1 (Contact esta semana)

| # | Lead | Messaging | Score | Status | Last Contact |
|---|------|----------|-------|--------|--------------|
| 1 | Estudio Medieval | wa.me/595961482854 | 133.2 | COLD | Never |
| 2 | SHINE Nails (Celeste) | wa.me/595986693259 | 130.7 | COLD | Never |
| 3 | Viviesteticpy | wa.me/595976668289 | 82.1 | COLD | Never |
| 4 | Nde Barba | wa.me/595991444268 | 92.6 | COLD | Never |
| 5 | Portas Barber Shop | wa.me/595994215627 | 85.6 | COLD | Never |
| 6 | Leticia Carballo | wa.me/595984904215 | 85.5 | COLD | Never |
| 7 | Cronos Academy | wa.me/595973160522 | 87.0 | COLD | Never |
| 8 | XXGym | wa.me/59521678171 | 92.4 | COLD | Never |

---

## OUTREACH PROTOCOL

### MESSAGE TEMPLATE — First Contact (3MD-style)
```
¡Hola! 👋 Soy de ParaguAI — ayudamos negocios como [NOMBRE]
a tener presencia online profesional.

Vi que [NOMBRE] tiene [X] reseñas en Google Maps — vos ya tenés
la reputación, solo te falta el sitio web para que nuevos clientes
te encuentren en Google y reserven online.

¿Te interesa que te muestre cómo funciona? Es rápido y sin compromiso.
```

### MESSAGE TEMPLATE — Barberías (Nde Barba / Portas)
```
¡Hola! Soy de ParaguAI — diseñamos sitios web para barberías
en Paraguay.

Te vi en Google Maps: 162 reseñas · 4.9⭐ — Portas es una
de las barberías mejor puntuadas de la zona.

Pero no.tenés website.

Isso significa que cada vez que alguien te Googlea, solo ve
un mapas. Un sitio con tu historia, tus precios y reserva
online.change eso.

¿Hablamos 5 minutos? Te muestro opciones sin compromiso.
```

### MESSAGE TEMPLATE — Tattoo (Estudio Medieval)
```
¡Hola Leo! Soy de ParaguAI.

Estudio Medieval es referente en tatuajes en San Lorenzo —
58K seguidores en IG, 392 reseñas en Maps. Lo que falta
es un sitio web profesional para:

✅ Mostrar tu portafolio completo
✅ Catálogo de servicios con precios
✅ Turnos online + consulta por Messaging
✅ Presencia real en Google (más allá del mapa)

¿Querés que te cuente cómo funciona? Sin compromiso.
```

---

## MESSAGING DELIVERY RULES
- Send 1 message per lead per day (max 3/day across all leads)
- Wait 48h before follow-up #2
- Wait 72h before follow-up #3
- Track response rate
- If "no" → move to BAjaLista/Never contact again
- If "interested" → escalate to Closer-Bot immediately

---

## RESPONSE HANDLING
- "Sí"/"Interesado" → Escalate immediately
- "No" → Remove from queue
- "Después" → Re-add at bottom in 7 days
- No response after 3 msgs → Move to Dormant (retry Q4)

---

## OUTREACH TRACKER FILE
`/root/paragu-ai-leads/outreach/OUTREACH_TRACKER.csv`

Format:
```
lead_name, messaging, score, msg1_sent, msg2_sent, msg3_sent, response, status, next_action
Estudio Medieval, wa.me/595961482854, 133.2, --, --, --, --, PENDING, msg1_today
```

---

## KNOWN BLOCKERS
- Estudio Medieval: Messaging directo ya funcionando = buena señal
- SHINE Nails: TikTok activo, usa Linktree = digitamente activo = alta aceptación
- Barbers: Sin IG = website llenaría ese vacío de marca
- All: Sin precios online = 82% del mercado tampoco muestra — FIRST MOVER advantage

---

## AUTONOMOUS DECISIONS
- Never send to a lead more than 1x/day
- Never contact leads marked DORMANT without Ivan approval
- Never send pricing in first message
- Always follow up within 48h if no response
- If lead says "no" → mark REMOVED and log reason

---

## NEXT CYCLE: 2026-05-29
Priority order for next outreach push:
1. Estudio Medieval (133.2 — THE show piece)
2. SHINE Nails (130.7 — digitamente activo)
3. Nde Barba (92.6 — nombre guaraní = diferenciador)
4. Portas Barber (85.6 — 162 reviews líder categoría)

*Generated: 2026-05-28 | Managed: Erebus (Autonomous) | Target: 3 paying clients by June 2026*
