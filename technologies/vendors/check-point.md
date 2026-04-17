# Check Point Software Technologies — Vendor Profile

**Type:** Platform Vendor (Security-pure-play)  
**HQ:** Tel Aviv, Israel  
**Security Revenue:** ~$2.4B (FY2024)  
**Architecture Reference:** [Check Point Infinity](../../architectures/checkpoint-infinity.md)

---

## Overview

Check Point Software is one of the original cybersecurity companies, founded by Gil Shwed in 1993 — inventor of the stateful firewall. Check Point remains a pure-play security company (no cloud infrastructure, no productivity suite), focused on prevention-first security across network, cloud, endpoint, and mobile.

The Infinity architecture consolidates the three product lines (Quantum, CloudGuard, Harmony) under unified management via the Infinity Portal and ThreatCloud AI. Check Point's claimed differentiator is the highest threat prevention rate in the industry, backed by ThreatCloud's collaborative intelligence from 150,000+ connected gateways.

---

## Product Portfolio

| Category | Product(s) | NIST Mapping |
|----------|-----------|--------------|
| NGFW | Quantum Security Gateways (all sizes) | Protect |
| Hyperscale NGFW | Quantum Maestro | Protect |
| SMB NGFW | Quantum Spark | Protect |
| IPS | Quantum NGFW IPS (integrated) | Protect |
| SD-WAN | Quantum SD-WAN (integrated) | Protect |
| DDoS | Check Point DDoS Protector | Protect |
| IoT | Quantum IoT Protect | Protect, Identify |
| CNAPP | CloudGuard CNAPP | Identify, Protect |
| CSPM | CloudGuard Posture Management | Identify |
| CWPP | CloudGuard Workload Protection | Protect |
| Cloud NGFW | CloudGuard Network Security | Protect |
| WAF / API | CloudGuard AppSec | Protect |
| CIEM | CloudGuard CIEM | Identify |
| Cloud Intelligence | CloudGuard Intelligence | Detect |
| EDR / EPP | Harmony Endpoint | Detect, Protect |
| Mobile (MTD) | Harmony Mobile | Protect |
| Email Security | Harmony Email & Collaboration | Protect |
| ZTNA / SSE | Harmony Connect | Protect |
| SWG / Browser Isolation | Harmony Browse | Protect |
| XDR | Horizon XDR / XPR | Detect, Respond |
| SIEM | Horizon Events | Detect |
| SOAR | Horizon Playbooks | Respond |
| MDR | Infinity SOC (SOC-as-a-Service) | Respond |
| Threat Intelligence | ThreatCloud AI | Detect |
| AI Copilot | Infinity AI Copilot | Detect |

---

## Strengths

- **Prevention-first** — ThreatCloud AI blocks threats before execution; claimed industry-leading block rates
- **NGFW heritage** — invented the stateful firewall; strong enterprise NGFW market presence
- **ThreatCloud AI** — 150K+ gateways contributing real-time intelligence; 90+ AI engines; collaborative blocking
- **Quantum Maestro** — hyperscale NGFW using commodity hardware; elastic scaling without chassis lock-in
- **CloudGuard CNAPP** — credible multi-cloud CNAPP with CSPM, CWPP, CIEM, AppSec (WAF)
- **Harmony Email** — strong email security for M365 and Google Workspace; behavioral AI for BEC
- **Pure-play security** — singular focus on security (no cloud revenue dilution); entire company focused on security R&D

---

## Weaknesses

- **EDR trailing** — Harmony Endpoint competes but trails CrowdStrike, MDE, SentinelOne in Gartner EPP positioning
- **SOAR maturity** — Horizon Playbooks newer; Palo Alto XSOAR leads with 1000+ integrations
- **XDR late entry** — Horizon XDR launched later than competitors; integration across Quantum/CloudGuard/Harmony still maturing
- **SIEM** — Horizon Events is Check Point-centric; enterprises need third-party SIEM for multi-source correlation
- **PAM** — no privileged access management product
- **OT depth** — Quantum IoT Protect covers IoT; limited industrial OT protocol depth vs. Fortinet/Claroty/Dragos
- **Innovation pace** — perceived as slower to innovate than CrowdStrike/SentinelOne in endpoint; innovation focused on NGFW/cloud

