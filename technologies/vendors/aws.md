# AWS (Amazon Web Services) — Vendor Profile

**Type:** Hyperscaler (Cloud-native Security)  
**HQ:** Seattle, WA, USA  
**Security Revenue:** Embedded in AWS (no separate security segment; estimated ~$4-6B)  
**Architecture Reference:** [AWS Security Reference Architecture](../../architectures/aws-sra.md)

---

## Overview

AWS security is different from all other vendors: it is **cloud infrastructure with security built in**, not a security vendor that sells products to protect infrastructure. AWS security services are native controls within the AWS platform — IAM, GuardDuty, Security Hub, Inspector, Macie, CloudTrail — that collectively implement the AWS Shared Responsibility Model.

AWS doesn't compete with endpoint security vendors (no EDR), SIEM vendors (no native SIEM — Security Lake fills part of this), or email security vendors. Instead, AWS provides the foundational security controls for AWS environments, with a rich partner ecosystem for everything above the infrastructure layer.

---

## Security Service Portfolio

| Category | AWS Service(s) | NIST Mapping |
|----------|---------------|--------------|
| IAM | AWS IAM, Identity Center (SSO) | Protect |
| IGA | IAM Access Analyzer, Identity Center Governance | Protect, Govern |
| CIEM | IAM Access Analyzer (external access) | Identify |
| Secrets Management | AWS Secrets Manager | Protect |
| Key Management | AWS KMS, CloudHSM | Protect |
| CSPM | AWS Security Hub, AWS Config | Identify |
| CNAPP (fragmented) | Inspector + Security Hub + GuardDuty | Identify, Protect |
| VM | Amazon Inspector | Identify |
| Threat Detection | Amazon GuardDuty | Detect |
| DFIR (cloud) | Amazon Detective | Respond |
| Audit Logging | AWS CloudTrail | Detect |
| Configuration Compliance | AWS Config + Config Rules | Govern |
| WAF | AWS WAF | Protect |
| DDoS | AWS Shield Standard/Advanced | Protect |
| NGFW (cloud) | AWS Network Firewall | Protect |
| Network Security Policy | AWS Firewall Manager | Govern |
| DLP (cloud) | Amazon Macie | Protect |
| Data Security | Amazon S3 Object Lock, S3 Versioning | Protect, Recover |
| DNS Security | Route 53 Resolver DNS Firewall | Protect |
| Automation/SOAR | Amazon EventBridge + Lambda | Respond |
| Security Data Lake | Amazon Security Lake (OCSF) | Detect |
| Backup | AWS Backup (Vault Lock = immutable) | Recover |
| Disaster Recovery | AWS Elastic Disaster Recovery (EDR-DR) | Recover |
| Supply Chain Security | AWS Signer, ECR image scanning | Protect |
| Network Telemetry | VPC Flow Logs | Detect |

---

## Strengths

- **Shared Responsibility Model** — AWS handles infrastructure security (physical, hypervisor, network); customer responsibility is clear
- **Native integration** — all AWS security services are API-native; no agents for infrastructure-level controls
- **GuardDuty** — ML-based threat detection using AWS-unique signals (CloudTrail, DNS, VPC Flow, S3, EKS, Lambda)
- **Security Hub** — central finding aggregation; CIS AWS Foundations, PCI-DSS, NIST benchmarks built-in
- **AWS Organizations + SCPs** — preventive guardrails that are mandatory across all member accounts
- **Immutable logging** — S3 Object Lock + CloudTrail ensures tamper-proof audit logs
- **Security Lake (OCSF)** — OCSF-normalized data lake from AWS + 50+ third-party sources; positions AWS as the security data backbone
- **Recovery** — AWS Backup with Vault Lock provides immutable backup; Elastic DR for server recovery

---

## Weaknesses

