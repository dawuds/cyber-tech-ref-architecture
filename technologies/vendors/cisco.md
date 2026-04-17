# Cisco — Vendor Profile

**Type:** Platform Vendor (Network + Security)  
**HQ:** San Jose, CA, USA  
**Security Revenue:** ~$3.8B (FY2024 Security segment)  
**Architecture Reference:** [Cisco Security Architecture](../../architectures/cisco-security.md)

---

## Overview

Cisco is the network vendor that became a security platform. Starting from NGFW (Firepower/ASA), Cisco built or acquired security capabilities across email (IronPort → ESA), MFA (Duo), web (Umbrella/OpenDNS), endpoint (AMP/Secure Endpoint), and SOC (XDR, Kenna VM). The $28B Splunk acquisition (September 2023) catapulted Cisco into enterprise SIEM leadership.

Cisco's differentiation: **network telemetry as a security sensor.** With Cisco switches and routers in 95% of enterprise networks, Cisco can extract security-relevant signals (NetFlow, Encrypted Traffic Analytics) from the network fabric without agents.

---

## Product Portfolio

| Category | Product(s) | NIST Mapping |
|----------|-----------|--------------|
| NGFW | Cisco Secure Firewall (Firepower) | Protect |
| IPS | Firepower IPS (Snort 3) | Protect |
| SASE / SSE | Cisco Secure Access | Protect |
| SWG / DNS | Cisco Umbrella | Protect |
| ZTNA | Cisco Secure Access ZTNA | Protect |
| VPN (legacy) | Cisco AnyConnect | Protect |
| MFA | Cisco Duo | Protect |
| NAC | Cisco ISE (Identity Services Engine) | Protect |
| Microsegmentation | Cisco Secure Workload (Tetration) | Protect |
| Email Security | Cisco Secure Email (ESA) | Protect |
| EDR / EPP | Cisco Secure Endpoint (AMP) | Detect |
| NDR | Cisco Secure Network Analytics (Stealthwatch) | Detect |
| SIEM | Splunk Enterprise Security | Detect |
| SOAR | Splunk SOAR (Phantom) | Respond |
| XDR | Cisco XDR | Detect, Respond |
| VM | Cisco Vulnerability Management (Kenna) | Identify |
| Threat Intelligence | Cisco Talos | Detect |
| Digital Experience | Cisco ThousandEyes | Identify |
| OT Security | Cisco Cyber Vision | Identify, Detect |
| CNAPP | Panoptica | Identify, Protect |
| Cloud NGFW | Cisco Multicloud Defense (Valtix) | Protect |
| SD-WAN | Cisco SD-WAN (Viptela) | Protect |

---

## Strengths

- **Network telemetry** — NetFlow + Encrypted Traffic Analytics from Cisco infrastructure = NDR without a separate sensor
- **Talos Threat Intelligence** — 250+ researchers; Snort/ClamAV open-source maintainer; 200B events/day
- **Splunk** — acquisition adds the leading enterprise SIEM (Splunk ES) + SOAR (Splunk SOAR) to Cisco portfolio
- **Duo MFA** — 40,000+ customers; trusted for MFA + device trust; easiest enterprise MFA to deploy
- **Umbrella DNS** — 2B+ DNS queries/day; fastest DNS-layer protection for mobile/remote users
- **Email security** — Cisco Secure Email (ESA) with Talos intelligence is top-3 SEG
- **OT/ICS** — Cyber Vision passive OT asset discovery deployed in industrial environments

---

## Weaknesses

- **CNAPP** — Panoptica is early-stage; lags Wiz, Prisma Cloud, Defender for Cloud significantly
- **EDR** — Cisco Secure Endpoint (AMP) lags CrowdStrike, MDE, SentinelOne in EPP/EDR Gartner positioning
- **PAM** — no native PAM; partners recommended
- **Splunk integration** — acquisition complete but Cisco XDR + Splunk SIEM integration still in progress (2024-2025)
- **Cloud-native** — Cisco's NGFW and security architecture are network-hardware-rooted; cloud-native security is secondary
- **Recovery** — no backup or DR products

