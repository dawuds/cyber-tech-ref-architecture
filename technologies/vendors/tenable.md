# Tenable — Vendor Profile

**Type:** Specialist Leader (Vulnerability Management / Exposure Management)  
**HQ:** Columbia, MD, USA  
**Revenue:** ~$950M (FY2024)  
**Category:** [Vulnerability Management](../categories/identify/vulnerability-management.yaml) | [Attack Surface Management](../categories/identify/attack-surface-management.yaml)

---

## Overview

Tenable is the market-defining vulnerability management vendor, originating from Nessus — the most widely deployed vulnerability scanner in history (created by Renaud Deraison in 1998). From the original open-source scanner, Tenable built an enterprise VM platform (Tenable.io / Tenable.sc) and in recent years evolved into an **Exposure Management** company under the "Tenable One" platform narrative.

Tenable's strategic evolution mirrors the market: from point-in-time network scanning → continuous VM → risk-based VM → unified exposure management that combines traditional VM + CAASM + OT + Active Directory + cloud posture + ASM.

---

## Product Portfolio

| Product | Category | Notes |
|---------|----------|-------|
| Tenable One | Unified Exposure Management | Platform aggregating all Tenable products with unified risk scoring |
| Tenable Nessus (Pro/Expert) | VM (SMB/departmental) | Industry-standard scanner; 70,000+ plugins; most widely deployed |
| Tenable Vulnerability Management (Tenable.io) | VM (Enterprise, SaaS) | Cloud-based VM platform; continuous assessment, CMDB integration |
| Tenable Security Center (Tenable.sc) | VM (Enterprise, on-prem) | On-premises VM for air-gapped or sovereignty requirements |
| Tenable Web App Scanning (WAS) | Application VM | DAST-based web app vulnerability scanning |
| Tenable Cloud Security (Ermetic) | CNAPP / CIEM / CSPM | Acquired Ermetic 2023; cloud identity + posture management |
| Tenable Identity Exposure (AD) | Active Directory Security | AD and Entra ID misconfiguration detection; Alsid acquisition (2021) |
| Tenable OT Security (Indegy) | OT/ICS Security | Passive OT/ICS asset discovery and vulnerability management |
| Tenable ASM (Bit Discovery) | EASM | External attack surface management; Bit Discovery acquisition (2022) |
| Tenable Attack Path Analysis | CTEM-adjacent | Attack path visualization connecting vulnerabilities to blast radius |
| Tenable Lumin | Risk Quantification | Cyber exposure scoring and benchmarking vs. industry peers |

---

## Strengths

- **VM market leadership** — Gartner MQ Leader 13+ consecutive years; Nessus is the industry reference scanner
- **Plugin breadth** — 70,000+ Nessus plugins; fastest coverage of new CVEs (often same day as NVD publication)
- **OT/ICS** — Tenable OT Security (Indegy) provides passive OT vulnerability management; convergence of IT and OT VM in one platform
- **Active Directory security** — Identity Exposure (Alsid) is top-3 in AD security; misconfigurations + real-time attack detection
- **Cloud (Ermetic/CIEM)** — Ermetic acquisition (2023) adds strong cloud identity + entitlement management (CIEM)
- **Tenable One** — unified risk scoring across all pillars (endpoint, cloud, AD, OT, web apps, ASM)
- **Nessus brand** — recognized and trusted by security practitioners globally for 25+ years

---

## Weaknesses

- **Not a detection tool** — Tenable is a vulnerability assessment platform, not a threat detection tool; no EDR, SIEM, or SOAR
- **Agent limitations** — Nessus agent vs. credentialed scanning vs. agentless differs in coverage; coverage gaps in cloud-native environments
- **CNAPP depth** — Ermetic provides CIEM/CSPM but Tenable Cloud Security trails Wiz, Prisma Cloud in overall CNAPP depth
- **Patch management** — Tenable identifies vulnerabilities but does not remediate; requires integration with patch management tools
- **EASM maturity** — Bit Discovery-based ASM is growing but trails Xpanse, Censys, and Mandiant ASM in feature depth
- **Response workflow** — VM data is exported to ticketing/ITSM; no native remediation workflow

