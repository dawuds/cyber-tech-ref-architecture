# Tool Inventory Schema

**File:** `tool-inventory-template.csv`  
**Purpose:** Capture every security tool in the estate with the fields required to run a consolidation analysis.  
**Usage:** Fill one row per tool (not per vendor). If a vendor provides two distinct products serving different capabilities, enter them as separate rows.

---

## Field Definitions

### Identity Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `tool_name` | string | Product name as sold/licensed | `Splunk Enterprise Security` |
| `vendor` | string | Vendor name | `Splunk (Cisco)` |
| `category` | string | Security capability category — use values from TECH-STACK.md | `SIEM`, `EDR`, `PAM`, `SSE`, `IAM`, `CNAPP` |
| `nist_function` | enum | Primary NIST CSF 2.0 function | `Govern`, `Identify`, `Protect`, `Detect`, `Respond`, `Recover` |
| `zt_pillar` | enum | Primary Zero Trust pillar | `Identity`, `Device`, `Network`, `Application`, `Data`, `Visibility` |

---

### Financial Fields

| Field | Type | Description | Notes |
|-------|------|-------------|-------|
| `annual_license_usd` | integer | Annual software/SaaS license cost | Exclude hardware; use contract value ÷ term |
| `annual_opex_usd` | integer | Operational cost estimate (FTE time × loaded rate) | 0.25 FTE × $150K = $37,500 |
| `total_annual_cost` | integer | `annual_license_usd + annual_opex_usd` | Calculated field |
| `contract_end_date` | date | Earliest exit point without penalty | `YYYY-MM-DD`; use `rolling` if month-to-month |

---

### Coverage Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `deployment_type` | enum | How the tool is deployed | `SaaS`, `on-prem`, `hybrid`, `agent`, `hardware` |
| `users_assets_covered` | string | Scope of what this tool covers | `3000 endpoints`, `all M365 users`, `12 AWS accounts` |
| `primary_capabilities` | pipe-separated | Specific capabilities delivered (not marketing claims) | `log ingestion | correlation rules | dashboards | alert triage` |

---

### Consolidation Analysis Fields

| Field | Type | Description | How to Fill |
|-------|------|-------------|-------------|
| `platform_overlap` | string | Which platform vendor could absorb this tool | `Microsoft Sentinel`, `CrowdStrike Falcon`, `Zscaler ZTE` |
| `overlap_with_tools` | pipe-separated | Other tools in this inventory doing the same job | `Splunk ES | Exabeam` — list both if they overlap |
| `zt_alignment` | enum | Does this tool advance Zero Trust maturity? | See scoring guidance below |
| `removal_risk` | enum | What breaks if you retire this tool tomorrow? | `Low` = easily replaced; `Critical` = compliance or operational dependency |
| `redundancy_flag` | enum | Does another tool in the estate cover the same capability? | `Yes` = full overlap; `Partial` = partial overlap; `No` = unique |
| `recommendation` | enum | Consolidation recommendation | `Retain`, `Consolidate`, `Replace`, `Retire` |
| `notes` | string | Commercial context, renewal leverage, internal politics | `Contract up June 2025; vendor offering 20% renewal discount` |

---

## Scoring Guidance

### ZT Alignment Values

| Value | Definition | Examples |
|-------|-----------|---------|
| `Advancing` | Tool enforces identity-aware, least-privilege, continuous-verification controls | ZTNA, CNAPP, MFA, PAM, workload identity |
| `Neutral` | Tool provides security value but doesn't advance or hinder ZT progress | SIEM, GRC, backup, email security |
| `Perimeter-era` | Tool assumes implicit network trust; becomes redundant as ZT matures | Legacy VPN, on-prem NAC, RADIUS, perimeter IDS |

### Removal Risk Values

| Value | Definition |
|-------|-----------|
| `Critical` | Regulatory/compliance dependency; removal requires board-level sign-off; or operationally essential with no available replacement |
| `High` | Significant detection or protection gap if removed; requires a replacement to be operational first |
| `Medium` | Another tool partially covers the capability; transition risk is manageable |
| `Low` | Full capability overlap exists in another tool; safe to retire after short parallel-run |

### Recommendation Values

| Value | Meaning |
|-------|---------|
| `Retain` | No overlap; best-in-class for this capability; strategic fit |
| `Consolidate` | Keep the capability; migrate to a platform that already covers it |
| `Replace` | Remove and replace with a better/cheaper tool (not a platform you already own) |
| `Retire` | Remove without replacement — capability is either covered elsewhere or no longer needed |

---

## Tips for Filling the Inventory

1. **Pull from finance/procurement first** — actual invoice amounts are more reliable than internal tracking systems
2. **Add opex honestly** — a tool that requires a dedicated analyst to run costs more than the license; a SaaS tool with no integration effort costs less
3. **Use TECH-STACK.md for category names** — consistency matters for the heatmap analysis
4. **Flag contract end dates immediately** — near-term renewals are your negotiation leverage
5. **Don't rationalize overlaps away** — if two tools both do endpoint detection, mark both as overlapping; the analysis will decide which survives
6. **Include "free" tools** — open-source tools (Wazuh, Zeek, OpenCTI) have opex even if no license cost