---

## Licensing Model

Complex, product-by-product licensing (no unified platform credit model).

| Product | Model | Approx. Annual Cost |
|---------|-------|---------------------|
| Firepower 1120 (NGFW) | Hardware + 1-year subscriptions | ~$8K-$15K/appliance |
| Cisco Secure Firewall subscriptions | Per-appliance/year | ~$2K-$8K/year |
| Cisco Umbrella | Per user/year | ~$30-80/user/year |
| Cisco Duo | Per user/month | ~$3-9/user/month (MFA to Access tiers) |
| Cisco Secure Access | Per user/year | ~$80-140/user/year |
| Cisco ISE | Per device + license tier | ~$50-200/concurrent endpoint |
| Cisco Secure Endpoint | Per endpoint/year | ~$50-80/endpoint/year |
| Splunk Enterprise Security | Per GB/day ingest | ~$1,800-$2,200/GB/day/year |
| Splunk SOAR | Per automation | ~$150K-$500K/year |

---

## NIST CSF Coverage

| Function | Coverage | Notes |
|----------|----------|-------|
| Govern | Weak | Kenna VM risk scoring; no GRC platform |
| Identify | Good | Kenna VM, ThousandEyes, Cyber Vision OT, Umbrella SaaS discovery |
| Protect | Very Strong | NGFW + SSE + Duo MFA + ISE NAC + Email + Microsegmentation |
| Detect | Strong (post-Splunk) | XDR + Splunk SIEM + NDR (Stealthwatch) + Talos TI |
| Respond | Strong (post-Splunk) | Splunk SOAR + Talos IR + Cisco XDR automated response |
| Recover | Absent | No backup or DR products |

---

## The Splunk Integration Story

Cisco's $28B Splunk acquisition (2023) is the largest security deal in history:

**What Cisco gained:**
- Market-leading enterprise SIEM (Splunk Enterprise Security)
- Leading SOAR platform (Splunk SOAR / Phantom)  
- Dominant log management and observability
- 15,000+ Splunk enterprise customers

**Integration roadmap:**
- Cisco XDR feeds detections into Splunk SIEM
- Talos intelligence enriches Splunk ES alerts
- Cisco network telemetry becomes a primary Splunk data source
- Unified SOC: Cisco XDR (investigation) + Splunk ES (SIEM) + Splunk SOAR (response)

**Risk:** Integration complexity; Splunk customers buying from Cisco vs. Cisco customers adding Splunk.

---

## Key Integrations

- **Cisco-native:** All Cisco security products integrate via SecureX/XDR APIs
- **Identity:** Duo integrates with Okta, Entra, Ping as MFA overlay; ISE integrates with AD
- **SIEM:** Splunk ES ingests all Cisco telemetry natively; Splunk connectors for AWS, Azure, GCP
- **SOAR:** Splunk SOAR integrates with 300+ tools (ServiceNow, Jira, PagerDuty, NGFW APIs)

---

## Recent Developments (2023-2025)

- **Splunk acquisition closes** (September 2023) — transforms Cisco into SIEM/SOAR leader
- **Cisco XDR launch** (2023) — replaces SecureX; integrates Talos, Secure Endpoint, Network Analytics, Umbrella, Email
- **Cisco AI Defense** (2024) — AI security product for LLM access control and AI workload protection
- **Cisco Secure Access** (2023) — unified SSE converging Umbrella + Duo + Secure Client into SASE
- **Valtix acquisition** (2023) — cloud NGFW for multi-cloud environments

---

## Analyst Position

- **Gartner MQ:** Leader in SIEM (Splunk), Network Firewalls, SSE, Email Security; Challenger in EPP
- **Forrester Wave:** Leader in Network Security, Zero Trust Platform
- **IDC:** Leader in network security hardware
