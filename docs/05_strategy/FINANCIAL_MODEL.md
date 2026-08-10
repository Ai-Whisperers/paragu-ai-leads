# Financial Model
## Revenue, Costs & Profitability Projections

---

## 1. Revenue Model

### Tier Pricing (Monthly)
| Tier | Price (USD) | Annual Revenue |
|------|-------------|----------------|
| FREE | $0 | $0 |
| BASIC | $29 | $348 |
| PRO | $59 | $708 |
| ENTERPRISE | $99 | $1,188 |

### Setup Fees (One-time)
| Tier | Setup Fee |
|------|-----------|
| FREE | $0 |
| BASIC | $50 |
| PRO | $100 |
| ENTERPRISE | $200 |

### Additional Revenue Streams
| Stream | Price | Frequency |
|--------|-------|-----------|
| Extra page | $25 | One-time |
| Photo session | $50 | One-time |
| Logo design | $75 | One-time |
| SEO setup | $50 | One-time |
| Featured listing | $20 | Monthly |

---

## 2. Cost Structure

### Fixed Costs (Monthly)
| Item | Cost | Notes |
|------|------|-------|
| Hosting (Vercel/Netlify) | $0 | Free tier |
| Domain (1 per customer) | $1.25 | $15/yr ÷ 12 |
| Messaging Business | $0 | Free |
| Email (Google Workspace) | $6 | Per user |
| Tools (Canva, etc) | $0 | Free tier |
| **Total Fixed/Month** | **$7.25** | |

### Variable Costs (Per Customer)
| Item | Cost | Notes |
|------|------|-------|
| Domain purchase | $15 | One-time at launch |
| Development time | 2 hrs | $25/hr = $50 |
| Support time | 1 hr/mo | $25 = $25 |
| **Total Variable** | **$90** | First month |

### Customer Acquisition Cost (CAC)
| Channel | Cost | Notes |
|---------|------|-------|
| Messaging outreach | $0.50 | Time only |
| Phone calls | $1.00 | Time only |
| Total CAC | **$1.50** | |

---

## 3. Unit Economics

### Free Tier Economics
| Metric | Value |
|--------|-------|
| Revenue | $0 |
| Fixed cost | $7.25 |
| Variable cost | $90 |
| First month profit | -$97.25 |

### BASIC Tier Economics
| Metric | Value |
|--------|-------|
| Revenue (monthly) | $29 |
| Setup fee | $50 |
| First month revenue | $79 |
| Costs | $97.25 |
| First month profit | -$18.25 |
| Month 2+ profit | $21.75 |

### PRO Tier Economics
| Metric | Value |
|--------|-------|
| Revenue (monthly) | $59 |
| Setup fee | $100 |
| First month revenue | $159 |
| Costs | $97.25 |
| First month profit | $61.75 |
| Month 2+ profit | $51.75 |

---

## 4. Break-even Analysis

### Break-even Calculation
```
Fixed Costs = $7.25/month
Average Revenue/Customer = $45/month (blended)
Gross Margin = 85% (after variable costs)

Break-even Customers = Fixed Costs / (Revenue × Margin)
                    = $7.25 / ($45 × 0.85)
                    = 7.25 / 38.25
                    = 0.19 customers
```

Actually with setup fees:
```
Break-even = ~3 paying customers
```

### LTV Calculation
```
Average customer lifespan = 24 months
Average monthly revenue = $45
Churn rate = 10%/year

LTV = Monthly Revenue × Gross Margin × (1 / Churn Rate)
     = $45 × 0.85 × (1 / 0.10)
     = $38.25 × 10
     = $382.50
```

### CAC:LTV Ratio
```
CAC = $1.50
LTV = $382.50
Ratio = 255:1
```

---

## 5. Revenue Projections

### Conservative Scenario (Monthly)
| Month | Free Customers | BASIC | PRO | Enterprise | MRR |
|-------|----------------|-------|-----|------------|-----|
| 1 | 15 | 0 | 0 | 0 | $0 |
| 2 | 30 | 3 | 2 | 0 | $275 |
| 3 | 45 | 8 | 5 | 1 | $807 |
| 4 | 55 | 12 | 8 | 2 | $1,254 |
| 5 | 65 | 15 | 12 | 3 | $1,773 |
| 6 | 75 | 18 | 15 | 4 | $2,347 |

### Year 1 Revenue Projection
```
Month 1-3:    $1,082 (revenue generation phase)
Month 4-6:    $5,374
Month 7-9:    (estimate) $8,000
Month 10-12:  (estimate) $12,000
-------------------------
Year 1 Total: ~$26,456
```

### Revenue Mix (Steady State)
| Tier | % of Customers | % of Revenue |
|------|----------------|--------------|
| FREE | 50% | 0% |
| BASIC | 25% | 20% |
| PRO | 20% | 40% |
| ENTERPRISE | 5% | 40% |

---

## 6. Cost Projections

