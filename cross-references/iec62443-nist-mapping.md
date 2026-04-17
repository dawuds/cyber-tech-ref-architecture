# IEC 62443-3-3 → NIST CSF 2.0 Cross-Reference

**Source:** [OT-Security repository](https://github.com/dawuds/OT-Security) — `cross-references/iec62443-to-nist-csf.json`  
**Note:** Mapping constructed from analysis of IEC 62443 SR objectives and NIST CSF 2.0 subcategory descriptions. Not normatively specified by either standard body.

---

## Purpose

IEC 62443-3-3 defines Security Requirements (SRs) for Industrial Automation and Control Systems (IACS). This mapping shows how each SR aligns to NIST CSF 2.0 functions and subcategories, enabling:
- OT/ICS security programs to demonstrate NIST CSF compliance using IEC 62443 controls
- Technology selection for OT environments mapped to the same NIST taxonomy as IT security
- Security assessment gap analysis across IT and OT domains

---

## NIST CSF Function Coverage

| NIST Function | IEC 62443 SR Coverage | Count |
|--------------|----------------------|-------|
| **Govern (GV)** | SR-1.12 (System use notification → GV.PO-01) | 1 SR |
| **Identify (ID)** | SR-7.8 (Component inventory → ID.AM) | 1 SR |
| **Protect (PR)** | SR-1.x (IAM), SR-2.x (Access control + audit), SR-3.x (Integrity), SR-4.x (Confidentiality), SR-5.x (Segmentation), SR-7.1-7.7 (Availability) | 46 SRs |
| **Detect (DE)** | SR-2.8 (Auditable events), SR-3.2-3.4 (Integrity), SR-6.2 (Continuous monitoring), SR-7.1 (DoS) | 5 SRs |
| **Respond (RS)** | SR-6.1 (Audit log → RS.AN-03) | 1 SR |
| **Recover (RC)** | SR-7.3-7.4 (Backup and recovery → RC.RP) | 2 SRs |

**Key observation:** IEC 62443 is heavily Protect-weighted (85%+ of requirements map to NIST Protect). This reflects OT's safety-first design philosophy — availability and integrity protection are paramount.

---

## Full SR → NIST CSF Mapping Table

### Group 1: Identification and Authentication (SR-1.x)
*NIST Primary: Protect (PR.AA)*

| IEC 62443 SR | Requirement Name | NIST CSF Subcategories | Similarity |
|-------------|-----------------|----------------------|------------|
| SR-1.1 | Human user identification and authentication | PR.AA-01, PR.AA-02, PR.AA-05 | High |
| SR-1.2 | Software process and device identification and authentication | PR.AA-01, PR.AA-03 | High |
| SR-1.3 | Account management | PR.AA-05, PR.AA-06 | High |
| SR-1.4 | Identifier management | PR.AA-01 | Medium |
| SR-1.5 | Authenticator management | PR.AA-02, PR.AA-05 | High |
| SR-1.6 | Wireless access management | PR.AA-01, PR.IR-01 | High |
| SR-1.7 | Strength of password-based authentication | PR.AA-02 | High |
| SR-1.8 | Public key infrastructure certificates | PR.AA-03, PR.DS-02 | Medium |
| SR-1.9 | Strength of public key authentication | PR.DS-02 | Medium |
| SR-1.10 | Authenticator feedback | PR.AA-01 | Medium |
| SR-1.11 | Unsuccessful login attempts | PR.AA-02 | High |
| SR-1.12 | System use notification | GV.PO-01 | Low |
| SR-1.13 | Access via untrusted networks | PR.AA-01, PR.AA-05, PR.IR-01 | High |

**Technology categories:** [IAM/SSO/MFA](../technologies/categories/protect/iam-sso-mfa.yaml), [PAM](../technologies/categories/protect/pam.yaml), [OT/ICS](../technologies/categories/protect/ot-ics-iot.yaml)

### Group 2: Use Control (SR-2.x)
*NIST Primary: Protect (PR.AA, PR.PS) + Detect (DE.AE)*

| IEC 62443 SR | Requirement Name | NIST CSF Subcategories | Similarity |
|-------------|-----------------|----------------------|------------|
| SR-2.1 | Authorization enforcement | PR.AA-05, PR.AA-06 | High |
| SR-2.2 | Wireless use control | PR.AA-01, PR.IR-01 | High |
| SR-2.3 | Use of portable and mobile devices | PR.AA-05, PR.DS-01 | High |
| SR-2.4 | Mobile code | PR.PS-01, PR.PS-02 | High |
| SR-2.5 | Session lock | PR.AA-05 | Medium |
| SR-2.6 | Remote session termination | PR.AA-05 | Medium |
| SR-2.7 | Concurrent session control | PR.AA-05 | Medium |
| SR-2.8 | Auditable events | DE.AE-02, PR.PT-01 | High |
| SR-2.9 | Audit storage capacity | PR.PT-01 | High |
| SR-2.10 | Response to audit processing failures | DE.AE-02 | High |
| SR-2.11 | Timestamps | PR.PT-01 | Medium |
| SR-2.12 | Non-repudiation | PR.PT-01, DE.AE-02 | High |

**Technology categories:** [SIEM](../technologies/categories/detect/siem.yaml), [PAM](../technologies/categories/protect/pam.yaml)

### Group 3: System Integrity (SR-3.x)
*NIST Primary: Protect (PR.DS, PR.PS) + Detect (DE.CM)*

| IEC 62443 SR | Requirement Name | NIST CSF Subcategories | Similarity |
|-------------|-----------------|----------------------|------------|
| SR-3.1 | Communication integrity | PR.DS-02, PR.DS-10 | High |
| SR-3.2 | Malicious code protection | DE.CM-09, PR.PS-04 | High |
| SR-3.3 | Security functionality verification | PR.PS-04, DE.CM-03 | High |
| SR-3.4 | Software and information integrity | PR.DS-01, PR.DS-10, DE.CM-03 | High |
| SR-3.5 | Input validation | PR.PS-04 | High |
| SR-3.6 | Deterministic output | PR.PS-04 | Medium |
| SR-3.7 | Error handling | PR.PS-04 | Medium |
| SR-3.8 | Session integrity | PR.DS-02 | High |
| SR-3.9 | Protection of audit information | PR.DS-01, PR.PT-01 | High |

**Technology categories:** [Endpoint Protection](../technologies/categories/protect/endpoint-protection.yaml), [OT/ICS](../technologies/categories/protect/ot-ics-iot.yaml)

### Group 4: Data Confidentiality (SR-4.x)
*NIST Primary: Protect (PR.DS)*

| IEC 62443 SR | Requirement Name | NIST CSF Subcategories | Similarity |
|-------------|-----------------|----------------------|------------|
| SR-4.1 | Information confidentiality | PR.DS-01, PR.DS-02 | High |
| SR-4.2 | Information persistence | PR.DS-01 | High |
| SR-4.3 | Use of cryptography | PR.DS-02, PR.DS-10 | High |

**Technology categories:** [DLP](../technologies/categories/protect/dlp.yaml), Encryption (within CNAPP/Cloud controls)

### Group 5: Restricted Data Flow (SR-5.x)
*NIST Primary: Protect (PR.IR)*

| IEC 62443 SR | Requirement Name | NIST CSF Subcategories | Similarity |
|-------------|-----------------|----------------------|------------|
| SR-5.1 | Network segmentation | PR.IR-01, PR.IR-02 | High |
| SR-5.2 | Zone boundary protection | PR.IR-01 | High |
| SR-5.3 | General purpose person-to-person communication restrictions | PR.IR-01 | High |
| SR-5.4 | Application partitioning | PR.IR-01, PR.IR-02 | High |

**Technology categories:** [NGFW/IPS](../technologies/categories/protect/ngfw-ips.yaml), [OT/ICS](../technologies/categories/protect/ot-ics-iot.yaml)

### Group 6: Timely Response to Events (SR-6.x)
*NIST Primary: Detect (DE.AE, DE.CM) + Respond (RS.AN)*

| IEC 62443 SR | Requirement Name | NIST CSF Subcategories | Similarity |
|-------------|-----------------|----------------------|------------|
| SR-6.1 | Audit log accessibility | DE.AE-02, RS.AN-03 | High |
| SR-6.2 | Continuous monitoring | DE.AE-02, DE.AE-06, DE.CM-01, DE.CM-06, DE.CM-09 | High |

**Technology categories:** [SIEM](../technologies/categories/detect/siem.yaml), [NDR](../technologies/categories/detect/ndr.yaml)

### Group 7: Resource Availability (SR-7.x)
*NIST Primary: Protect (PR.IR) + Recover (RC.RP)*

| IEC 62443 SR | Requirement Name | NIST CSF Subcategories | Similarity |
|-------------|-----------------|----------------------|------------|
| SR-7.1 | Denial of service protection | PR.IR-04, DE.CM-01 | High |
| SR-7.2 | Resource management | PR.IR-04 | High |
| SR-7.3 | Control system backup | PR.DS-11, RC.RP-04 | High |
| SR-7.4 | Control system recovery and reconstitution | RC.RP-01, RC.RP-04, RC.RP-05 | High |
| SR-7.5 | Emergency power | PR.IR-04 | High |
| SR-7.6 | Network and security configuration settings | PR.PS-01, DE.CM-03 | High |
| SR-7.7 | Least functionality | PR.PS-01, PR.PS-03 | High |
| SR-7.8 | Control system component inventory | ID.AM-01, ID.AM-02, ID.AM-03 | High |

**Technology categories:** [Backup & Recovery](../technologies/categories/recover/backup-recovery.yaml), [BCP/DR](../technologies/categories/recover/bcp-dr.yaml), [Asset Management](../technologies/categories/identify/asset-management.yaml)

---

## OT Technology Categories → IEC 62443 Mapping

| Security Category | IEC 62443 SRs Addressed | NIST CSF Function |
|------------------|------------------------|-------------------|
| OT/ICS Security Platform | SR-1.x, SR-2.x, SR-5.x, SR-6.x, SR-7.x | Protect, Detect |
| Network Segmentation (Industrial DMZ) | SR-5.1, SR-5.2, SR-5.4 | Protect |
| OT Asset Management | SR-7.8, SR-7.6 | Identify |
| OT Backup & Recovery | SR-7.3, SR-7.4 | Recover |
| OT SIEM/Monitoring | SR-2.8, SR-6.1, SR-6.2 | Detect |
| OT IAM | SR-1.1 to SR-1.13 | Protect |

---

## Key OT Security Vendors (IEC 62443 Aligned)

| Vendor | IEC 62443 Role | Certifications |
|--------|---------------|----------------|
| Claroty | OT visibility, VM, segmentation | IEC 62443 alignment |
| Dragos | OT threat detection, IR | IEC 62443 alignment |
| Nozomi Networks | Passive OT monitoring, asset discovery | IEC 62443 alignment |
| Fortinet | OT NGFW, IPS, NAC | IEC 62443-4-2 certified products |
| Cisco Cyber Vision | Passive OT discovery, segmentation via ISE | IEC 62443 alignment |
| Tenable OT (Indegy) | OT vulnerability management | IEC 62443 alignment |
| PAS Global (Hexagon) | OT asset management, configuration management | IEC 62443 alignment |
| Honeywell Forge | OT cybersecurity for process industry | IEC 62443 alignment |
| Schneider Electric EcoStruxure | ICS with embedded security | IEC 62443 compliant |

---

## References

- Source JSON: [OT-Security/cross-references/iec62443-to-nist-csf.json](https://github.com/dawuds/OT-Security/blob/main/cross-references/iec62443-to-nist-csf.json)
- IEC 62443-3-3:2013 — Security for IACS: System security requirements and security levels
- NIST CSF 2.0: https://www.nist.gov/cyberframework
- CISA ICS security: https://www.cisa.gov/topics/industrial-control-systems
- OT-Security repository: [OT-Security technology categories](../technologies/categories/protect/ot-ics-iot.yaml)
