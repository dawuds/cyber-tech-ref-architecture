# Proofpoint — Vendor Profile

**Type:** Specialist Leader (Email Security / Human-Centric Security)  
**HQ:** Sunnyvale, CA, USA (private since 2021 — Thoma Bravo)  
**Revenue:** ~$1.5B (est. FY2024; private company)  
**Category:** [Email Security](../categories/protect/email-security.yaml) | [DLP](../categories/protect/dlp.yaml) | [Security Awareness](../categories/govern/security-awareness.yaml)

---

## Overview

Proofpoint is the market-defining email security vendor and the leader in human-centric security. Taken private by Thoma Bravo in 2021 for $12.3B, Proofpoint's platform covers the complete people-centric attack surface: email (inbound threat protection + outbound DLP), security awareness training, insider risk management, and digital risk protection.

Proofpoint's core thesis: **People are the #1 attack vector.** 99%+ of breaches require human interaction (phishing click, credential entry, insider action). Therefore, protecting email + training people + monitoring human behavior forms the most important security control set.

---

## Product Portfolio

### Email Security
| Product | Category | Notes |
|---------|----------|-------|
| Proofpoint Email Protection (PPS/POD) | Email Gateway (SEG) | On-prem (PPS) and cloud (POD); reputation, AV, anti-spam, sandboxing |
| Targeted Attack Protection (TAP) | Advanced Email Threat | URL rewriting (Time of Click), attachment sandboxing, BEC detection |
| Email Fraud Defense (EFD) | Email Authentication | DMARC management, supplier fraud detection, lookalike domain monitoring |
| Proofpoint Isolation | Browser Isolation | URL isolation for risky links; integrated with TAP |
| Proofpoint Aegis | AI Email Platform | AI-powered email threat analysis; behavioral signal-based detection |
| Proofpoint Supplier Threat Intel | DRPS | Third-party email domain risk; lookalike domain and vendor impersonation |

### Security Awareness
| Product | Category | Notes |
|---------|----------|-------|
| Security Awareness Training (PSAT) | Security Awareness | Wombat acquisition (2018); phishing simulation + training content |
| Targeted Attack Training | Awareness (adaptive) | Training triggered based on TAP attack data — users who are targeted |
| Proofpoint Nexus People Risk Explorer | Human Risk | People Risk Management platform; very attacked people (VAPs) identification |

### Information Protection
| Product | Category | Notes |
|---------|----------|-------|
| Proofpoint Information Protection (DLP) | DLP | Email, cloud, and endpoint DLP; Tessian (ML email DLP) capability incorporated |
| Proofpoint Insider Threat Management | UEBA / Insider Risk | Behavioral monitoring for insider threats; ObserveIT acquisition (2019) |
| Proofpoint CASB | CASB | Cloud access security broker; SaaS usage monitoring |
| Proofpoint Sigma | Email DLP (cloud) | Cloud-native email DLP via API |

### Threat Intelligence
| Product | Category | Notes |
|---------|----------|-------|
| Proofpoint Threat Intelligence | CTI | Email-derived threat intelligence; actor attribution for email threats |
| Proofpoint Digital Risk Protection | DRPS | Domain spoofing, brand abuse, social media impersonation monitoring |
| Proofpoint Nexus Threat Graph | Threat Intelligence | Attack data from Proofpoint's 230K+ global customers |

---

## Strengths

- **Email security leadership** — Gartner MQ Leader in Email Security; processing 2B+ email messages/day; deepest email threat intelligence
- **BEC detection** — Business Email Compromise detection is market-leading; behavioral AI detects impersonation at pre-delivery
- **TAP (sandboxing + URL rewrite)** — Time of Click URL rewriting is the most effective defense against delayed phishing URL activation
- **Very Attacked People (VAP)** — unique targeting intelligence identifying the specific 1-5% of users receiving the majority of attacks; enables adaptive controls
- **Proofpoint Nexus** — threat graph from 230K+ customers creates unmatched email threat intelligence scale
- **Awareness integration** — security awareness training tied to actual attack data (users who clicked on TAP-detected phishing get targeted training)
- **Insider Risk** — ObserveIT integration provides comprehensive insider threat management (monitoring + DLP + behavioral analytics)

