# CrowdStrike — Vendor Profile

**Type:** Platform Vendor (Security-native)  
**HQ:** Austin, TX, USA  
**Security Revenue:** ~$3.9B (FY2025)  
**Architecture Reference:** [CrowdStrike Falcon](../../architectures/crowdstrike-falcon.md)

---

## Overview

CrowdStrike is the defining cloud-native endpoint security vendor and the fastest-growing security platform. Founded in 2011 by former McAfee executives, CrowdStrike built Falcon from scratch as a cloud-delivered, single-agent, single-platform architecture — no legacy code, no on-premises software to maintain.

CrowdStrike's core insight: **threat intelligence from incidents + AI/ML + a single cloud sensor = better prevention and detection than any on-premises product.** The OverWatch threat hunting team's findings from IR engagements feed directly back into Falcon detections globally.

---

## Product Portfolio

| Category | Product(s) | NIST Mapping |
|----------|-----------|--------------|
| EPP / NGAV | Falcon Prevent | Protect |
| EDR | Falcon Insight XDR | Detect |
| XDR | Falcon XDR (multi-platform) | Detect |
| MDR | Falcon Complete | Respond |
| Threat Hunting | Falcon OverWatch | Detect |
| Identity Threat | Falcon Identity Protection | Detect, Protect |
| Asset Discovery | Falcon Discover | Identify |
| ZTNA (ZTA scoring) | Falcon Zero Trust Assessment | Protect |
| Cloud Security (CNAPP) | Falcon Cloud Security | Identify, Protect |
| CSPM | Falcon CSPM | Identify |
| CIEM | Falcon CIEM | Identify |
| Vulnerability Management | Falcon Spotlight | Identify |
| EASM | Falcon Surface | Identify |
| Exposure Management | Falcon Exposure Management | Identify |
| Log Management / SIEM | Falcon LogScale (Humio) | Detect |
| SOAR | Falcon Fusion | Respond |
| Threat Intelligence | Falcon Intelligence / Adversary Intel | Detect |
| DRPS | Falcon Recon | Identify |
| AI SOC | Charlotte AI | Detect, Respond |
| Host Firewall | Falcon Firewall Management | Protect |
| Device Control | Falcon Device Control | Protect |

---

## Strengths

- **Single agent, single platform** — one Falcon sensor delivers EPP, EDR, XDR, VM, identity protection; minimal IT overhead
- **EDR leadership** — consistently #1 in Gartner EPP Magic Quadrant; OverWatch adds human hunting layer
- **Threat intelligence quality** — 400+ named adversary groups (Fancy Bear = COZY BEAR, etc.); fastest adversary tracking
- **Cloud-native architecture** — no on-prem infrastructure; instant global deployment
- **Falcon LogScale** — petabyte-scale log search at flat cost (Humio); competitive with Elasticsearch-based SIEM
- **Agentic Defense narrative** — Charlotte AI positioned as autonomous AI analyst

---

## Weaknesses

- **Network security** — no NGFW, no email security, no SD-WAN; platform stops at the endpoint
- **GRC / compliance** — no governance, risk management, or compliance tooling
- **Recovery** — no backup or DR capability
- **Email** — basic email integration; not a SEG competitor
- **PAM** — no privileged access management
- **July 2024 outage risk** — 8.5M Windows systems blue-screened from single content update; platform concentration risk

---

## Licensing Model

**Falcon Flex** (2024) — credit-based licensing across all modules.

| Tier | Key Inclusions | Approx. Annual Cost (per endpoint) |
|------|---------------|-----------------------------------|
| Falcon Go | Prevent (NGAV) | ~$60-80/endpoint |
| Falcon Pro | Prevent + Insight EDR + Spotlight VM | ~$100-130/endpoint |
| Falcon Enterprise | XDR + Identity + Cloud Security | ~$160-200/endpoint |
| Falcon Elite | Recon + Intel Premium + Threat Hunting | ~$200-250/endpoint |
| Falcon Complete | Full MDR management + all modules | ~$150-200/endpoint + service fee |

*Pricing varies significantly by volume, region, and negotiation.*

---

## NIST CSF Coverage

| Function | Coverage | Notes |
|----------|----------|-------|
| Govern | Weak | No GRC, risk quantification tools limited |
| Identify | Strong (endpoint/cloud) | Excellent VM, EASM, cloud posture; weak for network/OT |
| Protect | Strong (endpoint/identity) | Best-in-class EPP/EDR; no network/email protection |
| Detect | Very Strong | XDR + OverWatch + LogScale SIEM = outstanding detection |
| Respond | Strong | Complete MDR + Fusion SOAR; Charlotte AI accelerating |
| Recover | Absent | Zero backup/DR capability |

---

## Key Integrations

- Native integrations: Microsoft Entra ID (identity signals), Okta (identity), Zscaler ZPA (ZTA scoring)
- SIEM integrations: Splunk, Sentinel, Chronicle via Falcon Data Replicator
- SOAR integrations: Splunk SOAR, Palo Alto XSOAR, ServiceNow
- Cloud: AWS Security Hub, Azure Defender, GCP SCC native connectors

---

## Recent Developments (2023-2025)

- **Charlotte AI** (2023) — conversational GenAI SOC analyst across entire Falcon platform
- **Falcon Flex** licensing (2024) — flexible credit pool replacing per-module SKUs
- **Falcon Exposure Management** (2024) — unified exposure: endpoint + EASM + identity + cloud risk
- **July 2024 outage** — 8.5M Windows BSODs; accelerated update control and resilience features
- **Bionic acquisition** (2023) — adds AppSec/ASPM capability to Falcon Cloud Security
- **Reposify acquisition** (2022) → Falcon Surface EASM

---

## Analyst Position

- **Gartner MQ:** Leader in EPP (Endpoint Protection Platforms) — consistently #1 in execution
- **Forrester Wave:** Leader in XDR, Managed Detection & Response
- **SC Awards:** CISO Choice Award for EDR multiple years
