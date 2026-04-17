# Cloudflare — Vendor Profile

**Type:** Specialist Leader (SSE / SASE / DDoS / Edge Security)  
**HQ:** San Francisco, CA, USA  
**Revenue:** ~$1.6B (FY2024)  
**Category:** [ZTNA / SSE / SASE](../categories/protect/ztna-sse-sase.yaml) | [WAF / API Security](../categories/protect/waf-api-security.yaml) | [DDoS](../categories/protect/ngfw-ips.yaml)

---

## Overview

Cloudflare is the internet performance and security company, built on a globally distributed network spanning 310+ cities in 120+ countries. Unlike traditional security vendors, Cloudflare's security runs at the network edge — closer to users and applications than any data center-based solution — enabling sub-10ms latency for security enforcement globally.

Cloudflare operates in three markets simultaneously: **application security** (WAF, DDoS, Bot management, API security), **Zero Trust / SASE** (Cloudflare One), and increasingly **AI infrastructure security** (AI Gateway, Firewall for AI).

Cloudflare's key advantage: **scale.** Processing 20-25% of internet HTTP traffic gives Cloudflare threat intelligence from a unique vantage point — observing attack patterns, DDoS campaigns, and malicious IPs that no enterprise sensor network could replicate.

---

## Product Portfolio

### Application Security
| Product | Category | Notes |
|---------|----------|-------|
| Cloudflare WAF | WAF | Rules + ML-based WAF; exposed to 20%+ of internet HTTP traffic |
| Cloudflare DDoS Protection | DDoS | Unlimited DDoS mitigation (no cost cap on attack size) |
| Cloudflare Bot Management | Bot Protection | Intent-based bot scoring; behavioral analysis vs. good/bad bots |
| Cloudflare API Shield | API Security | API discovery, schema validation, rate limiting, mTLS |
| Cloudflare Rate Limiting | Traffic Control | Request rate controls at the edge |
| Cloudflare Page Shield | CSP / Skimming | Client-side script integrity; Magecart/skimming attack prevention |
| Cloudflare Advanced DDoS | Layer 3-7 DDoS | BGP-based L3 protection + L7 application DDoS |
| Cloudflare Spectrum | TCP/UDP DDoS | Layer 4 protection for arbitrary TCP/UDP ports (not just HTTP) |

### Zero Trust / SASE (Cloudflare One)
| Product | Category | Notes |
|---------|----------|-------|
| Cloudflare Access | ZTNA | Zero trust application access; identity-aware proxy for web apps and SSH/RDP |
| Cloudflare Gateway | SWG + DNS | Secure Web Gateway + DNS filtering; policy enforcement for internet traffic |
| Cloudflare CASB | CASB | API-based SaaS visibility and control |
| Cloudflare DLP | DLP | Inline DLP for web and SaaS traffic through Gateway |
| Cloudflare Browser Isolation | RBI | Remote browser isolation for risky/unverified sites |
| Cloudflare Email Security (Area 1) | Email Security | DNS-based anti-phishing (Area 1 acquisition 2022); no SEG — MX record not required |
| Cloudflare Magic WAN | SD-WAN | Network-as-a-Service; route enterprise network through Cloudflare fabric |
| Cloudflare Magic Transit | Network DDoS | BGP-based DDoS protection and routing for enterprise network infrastructure |
| Cloudflare Data Loss Prevention | DLP | Content inspection for Gateway and CASB traffic |
| Cloudflare Digital Experience Monitoring | DEM | End-to-end path monitoring for user experience (DEX equivalent) |

### Developer / AI Security
| Product | Category | Notes |
|---------|----------|-------|
| Cloudflare AI Gateway | AI Security | Rate limiting, cost control, caching, observability for LLM API calls |
| Cloudflare Firewall for AI | AI/LLM Security | Prompt injection detection and output filtering (2024 launch) |
| Cloudflare Workers | Edge Compute | Serverless compute at the edge; custom security logic |
| Cloudflare R2 | Storage | Zero-egress cloud storage; often used for log archiving |

---

## Strengths

- **Global network scale** — 310+ PoPs; Anycast routing means DDoS is absorbed globally before reaching origin
- **DDoS leadership** — unlimited mitigated DDoS volume; no capacity limit; $0 overage charges (model advantage vs. AWS Shield Advanced)
- **WAF intelligence** — ML models trained on 20%+ of internet traffic; attack detection lead time vs. enterprise WAFs
- **SASE simplicity** — Cloudflare One (ZTNA + SWG + CASB + DLP) deploys faster than Zscaler or Palo Alto Prisma
- **Email (Area 1)** — pre-delivery phishing detection via DNS MX analysis without needing a gateway; unique architecture
- **Developer-friendly** — REST APIs, Terraform, Workers for custom logic; easiest SASE to self-service by security engineers
- **Pricing** — competitive at all sizes; free tier for WAF/DDoS, transparent enterprise pricing vs. complex vendor bundling

