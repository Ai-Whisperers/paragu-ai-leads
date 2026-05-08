## WhatsApp AI Agent Integration

The Lead Scout can automatically onboard lead websites to the WhatsApp AI Agent once they're created.

### How It Works

1. **Lead created** → optional WhatsApp AI instance creation
2. **Website deployed** → Lead's WhatsApp business number linked to Evolution API
3. **LightRAG seeded** with lead's business info (from registration data)
4. **AI handles** incoming customer messages for sales/support

### Endpoints

```
POST https://whatsapp-ai.sunstein.cloud/clients
  Body: { "name": "...", "phone": "...", "mode": "ventas|soporte|default" }
  Returns: instance_name, qr_code (client scans with WhatsApp Business)

DELETE https://whatsapp-ai.sunstein.cloud/clients/{instance}
  Removes client and Evolution instance

GET https://whatsapp-ai.sunstein.cloud/clients
  Lists all active clients
```

### Knowledge Injection

After creating a client, seed their business data into LightRAG for accurate AI responses:

```python
# From lead-scout, after website generation:
requests.post("http://127.0.0.1:9623/documents/text", json={
    "text": f"Lead: {lead.name}. Business: {lead.type}. Products: {lead.products}",
    "description": f"{lead.name} - business info"
})
```

### Lead Profile Fields

The `leads` table should include:
- `whatsapp_ai_instance` (text) — Evolution instance name if onboarded
- `whatsapp_ai_mode` (text) — "ventas" | "soporte" | "default"
- `whatsapp_business_phone` (text) — client's registered WhatsApp Business number
