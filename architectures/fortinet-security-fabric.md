# Fortinet Security Fabric Architecture

**Version:** 2024  
**Source:** https://www.fortinet.com/solutions/enterprise-midsize-business/security-fabric  
**Type:** Platform Reference Architecture

---

## Overview

Fortinet Security Fabric is a broad, integrated security platform anchored by **FortiGate NGFW** as the cornerstone device. Unlike cloud-native or agent-first platforms, Fortinet's architecture is hardware-rooted: custom ASIC chips (NP7, SP5, NP6) power FortiGate, delivering hardware-accelerated threat inspection that can outperform software-only alternatives by 10-30x on throughput benchmarks.

The Fabric connects security elements across network, endpoint, cloud, and OT/ICS via a shared operating system (**FortiOS**), centralized management (**FortiManager/FortiAnalyzer**), and AI-driven threat intelligence subscription (**FortiGuard Labs**). The Fabric Open API ecosystem integrates 550+ partner products.

**Market position:** #1 or #2 NGFW shipments globally by unit volume (especially mid-market and branch), Leader in SD-WAN (Gartner MQ), Challenger/Niche in SSE. Revenue ~$5.3B (FY2024). Particularly strong in OT/ICS, education, and distributed enterprise (retail, branch-heavy).

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                   FORTINET SECURITY FABRIC                          │
│              (FortiOS as common operating system)                   │
├──────────────────┬──────────────────┬──────────────────┬────────────┤
│  NETWORK SEC.    │  SASE / ZTNA     │  SECURITY OPS    │  OT / ICS  │
│  FortiGate NGFW  │  FortiSASE       │  FortiSIEM       │  Rugged    │
│  FortiSwitch     │  FortiClient     │  FortiSOAR       │  FortiGate │
│  FortiAP (WLAN)  │  FortiNAC        │  FortiNDR        │  FortiNAC  │
│  FortiExtender   │  FortiAuthent.   │  FortiAnalyzer   │  OT Probes │
├──────────────────┼──────────────────┼──────────────────┼────────────┤
│  ENDPOINT        │  CLOUD SECURITY  │  MGMT & FABRIC   │            │
│  FortiEDR        │  FortiCWP (CSPM) │  FortiManager    │            │
│  FortiClient EPP │  Lacework (CNAPP)│  FortiCloud      │            │
│  FortiIsolator   │  FortiCASB       │  FortiTrust      │            │
└──────────────────┴──────────────────┴──────────────────┴────────────┘
                              ↑
              FortiGuard Labs — AI Threat Intelligence
          (100B+ daily events, 3M+ daily malware samples)
