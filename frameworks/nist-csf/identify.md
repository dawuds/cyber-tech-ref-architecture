# NIST CSF 2.0 — Identify (ID)

Develops understanding of the organization's assets, risks, and threat environment to prioritize cybersecurity efforts consistent with risk management strategy.

## Purpose

You cannot protect what you cannot see. Identify builds the foundational inventory and risk picture that all other functions depend on. It answers: *What assets do we have, what risks do they face, and what are our vulnerabilities?*

## Technology Categories

| Category | Description |
|----------|-------------|
| [Asset Management](../../technologies/categories/identify/asset-management.yaml) | Continuous discovery and inventory of all IT/OT/cloud assets |
| [Vulnerability Management](../../technologies/categories/identify/vulnerability-management.yaml) | Scanning, prioritizing, and tracking vulnerabilities |
| [Attack Surface Management](../../technologies/categories/identify/attack-surface-management.yaml) | External-facing asset discovery from attacker perspective |
| [Threat Intelligence](../../technologies/categories/identify/threat-intelligence.yaml) | Threat actor TTPs, IOCs, and strategic intelligence |
| [Identity Governance (IGA)](../../technologies/categories/identify/identity-governance.yaml) | Who has access to what — identity lifecycle and entitlements |
| [CIEM](../../technologies/categories/identify/ciem.yaml) | Cloud entitlement discovery and right-sizing |

## Key Outcomes (NIST CSF 2.0 Categories)

- **ID.AM** — Asset Management: software, hardware, data, and services inventoried
- **ID.RA** — Risk Assessment: risks identified, analyzed, and prioritized
- **ID.IM** — Improvement: lessons learned integrated; risk posture continuously improved

## Vendor Architecture Coverage

**Strong:** CrowdStrike Falcon (Discover, Spotlight, Intelligence), Google Mandiant (TI, ASM), Palo Alto (Xpanse ASM)  
**Partial:** Microsoft MCRA (Defender EASM, Defender VM), AWS SRA (Inspector, Config), Zscaler (ZDX)  
**Weak:** Cisco Security

## Key Architecture Note

Identify is often treated as a one-time exercise (annual risk assessment) rather than a continuous program. Technology investment in this function — especially ASM and continuous VM — converts it from periodic to real-time, which is the intent of CSF 2.0.
