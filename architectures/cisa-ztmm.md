# CISA Zero Trust Maturity Model v2.0 (ZTMM)

**Version:** 2.0 (April 2023)  
**Source:** https://www.cisa.gov/zero-trust-maturity-model  
**Type:** Government Reference Framework (US Federal)

---

## Overview

The CISA Zero Trust Maturity Model (ZTMM) v2.0 is the US Federal Government's authoritative guidance on implementing Zero Trust Architecture (ZTA) aligned with Executive Order 14028 (May 2021, "Improving the Nation's Cybersecurity"). It provides a **maturity progression model** across five pillars and three cross-cutting capabilities, with four maturity stages.

Unlike vendor architectures (which map to specific products), ZTMM is **vendor-neutral** — it describes capabilities that should be achieved, not which vendor achieves them. Federal agencies use ZTMM to self-assess and plan ZTA investments. ZTMM is also widely adopted by enterprises as a maturity framework for ZTA planning.

**Regulatory context:** ZTMM supports OMB Memorandum M-22-09 (Federal Zero Trust Strategy) requiring agencies to achieve specific ZTMM milestones by FY2024.

---

## Maturity Stages

| Stage | Description | Characteristics |
|-------|-------------|-----------------|
| **Traditional** | Legacy perimeter-based security | Static policies, manual processes, siloed tools |
| **Initial** | Early ZT adoption | Some automation, attribute-based access in limited areas |
| **Advanced** | Broad ZT implementation | Cross-pillar integration, continuous monitoring, automated responses |
| **Optimal** | Full ZT with continuous improvement | Fully automated, dynamic policy, all assets under ZT governance |

---

## Five Pillars

### Pillar 1: Identity
*Agencies must use strong authentication for all users and non-person entities.*

| Capability | Traditional | Initial | Advanced | Optimal |
|------------|-------------|---------|----------|---------|
| MFA | Password only | MFA on some systems | Phishing-resistant MFA (FIDO2) everywhere | Continuous auth; step-up for sensitive actions |
| Identity Governance | Manual provisioning | Some IGA | Automated lifecycle, access reviews | AI-driven access recommendations |
| Non-Person Entities | Static service accounts | Some rotation | Managed workload identities | Just-in-time, ephemeral credentials |

**Technology categories:** IAM/SSO/MFA, IGA, CIEM, PAM, Secrets Management

### Pillar 2: Devices
*All devices must be enrolled, inventoried, and assessed before access is granted.*

| Capability | Traditional | Initial | Advanced | Optimal |
|------------|-------------|---------|----------|---------|
| Asset Inventory | Manual/incomplete | Partial CMDB | Automated discovery, all devices | Real-time, authoritative inventory |
| Device Health | No posture check | Basic MDM | Continuous compliance assessment | Real-time risk scoring per request |
| EDR/Detection | AV only | EDR on some | EDR everywhere | Behavioral AI; automated response |

**Technology categories:** Asset Management, MDM/EMM, EDR/EPP, Vulnerability Management

### Pillar 3: Networks
*Networks must be segmented, monitored, and traffic must be encrypted.*

| Capability | Traditional | Initial | Advanced | Optimal |
|------------|-------------|---------|----------|---------|
| Segmentation | VLANs, coarse | Some microseg | Workload-level microsegmentation | Application-level, per-request |
| Encryption | TLS on external | TLS on most internal | Encrypt all data in transit | mTLS everywhere (east-west) |
| DNS Security | Recursive resolver | Basic DNS filtering | DNSSEC + RPZ filters | Encrypted DNS (DoH/DoT) with ML detection |
| Traffic Monitoring | Netflow only | Some NDR | Full NDR + SIEM integration | Real-time ML anomaly detection |

**Technology categories:** NGFW, ZTNA/SSE/SASE, NDR, Microsegmentation

### Pillar 4: Applications & Workloads
*Applications must be discovered, secured, and continuously monitored.*

| Capability | Traditional | Initial | Advanced | Optimal |
|------------|-------------|---------|----------|---------|
| Application Discovery | Manual | Some catalog | Automated discovery + classification | Continuous; includes shadow IT |
| Access Control | Role-based, coarse | RBAC with some ABAC | Attribute-based access per request | Dynamic, context-aware, per-session |
| Runtime Protection | WAF on external | RASP on some | CWPP on all workloads | Behavioral anomaly; auto-block |
| Testing | Annual pentest | Quarterly scanning | Continuous DAST/SAST in pipeline | Shift-left with developer gates |