### Monthly Costs (Year 1)
| Month | Fixed | Variable | Total |
|-------|-------|----------|-------|
| 1 | $7 | $1,350 | $1,357 |
| 2 | $7 | $900 | $907 |
| 3 | $7 | $600 | $607 |
| 4 | $7 | $400 | $407 |
| 5 | $7 | $350 | $357 |
| 6 | $7 | $300 | $307 |
| 7-12 | $7/mo | $250/mo | ~$257/mo |

### Cumulative Costs (Year 1)
```
Total Fixed:       ~$84
Total Variable:    ~$4,100
-------------------------
Total Year 1:      ~$4,184
```

---

## 7. Profitability

### Monthly Profit (Steady State)
```
Revenue (Month 6):  $2,347
Costs (Month 6):   $307
-------------------
Profit:            $2,040
Margin:            87%
```

### Year 1 P&L
```
Revenue:    ~$26,456
Costs:      ~$4,184
-----------
Profit:     ~$22,272
Margin:     84%
```

### Profit by Tier (Monthly, Steady State)
| Tier | Revenue | Costs | Profit | Margin |
|------|---------|-------|--------|--------|
| FREE | $0 | $90 | -$90 | - |
| BASIC | $29 | $25 | $4 | 14% |
| PRO | $59 | $25 | $34 | 58% |
| ENTERPRISE | $99 | $25 | $74 | 75% |

---

## 8. Cash Flow

### Month 1-3 (Investment Phase)
```
Week 1-2:  Spend $500 on tools/setup
Week 3-4:  Spend $300 on customer acquisition
Month 1:   -$800 cash outlay

Month 2:   -$400 (continuing investment)
Month 3:   Break-even point
```

### Month 4+ (Growth Phase)
```
Month 4:   +$900 cash flow
Month 5:   +$1,400 cash flow
Month 6:   +$2,000 cash flow
...
Month 12:  +$12,000 cash flow
```

### Cash Position
```
Start:          $0
Month 1:        -$800
Month 2:        -$1,200
Month 3:       -$725
Month 4:        +$175
Month 5:        +$1,575
Month 6:        +$3,575
...
Year End:      +$18,000 (est)
```

---

## 9. Scaling Costs

### Costs at Scale (100 customers)
```
Fixed:
- Hosting: $0 (optimized)
- Email: $6
- Tools: $20 (paid tier)
- Total: $26/mo

Variable:
- Domains: 100 × $15 = $1,500/yr = $125/mo
- Support: 100 × 0.5hr/mo × $25 = $1,250/mo
- Total: $1,375/mo

Per Customer Cost: $14/mo
```

### Margin Improvement at Scale
| Customers | Revenue | Costs | Profit | Margin |
|-----------|---------|-------|--------|--------|
| 10 | $500 | $200 | $300 | 60% |
| 50 | $2,500 | $500 | $2,000 | 80% |
| 100 | $5,000 | $1,400 | $3,600 | 72% |
| 200 | $10,000 | $2,800 | $7,200 | 72% |

---

## 10. Key Metrics Summary

### Financial KPIs
| Metric | Month 1 | Month 3 | Month 6 | Month 12 |
|--------|---------|---------|---------|----------|
| Customers | 15 | 45 | 75 | 150 |
| MRR | $0 | $800 | $2,300 | $5,000 |
| CAC | $1.50 | $1.50 | $1.50 | $1.50 |
| LTV | $0 | $380 | $380 | $380 |
| LTV:CAC | 0:1 | 253:1 | 253:1 | 253:1 |
| Gross Margin | - | 75% | 85% | 85% |

### Milestones
| Milestone | Timeline | Requirement |
|-----------|----------|-------------|
| First paying customer | Month 2 | 3 customers |
| Break-even | Month 3 | 15 customers |
| $1K MRR | Month 4 | 25 customers |
| $5K MRR | Month 8 | 80 customers |
| $10K MRR | Month 12 | 150 customers |

---

## 11. Sensitivity Analysis

### Revenue Sensitivity
| Scenario | MRR (Month 6) | Notes |
|----------|---------------|-------|
| Conservative | $1,500 | 50% of target |
| Expected | $2,300 | Target |
| Optimistic | $3,500 | 50% above target |

### Cost Sensitivity
| Scenario | Costs (Month 6) | Notes |
|----------|-----------------|-------|
| Low | $200 | Minimal support |
| Expected | $307 | Standard |
| High | $500 | Heavy support |

### Profit Sensitivity
| Scenario | Profit (Month 6) | Notes |
|----------|-----------------|-------|
| Conservative | $1,000 | |
| Expected | $2,000 | |
| Optimistic | $3,000 | |

---

## 12. Funding Requirements

### Bootstrap (Default)
- No external funding needed
- Use free tiers for everything
- Reinvest all profit

### Growth Scenario ($10K needed)
```
Use case:
- $3,000: Professional photos for templates
- $3,000: Marketing (Google Ads, social)
- $2,000: Additional development help
- $2,000: Tools and software

ROI: Should recoup in 6 months
```

---

*Financial Model - Version 1.0 - April 2026*