---

## Weaknesses

- **Endpoint security** — no EDR/EPP; ZTNA is device-trust via MDM integration, not agent-based endpoint control
- **SIEM** — no native SIEM; log export to third-party required
- **PAM** — no privileged access management
- **OT/ICS** — no operational technology products
- **Email depth** — Area 1 email security is strong for phishing prevention; limited for malware sandboxing vs. Proofpoint/Mimecast
- **Enterprise SOC integration** — less mature SIEM/SOAR integration ecosystem vs. Zscaler/Palo Alto
- **On-premises** — cloud-only architecture; no on-premises software for air-gapped or sovereignty requirements

---

## Licensing Model

**Cloudflare is one of the most transparent and competitive pricers in security:**

| Product | Model | Approx. Annual Cost |
|---------|-------|---------------------|
| WAF (Pro) | Per domain/month | ~$240/domain/year |
| WAF (Business/Enterprise) | Per domain/month + traffic | ~$2K-$50K+/year |
| DDoS Protection | Included in all plans | No separate cost |
| Cloudflare One (ZTNA + SWG) | Per user/month | ~$8-16/user/month |
| Email Security (Area 1) | Per mailbox/year | ~$20-40/mailbox/year |
| Magic Transit (Network DDoS) | Per Mbps capacity | ~$1,500-$2,000/Mbps/year |
| Bot Management | Per domain + requests | Custom |
| API Shield | Add-on to WAF | ~$30-$50/zone/month |

**Enterprise pricing** is negotiated; Cloudflare is known for significant discounting on multi-product commitments.

---

## NIST CSF Coverage

| Function | Coverage | Notes |
|----------|----------|-------|
| Govern | Weak | No GRC platform |
| Identify | Partial | API discovery, SaaS discovery via CASB; no asset management |
| Protect | Very Strong (web/access) | WAF + DDoS + ZTNA + SWG + Email = comprehensive web/access protection |
| Detect | Partial | WAF analytics, Area 1 phishing detection; no SIEM/XDR |
| Respond | Weak | Rate limiting / block rules; no native SOAR or case management |
| Recover | Absent | No backup or DR |

---

## The Cloudflare Network Advantage

Cloudflare's global Anycast network provides threat visibility unavailable to any enterprise:

- **20-25% of all HTTP/HTTPS internet requests** routed through Cloudflare
- Attack pattern detection within seconds of attack emergence globally
- **Botnet C2 resolution** — Cloudflare observes DNS queries to C2 domains before defender tools
- **DDoS amplification** — Cloudflare sees reflection/amplification attacks in their source networks, enabling BGP blackhole before they reach the target

This "internet sensor" position gives Cloudflare threat intelligence that is uniquely current and comprehensive for internet-facing threats.

---

## Area 1 Email Security (Acquired 2022)

Cloudflare's email security approach is architecturally unique:

**Traditional SEG:** Change MX record → all email flows through the gateway → inline inspection → deliver to mailbox.

**Area 1:** DNS-based analysis → crawl infrastructure behind phishing domains → pre-delivery blocking → no MX change required for M365/Google Workspace.

**Key differentiators:**
- No MX change for initial deployment; lower friction
- Integrates directly with M365 and Google Workspace APIs
- Pre-delivery blocking before email reaches the inbox (vs. post-delivery retraction)
- Phishing campaign intelligence from DNS crawling, not just email sampling

---

## Key Integrations

- **Identity:** Okta, Entra ID, Ping, Google Workspace for Cloudflare Access (ZTNA)
- **MDM:** Intune, Jamf, Workspace ONE for device posture in Zero Trust policies
- **SIEM:** Cloudflare Logpush → Splunk, Sentinel, Chronicle, Datadog
- **SOAR:** Integrations via Terraform/API; Splunk SOAR + Palo Alto XSOAR playbooks available

---

## Recent Developments (2023-2025)

- **Cloudflare AI Gateway** (2023) — observability and control for LLM API calls (OpenAI, Anthropic, Google)
- **Firewall for AI** (2024) — prompt injection detection for AI workloads
- **Workers AI** — inference at the edge; AI models deployed globally on Cloudflare network
- **Digital Experience Monitoring** (2023) — end-to-end user path monitoring for SASE deployments
- **CASB expansion** — deeper SaaS security posture (Jira, Salesforce, GitHub)
- **Cloudflare One expands** — full SASE positioning competing with Zscaler and Netskope

---

## Analyst Position

- **Gartner MQ:** Leader in Web Application and API Protection (WAAP); Strong Performer in SSE
- **Forrester Wave:** Leader in DDoS Mitigation, Strong Performer in Zero Trust Platform
- **Gartner Peer Insights:** Customers Choice for DDoS and WAAP