- **No endpoint security** — AWS has no EDR/EPP; SSM provides remote command execution but is not security detection
- **No SIEM** — Security Lake is a data lake, not a SIEM; customers need Splunk, Sentinel, Chronicle, or Sumo Logic
- **No email security** — SES (Simple Email Service) is for sending, not protecting
- **No identity provider beyond AWS** — IAM Identity Center is AWS-centric; enterprises run Okta or Entra for enterprise SSO
- **Fragmented CNAPP** — Inspector (VM) + Security Hub (CSPM) + GuardDuty (detection) + Macie (DLP) are four separate services with no unified CNAPP console
- **OT/ICS** — no OT security services; IoT Core is for device connectivity, not security
- **Professional services** — AWS does not offer MDR; partners (Mandiant, CrowdStrike Complete) fill this

---

## Licensing Model

AWS security services are primarily **pay-as-you-go** based on resource/activity volume.

| Service | Pricing Model | Typical Enterprise Cost |
|---------|--------------|------------------------|
| GuardDuty | Per GB analyzed (varies by log type) | ~$5-30K/month depending on activity |
| Security Hub | Per finding per region | ~$1-5K/month |
| Inspector | Per EC2 instance + container scan | ~$2-10K/month |
| AWS WAF | Per rule + per million requests | ~$1-10K/month |
| Shield Advanced | $3,000/month flat + overages | ~$36K+/year minimum |
| AWS Backup | Per GB stored + transfer | Variable |
| Security Lake | Per GB ingested + stored | ~$1-5K/month |
| CloudTrail | First trail free; additional trails per region | ~$1-5K/month |

Total security spend for a typical mid-enterprise AWS environment: **$50K-$200K/year** on native AWS security services (before partner SIEM/EDR/email costs).

---

## NIST CSF Coverage

| Function | Coverage | Notes |
|----------|----------|-------|
| Govern | Partial | SCPs + Config rules as guardrails; no GRC/risk management platform |
| Identify | Strong (AWS-native) | Inspector VM + Security Hub CSPM + CloudTrail inventory; blind to non-AWS |
| Protect | Strong (cloud-native) | IAM + KMS + WAF + Network Firewall + SCPs = strong cloud controls |
| Detect | Very Strong (AWS-native) | GuardDuty ML detection uniquely uses AWS signals unavailable to third parties |
| Respond | Good (automated) | EventBridge + Lambda automation; no case management/SOAR |
| Recover | Good | AWS Backup + Vault Lock + Elastic DR = credible recovery capability |

---

## AWS vs. Security Vendors: Complementary, Not Competitive

AWS does not compete with:
- CrowdStrike (EDR) — AWS recommends CrowdStrike Falcon on AWS Marketplace
- Splunk/Sentinel (SIEM) — AWS Security Lake is designed to feed these SIEMs
- Okta (IdP) — IAM Identity Center integrates with Okta as the enterprise IdP
- Palo Alto Prisma (CNAPP) — Prisma Cloud runs on AWS, Inspector is a complement not replacement

AWS's model: **provide the foundation, let the partner ecosystem provide the superstructure.**

---

## AWS Security Partner Ecosystem

Key security partners certified/preferred by AWS:
- **SIEM:** Splunk, Microsoft Sentinel, Google Chronicle, IBM QRadar
- **EDR:** CrowdStrike, SentinelOne, Microsoft Defender for Endpoint
- **CNAPP:** Wiz, Palo Alto Prisma Cloud, Lacework (Fortinet), Orca Security
- **PAM:** CyberArk, BeyondTrust, HashiCorp Vault
- **Email:** Proofpoint, Mimecast, Microsoft Defender for Office 365

---

## Recent Developments (2023-2025)

- **Amazon Security Lake GA** (2023) — OCSF-based security data lake; aggregates AWS + 50+ partner sources
- **GuardDuty ECS Runtime Monitoring** (2023) — extends GuardDuty to ECS task-level runtime detection
- **Inspector SBOM export** (2024) — Software Bill of Materials for container images
- **IAM Access Analyzer unused access** (2023) — identifies stale permissions for CIEM use case
- **AWS Verified Permissions** (2023) — policy-as-code fine-grained authorization service

---

## Analyst Position

- **Gartner:** Leader in Cloud Infrastructure & Platform Services (IaaS); not evaluated as "security vendor"
- **Forrester:** Leader in Public Cloud Platform (security capabilities evaluated within broader IaaS assessment)
- **CISA partnership:** CISA produces AWS-specific security guidance and SCuBA equivalents for AWS
