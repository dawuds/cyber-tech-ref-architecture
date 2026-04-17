# Wiz — Vendor Profile

**Type:** Specialist Leader (CNAPP / Cloud Security)  
**HQ:** New York, NY, USA  
**Revenue:** ~$500M ARR (2024), growing ~100% YoY  
**Category:** [CNAPP](../categories/protect/cnapp.yaml) | [CSPM](../categories/protect/cnapp.yaml) | [CIEM](../categories/identify/ciem.yaml)

---

## Overview

Wiz is the fastest-growing cybersecurity company in history, reaching $100M ARR in 18 months (2021-2022) and $500M ARR by 2024. Founded by the team that built Microsoft's cloud security organization (including the team behind Azure Security Center), Wiz reimagined cloud security posture management with a single killer feature: **agentless scanning that visualizes the complete cloud attack graph in minutes**.

Google announced acquisition of Wiz for ~$23B in June 2024 — the largest cybersecurity acquisition ever. As of April 2025, the acquisition remains pending regulatory review.

**Core insight:** Traditional CNAPP required agents, multiple consoles, and security expertise to correlate findings. Wiz connects directly to cloud APIs, maps every resource, permission, vulnerability, and network exposure into a single unified graph, and surfaces the critical attack paths that matter — without any agents.

---

## Product Portfolio

| Product | Category | Notes |
|---------|----------|-------|
| Wiz CNAPP | CNAPP | Unified cloud security: CSPM + CWPP + CIEM + vulnerability + network exposure |
| Wiz CSPM | CSPM | Cloud security posture; misconfigurations across AWS/Azure/GCP/OCI |
| Wiz CWPP | CWPP | Workload protection: VMs, containers, serverless (agentless + optional agent) |
| Wiz CIEM | CIEM | Cloud identity entitlements; effective permissions graph |
| Wiz Vulnerability Management | VM (cloud) | Agentless vulnerability scanning for OS, packages, containers |
| Wiz Code (ASPM) | AppSec | Application security posture management; IaC scanning, secrets in code |
| Wiz Defend | Cloud Detection & Response | Runtime threat detection (agent-based for Kubernetes) |
| Wiz Sensor | CWPP runtime | Optional lightweight agent for in-cluster threat detection |
| Wiz Data Security (DSPM) | DSPM | Data discovery, classification, exposure across cloud data stores |
| Wiz Threat Center | Threat Intelligence | Cloud-specific threat intelligence contextualized to the customer environment |

---

## The Wiz Security Graph

The core differentiator: **Wiz Security Graph** — a contextual relationship map of every cloud resource, identity, vulnerability, network exposure, and secret.

```
[VM with critical CVE]
     ↓ accessible by
[Overly permissive IAM role]
     ↓ accessible from
[Internet-exposed S3 bucket]
     ↓ containing
[Sensitive data (PII)]
```

A traditional CSPM tool would generate 4 separate alerts. Wiz correlates them into one **Toxic Combination** — a prioritized attack path requiring immediate remediation.

This "security graph" approach reduces alert volume by 90%+ vs. traditional CSPM tools by surfacing only findings that are both critical AND exploitable in context.

---

## Strengths

- **Agentless deployment** — connect cloud accounts; scan starts in minutes; no agent deployment/maintenance
- **Security Graph** — contextual attack path analysis; correlates misconfigurations + vulnerabilities + excessive permissions + sensitive data
- **Speed to value** — fastest deployment in CNAPP market; meaningful findings in Day 1
- **Multi-cloud** — AWS, Azure, GCP, OCI, Alibaba, and hybrid (Kubernetes on-prem)
- **Developer experience** — Wiz Code integrates into CI/CD (GitHub Actions, GitLab, Jenkins) for shift-left security
- **Investor confidence** — $1.9B raised at $12B valuation (2024); Google acquisition pending at $23B
- **ARR growth** — no other security company reached $500M ARR faster

---

## Weaknesses

