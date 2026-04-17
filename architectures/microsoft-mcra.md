# Microsoft Cybersecurity Reference Architecture (MCRA)

**Version:** 2024  
**Source:** https://aka.ms/mcra  
**Type:** Platform Reference Architecture

---

## Overview

The Microsoft Cybersecurity Reference Architecture (MCRA) is Microsoft's prescriptive guidance for building a security architecture using Microsoft and partner products. It is the most widely referenced vendor security architecture in enterprise, driven by M365 and Azure ubiquity. MCRA frames security across six domains and positions Microsoft 365 Defender, Microsoft Sentinel, Entra ID, and Defender for Cloud as the core pillars.

The architecture is notable for its **native integration** story — all Microsoft security products share a common identity plane (Entra ID), telemetry bus (Microsoft Defender XDR), and SIEM (Sentinel), enabling correlated detection that standalone tools struggle to match.

---

## Architecture Domains

```
┌─────────────────────────────────────────────────────────────────┐
│                   MICROSOFT SECURITY ARCHITECTURE               │
├───────────────────┬─────────────────────┬───────────────────────┤
│  SECURITY OPS     │  IDENTITY & ACCESS  │  INFORMATION PROT.   │
│  Microsoft Sentinel│  Entra ID (AAD)    │  Microsoft Purview    │
│  Defender XDR     │  Entra ID Governance│  MIP / Sensitivity    │
│  Defender TI      │  Entra Verified ID  │  DLP (M365 + Endpoint)│
│  Copilot Security │  Entra Permissions  │  Insider Risk Mgmt    │
├───────────────────┼─────────────────────┼───────────────────────┤
│  DEVICE SECURITY  │  CLOUD INFRA        │  AI SECURITY          │
│  Defender for     │  Defender for Cloud │  Defender for AI      │
│    Endpoint       │  Defender CSPM      │  AI Security Posture  │
│  Intune (MDM/MAM) │  Defender for       │  Entra Workload ID    │
│  Defender for     │    Servers/SQL/     │  Copilot for Security │
│    Business       │    Containers/App   │                       │
└───────────────────┴─────────────────────┴───────────────────────┘
```

### Domain 1: Security Operations
| Product | Category | Notes |
|---------|----------|-------|
| Microsoft Sentinel | SIEM | Cloud-native SIEM; SOAR built-in via Logic Apps |
| Microsoft Defender XDR | XDR | Unified XDR correlating endpoint, identity, email, cloud |
| Microsoft Defender Threat Intelligence (MDTI) | Threat Intelligence | RiskIQ acquisition; internet-scale threat intel |
| Copilot for Security | AI-assisted SOC | GenAI analyst assistant across all Defender products |

### Domain 2: Identity & Access Management
| Product | Category | Notes |
|---------|----------|-------|
| Microsoft Entra ID | IAM / SSO / MFA | Formerly Azure AD; cloud identity plane for M365 + Azure |
| Entra ID Governance | IGA | Access reviews, entitlement management, provisioning |
| Entra Permissions Management | CIEM | Cloud permissions/entitlement management (CloudKnox acquisition) |
| Entra Verified ID | Decentralized Identity | W3C VC standard; verifiable credentials |
| Entra Workload ID | Non-human identity | Service principal / managed identity lifecycle |
| Microsoft Entra Private Access | ZTNA | ZTNA for private apps (Defender for Cloud Apps backend) |
| Microsoft Entra Internet Access | SWG/CASB | SWG + CASB for internet traffic (part of Entra Suite) |

### Domain 3: Information Protection
| Product | Category | Notes |
|---------|----------|-------|
| Microsoft Purview | DLP / IRM | Unified data governance — sensitivity labels, DLP, compliance |
| Insider Risk Management | DLP / UEBA | Behavioral signals for insider threats; M365-native |
| Communication Compliance | eDiscovery | Regulatory compliance for Teams/Exchange communications |
| Defender for Office 365 | Email Security | Anti-phishing, safe links, safe attachments for Exchange/M365 |

### Domain 4: Device Security
| Product | Category | Notes |
|---------|----------|-------|
| Microsoft Defender for Endpoint (MDE) | EDR / EPP | Enterprise EDR; P1 = EPP, P2 = full EDR + threat hunting |
| Microsoft Intune | MDM / EMM | Unified endpoint management (Windows, macOS, iOS, Android) |
| Defender for Business | SMB EDR | Streamlined MDE for <300 seat organizations |
| Defender Vulnerability Management | Vulnerability Management | EASM-adjacent; device-centric exposure assessment |

