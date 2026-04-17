# Splunk (Cisco) — Vendor Profile

**Type:** Specialist Leader (SIEM / SOAR / Observability)  
**HQ:** San Francisco, CA, USA (Cisco acquisition closed September 2023)  
**Revenue:** ~$4.1B (FY2024, now part of Cisco)  
**Category:** [SIEM](../categories/detect/siem.yaml) | [SOAR](../categories/respond/soar.yaml)

---

## Overview

Splunk is the market-leading enterprise SIEM and the dominant log management platform. Founded in 2003 around machine data search ("Google for machine data"), Splunk became the default enterprise SIEM through its flexible SPL query language, vast app/connector ecosystem (2,400+ apps), and ability to handle high-volume log ingestion at scale.

Cisco acquired Splunk for $28B in September 2023 — the largest cybersecurity acquisition ever at time of close (surpassed by Google's pending Wiz acquisition). Splunk now operates as a standalone business unit within Cisco, with integration roadmaps connecting Cisco XDR, Talos threat intelligence, and network telemetry into the Splunk platform.

---

## Product Portfolio

| Product | Category | Notes |
|---------|----------|-------|
| Splunk Enterprise Security (ES) | SIEM | Enterprise SIEM; SPL query language; 2,400+ app ecosystem |
| Splunk SOAR (Phantom) | SOAR | Acquired as Phantom (2018); 300+ playbook integrations; Python-based |
| Splunk Cloud Platform | SIEM (SaaS) | Cloud-delivered Splunk; federated search across on-prem and cloud |
| Splunk Observability Cloud | APM / Monitoring | Full-stack observability: infrastructure, APM, RUM, synthetic |
| Splunk IT Service Intelligence (ITSI) | AIOps | Event correlation for IT operations; ML-based anomaly |
| Splunk UBA | UEBA | User and entity behavior analytics (now integrated into ES Premium) |
| Splunk Attack Analyzer | Malware Analysis | Sandboxing + automated analysis for alerts |
| Splunk Asset & Risk Intelligence | CAASM | Asset inventory and risk correlation within SIEM |
| Splunk Mission Control | SOAR/Case Mgmt | Unified SOC workflow management across ES + SOAR |

---

## Strengths

- **SIEM leadership** — Gartner MQ Leader 9 consecutive years; largest enterprise SIEM install base
- **SPL flexibility** — Splunk Processing Language is the most capable and widely learned SIEM query language; security analysts prefer Splunk
- **Ecosystem** — 2,400+ Splunkbase apps; Splunk Security Content (Detections as Code); community depth unmatched
- **SOAR** — Splunk SOAR (Phantom) is one of the most integrated SOAR platforms; 300+ playbook connectors
- **Hybrid deployment** — Splunk runs on-prem, cloud (AWS/Azure/GCP), or hybrid; most flexible deployment of any SIEM
- **Observability + security convergence** — Splunk Cloud Platform bridges IT ops and security teams on one platform
- **Cisco integration** — Talos TI, Cisco network telemetry, Cisco XDR correlating into Splunk = unique combined value post-acquisition

---

## Weaknesses

- **Cost** — most expensive SIEM at scale; $1,800-$2,200/GB/day is prohibitive for high-volume environments
- **Complexity** — Splunk admin and SPL expertise required; operational complexity vs. cloud-native SIEMs
- **Cloud-native competition** — Microsoft Sentinel (cheaper/cloud-native), Google Chronicle (flat-cost petabyte scale), AWS Security Lake gaining at the expense of Splunk
- **SOAR vs. XSOAR** — Palo Alto XSOAR leads in enterprise SOAR integrations and playbook depth
- **Acquisition uncertainty** — organizational changes post-Cisco acquisition; talent retention risk
- **Licensing model** — ingest-based pricing creates unpredictable costs; organizations limit logging to control cost (creates blind spots)

---

## Licensing Model

**Three models (pre-acquisition):**

| Model | Basis | Approx. Cost |
|-------|-------|--------------|
| Ingest-based | Per GB/day indexed | ~$1,800-$2,200/GB/day/year |
| Infrastructure-based | Per virtual CPU | ~$300-500/vCPU/year |
| Workload-based | Per peak workload DPUs | Newer model; varies |

**Splunk Cloud** adds SaaS delivery markup (~20-30% premium vs. self-hosted).

**Typical enterprise costs:**
- 100GB/day → ~$180-220K/year (ingest-based)
- 500GB/day → ~$900K-$1.1M/year
- 1TB/day → ~$1.8-2.2M/year

This is why Microsoft Sentinel (pay-per-GB-actual) and Chronicle (flat capacity) are winning deals at the high end.

---

## NIST CSF Coverage

| Function | Coverage | Notes |
|----------|----------|-------|
| Govern | Partial | Compliance reporting, ES Compliance Framework |
| Identify | Partial | Asset & Risk Intelligence; CAASM use case |
| Protect | Weak | SIEM is not a protection tool |
| Detect | Very Strong | Market-leading SIEM; detection rules ecosystem; UEBA via ES Premium |
| Respond | Very Strong | Splunk SOAR (Phantom) + Mission Control = leading automated response |
| Recover | Absent | No backup or DR |

---

## The SPL Advantage

Splunk Processing Language (SPL) is the de facto SIEM query language:
```spl
index=windows EventCode=4624 
| eval LogonType_Name=case(Logon_Type=2,"Interactive", Logon_Type=3,"Network", Logon_Type=10,"RemoteInteractive") 
| stats count by src_ip, user, LogonType_Name 
| where count > 10 
| sort -count
```

SPL's capabilities (joins, subsearches, machine learning, statistical functions) exceed KQL (Sentinel), YARA-L (Chronicle), and Sigma in flexibility. The downside: SPL expertise is a specialized skill; analysts must be trained.

**Sigma rules** — open-source detection rule format that can be converted to SPL, enabling sharing of community detections.

---

## Splunk Security Content

**Splunk Threat Research Team** maintains the Splunk Security Content library:
- 1,000+ detection rules mapped to MITRE ATT&CK
- All content open-source on GitHub (Splunk/security_content)
- Automated testing via Attack Range (Splunk's detection testing framework)
- ContentCTRL — cloud management of content updates for Splunk ES

This community content ecosystem gives Splunk a meaningful detection library advantage vs. newer SIEMs.

---

## Cisco + Splunk Integration Roadmap

| Integration | Status (2024-2025) |
|-------------|-------------------|
| Cisco Talos TI → Splunk ES | In progress; Talos alerts appearing in ES |
| Cisco XDR → Splunk SIEM | Bidirectional alert/case sync (2024 release) |
| Cisco network telemetry → Splunk | Native Cisco add-on for Splunk; enhanced post-acquisition |
| Cisco SecureX → Splunk Mission Control | Replaced by Cisco XDR integration |

---

## Recent Developments (2023-2025)

- **Cisco acquisition closes** (September 2023, $28B)
- **Splunk Edge Processor** — reduce data volume before ingest; filter noise at the edge
- **Splunk Mission Control** — unified SOC case management across ES and SOAR
- **Federated Search** — search across multiple Splunk deployments without centralizing data
- **AI/ML expansion** — Splunk AI (2024) adds anomaly detection and predictive analytics
- **Attack Analyzer** — automated malware analysis integrated into SOAR playbooks

---

## Analyst Position

- **Gartner MQ:** Leader in SIEM — 9+ consecutive years as Leader
- **Forrester Wave:** Leader in SOAR, Security Analytics
- **Peer Insights:** Customers Choice for SIEM multiple years
