# Fortinet — Vendor Profile

**Type:** Platform Vendor (Network-first)  
**HQ:** Sunnyvale, CA, USA  
**Security Revenue:** ~$5.3B (FY2024)  
**Architecture Reference:** [Fortinet Security Fabric](../../architectures/fortinet-security-fabric.md)

---

## Overview

Fortinet is the NGFW/network security vendor that built the broadest security platform outside of Microsoft and Palo Alto. The Security Fabric architecture is anchored by FortiGate — the world's most shipped NGFW by unit volume — and extends to SASE, endpoint, SOC, cloud, and OT/ICS. Fortinet's custom ASIC chips (NP7 network processor, SP5 security processor) deliver hardware-accelerated threat inspection at competitive throughputs.

Key market characteristics: dominant in mid-market and distributed enterprise (retail, education, healthcare, branch-heavy), particularly strong in OT/ICS where ruggedized hardware and passive protocol inspection matter.

---

## Product Portfolio

| Category | Product(s) | NIST Mapping |
|----------|-----------|--------------|
| NGFW | FortiGate (all form factors) | Protect |
| IPS | FortiGate IPS (integrated) | Protect |
| Email Security | FortiMail | Protect |
| WAF | FortiWeb | Protect |
| SSL Inspection | FortiGate + FortiProxy | Protect |
| DDoS | FortiDDoS | Protect |
| SD-WAN | FortiGate SD-WAN (integrated) | Protect |
| SASE / SSE | FortiSASE | Protect |
| ZTNA | FortiClient ZTNA | Protect |
| MFA | FortiAuthenticator + FortiToken | Protect |
| NAC | FortiNAC | Protect |
| PAM | FortiPAM | Protect |
| MDM | FortiClient (endpoint management) | Protect |
| EPP / AV | FortiClient EPP | Protect |
| EDR | FortiEDR | Detect |
| SIEM | FortiSIEM | Detect |
| SOAR | FortiSOAR | Respond |
| NDR | FortiNDR | Detect |
| Deception | FortiDeceptor | Detect |
| Log Analytics | FortiAnalyzer | Detect |
| CNAPP | Lacework (acquired 2024) | Identify, Protect |
| CSPM | FortiCWP | Identify |
| CASB | FortiCASB | Protect |
| Sandbox | FortiSandbox | Detect |
| OT/ICS | FortiGate Rugged + FortiNAC OT | Identify, Protect |
| Threat Intelligence | FortiGuard Labs | Detect |

---

## Strengths

- **NGFW volume leadership** — most shipped NGFW units globally; dominant in branch/campus/distributed enterprise
- **Security Fabric integration** — FortiOS as common OS, FortiManager/Analyzer as central pane; tight integration reduces console sprawl
- **FortiGuard Labs** — 100B+ daily events, strong threat signatures; OT-specific protocol signatures
- **OT/ICS depth** — ruggedized hardware + passive OT protocol inspection + IEC 62443 alignment = strongest enterprise OT security
- **SD-WAN integration** — FortiGate SD-WAN integrated into NGFW; no separate appliance; Gartner MQ Leader in SD-WAN
- **TCO** — custom ASIC hardware often provides better throughput/$ vs. software-only alternatives
- **SASE breadth** — FortiSASE provides full SSE from cloud + FortiGate SD-WAN at the branch = complete SASE story

---

## Weaknesses

- **SIEM depth** — FortiSIEM functional but lags Splunk, Sentinel, Chronicle in enterprise SOC features and integrations
- **EDR** — FortiEDR (enSilo) trails CrowdStrike, MDE, SentinelOne in Gartner EPP positioning
- **CNAPP** — Lacework (acquired August 2024) adds CNAPP but integration and market position still developing
- **Cloud-native** — architecture is hardware-rooted; cloud services are add-ons, not native
- **Threat intelligence services** — no Mandiant/Talos/Unit42-equivalent dedicated IR team
- **PAM** — FortiPAM is new; lacks maturity vs. CyberArk/BeyondTrust

---

## Licensing Model

Product-based licensing with FortiGuard subscription overlays.

| Product | Model | Approx. Annual Cost |
|---------|-------|---------------------|
| FortiGate 200F (mid-range) | Hardware + 1-year UTP bundle | ~$7K-$15K/year all-in |
| FortiGate VM | Virtual + subscriptions | ~$3K-$10K/year |
| FortiSASE | Per user/year | ~$70-120/user/year |
| FortiClient | Per endpoint/year (EMS + client) | ~$40-80/endpoint/year |
| FortiEDR | Per endpoint/year | ~$60-90/endpoint/year |
| FortiSIEM | Per device/year or EPS-based | ~$15-50/device/year |
| FortiSOAR | Per analyst seat or enterprise | ~$100-300K/year |
| FortiGuard subscriptions | Bundled per-appliance annually | ~30-50% of hardware cost/year |

**Fortinet UTP (Unified Threat Protection) bundle** packages most security subscriptions at a discount per FortiGate.

---

## NIST CSF Coverage

| Function | Coverage | Notes |
|----------|----------|-------|
| Govern | Weak | FortiManager policy management; no GRC/risk platform |
| Identify | Good | FortiNAC asset discovery, Lacework CSPM, FortiSIEM inventory |
| Protect | Very Strong | Widest hardware-backed coverage: NGFW + SASE + NAC + Email + WAF + OT |
| Detect | Good | FortiNDR + FortiSIEM + FortiEDR + FortiDeceptor + FortiGuard TI |
| Respond | Partial | FortiSOAR + FortiSIEM automated response; no MDR service |
| Recover | Absent | No backup or DR products |

---

## OT/ICS Differentiator

Fortinet's OT security is the most comprehensive among enterprise security vendors:

1. **FortiGate Rugged appliances** — temperature range: -40°C to +70°C; DIN-rail mount; IEC 61850-3/IEEE 1613 certified
2. **IEC 62443 alignment** — formal alignment to industrial cybersecurity standard
3. **OT protocol inspection** — Deep packet inspection for Modbus, DNP3, IEC 61850, BACnet, EtherNet/IP, PROFINET
4. **FortiNAC OT** — passive device discovery and profiling for PLCs, HMIs, engineering workstations
5. **Convergence** — same FortiOS and FortiManager manage both IT and OT environments; single console

See cross-reference: [IEC 62443 → NIST CSF mapping](../../cross-references/iec62443-nist-mapping.md)

---

## Lacework Acquisition (August 2024)

- **Price:** ~$200M (vs. $8.9B peak valuation in 2021 — ~97% markdown)
- **What Lacework provides:** CNAPP platform: CSPM + CWPP + CIEM + vulnerability scanning; strong composite score agent
- **Strategic rationale:** Fortinet needed a credible cloud-native security posture story to compete with Palo Alto Prisma/Wiz
- **Integration timeline:** Full Security Fabric integration expected 2025-2026

---

## Recent Developments (2023-2025)

- **Lacework acquisition** (August 2024) — CNAPP capability added
- **FortiSASE expansion** — SD-WAN + SSE convergence; SASE delivered from FortiGate branches + cloud PoPs
- **FortiAIOps** — AI-driven network and security operations
- **FortiPAM** — PAM product launched (2022), growing
- **FortiGuard AI** — LLM-enhanced threat analysis (2024)

---

## Analyst Position

- **Gartner MQ:** Leader in Network Firewalls, SD-WAN; Challenger in SSE, EPP
- **Forrester Wave:** Strong Performer in Network Security, Zero Trust Platform
- **IDC:** #1 in NGFW units shipped globally (mid-market + enterprise combined)
