# Security Tool Consolidation Framework

**Purpose:** A structured methodology to rationalize a security tool estate — reducing cost, advancing Zero Trust maturity, and improving operational efficiency.

---

## How to Use This Framework

**Step 1:** Fill in `tool-inventory-template.csv` — one row per tool.  
**Step 2:** Read `tool-inventory-schema.md` for field definitions and how to score each field.  
**Step 3:** Apply the scoring model from `scoring-methodology.md` to produce priority scores.  
**Step 4:** Review `example-analysis.md` to see a fully worked example (Acme Financial Corp, 22 tools → 12).  

---

## Files

| File | Purpose |
|------|---------|
| `tool-inventory-template.csv` | Blank CSV template — fill in your tool estate |
| `tool-inventory-schema.md` | Field definitions, scoring guidance, tips for filling the inventory |
| `scoring-methodology.md` | Scoring model, outcome themes, stakeholder presentation guides |
| `example-analysis.md` | Worked example: 22-tool estate → 3 consolidation scenarios, ZTA maturity delta, ATT&CK coverage delta |

---

## Key Outputs

1. **Consolidation Priority Score** per tool (0–25 scale)
2. **Coverage Heatmap** (NIST CSF function × ZTA pillar)
3. **3 Consolidation Scenarios** (tactical / strategic / platform)
4. **Contract-sequenced execution plan**
5. **ZTA maturity delta** (before → after by pillar)
6. **Executive summary** (spend, tool count, vendor count, coverage gaps)
