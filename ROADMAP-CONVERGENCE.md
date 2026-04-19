# Security Roadmap Convergence & Solutioning Guide

**Last Updated:** April 2025  
**Purpose:** Where vendor roadmaps converge → what the optimal stack looks like for each org type and use case

---

## On This Page
- [The Central Thesis](#the-central-thesis) — why convergence creates a solutioning opportunity
- [Where Roadmaps Are Converging](#where-roadmaps-are-converging) — 5 convergence themes with vendor comparison tables
- [Recommended Stacks by Organization Profile](#recommended-stacks-by-organization-profile) — SMB → Cloud-Native → OT/ICS
- [Vendor Selection Decision Trees](#vendor-selection-decision-trees) — SIEM, Identity, CNAPP, SSE
- [Where Roadmaps Diverge](#where-roadmaps-diverge-buyer-beware) — 4 structural gaps no platform covers
- [3-Year Security Architecture Roadmap Template](#3-year-security-architecture-roadmap-template) — Year 1 Foundation → Year 3 Advanced

## At a Glance
- **7 platform vendors** (Microsoft, Palo Alto, CrowdStrike, Google, Cisco, Zscaler, SentinelOne) are converging on the same destination: Identity + Endpoint + Network + Cloud + SOC unified
- **5 convergence themes**: AI SOC Platform, Identity Security Platform, CNAPP, SSE/SASE, Data Security Platform
- **Stack choice depends on current investment**: M365-first → Microsoft; CrowdStrike EDR → LogScale SIEM; Azure-primary → Defender for Cloud CNAPP
- **3 structural gaps** no platform covers: GRC/TPRM, Backup/Recovery, and deep PAM — require dedicated budget regardless of platform choice
- **3-year roadmap**: Year 1 Foundation (IdP + ZTNA + EDR + SIEM), Year 2 Depth (CNAPP + IGA + DSPM + SOAR), Year 3 Advanced (AI SOC + CTEM + Zero Trust Data)

## Summary

Seven platform vendors are independently converging on the same architectural destination: a unified platform covering Identity + Endpoint + Network + Cloud + SOC. CrowdStrike starts from endpoint and expands; Zscaler starts from network access; Microsoft starts from identity and the M365 productivity suite. The paths differ, but the destination is identical. This convergence creates a practical solutioning shortcut: the platform whose current coverage best matches your existing investment is typically the lowest-friction path forward.

This document translates that market observation into actionable guidance. The five convergence themes section maps exactly where platform roadmaps overlap — AI SOC Platform, Identity Security, CNAPP, SSE/SASE, and Data Security are all converging toward 2–3 dominant platforms each. The recommended stacks section gives concrete product choices by organisation profile (SMB through to OT/ICS operator). The decision trees provide structured vendor selection logic for the four most common buying decisions: SIEM, Identity, CNAPP, and SSE/ZTNA.

Critically, this document also identifies where vendor roadmaps do **not** converge. GRC/TPRM, backup/recovery, and deep PAM are structurally outside every platform strategy. These three areas require dedicated budget and specialist vendor relationships regardless of which platform you choose — no amount of platform consolidation eliminates this.

---

## The Central Thesis

Seven platform mega-vendors (Microsoft, Palo Alto, CrowdStrike, Google, Cisco, Zscaler, SentinelOne) are all converging on the same architectural destination: a **single platform covering Identity + Endpoint + Network + Cloud + SOC**. The path differs; the destination is identical.

This convergence creates a solutioning opportunity: match org context to the platform whose convergence path aligns with the org's current investment.

---

## Where Roadmaps Are Converging

### Convergence 1: The AI SOC Platform

**Every major SOC vendor is building the same thing:**

```
Traditional (2020):     SIEM + SOAR + UEBA + TI = 4 vendors
Modern (2025):          One platform = SIEM + XDR + SOAR + UEBA + TI
```

| Vendor | Platform | SIEM | XDR | SOAR | AI Layer |
|--------|---------|------|-----|------|----------|
| Palo Alto | Cortex XSIAM | QRadar SaaS (acq.) | Cortex XDR | XSOAR | AI Copilot |
| Microsoft | Sentinel + Defender XDR | Sentinel | Defender XDR | Logic Apps/Sentinel | Copilot for Security |
| Google | Google SecOps | Chronicle | Mandiant MDR | Chronicle SOAR | AI workbench |
| CrowdStrike | Falcon | LogScale | Falcon XDR | Falcon Fusion | Charlotte AI |
| Cisco | XDR + Splunk ES | Splunk ES | Cisco XDR | Splunk SOAR | AI Assistant |
| SentinelOne | Singularity | Singularity AI-SIEM | Singularity XDR | Singularity Automation | Purple AI |

**Solutioning implication:** If you are replacing or modernizing your SIEM, you are buying an AI SOC platform. Evaluate as a platform, not a point product.

---

### Convergence 2: Identity Security Platform

```
Traditional (2020):     SSO + MFA + IGA + PAM + CIEM = 5 vendors
Modern (2025):          2-3 vendors max; platform bundles are viable
```

**Three-way platform battle:**

| Platform | SSO/MFA | IGA | PAM | CIEM | Secrets |
|---------|---------|-----|-----|------|---------|
| **Microsoft Entra Suite** | ✓ (Entra ID P2) | ✓ (Entra Governance) | Partial (Entra PIM — cloud only) | ✓ (Entra Permissions Mgmt) | ✗ |
| **CyberArk Identity Security** | ✓ (CyberArk Identity) | ✓ (Identity Flows) | ✓ (Privilege Cloud — market leader) | ✓ (Cloud Entitlements) | ✓ (Conjur) |
| **Okta** | ✓ (Workforce Identity) | Growing (OIG) | ✓ (Okta PAM — new 2024) | ✗ (via partners) | ✗ |

**Convergence insight:** Microsoft Entra E5 bundle wins for SMB/M365-native orgs where feature parity is sufficient. CyberArk wins where PAM depth is non-negotiable (banks, critical infrastructure). Okta wins the workforce SSO + MFA platform; extending into PAM reduces its specialist disadvantage.

---

### Convergence 3: CNAPP as Cloud Security Default

```
Traditional (2020):     CSPM + CWPP + CIEM + Container Sec + IaC = 5 vendors
Modern (2025):          CNAPP = all of the above, one platform
```

| Vendor | CSPM | CWPP | CIEM | Container | IaC Scan | DSPM |
|--------|------|------|------|-----------|----------|------|
| **Wiz** (→ Google) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Palo Alto Prisma Cloud** | ✓ | ✓ | ✓ | ✓ | ✓ | Partial |
| **CrowdStrike Falcon Cloud** | ✓ | ✓ | ✓ | ✓ | Partial | ✗ |
| **Microsoft Defender for Cloud** | ✓ | ✓ | ✓ | ✓ | Partial | ✗ |
| **Lacework** (→ Fortinet) | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ |

**Convergence insight:** Wiz + Google acquisition ($23B, pending) accelerates CNAPP as the default GCP security posture. Prisma Cloud remains dominant in multi-cloud enterprise. Microsoft Defender for Cloud wins in Azure-first orgs through E5 bundling.

---

### Convergence 4: SSE / SASE Replacing VPN + On-prem NGFW (for Branch/Remote)

```
Traditional (2020):     VPN + SWG + CASB + NGFW (appliance) = 4 products
Modern (2025):          SSE/SASE = ZTNA + SWG + CASB + DLP + RBI, cloud-delivered
```

| Vendor | ZTNA | SWG | CASB | DLP | RBI | SD-WAN |
|--------|------|-----|------|-----|-----|--------|
| **Zscaler** | ZPA | ZIA | ZIA CASB | ZIA DLP | ZIA RBI | No |
| **Palo Alto Prisma Access** | Prisma ZTNA | Prisma SWG | Prisma CASB | Prisma DLP | No | Prisma SD-WAN |
| **Netskope** | NPA | Netskope SWG | Netskope CASB | Netskope DLP | Netskope RBI | No |
| **Cloudflare One** | Access | Gateway | CASB | DLP | RBI | Magic WAN |
| **Microsoft** | Global Secure Access | Entra Internet Access | Defender for Cloud Apps | Purview DLP | No | No |

**Convergence insight:** Zscaler ZTE (Zero Trust Everywhere) is the most complete SSE platform, justifying its premium pricing for large enterprises. Cloudflare One is gaining rapidly in mid-market due to pricing and edge network advantage. Microsoft's "Security Service Edge" (Global Secure Access) will absorb SMB demand for organizations already on E5.

---

### Convergence 5: Data Security Platform (DSPM + DLP + DAM)

**Still fragmenting; convergence is 2025-2027:**

```
Current state:
[Cloud DSPM] + [Network/Endpoint DLP] + [Database DAM] = 3 separate platforms

Converging toward:
[Unified Data Security Platform] = discover + classify + protect + monitor
```

**Vendors driving convergence:**
- **Microsoft Purview** — Classification + DLP (endpoint/cloud/network) + DAM (Defender for SQL) + compliance — strongest in M365 environments
- **Wiz DSPM** (post-Google) — Cloud data discovery + exposure path to data risk — CNAPP-native
- **Varonis** — File-centric data security + identity-aware behavioral analytics + DAM-lite
- **Dig Security** (→ Palo Alto, 2024) — DSPM + DLP + DDR — first true unified data security platform

---

## Recommended Stacks by Organization Profile

### Profile A: SMB / 100-500 Users / M365-First

**Strategic posture:** Maximize Microsoft E5 before adding point products.

```
Identity:     Microsoft Entra ID P2 (MFA + Conditional Access + PIM)
Endpoint:     Microsoft Defender for Endpoint P2 + Intune
Network:      Entra Internet Access (SSE) or Cloudflare One (if budget allows)
Email:        Defender for Office 365 P2
Data:         Microsoft Purview E5 Compliance (DLP + Sensitivity Labels)
Cloud:        Microsoft Defender for Cloud (if Azure)
SOC:          Microsoft Sentinel (E5 bundled)
```

**Total platform vendors:** 1 (Microsoft)  
**Key gap:** No on-prem PAM; limited DSPM outside Azure; no EDR behavioral depth vs. CrowdStrike

---

### Profile B: Mid-Enterprise / 500-5,000 Users / Cloud-Hybrid

**Strategic posture:** Best-of-breed for critical controls; consolidate where possible.

```
Identity:     Okta Workforce Identity + CyberArk PAM (for privileged accounts)
Endpoint:     CrowdStrike Falcon Complete (EDR + NGAV + Insight XDR)
Network:      Zscaler ZIA + ZPA (full SSE — replace VPN entirely)
Email:        Proofpoint Essentials or Microsoft Defender for Office P2
Data:         Microsoft Purview DLP + Varonis (for file/identity depth)
Cloud:        Wiz (CNAPP) or Microsoft Defender for Cloud
VM:           Tenable One or Qualys
SOC:          Microsoft Sentinel (if M365) or CrowdStrike Falcon + LogScale
```

**Total platform vendors:** 3-4  
**Key gap:** Requires integration work between CrowdStrike XDR and Okta/Zscaler telemetry; cost is higher than Microsoft mono-vendor

---

### Profile C: Large Enterprise / 5,000+ Users / Multi-Cloud / Regulated

**Strategic posture:** Depth over cost; multi-vendor for critical categories; platform for SOC.

```
Identity:
  SSO/MFA:    Okta Workforce Identity Cloud
  PAM:        CyberArk Privilege Cloud (privileged + DevOps secrets)
  IGA:        SailPoint IdentityNow
  CIEM:       Wiz CIEM or Entra Permissions Management

Endpoint:
  EDR/XDR:    CrowdStrike Falcon Enterprise + Insight XDR
  VM:         Tenable One Vulnerability Management

Network:
  SSE/SASE:   Zscaler ZTE (ZIA + ZPA + ZDX) for remote/branch
  DC NGFW:    Palo Alto Networks PA-Series or VM-Series
  NDR:        ExtraHop Reveal(x) or Darktrace (post-Thoma Bravo)

Cloud:
  CNAPP:      Wiz (CSPM + CWPP + CIEM + DSPM)
  Cloud NGFW: AWS Network Firewall + Palo Alto Cloud NGFW

Data:
  DLP:        Microsoft Purview (endpoint) + Zscaler (network/inline)
  DSPM:       Wiz DSPM
  DAM:        IBM Guardium (for regulated databases: Oracle, SQL Server)
  Classification: Microsoft Purview Sensitivity Labels

Email:        Proofpoint Enterprise (TAP + Archive + TRAP)

SOC:
  SIEM:       Microsoft Sentinel or Google Chronicle
  XDR:        CrowdStrike Falcon XDR
  SOAR:       Palo Alto XSOAR or Splunk SOAR (if Cisco/Splunk)
  TI:         Recorded Future (external) + Mandiant Threat Intel
  NDR feed:   Into SIEM

GRC:          ServiceNow GRC (risk, policy, vendor risk) + BitSight (TPRM)
Recovery:     Veeam Hardened Repository + Rubrik Polaris (immutable backup)
```

**Total platform vendors:** 6-8  
**Total annual cost range:** $8M-$20M depending on headcount and scope

---

### Profile D: Cloud-Native / SaaS Business / No On-Prem

**Strategic posture:** SSE + CNAPP + Identity platform as the entire perimeter.

```
Identity:     Okta (SSO + Adaptive MFA) or Google Workspace + BeyondCorp
Endpoint:     CrowdStrike or SentinelOne (cloud-managed)
Network:      Cloudflare One (ZTNA + Gateway + CASB) — no hardware NGFW
Cloud:        Wiz (CNAPP) — cloud is the perimeter
Data:         Netskope DLP (inline) + Wiz DSPM
SOC:          Google SecOps (Chronicle) or SentinelOne AI-SIEM
```

**Total platform vendors:** 3  
**No on-prem infrastructure required**

---

### Profile E: OT/ICS Operator / Critical Infrastructure

**Strategic posture:** IT/OT convergence; IEC 62443 compliance; passive inspection mandate.

```
IT Security (standard mid-enterprise stack above) + OT-specific:

OT Network:   Dragos Platform (OT asset inventory + threat detection)
              OR Claroty CDV (Continuous Threat Detection) + xDome
              OR Fortinet (FortiGate + FortiNAC for OT) — if integrated IT/OT preferred
OT Endpoint:  Claroty or Dragos (passive; no agent on PLC/SCADA)
OT Firewall:  Fortinet (IEC 62443 certified) or Palo Alto (PA-400 series)
Purdue Model: Enforce network segmentation (DMZ between IT L3 and OT L2)
SIEM:         Dragos/Claroty alerts → main SIEM (Sentinel or Splunk)
              OT-specific use cases ingested alongside IT alerts
```

**Key standard:** IEC 62443-3-3 (51 Security Requirements) → [mapped to NIST CSF](cross-references/iec62443-nist-mapping.md)

---

## Vendor Selection Decision Trees

### Which SIEM/SOC Platform?

```
Are you primarily Microsoft / Azure?
  YES → Microsoft Sentinel (E5 native; Copilot for Security)
  NO →
    Is EDR CrowdStrike?
      YES → CrowdStrike LogScale + Falcon XDR (single telemetry source)
      NO →
        Multi-cloud / MSSP / Compliance-heavy?
          YES → Google Chronicle (flat-cost; best at scale) or Splunk ES (Cisco)
          NO → SentinelOne AI-SIEM (if SentinelOne endpoint) or Cortex XSIAM (if PANW)
```

### Which Identity Platform?

```
< 500 users, primarily M365?
  → Microsoft Entra ID P2 (bundle wins on cost)

500-5,000 users, workforce identity priority?
  → Okta Workforce Identity + CyberArk for PAM (split best-of-breed)

5,000+ users, regulated (banking, healthcare, gov)?
  → SailPoint IGA + CyberArk PAM + Okta SSO (three-product identity stack)

DevOps secrets / cloud workload identity?
  → HashiCorp Vault (multi-cloud secrets) or CyberArk Conjur
  → Cloud-native: AWS IRSA / Azure WIF / GCP Workload Identity (no secrets needed)
```

### Which Cloud Security (CNAPP)?

```
Primary cloud is AWS?
  → Wiz (best multi-cloud coverage) OR CrowdStrike Falcon Cloud

Primary cloud is Azure?
  → Microsoft Defender for Cloud (E5 bundle) first; Wiz for depth

Primary cloud is GCP?
  → Wiz (→ Google; native GCP integration post-acquisition)

Multi-cloud, highly regulated?
  → Palo Alto Prisma Cloud (deepest compliance frameworks: PCI, HIPAA, GDPR)
```

### Which SSE/ZTNA?

```
Replacing VPN, cloud-first, cost-sensitive?
  → Cloudflare One (competitive pricing, 310+ PoPs, ZTNA + Gateway + CASB)

Large enterprise, ZTE (zero trust everywhere) commitment?
  → Zscaler ZTE (ZIA + ZPA + ZDX) — most complete platform

Palo Alto NGFW customer wanting consistent policy?
  → Palo Alto Prisma Access (same PAN-OS policy model in cloud)

Microsoft-first, E5?
  → Entra Internet Access + Entra Private Access (GA 2024; no extra license)
```

---

## Where Roadmaps Diverge (Buyer Beware)

### Gap 1: Govern / GRC — No Platform Vendor Has a Story

Zero of the 7 platform vendors have a compelling GRC/TPRM offering. This means:
- **ServiceNow IRM** remains the enterprise standard for risk management
- **Archer** (OpenPages) for financial services regulatory compliance
- **BitSight / SecurityScorecard** for vendor risk (TPRM)
- No "GRC-by-default" in any security platform bundle

**Implication:** Budget GRC separately; do not expect your CrowdStrike or Palo Alto rep to solve GRC.

### Gap 2: Backup / Recovery — Every Platform Has This Gap

None of the SOC/security platforms cover backup and recovery. The recovery market remains specialist:
- **Veeam** — enterprise backup + hardened repository (ransomware-resilient)
- **Rubrik** — SaaS-delivered backup + ransomware recovery guarantee
- **Cohesity** — data management + backup + cyber vault
- **Commvault** — multi-cloud backup + compliance archiving

**Implication:** Recovery is a board-level requirement (NIST Recover function); it requires dedicated budget, not a checkbox in a security platform.

### Gap 3: Email Security Depth (Behavioral BEC Detection)

Microsoft Defender for Office 365 P2 covers most threats. But for:
- **Account compromise (BEC)** — Proofpoint TAP behavioral analysis remains best-in-class
- **Compliance archiving + eDiscovery** — Proofpoint Archive or Mimecast Archive for non-M365 archiving requirements
- **Post-delivery TRAP** — Proofpoint TRAP for retraction of malicious emails post-delivery

**Implication:** M365-native shops on E5 should start with Defender for O365; add Proofpoint only if BEC detection gaps are validated in a POC.

### Gap 4: PAM Depth in Platform Bundles

Both Microsoft Entra PIM and Okta PAM (new 2024) provide cloud PAM features. Neither approaches CyberArk depth for:
- Just-in-time access to on-prem servers
- Session recording and video vault
- Secrets rotation for non-human identities (database passwords, API keys, SSH keys)
- Privileged cloud workload credentials (Conjur / Dynamic Secrets)

**Implication:** Organizations with PCI, SOX, or HIPAA compliance requirements need CyberArk or BeyondTrust; bundle PAM is insufficient.

---

## 3-Year Security Architecture Roadmap Template

### Year 1: Foundation
1. **Consolidate Identity** — Single IdP (Okta or Entra), MFA everywhere, JIT for admins (PAM)
2. **Replace VPN** — Deploy ZTNA (Zscaler ZPA or Cloudflare Access)
3. **Endpoint coverage** — EDR on all managed endpoints; block unmanaged access
4. **SIEM baseline** — Central log collection; NIST Detect function minimum coverage

### Year 2: Depth
5. **CNAPP deployment** — Cloud security posture; remediate top misconfigurations
6. **IGA rollout** — Access certification; birthright provisioning; lifecycle management
7. **DSPM activation** — Discover and classify sensitive data in cloud environments
8. **SOC maturity** — SOAR playbooks for top 5 incident types; MTTD/MTTR metrics established

### Year 3: Advanced
9. **AI SOC** — UEBA, anomaly detection, AI-assisted triage (Copilot for Security / Charlotte AI / Gemini)
10. **Zero Trust Data** — DLP inline + endpoint; IRM for sensitive documents; DAM for regulated databases
11. **Purple Team program** — ATT&CK Navigator + CALDERA emulation; D3FEND gap analysis
12. **Continuous Exposure Management (CTEM)** — EASM + CAASM + VM unified under exposure score

---

## References

- CONSOLIDATION.md — Industry consolidation analysis and M&A tracker
- architectures/zero-trust-blueprint.md — ZTA component-level blueprint
- architectures/cloud-native-patterns.md — Cloud security patterns
- TECH-STACK.md — Master technology category × vendor matrix
- frameworks/mitre/README.md — MITRE framework family and how to use them
- CATEGORY-ANALYSIS.md — Per-category spend, maturity, and vendor analysis