---

## Licensing Model

| Product | Model | Approx. Annual Cost |
|---------|-------|---------------------|
| Nessus Pro | Perpetual + annual maint. | ~$4,000/year (unlimited scanners, 1 user) |
| Nessus Expert | Annual subscription | ~$5,000/year (cloud scanning included) |
| Tenable Vulnerability Management | Per asset/year | ~$25-50/asset/year |
| Tenable Security Center (SC) | Per IP/year | ~$20-40/IP/year |
| Tenable OT Security | Per OT asset/year | ~$50-150/OT asset/year |
| Tenable Identity Exposure | Per user/year | ~$15-30/AD user/year |
| Tenable Cloud Security | Per cloud resource | ~$15-30/resource/month |
| Tenable One | Bundled enterprise | Custom; typically $200K-$1M+/year |
| Tenable Lumin | Add-on to VM | ~$10-20/asset/year |

---

## NIST CSF Coverage

| Function | Coverage | Notes |
|----------|----------|-------|
| Govern | Partial | Risk scoring (Lumin); compliance reporting |
| Identify | Very Strong | Asset discovery, VM, CAASM, cloud posture, AD, OT, ASM — broadest exposure management |
| Protect | Weak | VM prioritization informs patching; not a protection tool |
| Detect | Partial | Tenable Identity Exposure detects AD attacks in real-time; not a general-purpose detection tool |
| Respond | Absent | No SOAR or incident response capability |
| Recover | Absent | No backup or DR |

---

## Exposure Management vs. Vulnerability Management

**Traditional VM:** Scan → find CVEs → CVSS score → patch everything → repeat.

**Tenable One Exposure Management:** Continuous assessment across all attack surfaces → contextualize risk (what's exposed to internet? what has a public exploit? what's connected to crown jewel systems?) → prioritize using attack path analysis → risk score per business unit → benchmark vs. industry.

Key difference: **context over completeness.** A CVSS 9.8 vulnerability on an internal dev server with no internet exposure is lower priority than a CVSS 7.5 vulnerability on an internet-facing web server with public exploit code and direct database access.

---

## Tenable Identity Exposure (AD Security)

Active Directory is the #1 attack target in enterprise environments. Tenable Identity Exposure provides:
- **Misconfiguration detection** — ACL weaknesses, Kerberoastable accounts, AS-REP roasting, delegation issues
- **Attack path analysis** — visualization of how an attacker moves from a compromised workstation to Domain Admin
- **Real-time attack detection** — DCSync, Golden Ticket, Kerberoasting attacks detected in real-time
- **Entra ID** — extends to Azure AD/Entra ID for hybrid environments

This directly competes with CrowdStrike Falcon Identity Protection and SentinelOne Singularity Identity.

---

## Key Integrations

- **Patch Management:** SCCM, Ivanti, IBM BigFix, Ansible
- **ITSM:** ServiceNow (ITSM), Jira (remediation tickets)
- **SIEM:** Splunk, Sentinel, Chronicle (vulnerability data enrichment)
- **CMDB:** ServiceNow CMDB, BMC Helix
- **Cloud:** AWS, Azure, GCP API scanning; native cloud connector

---

## Recent Developments (2023-2025)

- **Ermetic acquisition** (2023, ~$240M) — CIEM and CNAPP capability; rebranded as Tenable Cloud Security
- **Tenable One platform** — unified exposure management across all products (2022 launch; maturing)
- **Tenable Attack Path Analysis** — ML-based attack path visualization across VM + cloud + AD data
- **AI-powered remediation guidance** — GenAI integration for plain-language vulnerability remediation steps
- **ExposureAI** — generative AI embedded in Tenable One for natural language queries over vulnerability data

---

## Analyst Position

- **Gartner MQ:** Leader in Vulnerability Assessment — 13+ consecutive years
- **Forrester Wave:** Leader in Vulnerability Risk Management
- **IDC:** Leader in Vulnerability Management
