# Microsoft — Vendor Profile

**Type:** Platform Vendor (Hyperscaler + Security)  
**HQ:** Redmond, WA, USA  
**Security Revenue:** ~$20B+ (FY2024, across M365 + Azure security)  
**Architecture Reference:** [Microsoft MCRA](../../architectures/microsoft-mcra.md)

---

## Overview

Microsoft is the largest cybersecurity vendor by revenue, driven by bundling security into M365 and Azure subscriptions rather than standalone security product sales. The M365 E5 license alone bundles 15+ security products, making Microsoft the default security platform for most enterprises that run on Microsoft infrastructure.

Microsoft's security strategy: **integrated platform over best-of-breed.** The argument is that native integration produces better detection (shared telemetry) and lower total cost of ownership (vs. buying 8-10 point solutions separately).

---

## Product Portfolio

| Category | Product(s) | NIST Mapping |
|----------|-----------|--------------|
| IAM / SSO / MFA | Microsoft Entra ID (AAD) | Protect |
| IGA | Entra ID Governance | Protect, Govern |
| CIEM | Entra Permissions Management | Identify |
| ZTNA | Entra Private Access | Protect |
| SWG / CASB | Entra Internet Access, Defender for Cloud Apps | Protect |
| PAM | No native — partner (CyberArk, BeyondTrust) | — |
| Secrets Management | Azure Key Vault | Protect |
| EDR / XDR | Defender for Endpoint + Defender XDR | Detect, Respond |
| SIEM | Microsoft Sentinel | Detect |
| SOAR | Sentinel (Logic Apps) | Respond |
| Email Security | Defender for Office 365 | Protect |
| DLP | Microsoft Purview DLP | Protect |
| CNAPP | Defender for Cloud | Identify, Protect |
| MDM / EMM | Microsoft Intune | Protect |
| VM | Defender Vulnerability Management | Identify |
| Threat Intelligence | Microsoft Defender Threat Intelligence (MDTI) | Detect |
| AI Security | Defender for AI | Protect, Detect |
| AI SOC | Copilot for Security | Detect, Respond |

---

## Strengths

- **M365 licensing** — most enterprises already own significant Microsoft security capabilities at marginal cost in E3/E5
- **Native XDR correlation** — Defender XDR correlates endpoint, identity, email, and cloud signals natively
- **Entra ID ubiquity** — identity plane for 95%+ of enterprise Microsoft environments; Conditional Access is strongest policy engine
- **Sentinel scale** — cloud-native SIEM with extensive connector library (200+ data sources)
- **AI-first** — Copilot for Security uses GPT-4 across all Defender products; significant lead in enterprise GenAI security tooling

---

## Weaknesses

- **PAM** — No native PAM; partners recommended
- **Network security** — Azure Firewall and WAF for cloud; no enterprise hardware NGFW
- **OT/ICS** — Defender for IoT (Cyberx) covers OT visibility but limited enforcement
- **SOAR complexity** — Sentinel SOAR via Logic Apps is powerful but complex to maintain
- **Recovery** — Azure Backup exists but is infrastructure-focused, not security-integrated
- **Professional services** — No Mandiant/Talos-equivalent IR services team at scale

---

## Licensing Model

| License | Annual Cost (per user) | Key Security Inclusions |
|---------|----------------------|------------------------|
| M365 E3 | ~$360/user/year | Entra ID P1, basic DLP, Defender AV |
| M365 E5 | ~$576/user/year | Entra ID P2, MDE P2, Defender XDR, Sentinel (SIEM), Purview |
| Microsoft Entra Suite | ~$12/user/month | Entra Private/Internet Access, ID Governance, Permissions Mgmt |
| Defender for Cloud | PAYG per resource | CSPM + CWPP per Azure/AWS/GCP resource |
| Sentinel | PAYG per GB ingested | SIEM: typically $2.46-$3.00/GB ingested |

**Enterprise Security E5 add-on** (~$12/user/month) is available for organizations not wanting full M365 E5.

---

## NIST CSF Coverage

| Function | Coverage | Notes |
|----------|----------|-------|
| Govern | Partial | Compliance Manager, Secure Score — posture only |
| Identify | Strong (cloud), Moderate (hybrid) | CSPM excellent; OT/legacy weak |
| Protect | Very Strong | E5 bundle covers most protection controls |
| Detect | Very Strong | XDR + Sentinel combination best-in-class for Microsoft environments |
| Respond | Strong | Automated investigation; Logic Apps SOAR; no native case mgmt |
| Recover | Partial | Azure Backup/ASR exist but outside security portfolio |

---

## Key Integrations

- Native integration with all Microsoft products (no API keys required in M365 environments)
- Sentinel connectors for CrowdStrike, Palo Alto, Okta, AWS, GCP, ServiceNow
- Entra ID Conditional Access integrates device compliance from Intune and CrowdStrike
- Defender for Cloud integrates with AWS Security Hub, GCP SCC

---

## Recent Developments (2023-2025)

- Copilot for Security (GA April 2024) — first enterprise GenAI security product
- Entra suite expansion — Entra Private/Internet Access as ZTNA/SWG replacement
- Defender for Cloud multi-cloud improvements — agentless scanning for AWS/GCP
- Security Exposure Management — unified attack surface including EASM elements
- Microsoft Sentinel free tier removed — all new workspaces require commitment tier

---

## Analyst Position

- **Gartner MQ:** Leader in SIEM, EPP, CSPM, IAM, EMM, Secure Web Gateway
- **Forrester Wave:** Leader in XDR, IDaaS, Zero Trust Platform
- **CISA SCuBA:** Microsoft M365 hardening baseline published by CISA (2023)