### Domain 5: Cloud Infrastructure Security
| Product | Category | Notes |
|---------|----------|-------|
| Microsoft Defender for Cloud | CNAPP | CSPM + CWPP; multi-cloud (AWS, GCP, Azure) |
| Defender CSPM | CSPM | Agentless posture management; attack path analysis |
| Defender for Servers | CWPP | Server workload protection (Defender for Endpoint integration) |
| Defender for Containers | Container Security | Runtime + image scanning + Kubernetes admission control |
| Defender for SQL / App Service | Workload-specific | PaaS service protection |
| Azure DDoS Protection | DDoS | Standard + Network layer volumetric protection |
| Azure Firewall | NGFW | Cloud-native stateful firewall (not hardware NGFW) |
| Azure Web Application Firewall | WAF | Integrated with Azure Front Door and Application Gateway |

### Domain 6: AI Security
| Product | Category | Notes |
|---------|----------|-------|
| Defender for AI | AI/LLM Security | Prompt injection detection, AI workload monitoring |
| AI Security Posture Management | AI Security | Posture management for AI services and model access |
| Copilot for Security | AI-assisted Security | GPT-4 powered analyst; summarization, script analysis, threat intel |

---

## NIST CSF 2.0 Mapping

| NIST Function | Microsoft Products | Coverage |
|--------------|-------------------|----------|
| **Govern** | Purview Compliance Manager, Secure Score, Entra ID Governance | Partial — compliance posture, no GRC platform |
| **Identify** | Defender Vulnerability Management, Defender CSPM, Entra Permissions Mgmt | Strong for cloud; weaker for OT/legacy |
| **Protect** | Entra ID (MFA, SSPR), MDE (EPP), Intune, Defender for Office 365, Azure Firewall | Strong — M365 licensing bundles most controls |
| **Detect** | Sentinel, Defender XDR, Defender for Cloud, MDTI | Strong — XDR correlation across all domains |
| **Respond** | Sentinel SOAR (Logic Apps), Defender XDR automated investigation | Strong for automated response; no native case management |
| **Recover** | Azure Backup, Azure Site Recovery (native Azure; not a security product) | Partial — DR exists but outside security portfolio |

---

## Coverage Gaps

- **GRC / Risk Management:** No native GRC product; Compliance Manager provides posture scores, not risk treatment workflows. Gap filled by ServiceNow, Archer, or OneTrust.
- **PAM:** No native privileged access management; Microsoft recommends CyberArk, BeyondTrust, or Delinea integration.
- **Recovery:** Azure Backup/ASR are infrastructure products; they don't integrate into the security architecture natively.
- **OT/ICS:** Microsoft Defender for IoT (acquired Cyberx) provides partial OT visibility but limited enforcement.
- **NDR:** No dedicated network detection and response product; relies on Defender for Identity (AD) + network signals into Sentinel.

---

## Licensing Architecture

Microsoft security is sold through **E3/E5 licensing bundles** rather than product-by-product:

| License | Key Security Inclusions |
|---------|------------------------|
| M365 E3 | Entra ID P1, Defender for Business, Basic DLP |
| M365 E5 | Entra ID P2, MDE P2, Defender XDR, Sentinel SIEM, Purview |
| Entra Suite | Entra Private/Internet Access (ZTNA/SWG), ID Governance, Permissions Mgmt |
| Microsoft Defender for Cloud (PAYG) | CSPM + CWPP billed per resource |

**Architecture decision:** Organizations with M365 E5 already own most of the security stack — the marginal cost of activating Microsoft security is low. The risk is vendor lock-in and reduced best-of-breed capability in specific domains.

---

## Key Architecture Principles

1. **Zero Trust** — Entra Conditional Access as the policy engine; least privilege across identity, device, app, and data
2. **XDR Correlation** — All signals flow to Defender XDR; Sentinel aggregates cross-platform
3. **AI Augmentation** — Copilot for Security overlaid on all Defender products
4. **Cloud-Native** — Architecture favors Azure/M365-native services over on-premises controls

---

## References

- MCRA poster: https://aka.ms/mcra
- Microsoft Security documentation: https://learn.microsoft.com/en-us/security/
- Secure Score: https://security.microsoft.com/securescore
- CISA SCuBA (M365 hardening guidance): https://www.cisa.gov/scuba
