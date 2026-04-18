# Data Protection Architecture Blueprint

**Domain:** Data Security (spans Protect + Identify + Govern NIST functions)  
**Position:** Cross-cutting capability — applies to all workloads, all environments

---

## Overview

Data protection is the discipline of ensuring sensitive data remains confidential, intact, and available only to authorized parties — from creation through destruction. Unlike perimeter or endpoint security (which protect the path to data), data protection controls attach to the data itself, remaining effective even after a perimeter breach.

**Core principle:** Classify first, protect everywhere. A data protection program that doesn't know what data it has cannot protect it.

---

## Data Protection Technology Stack

```
┌─────────────────────────────────────────────────────────────────────┐
│                     DATA PROTECTION LAYERS                          │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 1: DISCOVER    │  What data exists? Where is it?             │
│  LAYER 2: CLASSIFY    │  What is the sensitivity/type?              │
│  LAYER 3: GOVERN      │  Who should access it? For how long?        │
│  LAYER 4: PROTECT     │  Encrypt, DLP, IRM enforcement              │
│  LAYER 5: MONITOR     │  DAM, DSPM, behavioral analytics            │
│  LAYER 6: RESPOND     │  Data breach response, forensics            │
│  LAYER 7: RETAIN      │  Backup, archival, disposal                 │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Layer-by-Layer Technology Map

### Layer 1: Discovery

*Find all sensitive data across the organization — structured, unstructured, cloud, on-prem.*

| Technology | Description | Products |
|-----------|-------------|---------|
| **Data Discovery (Cloud)** | Agentless scan of cloud storage (S3, Azure Blob, GCS, Snowflake, BigQuery) | Wiz DSPM, Cyera, Varonis, Amazon Macie, Microsoft Purview |
| **Data Discovery (On-prem)** | File server, SharePoint, NAS scanning | Varonis, Spirion, BigID |
| **Database Discovery** | Structured data (SQL, NoSQL, data warehouses) | IBM Guardium, Imperva, Collibra |
| **SaaS Data Discovery** | Data in SaaS (Salesforce, Slack, Box, Google Workspace) | Varonis, BigID, Netskope CASB |
| **Shadow Data Discovery** | Undocumented data stores, dev/test copies with prod data | Cyera, Wiz, Securiti |

**Key vendors:**
- **Wiz** (cloud-native, agentless) — DSPM as part of CNAPP; correlates data location with exposure paths
- **Varonis** (file-centric) — deep file system analysis; who has access, who is using it
- **BigID** (privacy-first) — consent management + data inventory; strong GDPR/CCPA tooling
- **Cyera** (DSPM pure-play) — fast agentless cloud scanning; actionable risk scoring
- **Dig Security** — unified DSPM + DLP + DDR; acquired by Palo Alto (2024)
- **Securiti** (AI-driven) — Privacy operations + DSPM + consent management

---

### Layer 2: Classification

*Label data by sensitivity so downstream controls can enforce the right policy.*

**Classification schemes:**

| Level | Examples | Controls Applied |
|-------|---------|-----------------|
| **Public** | Marketing materials, public docs | No restrictions |
| **Internal** | Internal policies, org charts | No sharing outside org |
| **Confidential** | Business plans, contracts, HR data | Encryption, DLP, access review |
| **Restricted / Secret** | PII, PHI, PCI, IP, credentials | Encryption + DLP + IRM + MFA required |
| **Regulated** | GDPR personal data, HIPAA PHI, PCI CHD | Above + audit trail + DSAR workflow |

**Classification technology:**

| Tool | Approach | Products |
|------|---------|---------|
| Manual labeling | User applies sensitivity label | Microsoft Purview (sensitivity labels in Office apps) |
| Auto-classification (pattern) | Regex, NLP for PII/PCI patterns | Microsoft Purview auto-labeling, Spirion |
| ML-based classification | Context-aware ML models | BigID, Securiti, Varonis AI |
| At-rest scanner | Scan existing files, apply labels | Purview scanner, Varonis |

**Key standard:** Microsoft Purview Sensitivity Labels are the de facto enterprise standard for document classification (integrates with Office 365, Teams, SharePoint, and applies persistent encryption via IRM).

---

### Layer 3: Data Access Governance (DAG)

*Who has access to sensitive data? Is that access appropriate? Is it being used?*

| Capability | Description | Products |
|-----------|-------------|---------|
| Data access audit | Who accessed what data, when | Varonis, Imperva, IBM Guardium |
| Entitlement review | Does this person still need access? | Varonis, SailPoint, Collibra |
| ABAC enforcement | Attribute-based access (label drives policy) | Microsoft Purview (DLP policy), Varonis |
| Data catalog | Business-oriented view of data assets | Collibra, Alation, Informatica, Microsoft Purview Data Catalog |
| Sensitive data access alerts | Alert when classified data is accessed unusually | Varonis, Macie, Guardium |

---

### Layer 4: Data Protection (DLP + IRM + Encryption)

#### 4a. Data Loss Prevention (DLP)

DLP prevents sensitive data from leaving the organization or being shared inappropriately.

**Three deployment modes:**

| Mode | What It Protects | Products |
|------|----------------|---------|
| **Endpoint DLP** | Data in use on endpoints (copy, paste, screenshot, USB, print) | Microsoft Purview Endpoint DLP, Forcepoint, Trellix DLP |
| **Network DLP** | Data in transit over web/email/FTP | Zscaler DLP (inline), Netskope, Forcepoint Web DLP |
| **Cloud/SaaS DLP** | Data in SaaS apps (upload, share, sync) | Netskope CASB DLP, Microsoft Purview Cloud DLP, Zscaler CASB |

**Key DLP vendors:**

| Vendor | Strength | Architecture |
|--------|---------|-------------|
| **Microsoft Purview** | Native M365 integration; no extra agent | Cloud-native for M365 + endpoint agent |
| **Netskope** | CASB+DLP convergence; SaaS-first | Inline proxy + API |
| **Forcepoint** | Risk-adaptive DLP; insider threat focus | Agent + gateway hybrid |
| **Zscaler** | DLP integrated into SSE/ZTNA flow | Inline proxy (all traffic) |
| **Trellix (McAfee/FireEye)** | Deep endpoint DLP; legacy enterprise | Agent-based |
| **Symantec (Broadcom)** | Enterprise DLP with OCR/document fingerprinting | Agent + gateway |

#### 4b. Information Rights Management (IRM) / Digital Rights Management (DRM)

IRM attaches persistent protection to documents — the document remains encrypted even after leaving the organization.

| Product | Capabilities |
|---------|------------|
| **Microsoft Purview IRM** | Encrypt Office docs/PDFs; permissions (view, edit, copy, forward); revocation; expiry |
| **Adobe Acrobat Rights Mgmt** | PDF permissions: no-print, no-copy, password, expiry |
| **SealPath** | IRM for any file type; real-time revocation |
| **Vera (Broadcom)** | Enterprise IRM for any file |

#### 4c. Encryption

| Layer | Technology | Products |
|-------|-----------|---------|
| Data at rest (disk) | Full-disk encryption | BitLocker, FileVault, dm-crypt |
| Data at rest (file/object) | Object-level encryption with CMEK | AWS S3 SSE-KMS, Azure Blob encryption, GCS CMEK |
| Data in transit | TLS 1.3 | Mandatory; NGFW/SSE enforces |
| Database encryption | TDE (Transparent Data Encryption) | SQL Server TDE, Oracle TDE, PostgreSQL |
| Field-level encryption | Column/field encryption | AWS DynamoDB field encryption, application-level |
| Tokenization | Replace PAN/SSN with token | Braintree, Protegrity, Thales Vormetric |

#### 4d. Key Management

| Technology | Products | Use Case |
|-----------|---------|---------|
| Cloud KMS | AWS KMS, Azure Key Vault, Google Cloud KMS | Cloud-native key management |
| Enterprise KMS | Thales CipherTrust Manager | Multi-cloud + on-prem unified key management |
| HSM | Thales Luna, Utimaco, IBM Z HSM | FIPS 140-2/3 hardware key storage |
| Secrets Management | HashiCorp Vault, CyberArk Conjur, AWS Secrets Manager | Application secrets, service credentials |
| Cloud HSM | AWS CloudHSM, Azure Managed HSM | Dedicated hardware in cloud environment |

---

### Layer 5: Monitoring (DAM + DSPM + Analytics)

#### Database Activity Monitoring (DAM)

DAM captures every SQL query executed against a database — who, when, what data, from where.

| Product | Strength | Notes |
|---------|---------|-------|
| **IBM Guardium** | 40+ database types; behavioral analytics; real-time blocking | Strongest enterprise DAM |
| **Imperva (Sonar)** | DAM + WAF + DDR convergence; cloud and on-prem | Strong for PCI/compliance |
| **Solarwinds DAM** | Mid-market; activity log + ML anomaly | Simpler deployment |
| **Oracle Audit Vault** | Native Oracle environments | Free for Oracle databases |
| **Microsoft Defender for SQL** | Azure SQL, SQL Server on Azure | Integrated into Defender for Cloud |

#### Data Security Posture Management (DSPM)

DSPM continuously monitors the configuration and access posture of data stores — identifying exposed buckets, overly permissive database access, sensitive data in dev/test, and more.

**Gartner Innovation Insight on DSPM (2023):** DSPM is a distinct market; not just cloud DLP or CSPM extension.

| Product | Approach | Key Capability |
|---------|---------|---------------|
| **Wiz DSPM** | Agentless, CNAPP-integrated | Attack path: data exposure → cloud misconfig → blast radius |
| **Cyera** | Agentless; fast cloud scanning | Sensitive data classification + exposure scoring |
| **Varonis** | File-centric; identity-aware | Who has access to sensitive files; abnormal behavior alerts |
| **BigID** | Privacy-first; consent workflows | GDPR/CCPA DSAR automation; data lineage |
| **Securiti** | AI + privacy + DSPM | Privacy operations + data intelligence |
| **Dig Security** | DSPM + DLP + DDR | Unified; acquired by Palo Alto (2024) |

---

### Layer 6: Data Detection & Response (DDR)

DDR = detecting data breaches in progress and responding. Newer capability (2023-2024) combining DSPM + behavioral analytics.

**Core DDR capabilities:**
- Detect abnormal data access (bulk downloads, unusual query patterns)
- Alert on data movement to unsanctioned locations
- Correlate identity + data access for insider threat detection
- Automated response: revoke access, quarantine endpoint

**Products:** Dig Security (Palo Alto), Varonis MDDR (managed), Imperva Data Security, Cyera

---

### Layer 7: Data Retention, Backup & Disposal

| Capability | Products | Category |
|-----------|---------|---------|
| Immutable backup | Veeam Hardened Repository, Rubrik Polaris, AWS S3 Object Lock | [Backup & Recovery](../technologies/categories/recover/backup-recovery.yaml) |
| Compliance archiving | Microsoft Purview (compliance archiving), Proofpoint Archive | [DLP](../technologies/categories/protect/dlp.yaml) |
| eDiscovery | Microsoft Purview eDiscovery, Relativity | [GRC](../technologies/categories/govern/grc.yaml) |
| Secure data destruction | Blancco, WipeDrive | Physical/logical disposal |

---

## Privacy-Enhancing Technologies (PETs)

Enabling analytics without exposing raw sensitive data:

| Technology | Description | Maturity | Use Case |
|-----------|-------------|---------|---------|
| **Differential Privacy** | Add mathematical noise to prevent individual identification | Production (Apple, Google use in practice) | Analytics on aggregate data without exposing individuals |
| **Homomorphic Encryption** | Compute on encrypted data without decrypting | Early production (Intel, IBM HElib) | Outsource computation to untrusted party |
| **Secure Multi-Party Computation** | Multiple parties compute jointly without revealing inputs | Maturing | Financial fraud detection across banks |
| **Federated Learning** | Train ML models across distributed data without centralizing | Production | Healthcare AI across hospital networks |
| **Tokenization** | Replace sensitive value with non-sensitive token | Mature | PCI CHD protection; analytics on tokenized data |
| **Data Masking** | Replace with realistic fake data for dev/test | Mature | Non-prod environments with realistic test data |
| **Synthetic Data** | Generate statistically equivalent fake datasets | Growing | AI training without privacy risk |

---

## Data Protection by Regulatory Framework

| Regulation | Key Data Protection Requirements | Technology Controls |
|-----------|--------------------------------|-------------------|
| **GDPR (EU)** | Lawful basis, consent, data minimization, DSAR (access/deletion), breach notification 72h, Privacy by Design | DSPM (data inventory), DLP (prevent breach), Purview (consent/labels), BigID (DSAR automation) |
| **CCPA/CPRA (California)** | Right to know, delete, opt-out of sale; Sensitive PI special rules | BigID (consumer rights mgmt), Securiti (CCPA workflow) |
| **HIPAA (US Healthcare)** | PHI encryption, BAA, minimum necessary, audit controls | IBM Guardium (DAM), encryption (TDE + KMS), DLP (PHI detection) |
| **PCI DSS v4.0** | CHD encryption, network segmentation, access controls, tokenization preferred | Imperva DAM, tokenization, NGFW microsegmentation, Purview DLP |
| **Malaysia PDPA** | Security standards for personal data, consent, data subject rights | DLP, DSPM, BigID/Securiti for DSAR |
| **ISO 27001:2022** | A.8 Asset management, A.8.11 Data masking, A.8.12 DLP | DLP, Classification, Backup |
| **SOC 2 Type II** | Availability, Confidentiality, Security, Privacy trust service criteria | Broad — DSPM + DLP + Backup + Access Controls |

---

## Data Protection Architecture Patterns

### Pattern 1: Data-Centric Security Model

**Traditional:** Protect the network perimeter → data inside is trusted.  
**Data-centric:** Classify all data → protect based on label → enforcement follows data everywhere.

```
[Data Created]
    ↓ auto-classification (Purview AI)
