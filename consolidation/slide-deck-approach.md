# Security Tool Consolidation — Slide Deck Structure

**Deck title:** Security Tool Rationalisation: Reducing Cost, Advancing Zero Trust  
**Audience:** CISO + CFO + CIO (executive sponsor deck)  
**Length:** 12 slides + appendix  
**Narrative arc:** Problem → Approach → Findings → Options → Recommendation → Roadmap

---

## Slide 1 — Title

**Title:** Security Tool Rationalisation  
**Subtitle:** Reducing Cost, Closing Gaps, Advancing Zero Trust  
**Visual:** Clean — logo, date, classification marking  
**Speaker notes:** Set the tone: this is not a cost-cutting exercise dressed up as strategy. It is a strategic realignment of the security tool estate to deliver better outcomes at lower cost.

---

## Slide 2 — The Problem (Executive Hook)

**Title:** We Are Paying for Complexity, Not Security

**Three key facts (large numbers, short labels):**
```
    47 tools          $3.8M/year        6 coverage gaps
  in the estate      total spend       (no backup, no IGA,
                                        no cloud CNAPP...)
```

**One-line callout box:**
> "The average enterprise runs 45-75 security tools. More tools create more noise, more blind spots, and more cost — not more security."

**Bottom line:** Tool sprawl is a security problem, not just a cost problem.

**Speaker notes:** Don't lead with savings. Lead with the risk argument: fragmented tools mean fragmented telemetry, which means slower detection and slower response. The cost case will land harder after the risk case is made.

---

## Slide 3 — What We Are Solving For (Outcome Themes)

**Title:** Three Outcomes This Exercise Delivers

**Three columns, each with icon, title, and 2-line description:**

| Cost Optimisation | Zero Trust Advancement | Operational Efficiency |
|:-:|:-:|:-:|
| Eliminate redundant tools and platform-bundle opportunities. Target: 25-35% cost reduction. | Replace perimeter-era tools with identity-aware, continuous-verification equivalents. | Fewer vendors, fewer consoles, better telemetry fidelity → faster detection and response. |

**Note at bottom:** This is not a cost-cutting exercise. Cost reduction is a byproduct of strategic alignment.

---

## Slide 4 — Our Approach (The Methodology)

**Title:** A Capability-First Methodology (Not Tool-First)

**Four-step process visual (horizontal flow):**

```
[1. INVENTORY]      [2. MAP]           [3. SCORE]          [4. SEQUENCE]
 Capture every   →  Map to outcomes  →  Prioritise by    →  Build contract-
 tool, cost,        (NIST CSF,          consolidation       aligned roadmap
 and capability     ZT pillar,          score (6            with defined
                    ATT&CK coverage)    dimensions)         exit points
```

**Key principle callout:**
> Tools are mapped to capabilities — not the reverse. If two tools claim the same capability, only one survives.

**Speaker notes:** Explain the 6 scoring dimensions briefly: capability uniqueness, cost efficiency, platform absorption potential, ZT alignment, operational overhead, removal risk. Full detail in the methodology appendix.

---

## Slide 5 — Current State: What We Found

**Title:** Current Estate: [X] Tools Across [Y] Vendors

**Left side — Coverage Heatmap (table):**

```
              Identity  Device  Network  App  Data  Visibility
Govern           —        —        —      —    —        —
Identify         —        ██       —      —    ▓        —
Protect          ██       ██       ██     ▓    ██       —
Detect           —        ▓        —      ▓    —        ██
Respond          ▓        —        —      —    —        ▓
Recover          ✗        ✗        ✗      ✗    ✗        ✗
```

Legend: `██` Over-covered (blue) | `▓` Adequate (green) | `✗` Gap (red) | `—` N/A

**Right side — Three callouts:**
- 🔴 **Critical gap:** No backup/recovery coverage — ransomware resilience is unaddressed
- 🔵 **Over-covered:** Device detection (3 EDR tools) — paying 3x for same capability
- 🟡 **Compliance risk:** No IGA — access certifications are manual; MAS TRM finding risk

**Speaker notes:** The heatmap is the most important visual in the deck. It reframes the conversation from "how many tools do we have" to "what are we actually covered for." Executives respond to red cells.

---

## Slide 6 — The Overlaps (Where We're Paying Twice)

**Title:** [X] Tools Are Redundant — We Are Paying $[Y]K for Overlap

