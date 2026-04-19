# Zero Trust Architecture (ZTA) — Complete Blueprint

**Standards:** NIST SP 800-207, CISA ZTMM v2.0, DoD ZT Strategy, OMB M-22-09  
**Source references:** Microsoft MCRA, Palo Alto ZTA, Zscaler ZTE, Google BeyondCorp, CISA ZTMM

---

## On This Page
- [What Zero Trust Is (and Isn't)](#what-zero-trust-is-and-isnt) — definition, principles, what it replaces
- [NIST SP 800-207 Logical Components](#nist-sp-800-207-logical-components) — Policy Engine, Policy Administrator, Policy Enforcement Point
- [Five Zero Trust Pillars — Technology Blueprint](#five-zero-trust-pillars--technology-blueprint) — Identity, Device, Network, Application, Data
- [Cross-Cutting Capabilities](#cross-cutting-capabilities) — Visibility & Analytics, Automation, Governance
- [ZTA Implementation Patterns](#zta-implementation-patterns) — VPN replacement, cloud workload, third-party, OT/ICS
- [ZTA Maturity Stages](#zta-maturity-stages) — 4-stage progression
- [ZTA Technology Stack by Organization Size](#zta-technology-stack-by-organization-size) — SMB / Mid-Enterprise / Large Enterprise
- [References](#references)

## At a Glance
- **Zero Trust is a strategy, not a product** — based on NIST SP 800-207's Policy Engine / Policy Administrator / Policy Enforcement Point model; every access request is evaluated against policy
- **5 pillars with distinct enabling technology**: Identity (IAM/PAM/IGA), Device (EDR/MDM/posture), Network (ZTNA/NGFW/NDR), Application (CASB/WAF/CNAPP), Data (DSPM/DLP/DAM)
- **CISA ZTMM** defines 4 maturity stages per pillar — most organisations are at Initial (stage 2); Advanced requires 2–3 years of focused investment
- **Technology stack varies by org size**: SMB → Microsoft-centric; Mid-Enterprise → Okta + CrowdStrike + Zscaler; Large Enterprise → multi-vendor depth
- **Highest-ROI starting point**: replace VPN with ZTNA + enforce MFA everywhere + deploy EDR — covers the three most common ZT gaps at reasonable cost

## Summary

Zero Trust is the most overloaded term in cybersecurity — applied to everything from a marketing claim to a regulatory mandate to a specific product feature. This blueprint cuts through that noise. It grounds Zero Trust in NIST SP 800-207 (the authoritative US federal standard), defines what it actually requires architecturally, and maps the five ZTA pillars to the specific technology categories and products that implement them.

The architectural foundation is NIST SP 800-207's three logical components: a Policy Engine (the decision point), a Policy Administrator (the enforcement orchestrator), and a Policy Enforcement Point (the access gate). Every access request — from any user, device, or workload — flows through this model. Understanding this model is essential because it clarifies what vendors mean when they claim to deliver Zero Trust: a product that only operates at one of these three logical layers is not a complete ZTA, it is a component of one.

The five pillars (Identity, Device, Network, Application, Data) each have distinct enabling technology, a clear maturity progression, and different organisational owners. Most enterprises achieve Initial maturity in 12 months by focusing on Identity (MFA, conditional access) and Network (ZTNA replacing VPN). Reaching Advanced maturity across all pillars typically requires a 2–3 year programme. The technology stack by org size at the end of this document provides a concrete, vendor-specific implementation path for each maturity stage.

---

## What Zero Trust Is (and Isn't)

**Zero Trust is a strategy and architectural philosophy, not a product.** It rejects the assumption that anything inside a network perimeter is trustworthy. Every access request — from any user, device, application, or workload — must be verified explicitly, regardless of network location.

**Core principles (NIST SP 800-207):**
1. All data sources and computing services are resources
2. All communication is secured regardless of network location
3. Access is granted on a per-session basis
4. Access decisions are based on dynamic policy (identity + device + context)
5. All asset integrity and security posture is monitored and measured
6. Authentication and authorization are dynamic and continuously re-evaluated
7. The enterprise collects information about all assets, infrastructure, and network traffic

**What Zero Trust is NOT:** A single product, a firewall rule, a VPN replacement, or a one-time project.

---

## NIST SP 800-207 Logical Components

```
                    ┌─────────────────────────────────┐
                    │     CONTROL PLANE                │
                    │                                  │
User/Device ──────► │  Policy Engine (PE)              │
                    │  (Evaluates access request)       │
                    │         ↓                         │
                    │  Policy Administrator (PA)        │
                    │  (Communicates decision to PEP)   │
                    └──────────────┬──────────────────┘
                                   │ Allow/Deny
                    ┌──────────────▼──────────────────┐
                    │     DATA PLANE                   │
                    │                                  │
                    │  Policy Enforcement Point (PEP)  │
                    │  (Sits between user and resource) │
                    └──────────────┬──────────────────┘
                                   │ Authorized traffic only
                    ┌──────────────▼──────────────────┐
                    │     ENTERPRISE RESOURCES         │
                    │  (apps, data, services)           │
                    └──────────────────────────────────┘
```

### Component → Product Mapping

| NIST Component | Product Examples | Category |
|---------------|-----------------|---------|
| **Policy Engine (PE)** | Microsoft Entra Conditional Access, Okta Access Policies, Zscaler policy engine | [IAM/SSO/MFA](../technologies/categories/protect/iam-sso-mfa.yaml) |
| **Policy Administrator (PA)** | Entra ID, Okta, Ping, CyberArk (for privileged sessions) | [IAM/SSO/MFA](../technologies/categories/protect/iam-sso-mfa.yaml), [PAM](../technologies/categories/protect/pam.yaml) |
| **Policy Enforcement Point (PEP)** | Zscaler ZPA App Connector, Palo Alto Prisma Access, Microsoft Entra Private Access, CyberArk PSM | [ZTNA/SSE/SASE](../technologies/categories/protect/ztna-sse-sase.yaml) |
| **Continuous Diagnostics (CDM)** | CrowdStrike Falcon (device posture), Intune (MDM compliance), Tenable (VM) | [XDR/EDR](../technologies/categories/detect/xdr-edr.yaml), [MDM/EMM](../technologies/categories/protect/mdm-emm.yaml) |
| **Industry Compliance** | ServiceNow GRC, Compliance frameworks in SIEM | [GRC](../technologies/categories/govern/grc.yaml) |
| **Threat Intelligence** | Mandiant, CrowdStrike Intel, Talos | [Threat Intelligence](../technologies/categories/identify/threat-intelligence.yaml) |
| **Activity Logs / SIEM** | Sentinel, Splunk, Chronicle | [SIEM](../technologies/categories/detect/siem.yaml) |
| **Data Access Policy** | Microsoft Purview, Forcepoint DLP | [DLP](../technologies/categories/protect/dlp.yaml) |

---

## Five Zero Trust Pillars — Technology Blueprint

### Pillar 1: Identity

*Verify every identity, every time, with the least privilege needed.*

```
[User requests access]
        ↓
[Strong Authentication]     ← IAM/MFA (Entra, Okta) — FIDO2/Passkey preferred
        ↓
[Identity Risk Scoring]     ← Conditional Access policies + UEBA baseline
        ↓
[Device Health Check]       ← MDM compliance + EDR posture score (CrowdStrike ZTA)
        ↓
[Context Evaluation]        ← Location, time, risk score, application sensitivity
        ↓
[Grant Session (Scoped)]    ← JIT access via PAM for privileged; ZTNA for general
        ↓
[Continuous Monitoring]     ← UEBA monitors session behavior; step-up auth on anomaly
```

**Enabling technologies:**

| Capability | Technology | Products |
|-----------|-----------|---------|
| Phishing-resistant MFA | FIDO2/Passkey | Okta FastPass, Entra FIDO2, Duo FIDO |
| Conditional access | Policy engine | Entra Conditional Access, Okta Adaptive MFA |
| Identity governance | IGA | SailPoint, Saviynt, Entra ID Governance |
| Privileged access (JIT) | PAM | CyberArk Privilege Cloud, BeyondTrust |
| Non-human identity | Secrets Management | HashiCorp Vault, AWS Secrets Manager, CyberArk Conjur |
| Identity threat detection | ITDR | CrowdStrike Identity Protection, SentinelOne Singularity Identity, Entra ID Protection |
| Cloud permissions | CIEM | Entra Permissions Management, Wiz CIEM, Tenable Cloud Security |

**Maturity progression:** Password → MFA → Phishing-resistant MFA → Continuous risk evaluation → Passwordless

---

### Pillar 2: Devices

*Only healthy, managed devices gain access; device posture informs access decisions.*

```
[Device requests access]
        ↓
[Is device enrolled?]       ← MDM (Intune, Jamf) — enrolled + compliant required
        ↓
[Device health score]       ← EDR posture (CrowdStrike ZTA score, Defender compliance)
        ↓
[Vulnerability state]       ← VM (Tenable, Defender VM) — critical vulns = deny/limit
        ↓
[Trust level assigned]      ← Feeds into Policy Engine / Conditional Access
```

**Enabling technologies:**

| Capability | Technology | Products |
|-----------|-----------|---------|
| Enrollment + compliance | MDM/EMM | Microsoft Intune, Jamf, Workspace ONE |
| Device posture score | EDR + ZTA | CrowdStrike Falcon ZTA Assessment, Entra Device Compliance |
| Vulnerability state | VM | Defender VM, Tenable Nessus Agent, CrowdStrike Spotlight |
| Hardware attestation | TPM/Secure Boot | Device health attestation (Windows Hello for Business) |
| Mobile threat defense | MTD | Check Point Harmony Mobile, Lookout, Jamf Protect |
| Unmanaged device access | Browser isolation | Zscaler RBI, Cloudflare Browser Isolation |

**Maturity progression:** No controls → Basic MDM enrollment → MDM + EDR posture → Continuous risk scoring → Hardware-attested trusted devices

---

### Pillar 3: Networks

*Eliminate implicit trust based on network location; segment all traffic.*

```
[Traditional VPN model]            [Zero Trust Network model]
Corporate Network ──────────       User ──────────────────────────────────────
        ↓ (trusted once in)                                                    ↓
  All resources accessible         [Zscaler/Prisma PoP] → [App Connector] → App
  Lateral movement possible        Per-session, per-app authorization
  VPN = castle-and-moat            No network access — app access only
```

**Enabling technologies:**

| Capability | Technology | Products |
|-----------|-----------|---------|
| Replace VPN for users | ZTNA | Zscaler ZPA, Palo Alto Prisma Access, Entra Private Access, Cloudflare Access |
| Replace VPN for vendors | Vendor ZTNA | CyberArk Vendor Remote Access, BeyondTrust PRA |
| Microsegmentation | NGFW + policy | Palo Alto NGFW, FortiGate, Cisco TrustSec, Illumio |
| DNS security | DNS filtering | Cisco Umbrella, Zscaler DNS, Cloudflare Gateway |
| Encrypted traffic inspection | TLS inspection | Zscaler inline, Palo Alto NGFW SSL inspection |
| Network visibility | NDR | ExtraHop, Darktrace, Vectra AI, Cisco Stealthwatch |
| SD-WAN + security | SASE | Zscaler ZTE, Palo Alto Prisma, Cisco Secure Access |

**Maturity progression:** VLAN segmentation → NGFW microsegmentation → ZTNA VPN replacement → Application-level access only → Per-session, per-request authorization

---

### Pillar 4: Applications & Workloads

*Treat all applications as internet-facing; protect workloads at runtime.*

```
[External SaaS apps]    → Controlled via CASB + SWG (Zscaler ZIA / Netskope)
[Internal web apps]     → Protected via ZTNA + WAF (ZPA / Cloudflare Access)
[Cloud workloads]       → Protected via CNAPP + CWPP (Wiz / Prisma Cloud)
[Container workloads]   → Runtime security (Defender for Containers, Aqua)
[API endpoints]         → API security gateway (Kong, Apigee, AWS API GW + WAF)
[Serverless functions]  → IAM least privilege + runtime monitoring
```

**Enabling technologies:**

| Capability | Technology | Products |
|-----------|-----------|---------|
| App access (ZTNA) | Identity-aware proxy | Zscaler ZPA, Palo Alto Prisma, Entra Private Access |
| SaaS app control | CASB | Netskope, Zscaler CASB, Defender for Cloud Apps |
| Web app protection | WAF | Cloudflare WAF, Imperva, AWS WAF |
| API security | API gateway | Kong, Apigee, Azure APIM + Traceable |
| Cloud workload posture | CNAPP | Wiz, Prisma Cloud, Defender for Cloud |
| Container runtime | CWPP | Aqua Security, Sysdig, Defender for Containers |
| Application scanning | AppSec | Snyk, Checkmarx, Veracode (SAST/DAST) |

---

### Pillar 5: Data

*Classify all data; protect based on sensitivity; enforce at the data layer.*

```
[Data Classification]   → Microsoft Purview labels, Varonis auto-classification
        ↓
[Data Access Control]   → ABAC based on label (need-to-know enforcement)
        ↓
[Data in Use]           → Endpoint DLP (block copy/paste of sensitive data)
[Data in Transit]       → Network DLP + CASB (block upload to unsanctioned sites)
[Data at Rest]          → Encryption (KMS) + DSPM (discover misconfigured stores)
        ↓
[Data Rights]           → IRM (Microsoft Purview IRM — persistent encryption)
```

**Enabling technologies:**

| Capability | Technology | Products |
|-----------|-----------|---------|
| Discover & classify | DSPM | Wiz DSPM, Cyera, Varonis, BigID |
| Prevent leakage | DLP | Microsoft Purview DLP, Forcepoint, Netskope DLP |
| Protect at rest | Encryption + KMS | AWS KMS, Azure Key Vault, Thales CipherTrust |
| Protect in use | Endpoint DLP | Purview endpoint DLP, Forcepoint DLP |
| Protect cloud stores | CASB + CSPM | Netskope, Zscaler CASB, Wiz |
| Rights management | IRM | Microsoft Purview IRM, Adobe Acrobat |
| Database protection | DAM | Imperva, IBM Guardium |

---

## Cross-Cutting Capabilities

### Visibility & Analytics (SIEM + XDR + UEBA)

All five pillars generate signals that feed into the detection and response stack:

```
Identity signals (Entra/Okta)  ──┐
Device signals (EDR/MDM)        ──┤
Network signals (NDR/NGFW)      ──┼──► SIEM + XDR ──► SOAR ──► Automated Response
Application signals (WAF/ZTNA)  ──┤         ↑
Data signals (DLP/DSPM)         ──┘    UEBA baselines
```

**Products:** Microsoft Sentinel + Defender XDR, Google Chronicle + Mandiant, CrowdStrike XSIAM, Splunk ES + SOAR

### Automation & Orchestration (SOAR)

ZTA requires automated policy enforcement — manual processes cannot keep pace:
- Auto-revoke access when device compliance drops
- Auto-block user session on UEBA anomaly (step-up or terminate)
- Auto-rotate compromised credentials detected in dark web
- Auto-quarantine endpoint on malware detection

**Products:** Palo Alto XSOAR, Splunk SOAR, Microsoft Sentinel Logic Apps, CrowdStrike Falcon Fusion

### Governance (GRC + Policy)

ZTA requires formal policy decisions backed by risk management:
- Data classification policy drives DLP enforcement
- Access policy drives Conditional Access rules
- Incident response policy drives SOAR playbooks
- Compliance requirements (PCI, HIPAA, ZTMM) drive control selection

---

## ZTA Implementation Patterns

### Pattern 1: VPN Replacement (Remote Access ZTA)

**Problem:** VPN grants network-level access — too broad, lateral movement risk.

```
Before: [User] → [VPN] → [Corporate Network] (full access)
After:  [User] → [Identity + Device check] → [ZTNA broker] → [Specific app only]
```

**Stack:** Okta/Entra ID (identity) + Intune/Jamf (device) + Zscaler ZPA or Palo Alto Prisma Access (ZTNA) + CrowdStrike/MDE (device posture signal)

**Timeline:** 3-6 months for initial rollout; 12 months for full VPN retirement.

---

### Pattern 2: Cloud Workload ZTA

**Problem:** Cloud workloads with over-permissive IAM roles, east-west traffic without mTLS, secrets in environment variables.

```
[CI/CD] → [Image scan (Wiz/Snyk)] → [Deploy with workload identity (IRSA/Workload ID)]
[Runtime] → [CWPP monitoring] → [mTLS service mesh (Istio/Linkerd)]
[Secrets] → [Vault/Secrets Manager sidecar] → [No plaintext secrets in env vars]
```

**Stack:** Wiz (CNAPP + CIEM) + HashiCorp Vault or cloud Secrets Manager + Istio/Linkerd (service mesh) + Snyk/Prisma (shift-left)

---

### Pattern 3: Third-Party Vendor ZTA

**Problem:** Vendors need remote access to sensitive systems; VPN grants too much.

```
[Vendor] → [Vendor identity (external IdP federation)] → [JIT credential grant (CyberArk)]
         → [Session proxy (PSM)] → [Session recorded] → [Time-limited access]
```

**Stack:** CyberArk Vendor Remote Access or BeyondTrust Privileged Remote Access + SIEM for audit

---

### Pattern 4: OT/ICS Zero Trust

**Problem:** OT environments have legacy systems that can't run agents; VPN creates risk.

```
[IT-OT network boundary] → [Industrial DMZ] → [OT network]
[Vendor/engineer access] → [CyberArk PRA browser-based RDP/SSH] → [Jump server]
[Monitoring] → [Passive NDR (Claroty/Dragos)] → [SIEM]
[Segmentation] → [Fortinet/Palo Alto NGFW] → [Zone isolation]
```

**Stack:** PAM (CyberArk/BeyondTrust) for access + NDR (Claroty/Dragos) for monitoring + NGFW (FortiGate ruggedized) for segmentation + SIEM for audit

---

## ZTA Maturity Stages

| Stage | Description | Technologies Required |
|-------|-------------|----------------------|
| **Stage 1: Traditional** | Perimeter-based; VPN; implicit trust | Basic IAM, NGFW |
| **Stage 2: Initial** | MFA deployed; some MDM; ZTNA pilot | IAM + MFA, MDM, ZTNA (partial), basic SIEM |
| **Stage 3: Advanced** | ZTNA replaces VPN; EDR everywhere; microsegmentation on critical paths | ZTNA, EDR, UEBA, NDR, PAM (privileged), CNAPP |
| **Stage 4: Optimal** | ABAC/dynamic policy; AI-driven anomaly; automated response; data-centric | Full DSPM, SOAR automation, AI UEBA, passwordless, JIT access everywhere |

---

## ZTA Technology Stack by Organization Size

### SMB (100-500 users)
- **Identity:** Microsoft Entra ID P1 (MFA + Conditional Access)
- **Device:** Microsoft Intune + Defender for Endpoint P1
- **Network:** Zscaler or Cloudflare (ZTNA + SWG), Cisco Umbrella (DNS)
- **Data:** Microsoft Purview basic DLP

### Mid-Enterprise (500-5,000 users)
- **Identity:** Okta (SSO + Adaptive MFA) or Entra ID P2 + CyberArk PAM
- **Device:** CrowdStrike Falcon + Intune/Jamf
- **Network:** Zscaler ZPA + ZIA (full SSE), or Palo Alto Prisma Access
- **Detection:** Microsoft Sentinel + CrowdStrike XDR
- **Data:** Microsoft Purview DLP + Varonis

### Large Enterprise (5,000+ users)
- **Identity:** Okta Enterprise + CyberArk Privilege Cloud + SailPoint IGA
- **Device:** CrowdStrike Enterprise + Intune + Tenable VM
- **Network:** Zscaler full ZTE or Palo Alto full SASE
- **Detection:** Sentinel or Chronicle + CrowdStrike XDR + NDR (ExtraHop/Darktrace)
- **Data:** Purview E5 DLP + Wiz DSPM + Varonis
- **Response:** Palo Alto XSOAR or Splunk SOAR + CyberArk Conjur

---

## References

- NIST SP 800-207 Zero Trust Architecture: https://csrc.nist.gov/publications/detail/sp/800-207/final
- CISA Zero Trust Maturity Model v2.0: https://www.cisa.gov/zero-trust-maturity-model
- DoD Zero Trust Strategy: https://dodcio.defense.gov/Portals/0/Documents/Library/DoD-ZTStrategy.pdf
- OMB M-22-09 (Federal ZT Strategy): https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf
- NSA Zero Trust Guidance: https://media.defense.gov/2021/Feb/25/2002588479/-1/-1/0/CSI_EMBRACING_ZT_SECURITY_MODEL_UOO115131-21.PDF
- Google BeyondCorp: https://cloud.google.com/beyondcorp