[Label Applied: Confidential-PII]
    ↓ label triggers policies
[Encrypted]          → KMS wraps with classification-specific key
[DLP Rules Activate] → Cannot email externally; USB blocked; cloud upload denied
[IRM Applied]        → If shared externally, document remains encrypted; access tracked
[Audit Trail]        → Every access logged to SIEM
```

### Pattern 2: Zero Trust Data

Every access request to sensitive data must be justified by identity + context + classification policy:

```
[Request: User A wants to read DB table containing SSNs]
    ↓ evaluated by
[Policy engine checks:]
  ✓ User A has data access role (IGA verified)
  ✓ Device is compliant (MDM + EDR clean)
  ✓ Request is from office hours in expected location
  ✓ Data classification = Restricted; User role includes "need to know"
  → Grant access with session recording (DAM/PAM)
  → Alert if 100+ rows read in single session (DAM anomaly)
```

### Pattern 3: Cloud Data Security Architecture

```
[Cloud Data Store (S3, Azure Blob, BigQuery, Snowflake)]
         ↓
[DSPM scans continuously] → finds: "Bucket X is public + contains PII"
         ↓
[Alert → SOAR playbook] → removes public access, notifies owner
         ↓
[DLP policy configured] → blocks future public access for classified data
         ↓
[KMS encryption enabled] → CMEK with customer-controlled keys
         ↓