**Table (top overlaps only — keep to 6-8 rows):**

| Redundant Tool | Annual Cost | Covered By | Saving |
|---------------|------------|------------|--------|
| Exabeam UEBA | $225K | Splunk ML UEBA (already licensed) | $225K |
| RSA SecurID | $160K | Okta MFA (already deployed) | $160K |
| Carbon Black EDR | $155K | CrowdStrike Falcon (already deployed) | $155K |
| Tenable.io VM | $80K | Qualys VMDR (retained) | $80K |
| McAfee DLP (endpoint) | $140K | M365 E5 Purview DLP (licence upgrade) | $55K net |
| Rapid7 InsightIDR | $115K | Splunk SOAR module (add-on) | $75K net |
| **Total** | **$875K** | | **$750K net** |

**Callout:** Quick wins achievable within 12 months using contract end dates as natural exit points.

---

## Slide 7 — Zero Trust Gap Analysis

**Title:** 3 Tools Are Actively Working Against Zero Trust

**Left: ZTA pillar maturity (before/after — spider chart or table):**

| Pillar | Today | 24-Month Target | Key Change |
|--------|-------|----------------|-----------|
| Identity | Initial | Advanced | Add IGA; retire RSA (legacy MFA) |
| Device | Initial | Advanced | Retire Carbon Black; unify on CrowdStrike |
| Network | **Traditional** | Initial | Deploy ZTNA; **retire VPN** |
| Application | Initial | Initial | No change in this scenario |
| Data | **Traditional** | Initial | Activate Purview DLP; basic classification |
| Visibility | Initial | Advanced | Unified SIEM telemetry; AI-assisted triage |

**Right: The three perimeter-era tools to exit:**

```
1. Cisco AnyConnect VPN    → Replace with Zscaler ZPA (ZTNA)
   "Users connect to networks" → "Users connect to apps"

2. RSA SecurID (on-prem)   → Already replaced by Okta
   Implicit network MFA       Retire at contract end Nov-25

3. Forescout NAC           → Replace with device posture signal
   Perimeter device trust      (CrowdStrike + Okta Conditional Access)
```

---

## Slide 8 — Three Scenarios (The Options)

**Title:** Three Paths Forward — Choose Your Ambition Level

**Three columns:**

| | **Scenario A** | **Scenario B** | **Scenario C** |
|-|:---:|:---:|:---:|
| **Name** | Quick Wins | ZT Transformation | Platform Consolidation |
| **Timeline** | 12 months | 24 months | 36 months |
| **Tools: now → future** | 22 → 16 | 22 → 14 | 22 → 12 |
| **Annual saving** | $750K | $590K net | **$1.43M** |
| **New investment** | $125K | $640K | $640K + migration |
| **ZT maturity gain** | Minimal | **+1–2 stages all pillars** | +2–3 stages |
| **Coverage gaps closed** | 1 | 4 | **6 (all)** |
| **Complexity** | Low | Medium | High |

**Bottom recommendation flag:**
> Recommended: **Scenario B** — best balance of financial return, ZT advancement, and compliance risk reduction within a 24-month delivery window.

---

## Slide 9 — Financial Case

**Title:** The Business Case: $[X]M Saving Over 3 Years

**Waterfall chart (describe the visual):**

```
$3.78M  ──────────────────────────────────────────
        │
-$750K  ├──── Quick wins (Scenario A tools retired)
        │
-$350K  ├──── Perimeter tools retired (VPN, Forescout)
        │
+$515K  ├──── Net new investment (ZPA, Wiz, Veeam, IGA)
        │
-$430K  ├──── Platform migration saving (Splunk → Sentinel, Scenario C)
        │
$2.35M  └──────────────────────────────────────────  (Year 3 run-rate)
```

**Three-year cumulative saving:** ~$2.8M (Scenario C)  
**Payback period:** 14 months  

**Bottom callout:** Cost savings fund the capability gaps (backup, IGA, CNAPP) — the program is largely self-financing.

---

## Slide 10 — The Roadmap

**Title:** Sequenced Execution — Led by Contract End Dates

**Timeline visual (4 rows: Quick Wins / Perimeter Exits / New Capabilities / Platform):**

