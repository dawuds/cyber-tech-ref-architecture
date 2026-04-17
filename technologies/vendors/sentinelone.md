# SentinelOne — Vendor Profile

**Type:** Platform Vendor (Security-native, Endpoint-led)  
**HQ:** Mountain View, CA, USA  
**Security Revenue:** ~$800M (FY2025, ARR ~$850M+)  
**Architecture Reference:** N/A (no dedicated reference architecture document)

---

## Overview

SentinelOne is CrowdStrike's primary direct competitor in endpoint security. Founded in 2013 by former Unit 8200 (Israeli intelligence) veterans, SentinelOne built an AI/ML-first EPP/EDR architecture that runs entirely at the endpoint — autonomously blocking threats in milliseconds without cloud lookup dependency.

The key architectural differentiator: **on-agent AI inference.** SentinelOne's Singularity engine processes behavioral signals locally on the endpoint, enabling detection and response even when disconnected from the cloud. This contrasts with CrowdStrike's cloud-dependent detection model.

In 2022-2023, SentinelOne aggressively expanded from endpoint into a platform via acquisitions: Attivo Networks (identity threat detection), Scalyr (log analytics → Singularity Data Lake), Noname alternative positioning, and Wiz competition for cloud security.

---

## Product Portfolio

| Category | Product(s) | NIST Mapping |
|----------|-----------|--------------|
| EPP / NGAV | Singularity Endpoint (EPP) | Protect |
| EDR | Singularity Endpoint (EDR) | Detect |
| XDR | Singularity XDR | Detect |
| MDR | Vigilance MDR | Respond |
| Threat Hunting | Vigilance + Singularity Ranger | Detect |
| Identity Threat Detection | Singularity Identity (Attivo) | Detect, Protect |
| AD Assessment | Singularity Identity AD Assessor | Identify |
| Cloud Security (CNAPP) | Singularity Cloud | Identify, Protect |
| CSPM | Singularity Cloud Security (CSPM) | Identify |
| CWPP | Singularity Cloud Workload Protection | Protect |
| Container Security | Singularity Container Security | Protect |
| Log Analytics / SIEM | Singularity Data Lake (Scalyr) | Detect |
| VM | Singularity Ranger (network + endpoint VM) | Identify |
| EASM | Singularity Ranger (asset discovery) | Identify |
| Mobile | Singularity Mobile | Protect |
| Network Attack Surface | Singularity Ranger Pro | Identify |

---

## Strengths

- **On-agent AI** — autonomous protection without cloud dependency; detects on disconnected devices
- **Storyline technology** — patented behavioral AI linking all events in an attack chain (story) for forensic analysis
- **Attivo identity security** — acquired 2022; strongest identity threat detection in endpoint-first architecture
- **Data Lake** — Scalyr-based log analytics is fast and cost-effective vs. Splunk
- **Vigilance MDR** — strong managed detection and response service
- **1-Click Remediation** — automated full rollback of malicious changes (ransomware rollback)
- **Linux/macOS** — historically stronger Linux EDR than CrowdStrike (important for cloud workloads)
- **Pricing** — generally lower price point than CrowdStrike for equivalent endpoint protection

---

## Weaknesses

- **Platform breadth** — smaller portfolio than CrowdStrike/Palo Alto; network security absent
- **SIEM depth** — Singularity Data Lake growing but Humio (CrowdStrike LogScale) more established
- **Threat intelligence** — no Adversary Intelligence equivalent; CTI less mature than CrowdStrike
- **Revenue scale** — ~$800M vs. CrowdStrike ~$3.9B; less investment capacity for R&D
- **Cloud CNAPP** — Singularity Cloud competes but trails Wiz, Prisma Cloud, Defender for Cloud
- **Network security** — no NGFW, no SSE, no email security
- **GRC / PAM** — no governance or privileged access tooling

---

## Licensing Model

| Tier | Inclusions | Approx. Annual Cost (per endpoint) |
|------|-----------|-----------------------------------|
| Singularity Core | EPP (AV) | ~$45-65/endpoint |
| Singularity Control | EPP + Firewall + Device Control | ~$65-85/endpoint |
| Singularity Complete | Full EDR + Storyline + Ransomware Rollback | ~$80-120/endpoint |
| Singularity Commercial | Complete + Ranger + Data Retention | ~$100-140/endpoint |
| Singularity Enterprise | Complete + XDR + Data Lake + Identity add-ons | ~$150-200/endpoint |
| Vigilance MDR | Add-on MDR service | ~$15-25/endpoint/year |

---

## NIST CSF Coverage

| Function | Coverage | Notes |
|----------|----------|-------|
| Govern | Absent | No GRC or compliance management |
| Identify | Good (endpoint/cloud) | Ranger asset discovery, Singularity Cloud CSPM |
| Protect | Strong (endpoint) | Best-in-class EPP; cloud workload protection growing |
| Detect | Strong | Storyline AI correlation; XDR; identity threat detection |
| Respond | Good | Vigilance MDR + automated remediation; 1-click rollback |
| Recover | Partial | Ransomware rollback (endpoint files only); no true backup |

---

## Attivo Identity Security (Acquired May 2022)

Attivo Networks brought:
- **ThreatDefend** — deception platform (decoys for AD, endpoints, network)
- **AD Assessor** — Active Directory attack path analysis and misconfiguration detection
- **Identity Security for endpoints** — credential theft detection, lateral movement blocking
- **Integration** — now rebranded as Singularity Identity within the SentinelOne platform

This makes SentinelOne uniquely positioned as the only major EPP/EDR vendor with deep Active Directory security and identity-based deception built into the platform.

---

## Key Integrations

- **Identity:** Entra ID, Okta integration for identity signals
- **SIEM:** Singularity Data Lake + Splunk, Sentinel, Chronicle connectors
- **SOAR:** Splunk SOAR, Palo Alto XSOAR, ServiceNow integrations
- **Cloud:** AWS, Azure, GCP cloud workload agent
- **Ticketing:** ServiceNow, Jira, PagerDuty

---

## Recent Developments (2023-2025)

- **Singularity Data Lake** (Scalyr-based) — positioned as alternative to Splunk for security analytics
- **PinnacleOne** strategic advisory practice (2022) — executive cyber risk advisory
- **Purple AI** (2023) — GenAI threat hunting and investigation assistant (Charlotte AI competitor)
- **AI-SIEM** capabilities — threat correlation and automated triage via Purple AI
- **Singularity Cloud expansion** — CSPM, CWPP, Kubernetes security, IaC scanning

---

## Analyst Position

- **Gartner MQ:** Leader in EPP (Endpoint Protection Platforms) — consistently #2 or #3 behind CrowdStrike
- **Forrester Wave:** Strong Performer / Leader in XDR
- **Gartner Peer Insights:** Customers Choice for EPP multiple years