[DAM/Cloud Logging] → all queries logged; anomaly detection via GuardDuty/Guardium
```

---

## Data Protection Tool Decision Matrix

| Scenario | Primary Tool | Reasoning |
|---------|-------------|-----------|
| M365-heavy enterprise, need DLP for email + endpoint | Microsoft Purview | Native integration; zero deployment friction; E5 bundled |
| Cloud-first org, need DSPM across AWS/Azure/GCP | Wiz DSPM + Varonis | Wiz for cloud posture; Varonis for file/identity depth |
| PCI-regulated org, need CHD protection | Imperva DAM + Tokenization | DAM for database monitoring; tokenization removes CHD from scope |
| HIPAA healthcare, need PHI protection | IBM Guardium + Purview DLP | Guardium for clinical DBs; Purview for endpoints/email |
| Privacy-first (GDPR/CCPA operations) | BigID or Securiti | Purpose-built for privacy ops + DSAR automation |
| Need DLP on all internet traffic (cloud-first ZTNA) | Zscaler DLP or Netskope | Inline DLP on all proxied traffic |
| Insider threat + behavioral focus | Varonis or Forcepoint | Deep behavioral analytics on data access patterns |

---

## References

- Gartner Innovation Insight: Data Security Posture Management (2023)
- NIST SP 800-188 — De-Identifying Government Datasets
- PCI DSS v4.0: https://www.pcisecuritystandards.org/
- GDPR: https://gdpr.eu/
- ENISA Data Protection Guidelines: https://www.enisa.europa.eu/
- Microsoft Purview DSPM: https://learn.microsoft.com/en-us/purview/
- OWASP Data Classification: https://owasp.org/www-community/Data_Classification
