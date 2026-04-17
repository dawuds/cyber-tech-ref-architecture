# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

Maps best-practice cybersecurity frameworks (NIST CSF 2.0 as the primary spine) to technology categories and vendor products. Also maps vendor reference architectures (Microsoft MCRA, Palo Alto ZTA, Zscaler ZTE, Google CSA, CrowdStrike Falcon, CISA ZTMM, AWS SRA, Cisco) back into NIST CSF functions for cross-vendor comparison.

## Repository Structure

```
frameworks/
  nist-csf/           ← NIST CSF 2.0 function overviews (govern.md, identify.md, etc.)
  vendor-architectures/ ← One YAML per vendor reference architecture (10 vendors)

technologies/
  _schema.md          ← YAML schema documentation
  categories/
    govern/           ← GRC, TPRM, security awareness, policy management
    identify/         ← Asset management, VM, ASM, threat intel, IGA, CIEM
    protect/          ← IAM, PAM, secrets, NGFW, ZTNA/SSE/SASE, CASB, DLP,
                         email, endpoint, AppSec, WAF, CNAPP, MDM, OT/ICS
    detect/           ← SIEM, XDR/EDR, NDR, UEBA, deception
    respond/          ← SOAR, case management, DFIR
    recover/          ← Backup & recovery, BCP/DR
    emerging/         ← AI/LLM security, supply chain security
  vendors/            ← Vendor profile markdowns (17 vendors: 10 platform + 7 specialist)

architectures/        ← Vendor reference architecture deep-dive markdowns (10 files)

cross-references/     ← Framework integration files from other GRC repos
  iec62443-nist-mapping.md       ← IEC 62443-3-3 → NIST CSF (51 SRs; from OT-Security repo)
  ai-governance-security-mapping.md  ← AI governance controls → security technology (from AI-Governance repo)
  grc-portfolio-mapping.md       ← CSA CCM, RMIT, PDPA, NACSA → technology categories

TECH-STACK.md         ← Master mapping: all categories, 9-vendor matrix, ASM landscape, M&A tracker
CATEGORY-ANALYSIS.md  ← Per-category deep dive: purpose, modules, vendors, spend, maturity, trends
```

## Schema

Each category YAML has: `id`, `name`, `full_name`, `nist_primary`, `nist_secondary`, `description`, `related_categories`, `vendor_framework_coverage` (keyed by vendor id), and `products` (list with `name`, `vendor`, `platform`, `type`, `notes`).

Vendor architecture YAMLs have: `id`, `name`, `version`, `source`, `domains`/`pillars`, and `notes` on gaps.

## Conventions

- NIST CSF 2.0 functions are the canonical organizing spine — never add a product category that doesn't map to a function
- `nist_primary` is always a single function; `nist_secondary` is an array
- Product `type` values: `SaaS`, `on-prem`, `hybrid`, `open-source`, `services`, `hardware`
- If a product is a module of a larger platform, set `platform` to the parent platform id
- `notes` on products: one sentence — differentiator, acquisition status, or market context. No generic descriptions.
- Mark acquisition/merger status in `notes` (e.g., "acquired by X in 2024") — the market consolidates rapidly
- `vendor_framework_coverage`: use `null` when a vendor architecture does not meaningfully address the category; use the domain/pillar name when it does

## Key Design Decisions

- Technology **category** comes before vendor products — categories are the stable layer; products change via M&A
- CTEM (Continuous Threat Exposure Management) is a methodology, not a product category — do not add as a category
- UEBA is kept as a category despite absorption into SIEM/XDR platforms — document consolidation in `market_notes`
- Standalone CASB and SOAR are kept as categories but `market_notes` document their consolidation into SSE and SIEM/XDR
- Emerging categories live in `categories/emerging/` until they reach mainstream adoption

## Sanity Check Notes (2024-2025 M&A)

- Exabeam + LogRhythm merged July 2024 — use "Exabeam" brand
- IBM QRadar SaaS → Palo Alto Networks (Aug 2024); on-prem stays with IBM
- Lacework → Fortinet (Aug 2024)
- Ermetic → Tenable Cloud Security (Oct 2023)
- Attivo Networks → SentinelOne Singularity Identity (May 2022)
- Siemplify → Google Chronicle SOAR (2022)
- Phantom → Splunk SOAR (2018)
- VMware Carbon Black → Broadcom/Symantec (not divested as planned)
- Splunk → Cisco (2024, $28B)
- Wiz → Google (pending 2025, $32B)
- Noname Security → Akamai (2024)
- Omnissa = former VMware EUC division (divested by Broadcom 2024)
