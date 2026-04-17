# GRC Portfolio → Cybersecurity Technology Cross-Reference

**Source:** [GRC repository](https://github.com/dawuds/grc) — portfolio of 8 compliance/security framework repositories  
**Purpose:** Maps GRC/compliance framework requirements from the portfolio to cybersecurity technology categories in this reference architecture

---

## GRC Repository Portfolio

| Repository | Framework | Technology Relevance |
|-----------|-----------|---------------------|
| [nist](https://github.com/dawuds/nist) | NIST CSF 2.0 | Primary organizing framework for this architecture |
| [OT-Security](https://github.com/dawuds/OT-Security) | IEC 62443 + NACSA OT | OT/ICS security technology mapping → [iec62443-nist-mapping.md](iec62443-nist-mapping.md) |
| [AI-Governance](https://github.com/dawuds/AI-Governance) | 11 AI Governance Frameworks | AI security technology mapping → [ai-governance-security-mapping.md](ai-governance-security-mapping.md) |
| [cloud-sec](https://github.com/dawuds/cloud-sec) | CSA CCM v4 | Cloud security controls → CNAPP, CSPM, CASB technology mapping |
| [RMIT](https://github.com/dawuds/RMIT) | BNM RMIT (Malaysia) | Financial services security technology requirements |
| [nacsa](https://github.com/dawuds/nacsa) | NACSA Act 854 | Malaysia national cybersecurity — critical infrastructure |
| [pdpa-my](https://github.com/dawuds/pdpa-my) | Malaysia PDPA 2010 | Data protection technology requirements |
| [MCP-Security](https://github.com/dawuds/MCP-Security) | Model Context Protocol Security | Emerging AI agent security |

---

## CSA Cloud Controls Matrix (CCM v4) → Technology Mapping

CSA CCM v4 defines cloud security controls across 17 domains. Mapping to technology categories:

| CCM Domain | NIST CSF Function | Technology Categories |
|-----------|------------------|----------------------|
| **AIS** — Application & Interface Security | Protect | [Application Security](../technologies/categories/protect/application-security.yaml), [WAF/API Security](../technologies/categories/protect/waf-api-security.yaml) |
| **BCR** — Business Continuity Management | Recover | [BCP/DR](../technologies/categories/recover/bcp-dr.yaml) |
| **CCC** — Change Control & Configuration | Protect | [GRC](../technologies/categories/govern/grc.yaml), [Vulnerability Management](../technologies/categories/identify/vulnerability-management.yaml) |
| **CEK** — Cryptography, Encryption & Key Mgmt | Protect | Encryption (within CNAPP/cloud controls), [Secrets Management](../technologies/categories/protect/secrets-management.yaml) |
| **DCS** — Datacenter Security | Protect | Physical security (outside technology categories) |
| **DSP** — Data Security & Privacy Lifecycle Mgmt | Protect | [DLP](../technologies/categories/protect/dlp.yaml), [CNAPP/DSPM](../technologies/categories/protect/cnapp.yaml) |
| **GRC** — Governance, Risk & Compliance | Govern | [GRC](../technologies/categories/govern/grc.yaml), [Policy Management](../technologies/categories/govern/policy-management.yaml) |
| **HRS** — Human Resources Security | Govern | [Security Awareness](../technologies/categories/govern/security-awareness.yaml), [IGA](../technologies/categories/identify/identity-governance.yaml) |
| **IAM** — Identity & Access Management | Protect | [IAM/SSO/MFA](../technologies/categories/protect/iam-sso-mfa.yaml), [PAM](../technologies/categories/protect/pam.yaml), [CIEM](../technologies/categories/identify/ciem.yaml) |
| **IPY** — Interoperability & Portability | Identify | [Asset Management](../technologies/categories/identify/asset-management.yaml) |
| **IVS** — Infrastructure & Virtualization Security | Protect | [CNAPP](../technologies/categories/protect/cnapp.yaml), [NGFW/IPS](../technologies/categories/protect/ngfw-ips.yaml) |
| **LOG** — Logging & Monitoring | Detect | [SIEM](../technologies/categories/detect/siem.yaml), [XDR/EDR](../technologies/categories/detect/xdr-edr.yaml) |
| **SEF** — Security Incident Management | Respond | [SOAR](../technologies/categories/respond/soar.yaml), [IR Case Management](../technologies/categories/respond/case-management.yaml) |
| **STA** — Supply Chain Management & Transparency | Identify | [TPRM](../technologies/categories/govern/tprm.yaml), [Supply Chain Security](../technologies/categories/emerging/supply-chain-security.yaml) |
| **TVM** — Threat & Vulnerability Management | Identify | [Vulnerability Management](../technologies/categories/identify/vulnerability-management.yaml), [Threat Intelligence](../technologies/categories/identify/threat-intelligence.yaml) |
| **UEM** — Universal Endpoint Management | Protect | [MDM/EMM](../technologies/categories/protect/mdm-emm.yaml), [Endpoint Protection](../technologies/categories/protect/endpoint-protection.yaml) |

---

## BNM RMIT (Risk Management in Technology) → Technology Mapping

Bank Negara Malaysia's RMIT standard applies to licensed financial institutions in Malaysia. Key RMIT requirements map to security technologies:

| RMIT Requirement Area | Technology Category | Notes |
|----------------------|-------------------|-------|
| Technology Risk Management | [GRC](../technologies/categories/govern/grc.yaml) | Risk register, technology risk assessment |
| Cyber Risk Management | [GRC](../technologies/categories/govern/grc.yaml), [TPRM](../technologies/categories/govern/tprm.yaml) | Third-party cyber risk |
| Identity and Access Management | [IAM/SSO/MFA](../technologies/categories/protect/iam-sso-mfa.yaml), [PAM](../technologies/categories/protect/pam.yaml) | Privileged access controls |
| Patch Management | [Vulnerability Management](../technologies/categories/identify/vulnerability-management.yaml) | Mandatory patch SLAs |
| Incident Management | [SOAR](../technologies/categories/respond/soar.yaml), [IR Case Management](../technologies/categories/respond/case-management.yaml) | Mandatory incident reporting within 4h to BNM |
| Business Continuity / DR | [BCP/DR](../technologies/categories/recover/bcp-dr.yaml) | RTO/RPO requirements |
| Data Loss Prevention | [DLP](../technologies/categories/protect/dlp.yaml) | Customer data protection |
| Audit Logging | [SIEM](../technologies/categories/detect/siem.yaml) | Audit trail retention (minimum 7 years) |
| Vulnerability Assessment | [Vulnerability Management](../technologies/categories/identify/vulnerability-management.yaml), [Application Security](../technologies/categories/protect/application-security.yaml) | Annual VAPT mandatory |
| Outsourcing / Cloud | [TPRM](../technologies/categories/govern/tprm.yaml), [CNAPP](../technologies/categories/protect/cnapp.yaml) | Cloud service provider oversight |

---

## Malaysia PDPA 2010 → Technology Mapping

Malaysia's Personal Data Protection Act 2010 creates technology requirements for data controllers:

| PDPA Principle | Technology Control | Category |
|---------------|-------------------|---------|
| General Principle (lawful processing) | Data classification, consent management | [DLP](../technologies/categories/protect/dlp.yaml) |
| Notice & Choice Principle | Data discovery, privacy inventory | [CNAPP/DSPM](../technologies/categories/protect/cnapp.yaml) |
| Disclosure Principle | CASB (prevent unauthorized disclosure) | [CASB](../technologies/categories/protect/casb.yaml) |
| Security Principle | Encryption at rest/in transit, access control | [IAM/SSO/MFA](../technologies/categories/protect/iam-sso-mfa.yaml), [DLP](../technologies/categories/protect/dlp.yaml) |
| Retention Principle | Data lifecycle management | [DLP](../technologies/categories/protect/dlp.yaml), [Backup & Recovery](../technologies/categories/recover/backup-recovery.yaml) |
| Data Integrity Principle | Data quality controls | [GRC](../technologies/categories/govern/grc.yaml) |
| Access Principle | Data subject access request management | [GRC](../technologies/categories/govern/grc.yaml), [IGA](../technologies/categories/identify/identity-governance.yaml) |

---

## NACSA Act 854 (Malaysia Cybersecurity Act 2024) → Technology Mapping

Malaysia's Cybersecurity Act 2024 (Act 854) covers National Critical Information Infrastructure (NCII) operators across 11 sectors:

| Sector | NCII Designation | Primary Technology Needs |
|--------|-----------------|-------------------------|
| Energy (power, water, gas) | Yes | [OT/ICS Security](../technologies/categories/protect/ot-ics-iot.yaml), [SIEM](../technologies/categories/detect/siem.yaml) |
| Transportation (aviation, ports, rail) | Yes | [OT/ICS Security](../technologies/categories/protect/ot-ics-iot.yaml), [NDR](../technologies/categories/detect/ndr.yaml) |
| Banking & Finance | Yes | [GRC](../technologies/categories/govern/grc.yaml), [SIEM](../technologies/categories/detect/siem.yaml), [SOAR](../technologies/categories/respond/soar.yaml) |
| Healthcare | Yes | [DLP](../technologies/categories/protect/dlp.yaml), [Endpoint Protection](../technologies/categories/protect/endpoint-protection.yaml) |
| Government | Yes | [GRC](../technologies/categories/govern/grc.yaml), [IAM/SSO/MFA](../technologies/categories/protect/iam-sso-mfa.yaml) |
| Digital Communications / Telco | Yes | [NDR](../technologies/categories/detect/ndr.yaml), [DDoS/NGFW](../technologies/categories/protect/ngfw-ips.yaml) |
| Defense | Yes | Full stack |
| Sewage & Wastewater | Yes | [OT/ICS Security](../technologies/categories/protect/ot-ics-iot.yaml) |
| Food & Agriculture | Yes | [OT/ICS Security](../technologies/categories/protect/ot-ics-iot.yaml) |
| National Emergency Services | Yes | [BCP/DR](../technologies/categories/recover/bcp-dr.yaml) |
| Science, Technology & Innovation | Yes | [Supply Chain Security](../technologies/categories/emerging/supply-chain-security.yaml) |

**Key NACSA obligations that require security technology:**
1. **Cybersecurity audit** (biennial for NCII operators) → [GRC](../technologies/categories/govern/grc.yaml), [Vulnerability Management](../technologies/categories/identify/vulnerability-management.yaml)
2. **Incident reporting** (within 6 hours for serious incidents) → [SOAR](../technologies/categories/respond/soar.yaml), [IR Case Management](../technologies/categories/respond/case-management.yaml)
3. **Risk assessment** → [GRC](../technologies/categories/govern/grc.yaml)
4. **Penetration testing** → [Application Security](../technologies/categories/protect/application-security.yaml), [Vulnerability Management](../technologies/categories/identify/vulnerability-management.yaml)

---

## Multi-Framework Technology Requirement Summary

Technology categories required across multiple GRC frameworks in this portfolio:

| Technology Category | NIST CSF | IEC 62443 | AI Act | RMIT | PDPA | NACSA |
|-------------------|----------|-----------|--------|------|------|-------|
| GRC Platform | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| IAM / SSO / MFA | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| PAM | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| SIEM | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| DLP | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| SOAR / Case Mgmt | ✓ | — | ✓ | ✓ | — | ✓ |
| Vulnerability Mgmt | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| Endpoint Protection | ✓ | — | — | ✓ | — | ✓ |
| CNAPP | ✓ | — | ✓ | ✓ | ✓ | — |
| Backup & Recovery | ✓ | ✓ | — | ✓ | ✓ | — |
| OT/ICS Security | ✓ | ✓ | — | — | — | ✓ |
| TPRM | ✓ | — | — | ✓ | — | — |
| AI/LLM Security | — | — | ✓ | — | — | — |

**Most universally required:** IAM, SIEM, GRC, Vulnerability Management, DLP — these five categories appear across all or nearly all frameworks.

---

## References

- GRC Hub: [github.com/dawuds/grc](https://github.com/dawuds/grc)
- OT-Security: [github.com/dawuds/OT-Security](https://github.com/dawuds/OT-Security)
- AI-Governance: [github.com/dawuds/AI-Governance](https://github.com/dawuds/AI-Governance)
- Cloud-Sec (CSA CCM): [github.com/dawuds/cloud-sec](https://github.com/dawuds/cloud-sec)
- BNM RMIT: https://www.bnm.gov.my/rmit
- NACSA Act 854: https://www.nacsa.gov.my
- Malaysia PDPA: https://www.pdp.gov.my
