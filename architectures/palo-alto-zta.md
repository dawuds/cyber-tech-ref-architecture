# Palo Alto Networks Zero Trust Architecture

**Version:** 2024  
**Source:** https://www.paloaltonetworks.com/zero-trust  
**Type:** Zero Trust Reference Architecture

---

## Overview

Palo Alto Networks' Zero Trust Architecture (ZTA) is organized around five pillars — Identity, Devices, Networks, Applications & Workloads, and Data — drawn from NIST SP 800-207 and the DoD Zero Trust Strategy. The architecture is backed by three product platforms: **Strata** (network security / NGFW), **Prisma** (cloud/SASE), and **Cortex** (XDR/AI-driven security operations), now supplemented by an AI-powered operations layer called **Cortex XSIAM** (AI-driven SOC platform).

Palo Alto acquired IBM's QRadar SaaS assets (August 2024) to fold into Cortex, accelerating SIEM consolidation.

**Market position:** Leader in NGFW (Gartner MQ #1 alongside Fortinet), CNAPP, and XDR. Revenue ~$8B (FY2025 guidance). Broadest platform SKU count in security industry.

---

## Architecture Pillars

```
┌─────────────────────────────────────────────────────────────────────┐
│              PALO ALTO ZERO TRUST ARCHITECTURE                      │
├──────────────┬───────────────┬──────────────┬───────────┬───────────┤
│   IDENTITY   │    DEVICES    │   NETWORKS   │   APPS /  │   DATA    │
│              │               │              │  WORKLOADS│           │
│ Prisma Access│ Cortex XDR    │ NGFW (Strata)│ Prisma    │ Enterprise│
│ (identity-   │ (endpoint)    │ Prisma Access│   Cloud   │   DLP     │
│  aware ZTNA) │ Traps (NGAV)  │ (SASE/SSE)  │ (CNAPP)   │ Prisma    │
│ GlobalProtect│ GlobalProtect │ Prisma SD-WAN│ App-ID    │ Cloud DLP │
└──────────────┴───────────────┴──────────────┴───────────┴───────────┘
                            ↓ ↓ ↓
              ┌─────────────────────────────────┐
              │   CORTEX XSIAM — AI-DRIVEN SOC  │
              │   XDR + SIEM + SOAR + TI unified │
              └─────────────────────────────────┘
```

---

## Platform Products by Domain

### Strata — Network Security
| Product | Category | Notes |
|---------|----------|-------|
| Palo Alto NGFW (PA series) | NGFW | Hardware appliances 200M–3.8T NGFW throughput |
| Palo Alto VM-Series | NGFW | Virtualized NGFW for private/public cloud |
| Palo Alto CN-Series | NGFW | Containerized NGFW for Kubernetes |
| Panorama | Network Security Mgmt | Centralized NGFW policy and telemetry management |
| Advanced Threat Prevention (ATP) | IPS / Threat Prevention | Inline ML-based threat prevention across NGFW |
| Advanced URL Filtering | SWG | Web filtering with ML-based phishing detection |
| Advanced WildFire | Sandbox | Cloud-based malware analysis and sandboxing |
| DNS Security | DNS Security | DNS-layer protection integrated into NGFW |

### Prisma — Cloud & Access Security
| Product | Category | Notes |
|---------|----------|-------|
| Prisma Access | ZTNA / SSE / SASE | SASE delivered from 100+ cloud PoPs; SD-WAN integrated |
| Prisma Cloud (CNAPP) | CNAPP | Aqua Security-competing CNAPP: CSPM+CWPP+CIEM+AppSec |
| Prisma SD-WAN (CloudGenix) | SD-WAN | SD-WAN fabric (CloudGenix acquisition 2020) |
| Enterprise DLP | DLP | Network + endpoint + cloud DLP unified |
| SaaS Security | CASB | Inline + API CASB within Prisma Access |
| Autonomous Digital Experience Management (ADEM) | Digital Experience | End-to-end user experience monitoring |

### Cortex — AI-Driven Security Operations
| Product | Category | Notes |
|---------|----------|-------|
| Cortex XDR | XDR / EDR | Multi-platform XDR; stitches network, endpoint, cloud |
| Cortex XSIAM | AI SOC Platform | AI-driven SOC: XDR + SIEM + SOAR + TI in one platform |
| Cortex XSOAR | SOAR | Market-leading SOAR (Demisto acquisition 2019); IBM QRadar SOAR folded in |
| Cortex Xpanse | EASM | External attack surface management (Expanse acquisition 2020) |
| Cortex XMDR | MDR | Managed detection & response built on Cortex stack |
| Unit 42 | IR / CTI | Threat intelligence and incident response services team |

---

## NIST CSF 2.0 Mapping

| NIST Function | Palo Alto Products | Coverage |
|--------------|-------------------|----------|
| **Govern** | Prisma Cloud compliance dashboards, Panorama policy mgmt | Weak — no GRC platform; compliance posture only |
| **Identify** | Cortex Xpanse (EASM), Prisma Cloud (CSPM), Cortex XDR (asset inventory) | Strong for cloud/external exposure; agent-required for internal |
| **Protect** | NGFW, Prisma Access (SASE/ZTNA), Prisma Cloud CWPP, Enterprise DLP, Traps/Cortex XDR | Very strong — broadest protection surface in industry |
| **Detect** | Cortex XDR, Cortex XSIAM, Advanced Threat Prevention, WildFire | Very strong — unified XDR detection across all domains |
| **Respond** | Cortex XSOAR, XSIAM, Unit 42 (IR services), XMDR | Very strong — market-leading SOAR + managed IR team |
| **Recover** | No native recovery products | Absent — no backup or DR tooling |

---

## Coverage Gaps

- **IAM / Identity:** No native enterprise IAM/SSO/MFA; Prisma Access provides identity-aware access but relies on IdP (Okta, Entra). No PAM product.
- **Email Security:** No native email gateway; focuses on Secure Email Gateway integration with Cortex XDR.
- **Recovery:** No backup, BCP, or DR tooling.
- **GRC:** No governance, risk, and compliance platform.
- **Endpoint Maturity vs. CrowdStrike:** Cortex XDR on Windows competitive; weaker Linux/macOS agent historically.

---

## The XSIAM Bet

**Cortex XSIAM** (2022 launch, accelerating in 2024) is Palo Alto's most disruptive product: a replacement for SIEM + SOAR + UEBA + TI in a single AI-native platform. Positioned against Microsoft Sentinel and Splunk.

Key differentiators:
- ML-based alert stitching (reduces analyst alert volume by claimed 98%)
- Built-in SOAR automation without separate XSOAR license
- Integrated threat intelligence from Unit 42
- 30-second mean time to detection (MTTD) claim vs. hours for traditional SIEM

Risk: High price point, complex migration from legacy SIEM, data ingestion costs.

---

## References

- Palo Alto Zero Trust: https://www.paloaltonetworks.com/zero-trust
- Cortex XSIAM: https://www.paloaltonetworks.com/cortex/cortex-xsiam
- Unit 42 Threat Report: https://unit42.paloaltonetworks.com/
- Prisma Cloud documentation: https://docs.prismacloud.io/