---

## Weaknesses

- **Non-email gaps** — Proofpoint is email-centric; limited in endpoint, network, cloud security
- **SIEM integration** — alerts are exported to third-party SIEM; no native SIEM
- **SOAR** — no native SOAR; integrations via Splunk SOAR, Palo Alto XSOAR
- **Post-Thoma Bravo** — private ownership limits transparency on R&D investment; potential cost focus vs. innovation
- **Cloud delivery** — POD (cloud) is good; but on-prem PPS deployments are operationally complex
- **Microsoft competition** — Defender for Office 365 Plan 2 provides competitive email security for M365 customers at marginal cost

---

## Licensing Model

| Product | Model | Approx. Annual Cost |
|---------|-------|---------------------|
| Email Protection (POD) | Per mailbox/year | ~$10-20/mailbox/year |
| TAP (Advanced Threat) | Per mailbox/year | ~$15-30/mailbox/year |
| Email + TAP bundle | Per mailbox/year | ~$20-40/mailbox/year |
| Security Awareness Training | Per user/year | ~$10-20/user/year |
| Insider Threat Management | Per user/month | ~$10-20/user/month |
| DLP (Email + Endpoint) | Per user/year | ~$20-40/user/year |

**Full Proofpoint Human-Centric Security platform** (email + awareness + ITM): ~$50-80/user/year

---

## NIST CSF Coverage

| Function | Coverage | Notes |
|----------|----------|-------|
| Govern | Partial | Security awareness training; DMARC policy enforcement |
| Identify | Partial | VAP risk scoring; digital risk monitoring |
| Protect | Very Strong (email) | Best-in-class email protection; DLP; CASB; awareness training |
| Detect | Good (email) | TAP sandboxing; BEC detection; insider threat behavior |
| Respond | Partial | Alert export to SIEM/SOAR; limited native response |
| Recover | Absent | No backup or DR |

---

## The People-Centric Security Model

Proofpoint's framework — **Nexus People Risk Management** — maps security risk to individuals:

1. **Identify:** Who are the Very Attacked People (VAPs)? Who has privileged access? Who is at risk?
2. **Prioritize:** Focus controls on the high-risk humans, not uniformly across all employees
3. **Protect:** Adaptive controls based on role + attack targeting + behavior patterns
4. **Train:** Targeted awareness training based on actual attacks received (not generic phishing simulations)

This is distinct from perimeter/infrastructure security — Proofpoint measures and manages **human risk** as a security variable.

---

## Key Integrations

- **SIEM:** Splunk (Proofpoint app on Splunkbase), Sentinel, Chronicle, QRadar
- **SOAR:** Splunk SOAR, Palo Alto XSOAR (pre-built Proofpoint integrations)
- **ITSM:** ServiceNow (incident creation from TAP alerts)
- **CASB:** Integrates with Netskope, McAfee MVISION for combined DLP
- **IdP:** Okta, Entra ID for user identity context in TAP alerts

---

## Recent Developments (2023-2025)

- **Tessian acquisition** (2023) — ML-based email DLP for detecting misdirected emails and data exfiltration; integrated into Proofpoint Sigma
- **Proofpoint Aegis** — AI-powered email threat platform rebranding
- **Nexus People Risk Explorer** — unified people risk management dashboard
- **AI-based BEC detection** — behavioral AI improvements for Business Email Compromise detection
- **Proofpoint Supplier Threat Intel** — supply chain email security for vendor impersonation

---

## Analyst Position

- **Gartner MQ:** Leader in Email Security Gateway — multiple consecutive years
- **Forrester Wave:** Leader in Enterprise Email Security
- **Gartner Peer Insights:** Customers Choice for Email Security
