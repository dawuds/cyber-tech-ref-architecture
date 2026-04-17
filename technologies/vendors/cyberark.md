# CyberArk — Vendor Profile

**Type:** Specialist Leader (PAM / Identity Security)  
**HQ:** Newton, MA, USA (founded in Israel)  
**Revenue:** ~$900M (FY2024, growing ~30%)  
**Category:** [PAM](../categories/protect/pam.yaml) | [Secrets Management](../categories/protect/secrets-management.yaml) | [IGA](../categories/identify/identity-governance.yaml)

---

## Overview

CyberArk is the market-defining vendor for Privileged Access Management (PAM) and the leader in the broader identity security category. Founded in 1999, CyberArk built its reputation on securing privileged accounts — the credentials most targeted in advanced attacks (domain admin, root, service accounts).

CyberArk's strategic evolution: from standalone PAM vault (Enterprise Password Vault) to full **Identity Security Platform** — spanning PAM, secrets management, endpoint privilege management, CIAM for developers, and workforce SSO/MFA. This positions CyberArk against Okta (identity), HashiCorp (secrets), and BeyondTrust (PAM) simultaneously.

---

## Product Portfolio

### Privileged Access Management
| Product | Category | Notes |
|---------|----------|-------|
| Privilege Cloud | PAM (SaaS) | Cloud-native PAM vault; replaces on-prem EPV for SaaS delivery |
| Enterprise Password Vault (EPV) | PAM (on-prem) | Original CyberArk product; highest-assurance on-prem vault |
| Privileged Session Manager (PSM) | Session Management | Proxy-based session recording + isolation; no credentials on endpoint |
| Credential Provider | Secrets Management | Application credential storage + retrieval API |
| Central Policy Manager (CPM) | Password Rotation | Automated credential rotation on schedule or on-demand |

### Secrets Management
| Product | Category | Notes |
|---------|----------|-------|
| Conjur (open-source + enterprise) | Secrets Management | Machine identity secrets vault; competing with HashiCorp Vault |
| Secrets Hub | Secrets Management | Sync between CyberArk Conjur and cloud-native secret stores (AWS SM, Azure KV) |
| Workforce Password Management | Password Manager | Business-grade password vault for non-privileged users |

### Endpoint Privilege Management
| Product | Category | Notes |
|---------|----------|-------|
| Endpoint Privilege Manager (EPM) | Endpoint Least Privilege | Remove local admin rights; just-in-time elevation for specific tasks |
| Endpoint Privilege Manager for Servers | Server Least Privilege | Linux/Unix/Windows server privilege restriction |

### Access & Identity
| Product | Category | Notes |
|---------|----------|-------|
| CyberArk Identity (Workforce SSO/MFA) | SSO / MFA | Workforce identity acquired from Idaptive (2020); competing with Okta |
| CyberArk Identity Security Intelligence | UEBA (identity) | Behavioral analytics on identity and access patterns |
| Vendor Privileged Access Manager | Third-party PAM | Remote access for vendors without VPN; session isolation |
| Cloud Entitlement Manager | CIEM | Cloud privilege management across AWS/Azure/GCP |
| Remote Access | ZTNA (privileged) | Zero trust remote access for privileged users; no VPN required |

---

## Strengths

- **PAM market leadership** — CyberArk is the default "PAM" answer in enterprise; 8,000+ customers; broadest PAM feature set
- **Session isolation** — PSM proxy prevents credentials from ever reaching the endpoint; gold standard for privileged session security
- **Secrets management** — Conjur is production-proven at scale; used by leading DevOps/DevSecOps organizations
- **Compliance** — PCI DSS, SOX, HIPAA, NERC CIP all reference privileged access controls; CyberArk is auditor-familiar
- **Integration depth** — 400+ certified integrations with SIEM, ticketing, ITSM, cloud, and endpoint tools
- **EPM** — strongest endpoint privilege removal; least admin rights enforcement on Windows/Linux
- **Identity Security Platform vision** — cohesive product strategy to own the "identity security" category

---

## Weaknesses

