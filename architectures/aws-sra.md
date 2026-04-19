# AWS Security Reference Architecture (AWS SRA)

**Version:** 2024  
**Source:** https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/  
**Type:** Cloud-Native Security Reference Architecture

---

## On This Page
- [Overview](#overview) — multi-account architecture as the security foundation
- [Multi-Account Architecture](#multi-account-architecture) — Management Account, Security OU, Workload OUs
- [Security Service Domains](#security-service-domains) — IAM, Detective Controls, Infrastructure Security, Data Protection, Incident Response
- [NIST CSF 2.0 Mapping](#nist-csf-20-mapping) — function coverage table
- [Key Architecture Decisions](#key-architecture-decisions) — SCPs, immutable logging, delegated admin
- [Coverage Gaps](#coverage-gaps) — what AWS SRA does not address
- [AWS Security Services Summary Table](#aws-security-services-summary-table) — full product reference

## At a Glance
- **Multi-account is foundational**: Management Account + Security OU (Security Tooling + Log Archive) + Workload OUs — account boundaries enforced by SCPs are the primary isolation mechanism
- **Five service domains**: IAM (identity + federation), Detective Controls (CloudTrail + Config + GuardDuty + Security Hub), Infrastructure Security (WAF + Shield + VPC Flow), Data Protection (KMS + Secrets Manager + Macie), Incident Response (native playbooks)
- **Amazon Security Lake + OCSF** (2023): cross-cloud log normalisation — ingests AWS, Azure, GCP, CrowdStrike, Okta into a common OpenCybersecurity Schema Framework, enabling third-party SIEM queries across all sources
- **Gaps**: No EDR, no SIEM, no email security, no NDR — AWS provides security primitives and infrastructure; customers build multi-vendor stacks around them; this is intentional
- **Direction →** AWS stays deliberately in its lane as cloud infrastructure provider; Amazon Security Lake + OCSF is the 2024–2025 telemetry normalisation bet — positioning AWS as the data fabric for third-party SIEMs (Splunk, Sentinel, Chronicle); the AWS-native security play is cheapest for AWS-first shops but is never a complete stack on its own

---

## Overview

The AWS Security Reference Architecture (AWS SRA) is Amazon's prescriptive guidance for organizing AWS security services across a multi-account AWS Organizations structure. It defines which security services to deploy, in which accounts, and how they interact — providing a security baseline for AWS environments.

AWS SRA is unique among vendor architectures in that it is **infrastructure-first**: it describes how to organize AWS accounts and services, not how to operate a security platform. AWS security services are native controls within the cloud fabric — not an overlay product sold separately.

**Key architecture pattern:** Centralized security accounts (Security Tooling Account, Log Archive Account) with delegated administration to member accounts via AWS Organizations, Control Tower, and Service Control Policies (SCPs).

---

## Multi-Account Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    AWS ORGANIZATIONS ROOT                           │
├───────────────────────┬─────────────────────────────────────────────┤
│  MANAGEMENT ACCOUNT   │  SECURITY OU                                │
│  (minimal services)   │  ├── Security Tooling Account               │
│                       │  │   (GuardDuty delegated admin,            │
│                       │  │    Security Hub, Inspector, Macie,       │
│                       │  │    Detective, Firewall Manager)          │
│                       │  └── Log Archive Account                    │
│                       │      (S3 + CloudTrail + VPC Flow Logs       │
│                       │       centralized; immutable)               │
├───────────────────────┼─────────────────────────────────────────────┤
│  WORKLOAD OUs         │  INFRASTRUCTURE OU                          │
│  ├── Prod OU          │  ├── Network Account                        │
│  ├── Dev OU           │  │   (Transit Gateway, AWS Firewall,        │
│  └── Sandbox OU       │  │    Route53 Resolver)                     │
│                       │  └── Shared Services Account                │
└───────────────────────┴─────────────────────────────────────────────┘
```

---

## Security Service Domains

### Domain 1: Identity & Access Management
| Service | Category | Notes |
|---------|----------|-------|
| AWS IAM | IAM | Foundational identity for all AWS API calls |
| AWS IAM Identity Center (SSO) | IAM / SSO | Centralized SSO for AWS console + CLI access across accounts |
| AWS Organizations + SCPs | Governance | Preventive guardrails — deny-by-default for dangerous actions |
| IAM Access Analyzer | CIEM | Identifies over-permissive policies; external access analysis |
| IAM Roles Anywhere | Non-human IAM | X.509 cert-based temporary credentials for on-prem workloads |
| AWS Secrets Manager | Secrets Management | Managed secrets storage with automatic rotation |
| AWS KMS | Key Management | Customer-managed keys for encryption at rest |
| AWS CloudHSM | HSM | Dedicated hardware security module for FIPS 140-2 Level 3 |

### Domain 2: Detective Controls
| Service | Category | Notes |
|---------|----------|-------|
| Amazon GuardDuty | Threat Detection | ML-based threat detection across CloudTrail, VPC Flow, DNS, S3 |
| AWS Security Hub | CSPM / Findings Aggregation | Central findings aggregation; CIS/PCI/NIST benchmark checks |
| Amazon Detective | DFIR (cloud) | Graph-based investigation of GuardDuty findings; CloudTrail correlation |
| AWS CloudTrail | Audit Logging | API call logging across all accounts; immutable in Log Archive |
| AWS Config | Configuration Compliance | Resource configuration history; compliance rules and drift detection |
| Amazon Macie | Data Security | ML-based sensitive data discovery in S3 (PII, secrets, credentials) |
| Amazon Inspector | Vulnerability Management | EC2/Lambda/container image vulnerability scanning |
| VPC Flow Logs | Network Telemetry | Layer 4 network traffic logs for analysis in Athena/SIEM |

### Domain 3: Infrastructure Security
| Service | Category | Notes |
|---------|----------|-------|
| AWS Network Firewall | NGFW (cloud) | Stateful L3-L7 firewall with Suricata rule support |
| AWS WAF | WAF | Web Application Firewall for CloudFront, ALB, API Gateway |
| AWS Shield Standard/Advanced | DDoS | Layer 3/4 DDoS protection (Standard = free); Advanced = L7 + SRT |
| AWS Firewall Manager | Security Policy Mgmt | Centralized WAF/Shield/Network Firewall policy across accounts |
| Amazon VPC | Network Isolation | Fundamental network segmentation; security groups + NACLs |
| AWS PrivateLink | Private Connectivity | Service-to-service connectivity without internet exposure |
| AWS Transit Gateway | Network Hub | Central routing hub; inspection-friendly architecture |
| Route 53 Resolver DNS Firewall | DNS Security | DNS-layer threat blocking and exfiltration prevention |

### Domain 4: Data Protection
| Service | Category | Notes |
|---------|----------|-------|
| AWS KMS | Encryption | Envelope encryption for all storage and transit |
| Amazon Macie | DLP (cloud) | S3 data discovery and classification |
| AWS Certificate Manager | PKI | TLS certificate provisioning and rotation |
| S3 Object Lock | Immutable Storage | WORM (Write Once Read Many) for backup/compliance |
| AWS Backup | Backup & Recovery | Centralized backup with vault lock (immutable backup) |

### Domain 5: Incident Response
| Service | Category | Notes |
|---------|----------|-------|
| Amazon EventBridge | SOAR Automation | Event-driven automation; rules trigger Lambda for auto-remediation |
| AWS Step Functions | Workflow Automation | Multi-step IR workflow orchestration |
| AWS Lambda | Automation | Serverless auto-remediation actions triggered by GuardDuty/Config |
| Amazon Security Lake | Security Data Lake | OCSF-normalized security data lake from AWS + third-party sources |
| AWS Systems Manager | Incident Response | Patching, remote command execution (SSM Run Command), forensic isolation |

---

## NIST CSF 2.0 Mapping

| NIST Function | AWS Services | Coverage |
|--------------|-------------|----------|
| **Govern** | AWS Organizations/SCPs (guardrails), AWS Control Tower (baseline), Config rules | Partial — preventive controls strong; GRC/risk register absent |
| **Identify** | AWS Config (inventory), Inspector (VM), IAM Access Analyzer (CIEM), Security Hub | Strong for AWS resources; blind to non-AWS assets |
| **Protect** | IAM (least privilege), KMS (encryption), Network Firewall, WAF, Shield, SCPs | Strong for cloud-native; no endpoint, limited on-prem |
| **Detect** | GuardDuty, Security Hub, CloudTrail, Config, Macie, Inspector, VPC Flow Logs | Very strong for AWS-native detection; limited for hybrid |
| **Respond** | EventBridge automation, Lambda, Step Functions, Security Lake, Detective | Good automated response; no native SOAR case management |
| **Recover** | AWS Backup (with vault lock), AWS Elastic Disaster Recovery | Partial — backup present but recovery planning/DR testing minimal |

---

## Key Architecture Decisions

### 1. Security Tooling Account Pattern
Centralizing GuardDuty, Security Hub, and Macie administration in a single Security Tooling Account:
- Member accounts cannot disable security services
- Findings flow to central account for SIEM integration
- Reduces risk of "security turned off" by workload owners

### 2. Log Archive Account (Immutable)
S3 bucket with **Object Lock + Vault Lock** prevents tampering:
- CloudTrail, VPC Flow Logs, Config snapshots written once
- Even account root cannot delete within retention period
- Critical for forensic integrity post-incident

### 3. SCPs as Preventive Guardrails
Service Control Policies at the OU level enforce:
- `DenyLeaveOrganization` — prevents account escape
- `DenyRootAccountActions` — enforces root account lockdown
- `RequireIMDSv2` — forces metadata service hardening
- Regional restrictions for data residency

---

## Coverage Gaps

- **Endpoint Security:** AWS has no EDR/EPP. SSM can run endpoint scripts but is not an EDR.
- **Email Security:** No AWS-native email security (SES for sending only; no SEG).
- **Identity beyond AWS:** IAM Identity Center is AWS-centric; does not replace enterprise IAM (Okta, Entra).
- **OT/ICS:** No operational technology support.
- **SOAR Case Management:** EventBridge + Lambda provides automation but no case management or analyst workflow.
- **Network Telemetry (beyond AWS):** VPC Flow Logs cover AWS traffic; no agent for on-prem NDR.

---

## AWS Security Services Summary Table

| Category | AWS Service | Notes |
|----------|------------|-------|
| IAM | IAM, Identity Center, Access Analyzer | Strong |
| CSPM | Security Hub, Config | Good |
| CNAPP | Inspector + Security Hub + GuardDuty (no unified CNAPP product) | Fragmented |
| Threat Detection | GuardDuty | Strong for cloud signals |
| WAF | AWS WAF | Adequate |
| NGFW | AWS Network Firewall | Capable but limited vs. hardware NGFW |
| Backup | AWS Backup | Good with Vault Lock |
| SIEM | Amazon Security Lake + partner SIEM | No native SIEM |
| SOAR | EventBridge + Lambda | DIY automation only |

---

## References

- AWS SRA: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/
- AWS Security Hub: https://aws.amazon.com/security-hub/
- GuardDuty: https://aws.amazon.com/guardduty/
- AWS Security Blog: https://aws.amazon.com/blogs/security/
- CISA guidance on AWS: https://www.cisa.gov/cloud-security