- **No NGFW / network security** — Wiz is cloud-only; no on-premises or network security capability
- **EDR** — Wiz Defend is early-stage runtime detection; not a CrowdStrike/MDE competitor
- **On-premises blind spot** — if workloads are on-prem or in private data centers, Wiz has no visibility
- **Email / endpoint** — no workforce security products at all
- **PAM** — no privileged access management
- **SOAR** — no native SOAR; integrates with third-party SOAR tools
- **Google acquisition uncertainty** — pending regulatory approval; organizational uncertainty during transition

---

## Licensing Model

Volume-based, priced per cloud workload resource.

| Tier | Pricing Basis | Approx. Cost |
|------|--------------|--------------|
| Wiz CNAPP (base) | Per cloud resource/month | ~$30-60/resource/month |
| Wiz Code add-on | Per developer seat or pipeline | ~$20-40/developer/month |
| Wiz Defend (CDR) | Per cluster node/month | ~$40-80/node/month |
| Wiz Data Security | Per data store/month | Custom |

**Enterprise pricing** (500+ cloud resources): typically $300K-$1.5M/year for full CNAPP.
Wiz is aggressive with discounting for multi-year enterprise commitments.

---

## NIST CSF Coverage

| Function | Coverage | Notes |
|----------|----------|-------|
| Govern | Partial | Policy compliance reporting; no GRC platform |
| Identify | Very Strong | Cloud asset inventory + CIEM + vulnerabilities + exposure in one graph |
| Protect | Strong | Contextual risk remediation; IaC scanning prevents misconfigurations at deploy |
| Detect | Good | Wiz Defend (CDR) for runtime; Wiz Threat Center for contextualized intel |
| Respond | Partial | Integration to SOAR tools; no native case management |
| Recover | Absent | No backup or DR |

---

## Competitive Landscape

| Vendor | CNAPP Approach | vs. Wiz |
|--------|---------------|---------|
| Wiz | Agentless graph-based | — |
| Palo Alto Prisma Cloud | Agentless + agent; broader features | More mature; complex |
| Microsoft Defender for Cloud | Native Azure; multi-cloud via connectors | Free with Azure; less cloud-neutral |
| CrowdStrike Falcon Cloud | Agent-first; good for endpoint-cloud correlation | Better EDR integration |
| Lacework (Fortinet) | Agent-based (composite score); deep runtime | Less intuitive; integration still maturing |
| Orca Security | Agentless (Side-Scanning); similar graph approach | Smaller market share; similar model |
| SentinelOne Singularity Cloud | Agent-based; endpoint-cloud correlation | Better for endpoint-first shops |
| Aqua Security | Container/DevSecOps native | Stronger in containers; less CSPM |

---

## Key Integrations

- **ITSM/Ticketing:** Jira, ServiceNow (remediation ticket auto-creation)
- **CI/CD:** GitHub Actions, GitLab CI, Jenkins, Azure DevOps (Wiz Code)
- **SOAR:** Palo Alto XSOAR, Splunk SOAR, PagerDuty
- **SIEM:** Splunk, Sentinel, Chronicle (findings export)
- **Collaboration:** Slack, Teams (alert notifications)
- **Cloud:** Native API integration — no agents for CSPM; optional Wiz Sensor for runtime

---

## Recent Developments (2023-2025)

- **Google acquisition announced** (June 2024, ~$23B) — pending regulatory approval
- **Wiz Code** (2023) — ASPM and IaC security for developer shift-left
- **Wiz Data Security (DSPM)** (2023) — data discovery and classification across cloud stores
- **Wiz Defend** (2023) — cloud detection and response for runtime threats
- **Wiz Threat Center** — cloud-specific threat intelligence integrated into the security graph
- **OCI support** — Oracle Cloud Infrastructure added to multi-cloud coverage

---

## Analyst Position

- **Gartner MQ:** Leader in CNAPP (Gartner inaugural CNAPP MQ, 2023)
- **Forrester Wave:** Leader in Cloud Security (CNAPP)
- **IDC:** Fastest-growing cloud security vendor by revenue
