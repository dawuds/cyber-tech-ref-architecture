# Example Consolidation Analysis — Acme Financial Corp

**Profile:** 3,000 employees | Hybrid cloud (AWS primary + Azure M365) | Financial services (MAS TRM / PCI DSS regulated)  
**Current tool count:** 22 security tools  
**Current total annual spend:** $3.78M (licence + opex)  
**Analysis date:** April 2025

---

## On This Page
- [Current Tool Inventory](#current-tool-inventory) — all 22 tools with cost, ZT alignment, and redundancy flag
- [Scoring Results](#scoring-results) — priority scores and recommendations for each tool
- [Coverage Heatmap: Before Consolidation](#coverage-heatmap-before-consolidation) — gaps and over-coverage visualised
- [Consolidation Scenarios](#consolidation-scenarios) — Scenario A (12m), B (24m), C (36m) with financial cases
- [Executive Summary: Before vs. After](#executive-summary-before-vs-after) — tool count, spend, ZT maturity, coverage gaps across all scenarios
- [ZTA Maturity Delta: Scenario B](#zta-maturity-delta-scenario-b) — pillar-by-pillar maturity improvement
- [Sequencing: Contract-Driven Execution Plan](#sequencing-contract-driven-execution-plan) — quarterly exit plan aligned to contract end dates
- [ATT&CK Coverage Delta](#appendix-attck-coverage-delta) — which tactics are better covered post-consolidation

## At a Glance
- **22 tools, $3.78M/year** — 18 vendors, 3 perimeter-era tools actively undermining Zero Trust
- **6 tools are immediately redundant** — $750K quick-win saving available without any new investment
- **3 perimeter-era tools to exit**: Cisco AnyConnect VPN, RSA SecurID, Forescout NAC
- **Scenario B (24 months)**: 22 → 14 tools, $590K net saving, ZT maturity advances +1–2 stages across all 5 pillars
- **Scenario C (36 months)**: 22 → 12 tools, **$1.43M annual saving**, full ZT Advanced maturity, all 6 coverage gaps closed
- **All exits are contract-aligned** — no forced early termination penalties; sequenced to contract end dates from May 2025 onward

---

## Current Tool Inventory

| # | Tool | Vendor | Category | NIST | ZT Pillar | License $K | Opex $K | Total $K | Contract End | ZT Alignment | Redundancy |
|---|------|--------|---------|------|-----------|-----------|---------|---------|-------------|-------------|-----------|
| 1 | Splunk Enterprise Security | Cisco/Splunk | SIEM | Detect | Visibility | 480 | 120 | 600 | 2026-03 | Neutral | Partial |
| 2 | Exabeam UEBA | Exabeam | UEBA | Detect | Visibility | 180 | 45 | 225 | 2025-09 | Neutral | **Yes** |
| 3 | CrowdStrike Falcon Complete | CrowdStrike | EDR/XDR | Detect | Device | 320 | 30 | 350 | 2026-06 | Advancing | No |
| 4 | Carbon Black EDR (legacy) | Broadcom | EDR | Detect | Device | 95 | 60 | 155 | 2025-07 | Neutral | **Yes** |
| 5 | Cisco AnyConnect VPN | Cisco | VPN | Protect | Network | 65 | 40 | 105 | 2025-12 | **Perimeter-era** | Partial |
| 6 | Zscaler ZIA | Zscaler | SSE/SWG | Protect | Network | 180 | 25 | 205 | 2027-01 | Advancing | No |
| 7 | Okta Workforce Identity | Okta | IAM/SSO/MFA | Protect | Identity | 145 | 20 | 165 | 2026-04 | Advancing | Partial |
| 8 | RSA SecurID (on-prem MFA) | RSA Security | MFA | Protect | Identity | 85 | 75 | 160 | 2025-11 | **Perimeter-era** | **Yes** |
| 9 | CyberArk Privilege Cloud | CyberArk | PAM | Protect | Identity | 220 | 35 | 255 | 2026-09 | Advancing | No |
| 10 | Qualys VMDR | Qualys | VM | Identify | Device | 95 | 25 | 120 | 2025-10 | Neutral | **Yes** |
| 11 | Tenable.io | Tenable | VM | Identify | Device | 60 | 20 | 80 | 2025-06 | Neutral | **Yes** |
| 12 | Palo Alto PA-3200 (DC NGFW) | Palo Alto | NGFW | Protect | Network | 180 | 55 | 235 | 2027-06 | Neutral | No |
| 13 | Forescout NAC | Forescout | NAC | Protect | Device | 95 | 45 | 140 | 2025-08 | **Perimeter-era** | Partial |
| 14 | Varonis | Varonis | DSPM/DAG | Identify | Data | 140 | 30 | 170 | 2026-02 | Advancing | No |
| 15 | McAfee DLP (endpoint legacy) | Trellix | DLP | Protect | Data | 75 | 65 | 140 | 2025-05 | Neutral | **Yes** |
| 16 | Microsoft M365 E3 (security) | Microsoft | Email/Endpoint | Protect | Device | 200 | 15 | 215 | rolling | Advancing | Partial |
| 17 | Proofpoint TAP | Proofpoint | Email Security | Protect | Application | 120 | 15 | 135 | 2026-01 | Neutral | Partial |
| 18 | Archer GRC | OpenPages/IBM | GRC | Govern | — | 120 | 40 | 160 | 2026-11 | Neutral | No |
| 19 | Rapid7 InsightIDR | Rapid7 | DFIR | Respond | Visibility | 85 | 30 | 115 | 2025-09 | Neutral | **Yes** |
| 20 | PagerDuty (incident mgmt) | PagerDuty | Case Mgmt | Respond | — | 35 | 5 | 40 | rolling | Neutral | Partial |
| 21 | Cofense PhishMe | Cofense | Security Awareness | Govern | — | 35 | 10 | 45 | 2026-03 | Neutral | No |
| 22 | AWS Security Hub + GuardDuty | AWS | CNAPP/CSPM | Detect | Application | 45 | 20 | 65 | PAYG | Advancing | Partial |
| | **TOTAL** | | | | | **3,055** | **725** | **3,780** | | | |

---

## Scoring Results

Scored per [scoring-methodology.md](scoring-methodology.md). Fields: Uniqueness (U), Cost Efficiency (CE), Platform Absorption (PA), ZT Alignment (ZTA), Ops Overhead (OO), Removal Risk (RR).

**Priority Score = (5-U) + (5-CE) + PA + (5-ZTA) + (5-OO) - RR**

| # | Tool | U | CE | PA | ZTA | OO | RR | **Score** | **Band** | **Recommendation** |
|---|------|---|----|----|-----|----|----|-----------|----------|-------------------|
| 2 | Exabeam UEBA | 1 | 2 | 5 | 3 | 3 | 2 | **21** | Retire/Consolidate Now | **Retire** — Splunk ML + CrowdStrike UEBA covers this |
| 8 | RSA SecurID | 1 | 1 | 5 | 1 | 1 | 2 | **21** | Retire/Consolidate Now | **Retire** — Okta MFA is deployed and covers this entirely |
| 15 | McAfee DLP | 1 | 1 | 5 | 3 | 1 | 2 | **20** | Retire/Consolidate Now | **Retire** — M365 E5 Purview DLP replaces with licence upgrade |
| 4 | Carbon Black EDR | 1 | 2 | 5 | 3 | 2 | 2 | **20** | Retire/Consolidate Now | **Retire** — CrowdStrike is deployed; parallel-run then exit |
| 11 | Tenable.io | 1 | 3 | 4 | 3 | 4 | 2 | **17** | Consolidate 6–12m | **Consolidate** — retain Qualys VMDR; retire Tenable at Jun-25 renewal |
| 5 | Cisco VPN | 2 | 3 | 4 | 1 | 3 | 3 | **17** | Consolidate 6–12m | **Replace** — deploy Zscaler ZPA; retire VPN at Dec-25 renewal |
| 19 | Rapid7 InsightIDR | 2 | 3 | 4 | 3 | 3 | 2 | **16** | Consolidate 6–12m | **Consolidate** — Splunk SOAR covers IR workflow; retire at Sep-25 |
| 13 | Forescout NAC | 2 | 2 | 3 | 1 | 2 | 3 | **15** | Consolidate 6–12m | **Replace** — CrowdStrike device posture + Okta CA replaces function |
| 10 | Qualys VMDR | 3 | 3 | 3 | 3 | 3 | 3 | **10** | Evaluate at renewal | **Retain** — consolidate onto this after Tenable retired; reassess Oct-25 |
| 1 | Splunk ES | 3 | 2 | 2 | 3 | 2 | 4 | **9** | Evaluate at renewal | **Retain** — strategic SIEM; evaluate migration to Cisco XDR at 2026 renewal |
| 6 | Zscaler ZIA | 4 | 3 | 2 | 5 | 4 | 3 | **7** | Retain | **Retain** — strategic ZT platform; expand to ZPA |
| 7 | Okta Workforce | 4 | 3 | 2 | 5 | 4 | 4 | **6** | Retain | **Retain** — strategic identity platform |
| 9 | CyberArk PAM | 5 | 3 | 2 | 5 | 3 | 4 | **5** | Retain | **Retain** — no platform equivalent at this depth; PCI/MAS dependency |
| 3 | CrowdStrike Falcon | 4 | 3 | 2 | 5 | 4 | 4 | **5** | Retain | **Retain** — strategic EDR/XDR platform; expand capabilities |
| 12 | Palo Alto PA NGFW | 4 | 3 | 2 | 3 | 2 | 4 | **5** | Retain | **Retain** — DC perimeter; no cloud replacement yet |
| 14 | Varonis | 4 | 3 | 2 | 4 | 3 | 3 | **5** | Retain | **Retain** — unique file/identity depth; reassess if Wiz DSPM expands |
| 17 | Proofpoint TAP | 3 | 3 | 3 | 3 | 4 | 3 | **5** | Retain | **Retain** — BEC depth justifies cost; evaluate vs. Defender at 2026 renewal |
| 16 | Microsoft M365 E3 | 4 | 4 | 5 | 4 | 5 | 4 | **4** | Retain | **Retain + Upgrade** — upgrade to E5; unlocks Purview DLP, Defender XDR, UEBA |
| 22 | AWS Security Hub | 4 | 5 | 3 | 4 | 5 | 3 | **4** | Retain | **Retain** — PAYG; native AWS; expand with Wiz if multi-cloud grows |
| 18 | Archer GRC | 4 | 3 | 1 | 3 | 2 | 4 | **3** | Retain | **Retain** — no platform covers GRC depth; MAS regulatory dependency |
| 21 | Cofense PhishMe | 4 | 4 | 2 | 3 | 4 | 2 | **3** | Retain | **Retain** — low cost; phishing simulation unique; no platform covers this |
| 20 | PagerDuty | 3 | 4 | 3 | 3 | 5 | 2 | **3** | Retain | **Retain** — evaluate native Splunk incident management at 2026 renewal |

---

## Coverage Heatmap: Before Consolidation

```
              Identity  Device   Network  Application  Data   Visibility
Govern           -        -        -          -          -        -
Identify         -        B        -          -          G        -
Protect          B        B        B          G          B        -
Detect           -        G        -          Y          -        B
Respond          -        -        -          -          -        G
Recover          R        R        R          R          R        R
```

**Key:**
- `B` = Blue (over-covered — consolidation candidate)
- `G` = Green (adequate single coverage)
- `Y` = Yellow (single tool, medium risk)
- `R` = Red (gap — no coverage)
- `-` = Not applicable to this pillar

**Gaps identified:**
- Recover function: **no coverage** — no immutable backup, no BCP/DR tool in estate
- Govern × Identity/Device: no IGA (Identity Governance) — access certifications done manually
- Detect × Application: limited — AWS GuardDuty only; no CNAPP for cloud application workloads

---

## Consolidation Scenarios

### Scenario A: Tactical — Quick Wins Only (12-month horizon)

Retire the 6 highest-scoring tools. No new platform investment required.

| Action | Tool Retired | Replaced By | Annual Saving |
|--------|-------------|-------------|--------------|
| Retire Exabeam UEBA | Exabeam ($225K) | Splunk ML UEBA (already licensed) | $225K |
| Retire RSA SecurID | RSA ($160K) | Okta MFA (already deployed) | $160K |
| Retire Carbon Black | CB ($155K) | CrowdStrike (already deployed) | $155K |
| Retire Tenable.io | Tenable ($80K) | Qualys VMDR (retained) | $80K |
| Retire Rapid7 InsightIDR | Rapid7 ($115K) | Splunk SOAR (add $40K module) | $75K net |
| Retire McAfee DLP | McAfee ($140K) | M365 E5 upgrade (add $85K/yr) | $55K net |

**Scenario A Result:**
- Tools retired: 6
- Gross savings: $875K
- New investment: $125K (Splunk SOAR module + M365 E5 delta)
- **Net annual saving: $750K (20% of total spend)**
- Timeline: completable within 12 months using contract end dates

---

### Scenario B: Strategic — ZT Transformation (24-month horizon)

Scenario A + replace legacy perimeter tools + close the critical gaps.

**Additional actions beyond Scenario A:**

| Action | Investment | Replaces | Outcome |
|--------|-----------|---------|---------|
| Deploy Zscaler ZPA | +$120K/yr | Cisco VPN ($105K) | ZT Network pillar: Traditional → Initial |
| Retire Forescout NAC | -$140K | CrowdStrike device posture + Okta CA | ZT Device: Initial → Advanced |
| Add Wiz CNAPP | +$180K/yr | AWS Security Hub (retain at lower tier) | Close cloud application gap |
| Add Veeam Hardened Backup | +$95K/yr | (gap — no backup existed) | Close Recover gap |
| Add SailPoint IGA (basic) | +$120K/yr | (gap — manual access certs) | MAS TRM + PCI compliance |

**Scenario B Result:**
- Tools retired: 8 (Scenario A + VPN + Forescout + Carbon Black)
- Net new tools added: 4 (ZPA, Wiz, Veeam, SailPoint basic)
- Additional gross savings from retirements: +$350K
- Additional new investment: +$515K/yr
- **Net position vs. today: -$585K/yr (15% reduction) plus significantly higher coverage**
- ZTA maturity improvement: +1 to +2 stages across all 5 pillars

---

### Scenario C: Platform Consolidation (36-month horizon)

Scenario B + migrate Splunk to a next-generation AI SOC platform.

**Key decision: Splunk ($600K/yr) vs. platform alternatives**

| Option | Platform | Cost | Benefit | Risk |
|--------|---------|------|---------|------|
| Renew Splunk ES | Cisco/Splunk | $480K/yr | Familiar; Splunk SOAR included | No XDR convergence; Cisco integration unclear |
| Migrate to Sentinel | Microsoft | $300K/yr (consumption) | Native M365/Azure; E5 UEBA included; Copilot for Security | Data ingestion cost varies; needs tuning investment |
| Migrate to CrowdStrike LogScale | CrowdStrike | $280K/yr (flat) | Native CrowdStrike telemetry; Charlotte AI | Limited third-party connector breadth vs. Splunk |
| Migrate to Google Chronicle | Google | $250K/yr (flat-cost) | Best for high-volume ingestion; Mandiant TI | No native AWS/Azure integration depth |

**Recommended:** Microsoft Sentinel — given M365 E5 upgrade in Scenario A, Sentinel at near-zero marginal cost for M365 data; CrowdStrike connector mature; UEBA native; Copilot for Security adds AI-assisted triage.

**Scenario C Result:**
- Tools retired from Scenario B + Splunk replaced
- **Total tools: 22 → 12 (45% reduction)**
- **Total spend: $3.78M → $2.35M (38% reduction = $1.43M annual saving)**
- Full ZT coverage across all 5 pillars at Initial–Advanced maturity
- Recovered function addressed (Veeam)
- Compliance posture: MAS TRM + PCI DSS addressed via IGA + PAM + DAM coverage

---

## Executive Summary: Before vs. After

| Metric | Current State | Scenario A (12m) | Scenario B (24m) | Scenario C (36m) |
|--------|-------------|-----------------|-----------------|-----------------|
| Tool count | 22 | 16 | 14 | 12 |
| Annual spend | $3.78M | $3.03M | $3.19M | $2.35M |
| Annual saving | — | $750K | $590K net | **$1.43M** |
| ZT maturity (avg) | Traditional–Initial | Initial | Initial–Advanced | Advanced |
| Coverage gaps | 6 red cells | 5 red cells | 2 red cells | 0 red cells |
| Vendor count | 18 | 14 | 14 | 11 |
| Perimeter-era tools | 3 | 2 | 0 | 0 |

---

## ZTA Maturity Delta: Scenario B

| ZTA Pillar | Current | Post-Scenario B | Change | Key Driver |
|-----------|---------|----------------|--------|-----------|
| Identity | Initial | Advanced | +1 | Add IGA (SailPoint); retire RSA; Okta as IdP |
| Device | Initial | Advanced | +1 | Retire Carbon Black + Forescout; CrowdStrike unified posture |
| Network | Traditional | Initial | +1 | ZPA replaces VPN; ZIA enforced for all internet traffic |
| Application | Initial | Initial | 0 | Wiz CNAPP improves posture but Application ZT needs WAAP/API work |
| Data | Traditional | Initial | +1 | Varonis retained; M365 Purview DLP active; basic classification deployed |
| Visibility | Initial | Advanced | +1 | Unified telemetry (fewer tools → better SIEM fidelity); Charlotte AI |

---

## Sequencing: Contract-Driven Execution Plan

```
2025 Q2 (May-Jun)
  ✓ Retire McAfee DLP (contract May-2025) → activate M365 E5 Purview DLP
  ✓ Retire Tenable.io (contract Jun-2025) → consolidate VM onto Qualys

2025 Q3 (Jul-Sep)
  ✓ Retire Carbon Black (contract Jul-2025) → 30-day parallel with CrowdStrike verified
  ✓ Retire Forescout NAC (contract Aug-2025) → CrowdStrike device posture + Okta CA
  ✓ Retire Rapid7 InsightIDR (contract Sep-2025) → activate Splunk SOAR module
  ✓ Retire Exabeam UEBA (contract Sep-2025) → Splunk ML UEBA covers baseline

2025 Q4 (Oct-Dec)
  ✓ Retire RSA SecurID (contract Nov-2025) → Okta MFA fully validated
  ~ Begin Zscaler ZPA deployment (parallel with VPN)
  ~ Procure SailPoint IGA (basic) — start onboarding

2026 Q1 (Jan-Mar)
  ~ Complete ZPA deployment; begin VPN decommission pilot
  ~ Retire Cisco VPN at Dec-2025 contract end (if ZPA pilot passes)

2026 Q2 (Apr-Jun)
  ~ Procure Wiz CNAPP; begin cloud posture assessment
  ~ Okta renewal (Apr-2026) — leverage multi-product commitment for pricing

2026 Q3-Q4
  ~ Wiz CNAPP active; AWS Security Hub downscoped
  ~ Add Veeam Hardened Repository (close Recover gap)
  ~ Evaluate Splunk renewal (Mar-2026) vs. Sentinel migration decision

2027+
  ~ Splunk → Sentinel migration (if Scenario C selected)
  ~ Full ZT Advanced maturity target
```

---

## Appendix: ATT&CK Coverage Delta

Post-Scenario B consolidation improves detection coverage for these key technique groups:

| ATT&CK Tactic | Current Coverage | Post-Consolidation | Improvement |
|--------------|-----------------|-------------------|-------------|
| Initial Access | Proofpoint (email) + NGFW | + ZPA ZTNA (no implicit network access) | Lateral phishing harder |
| Credential Access | CyberArk + Okta | + Okta CA device posture; no RSA bypass path | Credential theft harder |
| Lateral Movement | Splunk correlation | + CrowdStrike XDR (unified agent sees all lateral) | Faster detection |
| Exfiltration | McAfee DLP (endpoint) | Purview DLP (endpoint) + Zscaler ZIA (network inline) | Dual-layer DLP |
| Command & Control | NGFW + ZIA | + Zscaler ZIA DNS security + CrowdStrike C2 detection | DNS-C2 coverage added |
| Impact (Ransomware) | Detection only | + Veeam immutable backup (Recover function) | Recovery capability added |

Reference: [MITRE ATT&CK mapping](../frameworks/mitre/attack-enterprise.md) | [D3FEND countermeasures](../frameworks/mitre/d3fend-overview.md)
