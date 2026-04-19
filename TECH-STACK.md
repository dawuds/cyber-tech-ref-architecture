# Cybersecurity Technology Stack Reference

Master mapping of security technology categories, vendor products, and reference architectures — all organized against NIST CSF 2.0 as the canonical spine.

## At a Glance
- **36 technology categories** mapped across 6 NIST CSF 2.0 functions — the stable layer beneath shifting vendor products
- **9-vendor platform coverage matrix** shows Microsoft + Palo Alto + CrowdStrike have the widest individual coverage but each leaves critical gaps (GRC, Backup/Recovery, deep PAM)
- **5 categories face high displacement risk** from platform bundles: UEBA, standalone CASB, standalone SOAR, basic container security, basic EASM
- **Emerging categories** (AI/LLM security, supply chain security, DSPM) are the fastest-growing but have the most fragmented, immature vendor landscape
- **Direction →** Over the next 3 years the effective category count will compress from ~36 to ~25–28 as platform absorption continues; the stable categories are those requiring deep specialist capability or regulatory depth — PAM, GRC, email security archiving, and backup/recovery

## Navigation

| Section | Contents |
|---------|----------|
| [NIST Function → Category Map](#nist-csf-20-function--category-map) | All 36 categories by function |
| [Vendor Platform Coverage Matrix](#vendor-platform-coverage-matrix) | Which platform vendors cover which categories |
| [Attack Surface Management](#attack-surface-management-vendor-landscape) | ASM vendor landscape (dedicated) |
| [Reference Architectures](#vendor-reference-architectures) | All 10 vendor reference frameworks |
| [Specialist Leaders](#specialist-leaders-by-category) | Best-of-breed for non-platform categories |
| [Emerging Categories](#emerging-categories) | AI/LLM security, supply chain |
| [M&A Tracker](#ma-tracker-2022-2025) | Recent acquisitions affecting the landscape |

---

## NIST CSF 2.0 Function → Category Map

| Function | Category | ID | Detail |
|----------|----------|----|--------|
| **Govern** | GRC | grc | [→](technologies/categories/govern/grc.yaml) |
| **Govern** | Third-Party Risk Management | tprm | [→](technologies/categories/govern/tprm.yaml) |
| **Govern** | Security Awareness Training | security-awareness | [→](technologies/categories/govern/security-awareness.yaml) |
| **Govern** | Policy & Compliance Management | policy-management | [→](technologies/categories/govern/policy-management.yaml) |
| **Govern** | Supply Chain Security *(emerging)* | supply-chain-security | [→](technologies/categories/emerging/supply-chain-security.yaml) |
| **Identify** | Asset Management | asset-management | [→](technologies/categories/identify/asset-management.yaml) |
| **Identify** | Vulnerability Management | vulnerability-management | [→](technologies/categories/identify/vulnerability-management.yaml) |
| **Identify** | Attack Surface Management | attack-surface-management | [→](technologies/categories/identify/attack-surface-management.yaml) |
| **Identify** | Threat Intelligence | threat-intelligence | [→](technologies/categories/identify/threat-intelligence.yaml) |
| **Identify** | Identity Governance (IGA) | identity-governance | [→](technologies/categories/identify/identity-governance.yaml) |
| **Identify** | Cloud Infrastructure Entitlement Mgmt (CIEM) | ciem | [→](technologies/categories/identify/ciem.yaml) |
| **Protect** | IAM / SSO / MFA | iam-sso-mfa | [→](technologies/categories/protect/iam-sso-mfa.yaml) |
| **Protect** | Privileged Access Management (PAM) | pam | [→](technologies/categories/protect/pam.yaml) |
| **Protect** | Secrets Management | secrets-management | [→](technologies/categories/protect/secrets-management.yaml) |
| **Protect** | NGFW / IPS | ngfw-ips | [→](technologies/categories/protect/ngfw-ips.yaml) |
| **Protect** | ZTNA / SSE / SASE | ztna-sse-sase | [→](technologies/categories/protect/ztna-sse-sase.yaml) |
| **Protect** | CASB | casb | [→](technologies/categories/protect/casb.yaml) |
| **Protect** | Data Loss Prevention (DLP) | dlp | [→](technologies/categories/protect/dlp.yaml) |
| **Protect** | Email Security | email-security | [→](technologies/categories/protect/email-security.yaml) |
| **Protect** | Endpoint Protection (EPP / NGAV) | endpoint-protection | [→](technologies/categories/protect/endpoint-protection.yaml) |
| **Protect** | Application Security (SAST/DAST/SCA) | application-security | [→](technologies/categories/protect/application-security.yaml) |
| **Protect** | WAF / API Security | waf-api-security | [→](technologies/categories/protect/waf-api-security.yaml) |
| **Protect** | CNAPP / CSPM / CWPP | cnapp | [→](technologies/categories/protect/cnapp.yaml) |
| **Protect** | MDM / UEM | mdm-emm | [→](technologies/categories/protect/mdm-emm.yaml) |
| **Protect** | OT / ICS / IoT Security | ot-ics-iot | [→](technologies/categories/protect/ot-ics-iot.yaml) |
| **Protect** | AI / LLM Security *(emerging)* | ai-llm-security | [→](technologies/categories/emerging/ai-llm-security.yaml) |
| **Detect** | SIEM | siem | [→](technologies/categories/detect/siem.yaml) |
| **Detect** | XDR / EDR | xdr-edr | [→](technologies/categories/detect/xdr-edr.yaml) |
| **Detect** | Network Detection & Response (NDR) | ndr | [→](technologies/categories/detect/ndr.yaml) |
| **Detect** | UEBA | ueba | [→](technologies/categories/detect/ueba.yaml) |
| **Detect** | Deception Technology | deception | [→](technologies/categories/detect/deception.yaml) |
| **Respond** | SOAR | soar | [→](technologies/categories/respond/soar.yaml) |
| **Respond** | IR Case Management | case-management | [→](technologies/categories/respond/case-management.yaml) |
| **Respond** | Digital Forensics & IR (DFIR) | dfir | [→](technologies/categories/respond/dfir.yaml) |
| **Recover** | Backup & Recovery | backup-recovery | [→](technologies/categories/recover/backup-recovery.yaml) |
| **Recover** | BCP / Disaster Recovery | bcp-dr | [→](technologies/categories/recover/bcp-dr.yaml) |

---

## Vendor Platform Coverage Matrix

Platform vendors covering multiple NIST functions. Cells show the specific product (abbreviated).  
`—` = not covered natively. Specialist leaders listed separately below.

| Category | Microsoft | CrowdStrike | Palo Alto | Google | Zscaler | Cisco | SentinelOne | Fortinet | AWS |
|----------|-----------|-------------|-----------|--------|---------|-------|-------------|----------|-----|
| **GOVERN** | | | | | | | | | |
| GRC | Purview Compliance Mgr | — | — | — | — | — | — | — | — |
| TPRM | — | — | — | — | — | — | — | — | — |
| Security Awareness | Defender Attack Sim | — | — | — | — | — | — | — | — |
| Policy Management | Purview Compliance Mgr | — | — | — | — | — | — | — | — |
| Supply Chain Security | GitHub Adv Security | — | Prisma Cloud (code) | — | — | — | — | — | CodeArtifact |
| **IDENTIFY** | | | | | | | | | |
| Asset Management | Defender for Endpoint | Falcon Discover | — | — | ZDX (partial) | — | Singularity Ranger | FortiEMS | AWS Config |
| Vulnerability Management | Defender VM | Falcon Spotlight | Prisma Cloud (VM) | SCC (GCP) | — | — | — | FortiGuard PSIRT | AWS Inspector |
| Attack Surface Management | **Defender EASM** | **Falcon Surface** | **Cortex Xpanse** | **Mandiant ASM** | — | — | — | FortiRecon | — |
| Threat Intelligence | Defender TI | Falcon Intelligence | Unit 42 TI | Mandiant TI | — | Talos | — | FortiGuard TI | GuardDuty (partial) |
| Identity Governance (IGA) | Entra ID Governance | — | — | — | — | — | — | — | IAM Identity Center |
| CIEM | Entra Permissions Mgmt | Falcon CIEM | Prisma Cloud CIEM | — | — | — | — | — | IAM Access Analyzer |
| **PROTECT** | | | | | | | | | |
| IAM / SSO / MFA | Entra ID | Falcon Identity Protect | — | Cloud Identity | — | Duo | — | FortiAuthenticator | AWS IAM + SSO |
| PAM | Entra PIM | Falcon Privileged Access | — | — | — | — | — | FortiPAM | — |
| Secrets Management | Azure Key Vault | — | — | Cloud Secret Manager | — | — | — | — | Secrets Manager + KMS |
| NGFW / IPS | Azure Firewall | — | PA NGFW | Cloud IDS | — | Secure Firewall | — | FortiGate | Network Firewall |
| ZTNA / SSE / SASE | Global Secure Access | — | Prisma Access | BeyondCorp Enterprise | ZIA + ZPA | Cisco+ Secure Connect | — | FortiSASE | — |
| CASB | Defender for Cloud Apps | — | Prisma Access (CASB) | — | ZIA CASB | Umbrella CASB | — | — | — |
| DLP | Purview DLP | — | Enterprise DLP | Cloud DLP | ZIA DLP | — | — | FortiDLP | Macie |
| Email Security | Defender for O365 | — | — | Google Workspace | — | Secure Email Gateway | — | FortiMail | — |
| Endpoint Protection (EPP) | Defender Antivirus | Falcon Prevent | Cortex XDR (NGAV) | — | — | — | Singularity Core | FortiClient | — |
| Application Security | GitHub Adv Security | — | Prisma Cloud Code | — | — | — | — | — | Amazon Inspector |
| WAF / API Security | Azure WAF | — | Prisma Cloud WAAS | Cloud Armor | — | — | — | FortiWeb | AWS WAF |
| CNAPP | Defender for Cloud | Falcon Cloud Security | Prisma Cloud | Security Command Center | Posture Control | Panoptica | — | Fortinet Lacework | Security Hub |
| MDM / UEM | Microsoft Intune | — | — | Google Endpoint Mgmt | — | — | — | — | — |
| OT / ICS / IoT | Defender for IoT | — | Industrial OT Security | — | — | Cisco Cyber Vision | — | FortiNAC + FortiOT | — |
| **DETECT** | | | | | | | | | |
| SIEM | Microsoft Sentinel | Falcon LogScale | — *(QRadar SaaS acq.)* | Chronicle SIEM | — | Cisco XDR (partial) | — | FortiSIEM | Security Hub (partial) |
| XDR / EDR | Defender XDR | Falcon Insight XDR | Cortex XDR | Chronicle + Mandiant | — | Cisco XDR | Singularity XDR | FortiEDR | — |
| NDR | — | — | Cortex NDR | — | — | Secure Network Analytics | — | FortiNDR | GuardDuty (VPC Flow) |
| UEBA | Sentinel UEBA | — | — | Chronicle ML detection | — | — | — | FortiInsight | — |
| Deception | — | — | — | — | Zscaler Deception | — | Ranger Deception | FortiDeceptor | — |
| **RESPOND** | | | | | | | | | |
| SOAR | Sentinel SOAR | Falcon Fusion SOAR | Cortex XSOAR | Chronicle SOAR | — | XDR automation | — | FortiSOAR | EventBridge + Step Functions |
| IR Case Management | Sentinel (partial) | — | Cortex XSOAR | — | — | — | — | FortiSOAR (partial) | — |
| DFIR | — | Falcon Complete / OverWatch | Unit 42 (services) | Mandiant (services) | — | — | — | — | — |
| **RECOVER** | | | | | | | | | |
| Backup & Recovery | Azure Backup | — | — | Cloud Backup & DR | — | — | — | — | AWS Backup |
| BCP / DR | — | — | — | — | — | — | — | — | — |

> **Coverage gaps visible across all vendors:** Govern (GRC, TPRM) and Recover (BCP/DR) are structurally underserved by security platform vendors — these require dedicated specialist products.

---

## Attack Surface Management Vendor Landscape

ASM discovers and monitors internet-facing assets from an attacker's perspective. No vendor publishes a dedicated ASM reference architecture — these are product capabilities within broader platforms.

### Integrated Platform ASM (bundled with XDR/CNAPP/TI)

| Vendor | Product | Integration Point | Differentiator |
|--------|---------|-------------------|----------------|
| Palo Alto Networks | **Cortex Xpanse** | Cortex platform | Real-time discovery; largest internet scan dataset; most mature ASM |
| Microsoft | **Defender EASM** | Defender / Azure | Azure-native; tight Sentinel integration; based on RiskIQ acquisition |
| CrowdStrike | **Falcon Surface** | Cortex (via Reposify) | Integrated with Falcon Discover for combined internal + external inventory |
| Google / Mandiant | **Mandiant ASM** | Chronicle + Mandiant TI | Mandiant intelligence-enriched; attacker-perspective prioritization |
| Fortinet | **FortiRecon** | Security Fabric | Dark web monitoring + external attack surface combined |

### Specialist / Pure-Play ASM

| Vendor | Product | Differentiator |
|--------|---------|----------------|
| Censys | Censys ASM | Largest internet scan database; research-grade; government/federal strong |
| Cycognito | Cycognito | Subsidiary and supply chain asset discovery |
| IBM / Randori | Randori (acquired 2022) | Attacker-perspective continuous red team validation |
| Tenable | Tenable ASM | Integrated with Tenable One VM platform |
| NetSPI | NetSPI ASM | Human-validated findings from penetration testing firm |
| Searchlight Cyber | Searchlight | Dark web + external threat monitoring combined |

### ASM vs. EASM vs. CAASM

| Term | Focus | Primary Tools |
|------|-------|---------------|
| EASM (External ASM) | Internet-facing assets from outside the perimeter | Xpanse, Defender EASM, Censys |
| CAASM (Cyber Asset ASM) | Internal + external asset inventory consolidation | Axonius, JupiterOne, Noetic |
| DRPS (Digital Risk Protection) | Brand, domain, dark web impersonation monitoring | Recorded Future, CrowdStrike Recon |

---

## Vendor Reference Architectures

All 10 reference architectures mapped to NIST CSF functions.

| Architecture | Vendor | Version | Primary Focus | NIST Coverage | Detail |
|-------------|--------|---------|---------------|---------------|--------|
| [Microsoft MCRA](architectures/microsoft-mcra.md) | Microsoft | Apr 2025 | End-to-end enterprise | Protect, Detect, Respond strong; Govern partial | [YAML](frameworks/vendor-architectures/microsoft-mcra.yaml) |
| [Palo Alto Zero Trust Architecture](architectures/palo-alto-zta.md) | Palo Alto Networks | 2024 | Zero Trust + NGFW + cloud | Protect, Detect strong; Identify (Xpanse) | [YAML](frameworks/vendor-architectures/palo-alto-zta.yaml) |
| [Zscaler Zero Trust Exchange](architectures/zscaler-zte.md) | Zscaler | 2024 | SSE / SASE / ZTNA | Protect strong; Detect partial | [YAML](frameworks/vendor-architectures/zscaler-zte.yaml) |
| [Google Cloud Security Architecture](architectures/google-csa.md) | Google / Mandiant | 2025 | Cloud + SOC | Detect, Identify, Protect strong | [YAML](frameworks/vendor-architectures/google-csa.yaml) |
| [CrowdStrike Falcon Platform](architectures/crowdstrike-falcon.md) | CrowdStrike | 2025 | Endpoint-first XDR | Identify, Protect, Detect, Respond strong | [YAML](frameworks/vendor-architectures/crowdstrike-falcon.yaml) |
| [CISA Zero Trust Maturity Model v2](architectures/cisa-ztmm.md) | CISA | Apr 2023 | Federal Zero Trust maturity | All functions; Govern explicit | [YAML](frameworks/vendor-architectures/cisa-ztmm.yaml) |
| [AWS Security Reference Architecture](architectures/aws-sra.md) | AWS | 2025 | Cloud-native AWS | Identify, Protect, Detect strong; limited Recover | [YAML](frameworks/vendor-architectures/aws-sra.yaml) |
| [Cisco Security Reference Architecture](architectures/cisco-security.md) | Cisco | 2024 | Network-centric + SASE | Protect, Detect strong; Hypershield emerging | [YAML](frameworks/vendor-architectures/cisco-security.yaml) |
| [Fortinet Security Fabric](architectures/fortinet-security-fabric.md) | Fortinet | 2024 | Integrated network security | Protect, Detect, Respond; OT strong | [YAML](frameworks/vendor-architectures/fortinet-security-fabric.yaml) |
| [Check Point Infinity Architecture](architectures/checkpoint-infinity.md) | Check Point | 2024 | Unified threat prevention | Protect, Detect; AI factory security (2026) | [YAML](frameworks/vendor-architectures/checkpoint-infinity.yaml) |

### NIST Function Coverage by Reference Architecture

| Function | MS MCRA | PA ZTA | Zscaler ZTE | Google CSA | CS Falcon | CISA ZTMM | AWS SRA | Cisco | Fortinet | Check Point |
|----------|---------|--------|-------------|------------|-----------|-----------|---------|-------|----------|-------------|
| **Govern** | Partial | Weak | None | None | None | **Strong** | None | None | None | None |
| **Identify** | Strong | Partial | Partial | **Strong** | **Strong** | Strong | Strong | Weak | Partial | Weak |
| **Protect** | **Strong** | **Strong** | **Strong** | Strong | Strong | Strong | Strong | **Strong** | **Strong** | **Strong** |
| **Detect** | **Strong** | Strong | Partial | **Strong** | **Strong** | Strong | Strong | Strong | Strong | Strong |
| **Respond** | Strong | Strong | Weak | **Strong** | **Strong** | Partial | Partial | Partial | Strong | Partial |
| **Recover** | Weak | None | None | Weak | None | None | Partial | None | None | None |

---

## Specialist Leaders by Category

For categories where platform vendors are secondary and specialist vendors lead:

| Category | Market Leaders | Notes |
|----------|----------------|-------|
| GRC | Archer (RSA), ServiceNow GRC, MetricStream, OneTrust | Platform vendors don't compete here |
| TPRM | BitSight, SecurityScorecard, Prevalent, ProcessUnity | Standalone market |
| Security Awareness | KnowBe4, Proofpoint SAT, SANS, Cofense | Standalone market |
| IAM / SSO / MFA | Okta, Microsoft Entra, Ping Identity, Cisco Duo | Okta leads independent; Microsoft in M365 orgs |
| PAM | CyberArk, BeyondTrust, Delinea | Standalone dominant |
| Secrets Management | HashiCorp Vault, AWS Secrets Manager, Azure Key Vault | Platform + HashiCorp |
| CNAPP | Wiz, Palo Alto Prisma Cloud, MS Defender for Cloud | Wiz is market share leader |
| SIEM | Microsoft Sentinel, Google Chronicle, Splunk ES | Top 3 by MQ 2025 |
| Email Security | Proofpoint, Mimecast, Abnormal Security | Outside of built-in M365/Google |
| NDR | ExtraHop, Darktrace, Vectra AI, Corelight | Specialists dominate |
| Deception | SentinelOne (Attivo), Thinkst Canary, Acalvio | Niche but growing |
| DFIR | Mandiant (Google), CrowdStrike Services, Magnet Forensics | Services-heavy |
| Backup & Recovery | Veeam, Rubrik, Cohesity, Commvault | Platform vendors play minimally |
| OT / ICS Security | Claroty, Dragos, Nozomi Networks | Specialist-only |
| Vulnerability Management | Tenable, Qualys, Rapid7 | Specialists; platforms adding VM modules |

---

## Emerging Categories

| Category | NIST Primary | Status | Key Vendors |
|----------|-------------|--------|-------------|
| [AI / LLM Security](technologies/categories/emerging/ai-llm-security.yaml) | Protect | Rapidly emerging 2024-2025 | Azure AI Content Safety, Google Model Armor, Guardrails AI (OSS), Lakera, HiddenLayer |
| [Supply Chain Security / SBOM](technologies/categories/emerging/supply-chain-security.yaml) | Govern | Maturing post-EO 14028 | Snyk, Black Duck, Chainguard, Socket, Sigstore (OSS) |

**Not a product category (methodology only):**
- **CTEM** (Continuous Threat Exposure Management) — Gartner framework, not a product. Implemented using VM + ASM + risk platforms.

---

## Vendor Profiles

Detailed per-vendor product portfolios mapped to NIST functions:

| Vendor | Profile | Architecture |
|--------|---------|-------------|
| Microsoft | [technologies/vendors/microsoft.md](technologies/vendors/microsoft.md) | [MCRA](architectures/microsoft-mcra.md) |
| CrowdStrike | [technologies/vendors/crowdstrike.md](technologies/vendors/crowdstrike.md) | [Falcon Platform](architectures/crowdstrike-falcon.md) |
| Palo Alto Networks | [technologies/vendors/palo-alto.md](technologies/vendors/palo-alto.md) | [Zero Trust Architecture](architectures/palo-alto-zta.md) |
| Google / Mandiant | [technologies/vendors/google.md](technologies/vendors/google.md) | [Cloud Security Architecture](architectures/google-csa.md) |
| Zscaler | [technologies/vendors/zscaler.md](technologies/vendors/zscaler.md) | [Zero Trust Exchange](architectures/zscaler-zte.md) |
| Cisco | [technologies/vendors/cisco.md](technologies/vendors/cisco.md) | [Security Reference Architecture](architectures/cisco-security.md) |
| SentinelOne | [technologies/vendors/sentinelone.md](technologies/vendors/sentinelone.md) | Singularity Platform |
| Fortinet | [technologies/vendors/fortinet.md](technologies/vendors/fortinet.md) | [Security Fabric](architectures/fortinet-security-fabric.md) |
| AWS | [technologies/vendors/aws.md](technologies/vendors/aws.md) | [Security Reference Architecture](architectures/aws-sra.md) |
| Check Point | [technologies/vendors/check-point.md](technologies/vendors/check-point.md) | [Infinity Architecture](architectures/checkpoint-infinity.md) |
| Okta | [technologies/vendors/okta.md](technologies/vendors/okta.md) | IAM specialist |
| CyberArk | [technologies/vendors/cyberark.md](technologies/vendors/cyberark.md) | PAM specialist |
| Wiz | [technologies/vendors/wiz.md](technologies/vendors/wiz.md) | CNAPP specialist |
| Splunk | [technologies/vendors/splunk.md](technologies/vendors/splunk.md) | SIEM/SOAR specialist |
| Proofpoint | [technologies/vendors/proofpoint.md](technologies/vendors/proofpoint.md) | Email / human risk specialist |
| Cloudflare | [technologies/vendors/cloudflare.md](technologies/vendors/cloudflare.md) | Network / WAF / SSE |
| Tenable | [technologies/vendors/tenable.md](technologies/vendors/tenable.md) | Exposure management specialist |

---

## M&A Tracker (2022–2025)

| Year | Acquirer | Target | Category Impact |
|------|----------|--------|-----------------|
| 2025 | Google (pending) | Wiz ($32B) | CNAPP — Wiz joins Google Security portfolio |
| 2024 | Cisco | Splunk ($28B) | SIEM/SOAR — Splunk now part of Cisco Security |
| 2024 | Palo Alto Networks | IBM QRadar SaaS | SIEM — QRadar SaaS absorbed into Cortex; on-prem stays IBM |
| 2024 | Fortinet | Lacework | CNAPP — Lacework CNAPP now Fortinet Lacework |
| 2024 | Exabeam + LogRhythm | Merger | SIEM/UEBA — LogRhythm brand retired; Exabeam leads |
| 2024 | Mastercard | Recorded Future | TI — Recorded Future acquired for $2.65B |
| 2024 | Akamai | Noname Security | WAF/API Security — Noname API security joins Akamai |
| 2024 | Armis | Honeywell Forge Cybersecurity | OT/IoT — Expands Armis industrial coverage |
| 2024 | Broadcom (VMware) | divested EUC → Omnissa | MDM — Workspace ONE now under Omnissa brand |
| 2023 | Tenable | Ermetic ($265M) | CIEM — Now Tenable Cloud Security |
| 2023 | Ping Identity | Thales | IAM — Ping Identity acquired by Thales |
| 2023 | Ping Identity | ForgeRock | IAM — ForgeRock merged into Ping Identity |
| 2022 | SentinelOne | Attivo Networks ($616M) | Deception/ITDR — Now Singularity Ranger Deception |
| 2022 | Google | Mandiant ($5.4B) | TI/DFIR — Mandiant becomes Google Cloud arm |
| 2022 | Google | Siemplify | SOAR — Now Chronicle SOAR |
| 2021 | Microsoft | RiskIQ | ASM — Now Defender EASM + Defender TI |
| 2021 | Palo Alto Networks | Expanse | ASM — Now Cortex Xpanse |
