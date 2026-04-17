# Okta — Vendor Profile

**Type:** Specialist Leader (Identity)  
**HQ:** San Francisco, CA, USA  
**Revenue:** ~$2.6B (FY2025)  
**Category:** [IAM / SSO / MFA](../categories/protect/iam-sso-mfa.yaml) | [IGA](../categories/identify/identity-governance.yaml)

---

## Overview

Okta is the market-defining independent identity platform. In a market where Microsoft (Entra ID), Ping Identity, and CyberArk provide identity capabilities as part of broader platforms, Okta remains the most widely deployed enterprise IdP specifically because it is **platform-agnostic** — integrating with Microsoft, Google, AWS, and on-premises applications equally.

The Okta Customer Identity Cloud (formerly Auth0, acquired 2021 for $6.5B) serves B2C/B2B customer-facing identity, while the Okta Workforce Identity Cloud targets enterprise employee identity (SSO, MFA, IGA, PAM-adjacent).

---

## Product Portfolio

### Workforce Identity Cloud
| Product | Category | Notes |
|---------|----------|-------|
| Okta SSO | SSO | SAML, OIDC, WS-Fed; 7,000+ pre-integrated apps in Okta Integration Network |
| Okta Adaptive MFA | MFA | Context-aware step-up MFA; FIDO2/WebAuthn, Okta Verify, SMS |
| Okta Device Trust | Device Posture | MDM compliance check before SSO grant; Intune, Jamf, CrowdStrike integration |
| Okta Lifecycle Management | IGA (provisioning) | Automated provisioning/deprovisioning; SCIM, HR-driven joiner/mover/leaver |
| Okta Access Governance | IGA (governance) | Access certifications, access requests, separation of duties (2023 launch) |
| Okta Privileged Access | PAM | Browser-based privileged access management (2023 launch; growing) |
| Okta Identity Threat Protection | Identity Threat Detection | Continuous session risk evaluation; post-auth threat signals |
| Okta Workflows | Identity Automation | No-code automation for identity events (provisioning workflows) |
| Okta FastPass | Passwordless | Device-bound FIDO2 passkey authentication |

### Customer Identity Cloud (Auth0)
| Product | Category | Notes |
|---------|----------|-------|
| Auth0 | CIAM | Customer identity: SSO, MFA, social login, B2B federation for applications |
| Auth0 Fine-Grained Authorization | Authorization | Fine-grained RBAC/ABAC for B2B SaaS applications |

---

## Strengths

- **Platform-neutral IdP** — integrates with Microsoft, Google, AWS, Salesforce, and on-prem apps equally; preferred where multi-cloud identity is required
- **Okta Integration Network** — 7,000+ pre-built connectors to SaaS apps; lowest integration effort in market
- **Adaptive MFA** — strongest context-aware MFA policy engine; device + location + behavior signals
- **Auth0 CIAM** — Auth0 is the leading developer-oriented CIAM platform; B2C/B2B app authentication
- **Lifecycle Management** — HR-driven automated provisioning (Workday, SAP, ADP integration)
- **Market position** — 18,000+ enterprise customers; most widely deployed independent IdP

---

## Weaknesses

- **October 2023 breach** — Okta support system compromised (HAR files); customer sessions exposed (BeyondTrust, Cloudflare, 1Password affected). Damage to CISO trust in identity platform security
- **Access Governance maturity** — Okta AG (IGA) launched 2023; trails SailPoint, Saviynt in IGA depth
- **PAM** — Okta Privileged Access is early-stage; not enterprise-ready vs. CyberArk/BeyondTrust
- **Revenue growth slowdown** — growth decelerating (30%+ → 15-20%) as market matures and Microsoft Entra competes
- **Microsoft competition** — Entra ID P2 + Entra ID Governance threatens Okta in Microsoft-first environments

---

## Licensing Model

| Product | Model | Approx. Annual Cost (per user) |
|---------|-------|-------------------------------|
| Okta Workforce SSO | Per user/month | ~$2-4/user/month |
| Okta Adaptive MFA | Per user/month | ~$3-6/user/month |
| Okta SSO + MFA bundle | Per user/month | ~$4-8/user/month |
| Lifecycle Management | Per user/month | ~$4/user/month |
| Okta Access Governance | Per user/month | ~$5/user/month |
| Okta Privileged Access | Per user/month | ~$8-15/user/month |
| Auth0 | Per Monthly Active User | ~$0.02-$0.25/MAU |

---

## NIST CSF Coverage

| Function | Coverage | Notes |
|----------|----------|-------|
| Govern | Partial | Access governance certifications; no GRC |
| Identify | Partial | Identity inventory; IGA access visibility |
| Protect | Very Strong | SSO + Adaptive MFA + Device Trust + Passwordless = comprehensive identity protection |
| Detect | Partial | Identity Threat Protection (continuous session risk); limited XDR integration |
| Respond | Weak | Okta Workflows can automate remediation; no native SOAR |
| Recover | Absent | No backup or recovery |

---

## The Okta Breach (October 2023) — Lessons

Attack vector: Credential stuffing against Okta's support portal → HAR file access → session tokens extracted → impersonation of Okta support sessions for customer environments.

**Impacted customers:** BeyondTrust, Cloudflare, 1Password detected the breach independently and notified Okta before Okta disclosed.

**Aftermath:**
- Okta locked down HAR file handling in support portal
- Customer admins could no longer expose full session details
- Okta accelerated rollout of security telemetry for customers
- Significant reputational impact in the CISO community

**Architecture lesson:** Identity platforms are critical infrastructure — their breach is a platform-wide security event. Require phishing-resistant MFA for all administrative access, monitor identity provider administrative actions, and implement SIEM integration for IdP audit logs.

---

## Key Integrations

- **MDM:** Intune, Jamf, Workspace ONE for device posture in adaptive policies
- **EDR:** CrowdStrike Falcon Zero Trust Assessment, SentinelOne for device risk signals
- **SIEM:** Splunk, Sentinel, Chronicle via Okta System Log
- **SOAR:** Splunk SOAR, Palo Alto XSOAR, Okta Workflows
- **HRMS:** Workday, SAP SuccessFactors, ADP, BambooHR for lifecycle automation

---

## Recent Developments (2023-2025)

- **Okta Privileged Access** (2023) — PAM product entering CyberArk/BeyondTrust market
- **Okta Access Governance** (2023) — IGA expansion competing with SailPoint/Saviynt
- **Okta Identity Threat Protection** (2023) — continuous post-authentication risk evaluation
- **FastPass / Passkeys** — passwordless FIDO2 passkey deployment for enterprise
- **October 2023 breach** — support system compromise; significant reputational impact

---

## Analyst Position

- **Gartner MQ:** Leader in Access Management (IAM SSO/MFA)
- **Forrester Wave:** Leader in IDaaS (Identity-as-a-Service), Zero Trust Platform
- **KuppingerCole:** Leader in Access Management and Customer Identity