- **Cost** — CyberArk is one of the most expensive security products in the market; deployment complexity adds professional services cost
- **Deployment complexity** — on-prem EPV implementation is complex; 6-12 month implementations common at large enterprises
- **Workforce SSO/MFA** — CyberArk Identity SSO trails Okta and Entra ID in integration breadth and maturity
- **CIAM** — no consumer-facing CIAM (Auth0/Okta CIAM market)
- **Cloud-native speed** — Privilege Cloud (SaaS) is faster to deploy but organizations still prefer EPV on-prem for highest assurance

---

## Licensing Model

| Product | Model | Approx. Annual Cost |
|---------|-------|---------------------|
| Privilege Cloud | Per privileged user/month | ~$10-20/privileged user/month |
| Enterprise Password Vault | Perpetual + annual maintenance | ~$50K-$500K+ depending on scale |
| Conjur Enterprise | Per workload/secret | ~$50-200K/year |
| Endpoint Privilege Manager | Per endpoint/year | ~$30-60/endpoint/year |
| CyberArk Identity (SSO/MFA) | Per user/month | ~$3-8/user/month |
| Remote Access | Per vendor session capacity | ~$10-20/user/month |

Total PAM implementation cost (including professional services): **$200K-$2M+** for mid-to-large enterprise.

---

## NIST CSF Coverage

| Function | Coverage | Notes |
|----------|----------|-------|
| Govern | Partial | Audit reporting; privileged access policy enforcement |
| Identify | Partial | Privileged account discovery; cloud entitlement visibility |
| Protect | Very Strong | PAM vault + session isolation + secrets management + EPM = core IAM controls |
| Detect | Partial | Identity Security Intelligence (UEBA for privileged accounts) |
| Respond | Weak | Session termination automation; no native SOAR |
| Recover | Absent | No backup or DR |

---

## Why PAM Matters (Attack Context)

Privileged credentials are the #1 target in advanced attacks:
- **Ransomware operators** escalate to domain admin to deploy ransomware across all systems
- **APT actors** target service accounts for persistence (Kerberoasting, AS-REP Roasting)
- **Supply chain attackers** target CI/CD secrets to poison the build pipeline
- **Insider threats** abuse privileged access with no legitimate business need

**CyberArk's value proposition:** Vault the credential (never expose it to the human/machine), record the session (forensic evidence), rotate automatically (break the persistence chain).

---

## Key Integrations

- **SIEM:** Splunk, Sentinel, Chronicle, QRadar (syslog + REST API)
- **ITSM:** ServiceNow (PAM request workflows), Jira
- **EDR:** CrowdStrike, SentinelOne (EPM integration for endpoint context)
- **Cloud:** AWS IAM, Azure Key Vault, GCP Secret Manager (Secrets Hub sync)
- **SOAR:** Splunk SOAR, Palo Alto XSOAR, ServiceNow SecOps

---

## BeyondTrust Comparison

| Dimension | CyberArk | BeyondTrust |
|-----------|----------|-------------|
| PAM depth | Highest assurance; EPV is gold standard | Good; more modern UX |
| Remote access | Vendor PAM + Remote Access | Privileged Remote Access (PRA) is stronger |
| EPM | Strong | Strong (PowerBroker for Windows/Linux) |
| Price | Premium | Mid-range |
| Cloud delivery | Privilege Cloud (SaaS) | BeyondTrust Cloud |
| Integration breadth | 400+ | 200+ |

---

## Recent Developments (2023-2025)

- **CyberArk Identity Security Platform** rebranding — unified portfolio under one platform narrative
- **Conjur Secrets Hub** (2023) — syncs CyberArk secrets to AWS SM / Azure KV for cloud-native apps
- **Workforce Password Management** — enterprise password manager for non-privileged users
- **AI-powered threat detection** — CyberArk Identity Security Intelligence ML improvements
- **Vendor Remote Access** — secure third-party access replacing VPN + jump server for vendors

---

## Analyst Position

- **Gartner MQ:** Leader in PAM (Privileged Access Management) — consistently #1
- **Forrester Wave:** Leader in Privileged Identity Management
- **KuppingerCole:** Leader in PAM
