# NIST CSF 2.0 — Protect (PR)

Implements safeguards to ensure delivery of critical services and reduce the likelihood and impact of cybersecurity events.

## Purpose

Protect encompasses the broadest range of security technology categories — identity, network, data, endpoint, application, and cloud controls. It answers: *What safeguards do we have in place?*

## Technology Categories

| Category | Description |
|----------|-------------|
| [IAM / SSO / MFA](../../technologies/categories/protect/iam-sso-mfa.yaml) | Identity platform, authentication, and authorization |
| [PAM](../../technologies/categories/protect/pam.yaml) | Privileged account and session management |
| [Secrets Management](../../technologies/categories/protect/secrets-management.yaml) | API keys, credentials, and cryptographic key lifecycle |
| [NGFW / IPS](../../technologies/categories/protect/ngfw-ips.yaml) | Network perimeter and east-west enforcement |
| [ZTNA / SSE / SASE](../../technologies/categories/protect/ztna-sse-sase.yaml) | Zero Trust access, secure web gateway, cloud-delivered security |
| [CASB](../../technologies/categories/protect/casb.yaml) | Cloud app visibility and control |
| [DLP](../../technologies/categories/protect/dlp.yaml) | Sensitive data protection across channels |
| [Email Security](../../technologies/categories/protect/email-security.yaml) | Anti-phishing, BEC protection, and secure email |
| [Endpoint Protection](../../technologies/categories/protect/endpoint-protection.yaml) | NGAV and malware prevention |
| [Application Security](../../technologies/categories/protect/application-security.yaml) | SAST/DAST/SCA in the SDLC |
| [WAF / API Security](../../technologies/categories/protect/waf-api-security.yaml) | Web and API layer protection |
| [CNAPP](../../technologies/categories/protect/cnapp.yaml) | Cloud-native workload and posture protection |
| [MDM / EMM](../../technologies/categories/protect/mdm-emm.yaml) | Device configuration and policy enforcement |
| [OT / ICS / IoT](../../technologies/categories/protect/ot-ics-iot.yaml) | Industrial and operational technology security |

## Key Outcomes (NIST CSF 2.0 Categories)

- **PR.AA** — Identity Management, Authentication & Access Control
- **PR.AT** — Awareness & Training
- **PR.DS** — Data Security
- **PR.PS** — Platform Security (config management, software integrity)
- **PR.IR** — Technology Infrastructure Resilience

## Vendor Architecture Coverage

**Strong:** All major vendor architectures — Protect is where vendors compete most intensely.  
**Key differentiation:** Breadth (Microsoft covers most categories), depth (Palo Alto for network), cloud-native (Wiz/CrowdStrike for cloud workloads), access control (Zscaler for ZTNA).

## Architecture Note: Zero Trust as a Protect Framework

Zero Trust (CISA ZTMM, Palo Alto ZTA, Zscaler ZTE) is primarily a **Protect** strategy with **Detect** implications. The five CISA ZTMM pillars (Identity, Devices, Networks, Applications, Data) map almost entirely to Protect categories above.
