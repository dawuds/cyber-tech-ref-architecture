# Cyber Technology Reference Architecture

A structured knowledge base mapping cybersecurity frameworks, technology categories, vendor architectures, and implementation patterns — organised around NIST CSF 2.0 as the primary spine.

---

## On This Page
- [Purpose](#purpose) — what this repo is and who it's for
- [Quick Navigation](#quick-navigation) — five themed sections: landscape → architecture → technology selection → consolidation → regulatory
- [Repository Structure](#repository-structure) — full directory map with annotations
- [Core Frameworks](#core-frameworks) — NIST CSF 2.0, Zero Trust pillars, MITRE frameworks
- [Vendor Coverage](#vendor-coverage) — 10 reference architectures + 17 vendor profiles
- [Cross-Referenced Repositories](#cross-referenced-repositories) — OT-Security, AI-Governance, GRC Portfolio
- [M&A Tracker](#ma-tracker-20242025) — 2024–2025 acquisitions affecting product naming
- [Schema Reference](#schema-reference) — YAML structure for technology category files

## At a Glance
- **30+ technology categories** organised against NIST CSF 2.0 functions and Zero Trust pillars
- **10 vendor reference architectures** (Microsoft, Palo Alto, CrowdStrike, Zscaler, Google, Cisco, AWS, Fortinet, Check Point, CISA ZTMM) + **17 vendor profiles**
- **Full MITRE mapping**: ATT&CK Enterprise (14 tactics → tech categories) + D3FEND countermeasures
- **Consolidation methodology**: inventory template, 6-dimension scoring model, worked example (22 tools), and 12-slide deck structure
- **Cross-references**: IEC 62443 OT/ICS (51 SRs), AI governance controls, GRC frameworks (PDPA, BNM RMIT, NACSA)
- **Living reference**: M&A tracker kept current; vendor notes flag acquisition status

---

## Purpose

This repository answers three questions for security architects and CISOs:

1. **What controls do I need?** — NIST CSF 2.0 functions and MITRE frameworks define the outcome requirements
2. **What technology categories deliver those controls?** — 30+ categories mapped to frameworks and Zero Trust pillars
3. **Which vendors and products best fit my context?** — 17 vendor profiles, 10 reference architectures, and a consolidation methodology

It is designed as a living reference — not a one-time assessment. Use it to evaluate tools, plan consolidation, design Zero Trust programmes, and map regulatory requirements to technology controls.

---

## Quick Navigation

### 1. Understand the Market Landscape

| What you need | Where to go |
|--------------|------------|
| Where the industry is consolidating — M&A, PE, absorbed categories | [CONSOLIDATION.md](CONSOLIDATION.md) |
| Where vendor roadmaps are converging — platform strategies, 2027 predictions | [ROADMAP-CONVERGENCE.md](ROADMAP-CONVERGENCE.md) |
| Per-category spend, maturity ratings, and market trends | [CATEGORY-ANALYSIS.md](CATEGORY-ANALYSIS.md) |
| All 39 categories mapped against the 10 major platform vendors | [TECH-STACK.md](TECH-STACK.md) |

### 2. Design Your Architecture

| What you need | Where to go |
|--------------|------------|
| Design a Zero Trust programme from first principles | [Zero Trust Blueprint](architectures/zero-trust-blueprint.md) — NIST 800-207 model, 5 pillars, maturity stages |
| Cloud-native security patterns (landing zones, workload identity, eBPF, service mesh) | [Cloud-Native Patterns](architectures/cloud-native-patterns.md) |
| Data protection end-to-end (discover → classify → protect → monitor → retain) | [Data Protection Blueprint](architectures/data-protection-blueprint.md) |
| See how a specific vendor structures their reference architecture | [architectures/](architectures/) — 10 deep-dive markdowns |

### 3. Select and Evaluate Technologies

| What you need | Where to go |
|--------------|------------|
| Which technology categories defend against a specific ATT&CK tactic | [MITRE ATT&CK → Technology mapping](frameworks/mitre/attack-enterprise.md) |
| Which defensive technique counters a specific attack | [MITRE D3FEND Countermeasures](frameworks/mitre/d3fend-overview.md) |
| Evaluate a specific vendor — strategy, gaps, pricing, direction | [technologies/vendors/](technologies/vendors/) — 17 vendor profiles |
| Compare platforms side-by-side across all categories | [TECH-STACK.md — Vendor Coverage Matrix](TECH-STACK.md#vendor-platform-coverage-matrix) |
| Recommended stack by org size and profile | [ROADMAP-CONVERGENCE.md — Recommended Stacks](ROADMAP-CONVERGENCE.md#recommended-stacks-by-organization-profile) |

### 4. Consolidate Your Tool Estate

| What you need | Where to go |
|--------------|------------|
| **Principles driving consolidation** — cost optimisation, ZT advancement, platform absorption, operational efficiency | [Outcome Themes](consolidation/scoring-methodology.md#outcome-themes-the-why) |
| How to run a consolidation exercise end-to-end | [consolidation/README.md](consolidation/README.md) |
| Scoring model — 6 dimensions, priority bands, presenting to stakeholders | [Scoring Methodology](consolidation/scoring-methodology.md) |
| **Sample artifact: Tool inventory template** (CSV — fill in your estate) | [tool-inventory-template.csv](consolidation/tool-inventory-template.csv) |
| **Sample artifact: Worked example** — 22 tools, 3 scenarios, ZTA delta, contract plan | [example-analysis.md](consolidation/example-analysis.md) |
| **Sample artifact: Executive slide deck** — 12-slide narrative with speaker notes | [slide-deck-approach.md](consolidation/slide-deck-approach.md) |

### 5. Map to Regulatory Frameworks

| What you need | Where to go |
|--------------|------------|
| OT/ICS security — IEC 62443-3-3 (51 SRs) mapped to NIST CSF and technology categories | [IEC 62443 ↔ NIST CSF](cross-references/iec62443-nist-mapping.md) |
| AI governance — EU AI Act, NIST AI RMF, ISO 42001, Malaysia NGAIGE → security controls | [AI Governance ↔ Security](cross-references/ai-governance-security-mapping.md) |
| GRC frameworks — CSA CCM, BNM RMIT, Malaysia PDPA, NACSA Act 854 → tech categories | [GRC Portfolio Mapping](cross-references/grc-portfolio-mapping.md) |

---

## Repository Structure

```
cyber-tech-ref-architecture/
│
├── TECH-STACK.md                    ← Master: all categories × 9-vendor matrix + M&A tracker
├── CATEGORY-ANALYSIS.md             ← Per-category: purpose, vendors, spend, maturity, trends
├── CONSOLIDATION.md                 ← Industry M&A, platform convergence, PE portfolios, 2027 outlook
├── ROADMAP-CONVERGENCE.md           ← Where vendor roadmaps converge → recommended stacks by org profile
│
├── frameworks/
│   ├── nist-csf/                    ← NIST CSF 2.0: one overview per function (Govern → Recover)
│   ├── vendor-architectures/        ← 10 vendor reference architecture YAMLs (structured data)
│   └── mitre/                       ← MITRE ATT&CK Enterprise, D3FEND, ENGAGE, ATLAS
│
├── technologies/
│   ├── _schema.md                   ← YAML schema: fields, types, conventions
│   ├── categories/
│   │   ├── govern/                  ← GRC, TPRM, security awareness, policy management
│   │   ├── identify/                ← Asset mgmt, VM, ASM, threat intel, IGA, CIEM
│   │   ├── protect/                 ← IAM, PAM, secrets, NGFW, ZTNA/SSE/SASE, CASB, DLP,
│   │   │                               email, endpoint, AppSec, WAF, CNAPP, MDM, OT/ICS
│   │   ├── detect/                  ← SIEM, XDR/EDR, NDR, UEBA, deception
│   │   ├── respond/                 ← SOAR, case management, DFIR
│   │   ├── recover/                 ← Backup & recovery, BCP/DR
│   │   └── emerging/                ← AI/LLM security, supply chain security
│   └── vendors/                     ← 17 vendor profiles (platform + specialist)
│
├── architectures/
│   ├── zero-trust-blueprint.md      ← Full ZTA: NIST 800-207 model, 5 pillars, maturity stages
│   ├── data-protection-blueprint.md ← 7-layer data security stack: discover → retain
│   ├── cloud-native-patterns.md     ← 10 cloud security patterns (landing zones, IRSA, eBPF, etc.)
│   ├── microsoft-mcra.md            ← Microsoft MCRA deep-dive
│   ├── palo-alto-zta.md             ← Palo Alto ZTA + Cortex XSIAM
│   ├── zscaler-zte.md               ← Zscaler Zero Trust Everywhere
│   ├── crowdstrike-falcon.md        ← CrowdStrike Falcon platform
│   ├── google-csa.md                ← Google CSA (Chronicle + Mandiant + Wiz)
│   ├── aws-sra.md                   ← AWS Security Reference Architecture
│   ├── cisco-security.md            ← Cisco + Splunk security platform
│   ├── fortinet-security-fabric.md  ← Fortinet Security Fabric + OT/ICS
│   ├── checkpoint-infinity.md       ← Check Point Infinity + ThreatCloud AI
│   └── cisa-ztmm.md                 ← CISA Zero Trust Maturity Model v2.0
│
├── cross-references/
│   ├── iec62443-nist-mapping.md     ← IEC 62443-3-3 (51 SRs) → NIST CSF
│   ├── ai-governance-security-mapping.md ← AI governance controls → security technology
│   └── grc-portfolio-mapping.md     ← CSA CCM, BNM RMIT, Malaysia PDPA, NACSA → tech categories
│
└── consolidation/
    ├── README.md                    ← How to run a consolidation exercise
    ├── tool-inventory-template.csv  ← Blank CSV: fill in your tool estate
    ├── tool-inventory-schema.md     ← Field definitions, scoring guidance
    ├── scoring-methodology.md       ← 6-dimension scoring model, outcome themes, exec presentation guides
    ├── example-analysis.md          ← Worked example: 22-tool estate → 3 scenarios, ZTA delta
    └── slide-deck-approach.md       ← 12-slide deck structure with speaker notes
```

---

## Core Frameworks

### NIST CSF 2.0 (Primary Spine)

All technology categories map to one primary NIST CSF 2.0 function:

| Function | Focus | Key Categories |
|---------|-------|---------------|
| [**Govern**](frameworks/nist-csf/govern.md) | Risk management, policy, compliance | GRC, TPRM, Security Awareness |
| [**Identify**](frameworks/nist-csf/identify.md) | Asset inventory, exposure, risk | VM, ASM, Threat Intel, IGA, CIEM |
| [**Protect**](frameworks/nist-csf/protect.md) | Preventive controls | IAM, PAM, NGFW, ZTNA/SSE, DLP, Email, Endpoint, CNAPP |
| [**Detect**](frameworks/nist-csf/detect.md) | Threat detection | SIEM, XDR/EDR, NDR, UEBA, Deception |
| [**Respond**](frameworks/nist-csf/respond.md) | Incident response | SOAR, Case Management, DFIR |
| [**Recover**](frameworks/nist-csf/recover.md) | Business continuity | Backup & Recovery, BCP/DR |

### Zero Trust Architecture (NIST SP 800-207)

Five pillars with enabling technology per pillar — [full blueprint](architectures/zero-trust-blueprint.md):

| Pillar | Primary Controls |
|--------|----------------|
| **Identity** | IAM/SSO/MFA, PAM, IGA, CIEM, ITDR |
| **Device** | EDR/XDR, MDM/UEM, VM, Device Posture |
| **Network** | ZTNA/SSE/SASE, NGFW, Microsegmentation, NDR |
| **Application** | CASB, WAF/API Security, CNAPP, AppSec |
| **Data** | DSPM, DLP, IRM, Encryption/KMS, DAM |

### MITRE Frameworks

| Framework | Purpose | File |
|---------|---------|------|
| **ATT&CK Enterprise** v15 | 14 tactics × technology countermeasures | [attack-enterprise.md](frameworks/mitre/attack-enterprise.md) |
| **D3FEND** v1.0 | Defensive technique → technology mapping | [d3fend-overview.md](frameworks/mitre/d3fend-overview.md) |
| **ENGAGE** | Deception operations framework | [d3fend-overview.md](frameworks/mitre/d3fend-overview.md) |
| **ATLAS** | Adversarial AI/ML attack taxonomy | [d3fend-overview.md](frameworks/mitre/d3fend-overview.md) |

---

## Vendor Coverage

### Platform Vendors — Reference Architectures + Profiles

| Vendor | Architecture | Profile | Primary Strength |
|--------|------------|---------|-----------------|
| Microsoft | [MCRA](architectures/microsoft-mcra.md) | [Profile](technologies/vendors/microsoft.md) | E5 bundle; native M365 integration |
| Palo Alto Networks | [ZTA](architectures/palo-alto-zta.md) | [Profile](technologies/vendors/palo-alto.md) | Platformization; Cortex XSIAM AI SOC |
| CrowdStrike | [Falcon](architectures/crowdstrike-falcon.md) | [Profile](technologies/vendors/crowdstrike.md) | Single-agent XDR; Charlotte AI |
| Zscaler | [ZTE](architectures/zscaler-zte.md) | [Profile](technologies/vendors/zscaler.md) | Proxy-based SSE; ZPA ZTNA |
| Google | [CSA](architectures/google-csa.md) | [Profile](technologies/vendors/google.md) | Chronicle SIEM; Mandiant TI; Wiz CNAPP |
| Cisco | [Security](architectures/cisco-security.md) | [Profile](technologies/vendors/cisco.md) | Network + Splunk SOC; Talos TI |
| AWS | [SRA](architectures/aws-sra.md) | [Profile](technologies/vendors/aws.md) | Native cloud-embedded security |
| Fortinet | [Security Fabric](architectures/fortinet-security-fabric.md) | [Profile](technologies/vendors/fortinet.md) | OT/ICS + IT convergence; FortiOS |
| Check Point | [Infinity](architectures/checkpoint-infinity.md) | [Profile](technologies/vendors/check-point.md) | Prevention-first; ThreatCloud AI |
| CISA | [ZTMM v2.0](architectures/cisa-ztmm.md) | — | Government ZT maturity reference |

### Specialist Vendors — Profiles

| Vendor | Category | Profile |
|--------|---------|---------|
| Okta | Identity / SSO / MFA | [Profile](technologies/vendors/okta.md) |
| CyberArk | PAM / Secrets | [Profile](technologies/vendors/cyberark.md) |
| Wiz | CNAPP / DSPM | [Profile](technologies/vendors/wiz.md) |
| Splunk (Cisco) | SIEM / SOAR | [Profile](technologies/vendors/splunk.md) |
| Proofpoint | Email Security | [Profile](technologies/vendors/proofpoint.md) |
| Cloudflare | SSE / Edge Security | [Profile](technologies/vendors/cloudflare.md) |
| Tenable | Vulnerability Management | [Profile](technologies/vendors/tenable.md) |
| SentinelOne | EDR / Identity / AI-SIEM | [Profile](technologies/vendors/sentinelone.md) |

---

## Cross-Referenced Repositories

| Companion Repo | Integration Point | File |
|---------------|-----------------|------|
| **OT-Security** | IEC 62443-3-3 (51 SRs) mapped to NIST CSF functions and technology categories | [iec62443-nist-mapping.md](cross-references/iec62443-nist-mapping.md) |
| **AI-Governance** | 22 AI governance controls (EU AI Act, NIST AI RMF, ISO 42001, Malaysia NGAIGE) → security technology | [ai-governance-security-mapping.md](cross-references/ai-governance-security-mapping.md) |
| **GRC Portfolio** | CSA CCM v4, BNM RMIT, Malaysia PDPA, NACSA Act 854 → technology categories | [grc-portfolio-mapping.md](cross-references/grc-portfolio-mapping.md) |

---

## M&A Tracker (2024–2025)

Key acquisitions affecting product naming and positioning in this repository:

| Acquired | By | Date | Notes |
|---------|----|------|-------|
| IBM QRadar SaaS | Palo Alto Networks | Aug 2024 | QRadar SaaS → Cortex; on-prem stays IBM |
| Lacework | Fortinet | Aug 2024 | CNAPP module in Security Fabric |
| Splunk | Cisco | Mar 2024 | Splunk ES + SOAR now Cisco portfolio |
| Wiz | Google (pending) | 2025 | CNAPP → Google Cloud Security ($32B) |
| Exabeam + LogRhythm | Merged | Jul 2024 | Use "Exabeam" brand going forward |
| Noname Security | Akamai | 2024 | API security in Akamai platform |
| Dig Security | Palo Alto | 2024 | DSPM + DDR in Prisma Cloud |
| Attivo Networks | SentinelOne | May 2022 | Singularity Identity |
| Ermetic | Tenable | Oct 2023 | Tenable Cloud Security |

Full analysis and 2027 outlook: [CONSOLIDATION.md](CONSOLIDATION.md)

---

## Schema Reference

Each technology category YAML (`technologies/categories/**/*.yaml`) follows this structure:

```yaml
id:                    # snake_case identifier
name:                  # Short display name
full_name:             # Full product category name
nist_primary:          # Single NIST CSF 2.0 function
nist_secondary:        # Array of secondary functions
description:           # One-paragraph purpose description
related_categories:    # Array of related category IDs
vendor_framework_coverage:
  microsoft_mcra:      # Domain/pillar name, or null if not addressed
  palo_alto_zta:       # ...
  # (10 vendor architectures keyed by vendor id)
products:
  - name:              # Product name
    vendor:            # Vendor name
    platform:          # Parent platform ID if a module; null if standalone
    type:              # SaaS | on-prem | hybrid | open-source | services | hardware
    notes:             # One sentence: differentiator, acquisition status, or market context
```

Full schema: [technologies/_schema.md](technologies/_schema.md)
