# NIST Cybersecurity Framework 2.0

**Version:** CSF 2.0  
**Published:** February 2024  
**Source:** https://www.nist.gov/cyberframework

## Overview

The NIST CSF 2.0 organizes cybersecurity activities into **six Functions** — the backbone of this reference architecture. The framework is outcome-based and vendor-neutral.

## The Six Functions

| Function | ID | Purpose |
|----------|----|---------|
| [Govern](govern.md) | GV | Establish risk management strategy, policies, and organizational accountability |
| [Identify](identify.md) | ID | Understand assets, risks, vulnerabilities, and the threat environment |
| [Protect](protect.md) | PR | Implement safeguards for critical services and assets |
| [Detect](detect.md) | DE | Discover and analyze cybersecurity events and incidents |
| [Respond](respond.md) | RS | Take action on detected incidents |
| [Recover](recover.md) | RC | Restore capabilities and services impaired by incidents |

## What's New in CSF 2.0 (vs. 1.1)

- **Govern function added** — Was embedded across other functions; now explicit. Covers organizational context, supply chain risk, roles/responsibilities, and board-level risk oversight.
- **Scope expanded** — Explicitly addresses all organizations, not just critical infrastructure.
- **Supply chain** — Elevated to a dedicated category within Govern.
- **Profiles and Tiers** — Retained but refined for easier application.

## How This Repository Uses NIST CSF

NIST CSF 2.0 functions serve as the **primary organizing spine** of this reference architecture:

1. Each technology **category** is mapped to a primary NIST function (and secondary functions where applicable)
2. Vendor reference architectures (Microsoft MCRA, Palo Alto ZTA, etc.) are mapped **into** NIST functions, not treated as parallel structures
3. This enables cross-vendor comparison by NIST function

## Vendor Framework Gaps vs. NIST CSF

Most vendor architectures are strong on **Protect + Detect + Respond** and weak on **Govern** and **Recover**:

| Vendor | Govern | Identify | Protect | Detect | Respond | Recover |
|--------|--------|----------|---------|--------|---------|---------|
| Microsoft MCRA | Partial (Purview) | Strong | Strong | Strong | Strong | Weak |
| Palo Alto ZTA | Weak | Partial | Strong | Strong | Strong | Weak |
| Zscaler ZTE | Weak | Partial | Strong | Partial | Weak | None |
| Google CSA | Weak | Strong (Mandiant) | Strong | Strong | Strong | Weak |
| CrowdStrike Falcon | Weak | Strong | Strong | Strong | Strong | None |
| CISA ZTMM | Strong (Governance thread) | Strong | Strong | Strong | Partial | Weak |
| AWS SRA | Weak | Partial | Strong | Strong | Partial | Partial |
| Cisco Security | Weak | Weak | Strong | Strong | Partial | None |