---

## Licensing Model

Product and subscription-based; complex licensing with maintenance + subscription components.

| Product | Model | Approx. Annual Cost |
|---------|-------|---------------------|
| Quantum 6200 (mid-range NGFW) | Hardware + annual subscriptions | ~$20K-$50K/year |
| Quantum Maestro (hyperscale) | Orchestrator + security groups + subscriptions | ~$100K-$500K+/year |
| Quantum Spark (SMB) | Hardware + 1-year Next Business Day | ~$3K-$10K/year |
| CloudGuard CNAPP | Per asset/month | ~$10-25/asset/month |
| Harmony Endpoint | Per endpoint/year | ~$50-80/endpoint/year |
| Harmony Email | Per mailbox/year | ~$30-60/mailbox/year |
| Harmony Connect (ZTNA) | Per user/year | ~$60-100/user/year |
| Infinity SOC MDR | Capacity-based | ~$200K-$500K+/year |

---

## NIST CSF Coverage

| Function | Coverage | Notes |
|----------|----------|-------|
| Govern | Weak | Compliance dashboards in CloudGuard; no GRC platform |
| Identify | Partial | CloudGuard CNAPP for cloud; IoT Protect for IoT; limited on-prem asset mgmt |
| Protect | Very Strong | Prevention-first: NGFW + CloudGuard + Harmony = broad surface; ThreatCloud inline |
| Detect | Good | ThreatCloud real-time; Horizon XDR maturing; CloudGuard Intelligence |
| Respond | Partial | Horizon Playbooks + Infinity SOC; SOAR depth limited |
| Recover | Absent | No backup or DR |

---

## ThreatCloud AI Architecture

ThreatCloud AI is the intelligence fabric underlying all Check Point products:

```
[150,000+ Connected Gateways]
         ↓ (telemetry)
   [ThreatCloud AI Cloud]
    90+ AI/ML Engines
    3B+ transactions/day
    1.5M+ malware signatures
    Real-time campaign correlation
         ↓ (prevention updates in milliseconds)
[All Gateways Block Attack Simultaneously]
```

**Key ThreatCloud capabilities:**
- **Autonomous intelligence sharing** — attack on one gateway triggers block on all within milliseconds
- **Campaign hunting** — partial IOCs correlated across customer telemetry to identify attack campaigns
- **Zero-day AI** — behavioral engines block unknown malware before signature exists
- **Phishing prevention** — collaborative URL reputation sharing across 150K+ gateways

---

## Horizon XPR: Extended Prevention & Response

XPR is Check Point's differentiation on top of XDR:
- **XDR:** Detect → Alert → Manual response
- **XPR:** Detect → Alert → **Automatic prevention action** (block at NGFW, quarantine endpoint, revoke credentials)

This aligns with Check Point's prevention philosophy: don't just alert that an attack happened — stop it automatically.

---

## Key Integrations

- **SIEM:** Splunk, Sentinel, QRadar (Check Point SmartEvent sends events to external SIEM)
- **SOAR:** Splunk SOAR, Palo Alto XSOAR, ServiceNow (Horizon Playbooks supplements)
- **Identity:** Entra ID, Okta for identity-aware policy in NGFW and Harmony Connect
- **Threat Intelligence:** VirusTotal, MISP, TAXII/STIX feeds

---

## Recent Developments (2023-2025)

- **Infinity AI Copilot** (2023) — GenAI assistant for SmartConsole configuration, policy review
- **Horizon XPR** — XDR with automated prevention (not just detection+alert)
- **Infinity Portal** — cloud management replacing on-prem SmartConsole for cloud-delivered products
- **CloudGuard CNAPP** — continued expansion; CIEM, shift-left AppSec, IaC scanning added
- **Harmony Connect expansion** — full SSE positioning with SWG + ZTNA + CASB + RBI

---

## Analyst Position

- **Gartner MQ:** Leader in Network Firewalls; Challenger in EPP, SSE; Niche/Visionary in CNAPP
- **Forrester Wave:** Strong Performer in Network Security, Zero Trust
- **NSS Labs / SE Labs:** Consistently highest block rates in independent testing