**Technology categories:** ZTNA, WAF/API Security, CNAPP, Application Security

### Pillar 5: Data
*Data must be categorized, protected, and access must be logged.*

| Capability | Traditional | Initial | Advanced | Optimal |
|------------|-------------|---------|----------|---------|
| Data Classification | Manual, inconsistent | Some automated labels | AI-assisted classification at ingestion | Real-time; policy-enforced at creation |
| DLP | Email gateway DLP | Endpoint + email DLP | Unified DLP across all channels | Dynamic; ML-based context-aware |
| Encryption | Encrypt at rest | Encrypt in transit | Encrypt + key management | Customer-managed keys, hardware HSM |
| Data Access Governance | File-share ACLs | RBAC on key stores | DSPM + access governance | Zero-standing access to sensitive data |

**Technology categories:** DLP, DSPM, Data Governance, Encryption/KMS

---

## Three Cross-Cutting Capabilities

### 1. Visibility & Analytics
Unified visibility across all five pillars — threat detection, anomaly detection, and security analytics.

- SIEM for log aggregation and correlation
- UEBA for behavioral baselines
- XDR for cross-domain detection
- Security Data Lake for historical analysis

**Technology categories:** SIEM, XDR/EDR, UEBA, NDR

### 2. Automation & Orchestration
Automated policy enforcement, incident response, and remediation across pillars.

- SOAR for playbook automation
- Infrastructure as Code for policy enforcement
- Auto-remediation triggered by detection signals
- Automated access revocation on anomaly

**Technology categories:** SOAR, Infrastructure Automation

### 3. Governance
Policy management, compliance, risk management, and decision frameworks for ZTA.

- Risk-informed ZT policy decisions
- Continuous compliance measurement
- Vendor risk management for ZTA supply chain
- Security awareness for ZT concepts

**Technology categories:** GRC, Policy Management, Security Awareness, TPRM

---

## NIST CSF 2.0 / ZTMM Crosswalk

| ZTMM Pillar | NIST CSF Function | Key Overlap |
|------------|------------------|-------------|
| Identity | Protect (PR.AA) | Authentication and authorization controls |
| Devices | Identify (ID.AM), Protect (PR.IR) | Asset management, device hardening |
| Networks | Protect (PR.IR), Detect (DE.CM) | Network segmentation, continuous monitoring |
| Applications | Protect (PR.PS), Detect (DE.CM) | Software integrity, workload monitoring |
| Data | Protect (PR.DS), Govern (GV.RM) | Data security, data-driven risk management |
| Visibility & Analytics | Detect (DE.CM, DE.AE) | Continuous monitoring, adverse event analysis |
| Automation & Orchestration | Respond (RS.MA, RS.MI) | Incident management, automated mitigation |
| Governance | Govern (GV.OC, GV.RM, GV.PO) | Organizational context, risk management, policy |

---

## Implementation Roadmap (Federal Agency Pattern)

**Year 1 (Traditional → Initial):**
- MFA for all privileged users (phishing-resistant preferred)
- Asset inventory automation (CMDB)
- EDR deployed on 80%+ of endpoints
- SIEM with cloud log ingestion
- Data classification policy and initial labeling

**Year 2 (Initial → Advanced):**
- FIDO2/phishing-resistant MFA everywhere
- ZTNA replacing VPN for remote access
- Microsegmentation on Crown Jewel systems
- NDR deployed for network visibility
- Unified DLP across endpoints, email, cloud

**Year 3+ (Advanced → Optimal):**
- Dynamic, attribute-based access control (ABAC)
- AI-driven anomaly detection (UEBA/XDR)
- Automated response playbooks (SOAR)
- DSPM for data-centric risk
- Continuous compliance measurement

---

## Applicability Beyond Federal

ZTMM is adopted by:
- **Financial services** — OCC, FFIEC use ZTMM as a ZTA assessment lens
- **Healthcare** — HHS/CISA joint guidance references ZTMM for HIPAA-adjacent ZTA
- **Critical infrastructure** — CISA Sector Risk Management Agencies (SRMAs) recommend ZTMM
- **Enterprise** — Widely used as a self-assessment tool regardless of regulatory mandate

---

## References

- CISA ZTMM v2.0: https://www.cisa.gov/zero-trust-maturity-model
- OMB M-22-09 (Federal ZT Strategy): https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf
- NIST SP 800-207 (ZTA): https://csrc.nist.gov/publications/detail/sp/800-207/final
- DoD ZT Strategy: https://dodcio.defense.gov/Portals/0/Documents/Library/DoD-ZTStrategy.pdf
