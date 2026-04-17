# Cisco Security Architecture (Cisco Security Reference Architecture)

**Version:** 2024  
**Source:** https://www.cisco.com/c/en/us/solutions/security/  
**Type:** Platform Reference Architecture

---

## Overview

Cisco's security architecture is built around **network-first security** — Cisco's foundational strength is the network (routers, switches, firewalls, SD-WAN), and security is layered on top via embedded intelligence and dedicated security products. Cisco XDR (launched 2023) is the unifying SOC platform, replacing the older SecureX integration layer.

The security portfolio spans six domains: Network Security, SASE/Zero Trust, Identity, Cloud Security, Email & Web, and SOC Operations. Cisco's key differentiators are **network telemetry at scale** (NetFlow, Encrypted Traffic Analytics), **Talos Threat Intelligence** (one of the largest commercial threat intelligence organizations, with visibility from 200+ Cisco products globally), and **deep SD-WAN integration** for branch security.

**Market position:** Leader in network security (NGFW market share), SASE (Gartner MQ), and email security (Secure Email Gateway). Lagging in cloud-native (CNAPP), EDR vs. CrowdStrike/Microsoft, and SIEM. Revenue: ~$3.8B security (FY2024).

---

## Architecture Domains

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CISCO SECURITY ARCHITECTURE                      │
├────────────────────┬─────────────────────┬──────────────────────────┤
│  NETWORK SECURITY  │  SASE / ZERO TRUST  │  IDENTITY & ACCESS       │
│  Firepower NGFW    │  Cisco Secure Access│  Duo Security (MFA)      │
│  Firepower IPS     │  (SSE)              │  Cisco ISE (NAC)         │
│  Secure Firewall   │  Umbrella (SWG/DNS) │  Cisco Identity Services │
│  (Appliance+Cloud) │  AnyConnect (VPN)   │                          │
├────────────────────┼─────────────────────┼──────────────────────────┤
│  CLOUD SECURITY    │  EMAIL & WEB        │  SOC OPERATIONS          │
│  Panoptica (CNAPP) │  Cisco Secure Email │  Cisco XDR               │
│  Multicloud Def.   │  (ESA/CES)          │  Cisco Splunk SIEM       │
│  AppDynamics       │  Umbrella (SWG)     │  Talos Threat Intel      │
└────────────────────┴─────────────────────┴──────────────────────────┘
```

---

## Platform Domains

### Domain 1: Network Security
| Product | Category | Notes |
|---------|----------|-------|
| Cisco Secure Firewall (Firepower) | NGFW | Industry's broadest NGFW appliance line; FTD OS + FMC management |
| Firepower IPS | IPS | NGIPS integrated into Secure Firewall; Snort 3 engine |
| Cisco Secure Firewall Cloud Native | Cloud NGFW | Container-based NGFW for Kubernetes/cloud environments |
| Cisco Catalyst Center (DNA Center) | Network Management | Intent-based network management; policy enforcement via SD-Access |
| Cisco TrustSec | Microsegmentation | SGT-based network segmentation via Catalyst switches |
| Cisco SD-WAN (Viptela) | SD-WAN | SD-WAN fabric integrated with Secure Firewall for branch security |
| Cisco Secure Network Analytics (Stealthwatch) | NDR | NetFlow-based network threat detection; Encrypted Traffic Analytics |
| Cisco Cyber Vision | OT/ICS | Passive OT/ICS asset discovery and threat detection |

### Domain 2: SASE & Zero Trust
| Product | Category | Notes |
|---------|----------|-------|
| Cisco Secure Access | SSE / SASE | Unified SSE: SWG + CASB + ZTNA + RBI + DLP (converged 2023) |
| Cisco Umbrella | SWG / DNS Security | DNS + cloud proxy; largest DNS resolver globally (2B+ queries/day) |
| Cisco Secure Access (ZTNA) | ZTNA | ZTA for private apps; successor to AnyConnect for ZTNA use cases |
| Cisco AnyConnect | VPN (legacy) | Legacy SSL VPN; being replaced by ZTNA/SSE for remote access |
| Cisco ThousandEyes | Digital Experience | Internet and cloud path monitoring; network performance visibility |

### Domain 3: Identity & Access
| Product | Category | Notes |
|---------|----------|-------|
| Cisco Duo Security | MFA / ZTNA | MFA platform (acquired 2018, $2.35B); trusted by 40,000+ orgs |
| Cisco Identity Services Engine (ISE) | NAC / Policy | Network access control; device profiling, posture, segmentation |
| Cisco Secure Workload (Tetration) | Microsegmentation | Workload-level microsegmentation with telemetry from the workload |

### Domain 4: Cloud & Application Security
| Product | Category | Notes |
|---------|----------|-------|
| Panoptica | CNAPP | Cloud-native app security (Orca Security-adjacent); CSPM + CWPP |
| Cisco Multicloud Defense (Valtix) | Cloud NGFW | Multi-cloud distributed NGFW (Valtix acquisition 2023) |
| AppDynamics | Application Performance | APM + security (acquired 2017 for $3.7B); business transaction monitoring |
| Cisco Secure Application | API Security | Runtime application security; RASP-adjacent |

### Domain 5: Email & Web Security
| Product | Category | Notes |
|---------|----------|-------|
| Cisco Secure Email Gateway (ESA) | Email Security | On-prem and cloud email gateway; Talos-powered threat detection |
| Cisco Secure Email Cloud (CES) | Email Security | Cloud-delivered email security; integrated with Umbrella |
| Cisco Umbrella SWG | SWG | Proxy-based web filtering + cloud app control |

### Domain 6: SOC Operations
| Product | Category | Notes |
|---------|----------|-------|
| Cisco XDR | XDR | Launched 2023; integrates Secure Endpoint, Secure Network Analytics, Umbrella, Email, Talos |
| Cisco Splunk (SIEM) | SIEM | Splunk acquired September 2023 ($28B); Cisco's enterprise SIEM play |
| Cisco Talos Intelligence | Threat Intelligence | One of world's largest commercial threat intel teams; 250+ researchers |
| Cisco Secure Endpoint | EDR / EPP | EDR with AMP (Advanced Malware Protection); Talos-powered |
| Cisco Vulnerability Management (Kenna) | Vulnerability Management | Risk-based VM (Kenna Security acquisition 2021) |

---

## The Splunk Acquisition Impact

Cisco's **$28B acquisition of Splunk** (September 2023) fundamentally changes Cisco's security architecture:
- **Splunk Enterprise Security** becomes Cisco's enterprise SIEM
- **Splunk SOAR (Phantom)** becomes Cisco's SOAR platform
- **Splunk observability** provides full-stack monitoring
- Cisco XDR + Splunk SIEM + Talos TI = end-to-end SOC platform

This positions Cisco as a direct competitor to Microsoft Sentinel + Defender XDR, and Google Chronicle + Mandiant. Integration is still in progress (2024-2025).

---

## NIST CSF 2.0 Mapping

| NIST Function | Cisco Products | Coverage |
|--------------|---------------|----------|
| **Govern** | Cisco Vulnerability Management (risk scoring), ISE policy management | Weak — no GRC platform |
| **Identify** | Cisco Vulnerability Management, Cyber Vision (OT), ThousandEyes (network assets) | Good for network/OT assets; weaker for cloud |
| **Protect** | Secure Firewall (NGFW), Duo (MFA), ISE (NAC), Secure Access (SSE/ZTNA), Secure Email | Very strong — network-centric protection |
| **Detect** | Cisco XDR, Secure Network Analytics (NDR), Secure Endpoint (EDR), Splunk SIEM, Talos | Strong — especially network telemetry; XDR maturing |
| **Respond** | Cisco XDR, Splunk SOAR, Talos IR (services) | Strong — Splunk acquisition fills SOAR/SIEM gap |
| **Recover** | No native recovery products | Absent — infrastructure recovery via partner ecosystem |

---

## Coverage Gaps

- **CNAPP:** Panoptica is early-stage; lags Wiz, Prisma Cloud, Defender for Cloud significantly.
- **PAM:** No native PAM product; relies on CyberArk, BeyondTrust partnerships.
- **SIEM Leadership:** Splunk is market-leading but integration with Cisco XDR still in progress.
- **Recovery:** No backup or DR products.
- **Identity Provider:** Duo is MFA; not a full IdP (Cisco relies on Okta, Entra, or Ping as IdP).

---

## Network Telemetry Advantage

Cisco's unique position: **network as the sensor.** With Cisco infrastructure in 95%+ of enterprise networks, Cisco can extract security signals from:
- **NetFlow/IPFIX** — layer 4 traffic metadata from all Cisco routers/switches
- **Encrypted Traffic Analytics (ETA)** — ML-based malware detection without decryption
- **TrustSec SGTs** — policy enforcement at the network layer for microsegmentation
- **Catalyst Center** — behavioral analytics on network access patterns

This telemetry richness is difficult for endpoint-first vendors (CrowdStrike, SentinelOne) to replicate on non-managed devices.

---

## Talos Threat Intelligence

Talos is Cisco's threat intelligence organization — one of the largest in the industry:
- 250+ researchers and analysts
- Telemetry from Cisco's 200+ security products worldwide
- 200B+ security events per day
- Snort rule signatures (open-source IDS/IPS engine originally from Sourcefire, acquired by Cisco)
- ClamAV (open-source antivirus engine)

Talos intelligence powers Secure Email, Umbrella, Secure Firewall IPS, XDR, and Secure Endpoint detection.

---

## References

- Cisco Security: https://www.cisco.com/c/en/us/solutions/security/
- Talos Intelligence: https://talosintelligence.com/
- Cisco XDR: https://www.cisco.com/c/en/us/products/security/xdr/
- Splunk integration roadmap: https://www.cisco.com/c/en/us/solutions/security/splunk.html
- Cisco ThousandEyes: https://www.thousandeyes.com/