```
2025 Q2   │ Retire McAfee DLP → activate Purview DLP
          │ Retire Tenable.io → consolidate on Qualys

2025 Q3   │ Retire Carbon Black → CrowdStrike verified
          │ Retire Forescout → CrowdStrike device posture
          │ Retire Rapid7 → Splunk SOAR active
          │ Retire Exabeam UEBA → Splunk ML covers

2025 Q4   │ Retire RSA SecurID → Okta MFA primary
          │ Deploy Zscaler ZPA (parallel with VPN)
          │ Procure SailPoint IGA

2026 Q1   │ Retire Cisco VPN → ZPA pilot passed
          │ Veeam Hardened Backup deployed

2026 Q2   │ Wiz CNAPP deployed
          │ M365 E5 upgrade completed

2026 Q4   │ Splunk renewal decision → Sentinel migration starts (Scenario C)

2027      │ Full ZT Advanced maturity target
          │ 12 tools, 11 vendors, $2.35M run-rate
```

**Callout:** No forced retirements — every exit aligned to contract end date.

---

## Slide 11 — Risks and Mitigations

**Title:** Key Risks and How We Manage Them

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Detection gap during tool transition | Medium | High | Parallel-run minimum 30 days before retirement |
| Platform feature parity not met | Medium | Medium | POC/pilot before commitment; keep incumbent on rolling month-to-month |
| Splunk → Sentinel migration complexity | High | Medium | Phased migration; start with M365 data sources; keep Splunk for 6 months post-cutover |
| Stakeholder resistance (tool owners) | High | Medium | Capability ownership stays with team; tool changes are the implementation detail |
| VPN retirement before ZPA fully adopted | Low | High | Hard dependency: ZPA 100% coverage validated before VPN decommission begins |
| Contract penalty on early exit | Low | Low | All retirements timed to natural contract end dates |

---

## Slide 12 — Recommendation and Ask

**Title:** Recommendation: Approve Scenario B with Scenario C Option

**Three asks (large, clear):**

```
ASK 1: Approve the consolidation programme
        Scenario B baseline (24 months, $590K net saving)

ASK 2: Fund the capability gaps
        $515K new investment (ZPA, Wiz, Veeam, IGA)
        Self-funded from tool retirement savings by Month 8

ASK 3: Authorise Scenario C evaluation
        Splunk renewal decision (March 2026)
        Sentinel migration assessment Q3 2025
```

**Bottom line:**
> 22 tools → 14 tools. $3.78M → $3.19M (24m) → $2.35M (36m).  
> Zero Trust: Traditional → Advanced across all pillars.  
> All critical compliance gaps (backup, IGA, cloud posture) closed.

---

## Appendix Slides

### A1 — Full Tool Inventory with Scores
Full 22-row scoring table (from example-analysis.md)

### A2 — Scoring Methodology Detail
6-dimension scoring model; priority band definitions

### A3 — ZTA Maturity Framework Reference
CISA ZTMM v2.0 — 4 stages per pillar (from architectures/cisa-ztmm.md)

### A4 — NIST CSF Coverage by Tool (Full Heatmap)
Detailed version with all 22 tools mapped to NIST CSF functions

### A5 — ATT&CK Coverage Delta
Which MITRE ATT&CK techniques are better covered post-consolidation (from example-analysis.md)

### A6 — Vendor Consolidation Summary
From 18 vendors → 11 vendors. Which relationships remain; which are exited.

### A7 — Commercial Negotiation Leverage Points
Contract end dates; multi-product commitments; competitive alternatives for each renewal

---

## Slide Design Notes

**Colour coding (consistent throughout):**
- 🔴 Red = gap / risk / retire / perimeter-era
- 🟠 Amber = partial coverage / evaluate
- 🟢 Green = retained / advancing ZT / adequate
- 🔵 Blue = over-covered / consolidation candidate
- ⬛ Grey = out of scope / N/A

**Slide principles:**
- One message per slide — title states the conclusion, not the topic
- Lead with the so-what, not the analysis
- All financial figures net of investment, not gross
- ZT maturity shown as before/after — not abstract framework description
- Appendix carries all supporting detail — main deck max 12 slides

**What to avoid:**
- Tool logo walls (vendor-centric, not outcome-centric)
- Feature comparison matrices in the main deck (belongs in appendix)
- Percentage savings without absolute numbers (both matter to CFO)
- Security jargon without definition in any exec-facing slide