```

---

## Platform Domains

### Domain 1: Network Security
| Product | Category | Notes |
|---------|----------|-------|
| FortiGate NGFW | NGFW / IPS | All form factors: desktop to 400Gbps chassis; custom NP7 ASIC |
| FortiSwitch | Network Access | Fabric-managed switching; 802.1X, VLAN, SGT integration |
| FortiAP | Wireless LAN | Wi-Fi 6/6E APs managed by FortiGate or FortiCloud |
| FortiExtender | LTE/5G WAN | Cellular WAN extension for branch/OT sites |
| FortiDDoS | DDoS Protection | Hardware-based volumetric DDoS mitigation |
| FortiProxy | Web Proxy / SWG | Explicit proxy for web filtering and SSL inspection |
| FortiMail | Email Security | On-prem and cloud email gateway; Fortinet's SEG |
| FortiDNS | DNS Security | DNS filtering and recursive DNS security |

### Domain 2: SASE & Zero Trust
| Product | Category | Notes |
|---------|----------|-------|
| FortiSASE | SSE / SASE | Cloud-delivered SSE: SWG + CASB + ZTNA + RBI (SD-WAN integrated) |
| FortiClient | ZTNA / EPP Agent | Unified agent: ZTNA, VPN, AV, EDR, vulnerability scan, DLP |
| FortiAuthenticator | MFA / Certificate Mgmt | On-prem MFA, certificate authority, RADIUS/LDAP |
| FortiToken | OTP | Hardware and software OTP tokens (OATH-compliant) |
| FortiNAC | Network Access Control | Agentless and agent-based NAC; device profiling and remediation |
| FortiPAM | PAM | Privileged access management (launched 2022; growing) |

### Domain 3: Security Operations
| Product | Category | Notes |
|---------|----------|-------|
| FortiSIEM | SIEM / UEBA | SIEM with embedded UEBA; multi-tenant MSSP architecture |
| FortiSOAR | SOAR | Enterprise SOAR with 300+ connectors; acquired CYSIV (2020) |
| FortiNDR | NDR | Network detection and response; traffic analysis + ML |
| FortiDeceptor | Deception | Decoy assets; lure-based detection with automated response |
| FortiAnalyzer | Log Analytics | Centralized log storage + correlation for Fortinet devices |
| FortiMonitor | NPM / Infrastructure | Network performance monitoring + infrastructure telemetry |

### Domain 4: Endpoint Security
| Product | Category | Notes |
|---------|----------|-------|
| FortiEDR | EDR | Real-time threat hunting and response; acquired enSilo (2019) |
| FortiClient (EPP) | EPP / AV | Next-gen AV powered by FortiGuard AI |
| FortiIsolator | Remote Browser Isolation | Cloud browser isolation for risky web content |
| FortiSandbox | Sandbox | On-prem and cloud sandboxing for unknown files/URLs |

### Domain 5: Cloud & Application Security
| Product | Category | Notes |
|---------|----------|-------|
| Lacework | CNAPP | CNAPP platform (acquired August 2024; ~$200M vs. $8.9B peak valuation) |
| FortiCWP | CSPM | Cloud workload protection and posture management (older product, pre-Lacework) |
| FortiCASB | CASB | API-based CASB for SaaS visibility and control |
| FortiWeb | WAF | Web application firewall (hardware + cloud) |
| FortiADC | Application Delivery | L4-L7 load balancer + application security |
| FortiGSLB | DNS Load Balancing | Global server load balancing and DNS failover |

### Domain 6: OT / ICS Security
| Product | Category | Notes |
|---------|----------|-------|
| FortiGate Rugged | NGFW (OT) | Temperature-hardened, DIN-rail mount NGFW for industrial environments |
| FortiNAC OT | OT NAC | Passive OT device discovery; IEC 62443-aware profiling |
| Operational Technology Security Manager (OTSSM) | OT Security Mgmt | OT-aware security management and alerting |
| FortiGuard OT Signatures | IPS (OT protocols) | SCADA/ICS protocol inspection: Modbus, DNP3, IEC 61850 |

---

## FortiGuard Labs — Threat Intelligence
FortiGuard Labs is Fortinet's threat intelligence organization, powering all FortiGuard subscription services:
- **100B+ daily events** analyzed across global customer base
- **3M+ daily malware samples** processed
- **AI/ML models** for zero-day detection, botnet C2, and phishing
- **OT-specific signatures** for industrial control system protocols

Services delivered as subscription overlays to FortiGate and other products:
- AntiVirus (AV), Intrusion Prevention (IPS), Web Filtering, Anti-Spam
- Application Control, DNS Filtering, IoT Detection, OT Signatures
- Sandbox (FortiSandbox cloud), Credential Stuffing Defense

---

## NIST CSF 2.0 Mapping

| NIST Function | Fortinet Products | Coverage |
|--------------|------------------|----------|
| **Govern** | FortiManager (policy), FortiAnalyzer (compliance), FortiTrust (licensing) | Weak — policy management yes; GRC/risk framework absent |
| **Identify** | FortiNAC (asset discovery), FortiEDR (endpoint inventory), Lacework CSPM, FortiSIEM | Good for network/OT assets; maturing for cloud |
| **Protect** | FortiGate NGFW, FortiSASE, FortiClient ZTNA, FortiMail, FortiWeb, FortiPAM, FortiNAC | Very strong — widest hardware-backed protection surface |
| **Detect** | FortiNDR, FortiSIEM, FortiEDR, FortiDeceptor, FortiGuard AI | Good — Fabric integration strong; depth vs. CrowdStrike/Sentinel limited |
| **Respond** | FortiSOAR, FortiSIEM automated response, FortiDeceptor isolation | Partial — SOAR present but fewer integrations than Palo Alto XSOAR |
| **Recover** | No native recovery products | Absent — relies on Veeam, Commvault, or vendor backup |

---

## Coverage Gaps

- **SIEM Depth:** FortiSIEM is functional but lags Microsoft Sentinel, Splunk, and Chronicle in enterprise SOC depth and integrations.
- **EDR Leadership:** FortiEDR competes but trails CrowdStrike Falcon, MDE, and SentinelOne in Magic Quadrant position.
- **PAM:** FortiPAM is new and growing but not yet enterprise-grade vs. CyberArk/BeyondTrust.
- **Threat Intelligence Services:** No Mandiant/Talos-equivalent dedicated IR services team.
- **Cloud-Native:** Lacework acquisition helps CNAPP but integration and market position still developing.

---

## OT/ICS Differentiation

Fortinet is the strongest enterprise security vendor in OT/ICS security:
- Ruggedized hardware for factory floor, substations, and harsh environments
- Passive OT protocol inspection (no agent required in OT environments)
- IEC 62443 compliance mapping
- FortiNAC OT-aware device profiling (identifies PLCs, HMIs, engineering workstations)
- Deployed in power utilities, manufacturing, oil & gas, and transportation

This differentiates Fortinet significantly from CrowdStrike (agent-first, OT limited), Microsoft (Defender for IoT via Cyberx), and Palo Alto (IoT Security — cloud-based).

---

## References

- Fortinet Security Fabric: https://www.fortinet.com/solutions/enterprise-midsize-business/security-fabric
- FortiGuard Labs: https://www.fortiguard.com/
- OT Security: https://www.fortinet.com/solutions/industries/scada-industrial-control-systems
- Lacework: https://www.lacework.com/
