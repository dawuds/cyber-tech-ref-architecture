# CrowdStrike Falcon Platform — Agentic Defense Architecture

**Version:** 2024 (Falcon Flex / Agentic AI era)  
**Source:** https://www.crowdstrike.com/platform/  
**Type:** Platform Reference Architecture

---

## On This Page
- [Overview](#overview) — platform scope and single-agent architecture
- [Architecture Domains](#architecture-domains) — domain map
- [Platform Domains](#platform-domains) — products by domain with category links
- [NIST CSF 2.0 Mapping](#nist-csf-20-mapping) — function coverage
- [Coverage Gaps](#coverage-gaps) — what Falcon does not address
- [The Single-Agent Advantage (and Risk)](#the-single-agent-advantage-and-risk) — architectural analysis
- [Licensing Model](#licensing-model) — Falcon Flex pricing tiers

## At a Glance
- **Single-agent architecture**: one lightweight Falcon sensor on every endpoint expands to EDR, XDR, SIEM (LogScale), SOAR (Fusion), identity protection (Singularity Identity), and cloud workload security — no tool sprawl
- **Charlotte AI** (agentic defense, 2024): AI-assisted triage, automated investigation, and self-healing response — the differentiation play against Microsoft Copilot for Security
- **July 2024 global outage**: faulty content update affected 8.5M Windows devices — the largest IT incident in history; Falcon Flex ARR continued growing, confirming high customer stickiness despite the event
- **Gaps**: No native email security, no GRC/compliance platform, no backup/recovery
- **Direction →** CrowdStrike's single-agent + AI-SIEM (LogScale) play positions it as the default security platform for organisations starting with EDR and expanding to full XDR; Falcon Flex (all-modules subscription) is the primary consolidation vehicle; Charlotte AI's agentic capabilities are the 2025–2026 competitive differentiator

---

## Overview

CrowdStrike Falcon is a cloud-native, single-agent, single-platform architecture. Every capability is delivered from one lightweight agent (Falcon sensor) and one cloud platform (Falcon Cloud). This eliminates the multi-agent, multi-console complexity of legacy security stacks.

In 2024, CrowdStrike rebranded its platform story around **Agentic Defense** — AI agents that autonomously detect, investigate, and respond to threats, with Charlotte AI as the conversational interface. The platform now spans endpoint, identity, cloud, and threat intelligence, positioning CrowdStrike as a full-platform competitor to Microsoft.

**Market position:** Leader in EDR/XDR (Gartner MQ #1), fastest-growing in enterprise security, revenue ~$3.9B (FY2025). Single largest global IT outage caused by faulty content update (July 2024 Falcon sensor update) — accelerated platform resilience investments.

---

## Architecture Domains

```
┌──────────────────────────────────────────────────────────────────┐
│                    CROWDSTRIKE FALCON PLATFORM                   │
│                    (Single Cloud, Single Agent)                  │
├─────────────────────┬────────────────────┬───────────────────────┤
│  ENDPOINT &         │  CLOUD SECURITY    │  IDENTITY SECURITY    │
│  IDENTITY           │                    │                       │
│  Falcon Prevent     │  Falcon CSPM       │  Falcon Identity Prot │
│  Falcon Insight XDR │  Falcon CWP        │  Falcon Discover      │
│  Falcon Complete    │  Falcon Horizon    │  Falcon Zero Trust    │
├─────────────────────┼────────────────────┼───────────────────────┤
│  THREAT INTEL       │  SECURITY OPS      │  RISK & EXPOSURE      │
│  Falcon Intel       │  Falcon Fusion     │  Falcon Spotlight     │
│  Falcon Adversary   │  (SOAR)            │  (VM)                 │
│  Intelligence       │  Falcon LogScale   │  Falcon Surface       │
│  Falcon Recon       │  (SIEM/log mgmt)   │  (EASM)               │
│  (DRPS)             │  Charlotte AI      │  Falcon Exposure Mgmt │
└─────────────────────┴────────────────────┴───────────────────────┘
```

---

## Platform Domains

### Domain 1: Endpoint & Identity
| Product | Category | Notes |
|---------|----------|-------|
| Falcon Prevent | EPP/AV | NGAV with AI/ML behavioral prevention |
| Falcon Insight XDR | XDR / EDR | Core EDR — process tree, timeline, 90-day telemetry |
| Falcon Overwatch | Threat Hunting | 24/7 managed threat hunting by CrowdStrike analysts |
| Falcon Complete MDR | MDR | Fully managed detection and response service |
| Falcon Device Control | DLP (endpoint) | USB / peripheral device control |
| Falcon Firewall Management | Host Firewall | Windows host-based firewall management |

### Domain 2: Identity Security
| Product | Category | Notes |
|---------|----------|-------|
| Falcon Identity Protection | Identity Threat Detection | AD + Entra ID threat detection; replaces Preempt (acquired 2020) |
| Falcon Discover | Asset / Identity Inventory | Account and asset visibility; shadow IT detection |
| Falcon Zero Trust Assessment | Zero Trust | Continuous device/identity trust scoring for ZTA policy |

### Domain 3: Cloud Security
| Product | Category | Notes |
|---------|----------|-------|
| Falcon Cloud Security (CNAPP) | CNAPP | Unified CSPM + CWPP + CIEM + IaC scanning |
| Falcon CSPM | CSPM | Cloud posture management (AWS, Azure, GCP, OCI) |
| Falcon Cloud Workload Protection | CWPP | Runtime container + server workload protection |
| Falcon CIEM | CIEM | Cloud identity entitlement management |
| Falcon Application Security | AppSec | Code scanning, pipeline security (Bionic acquisition 2023) |

### Domain 4: Threat Intelligence
| Product | Category | Notes |
|---------|----------|-------|
| Falcon Intelligence | Threat Intelligence | Automated threat intel enrichment per alert |
| Falcon Adversary Intelligence | CTI | Named adversary tracking (400+ threat actors with animal names) |
| Falcon Recon | DRPS | Digital risk protection — dark web, brand, credential monitoring |
| Falcon Intelligence Premium | CTI | Analyst-written intelligence reports |

### Domain 5: Security Operations
| Product | Category | Notes |
|---------|----------|-------|
| Falcon LogScale | Log Management / SIEM | Humio acquisition (2021); 1-second search at petabyte scale |
| Falcon Fusion | SOAR | Embedded SOAR/automation within Falcon console |
| Charlotte AI | AI SOC Assistant | Conversational AI for investigation, triage, report generation |
| Falcon Data Replicator | Data Pipeline | Stream Falcon telemetry to external SIEM/data lake |

### Domain 6: Risk & Exposure Management
| Product | Category | Notes |
|---------|----------|-------|
| Falcon Spotlight | Vulnerability Management | Agent-based VM; CVE visibility across managed endpoints |
| Falcon Surface | EASM | External attack surface management (Reposify acquisition 2022) |
| Falcon Exposure Management | CTEM Platform | Unified exposure: endpoint VM + EASM + identity + cloud risk |

---

## NIST CSF 2.0 Mapping

| NIST Function | CrowdStrike Products | Coverage |
|--------------|---------------------|----------|
| **Govern** | Policy management (via Falcon console), Exposure Management risk scoring | Weak — no GRC, risk register, or compliance framework tooling |
| **Identify** | Falcon Discover (assets), Spotlight (VM), Surface (EASM), CIEM | Strong for endpoints/cloud; limited for network/OT assets |
| **Protect** | Falcon Prevent (EPP), Device Control, Firewall Mgmt, Identity Protection, Cloud Security | Strong for endpoint/identity/cloud; limited for network perimeter |
| **Detect** | Falcon Insight XDR, LogScale (SIEM), Overwatch, Cloud Security | Very strong — XDR + human threat hunting combination |
| **Respond** | Falcon Complete (MDR), Fusion (SOAR), Charlotte AI, Overwatch escalation | Strong managed response; native SOAR basic vs. Palo Alto XSOAR |
| **Recover** | No native recovery products | Absent — no backup, DR, or recovery tooling |

---

## Coverage Gaps

- **Network Security:** No NGFW, no SD-WAN, no email security. Platform is agent/cloud-centric.
- **GRC / Compliance:** No native governance or compliance management tooling.
- **Recovery:** No backup or disaster recovery capability.
- **Email Security:** Falcon for Email was basic; CrowdStrike partners with Proofpoint/Microsoft.
- **PAM:** No privileged access management; relies on partners.

---

## The Single-Agent Advantage (and Risk)

**Advantage:** One Falcon sensor delivers EPP, EDR, XDR, VM, device control, ZTA, cloud workload protection, and identity threat detection. No additional software installs, no multi-vendor management console.

**Risk — July 2024 Falcon Sensor Outage:** A faulty content configuration update caused ~8.5 million Windows systems to blue-screen simultaneously. The incident exposed the systemic risk of a single vendor's kernel-level agent running on critical infrastructure globally. CrowdStrike subsequently introduced:
- Phased channel file updates (canary deployment)
- Rapid Response Content delivered separately from sensor updates
- Customer control over update timing

---

## Licensing Model

**Falcon Flex** (2024) — unified licensing pool across all Falcon products. Customers buy capacity credits and flex across modules. Replaces per-module SKU complexity.

| Tier | Inclusions |
|------|-----------|
| Falcon Go | Prevent (AV), basic EDR |
| Falcon Pro | Full EDR + Spotlight VM |
| Falcon Enterprise | XDR, Identity Protection, Cloud Security |
| Falcon Elite | Recon, Intelligence Premium, MDR bundles |
| Falcon Complete | Fully managed MDR service |

---

## References

- CrowdStrike Falcon Platform: https://www.crowdstrike.com/platform/
- Adversary Intelligence: https://www.crowdstrike.com/adversary-intelligence/
- 2024 Global Threat Report: https://www.crowdstrike.com/global-threat-report/
- July 2024 incident PIR: https://www.crowdstrike.com/falcon-content-update-remediation-and-guidance-hub/
