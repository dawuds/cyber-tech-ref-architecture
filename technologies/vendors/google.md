# Google (Chronicle / Mandiant / Google Cloud Security) — Vendor Profile

**Type:** Platform Vendor (Hyperscaler + Security)  
**HQ:** Mountain View, CA, USA  
**Security Revenue:** ~$3B+ (FY2024, Google Cloud security segment)  
**Architecture Reference:** [Google Cloud Security Architecture](../../architectures/google-csa.md)

---

## Overview

Google's security portfolio spans two distinct but increasingly integrated lines: **Google Cloud security-native controls** (identity, infrastructure, posture management) and **Google Mandiant** (threat intelligence, IR services, Chronicle SecOps platform). The 2023 full integration of the $5.4B Mandiant acquisition transformed Google from a cloud security vendor into a full-spectrum security platform with the deepest threat intelligence in the industry.

Google's architecture is built on planetaryR-scale principles proven internally: BeyondCorp (zero trust without a VPN, invented at Google in 2010), BeyondProd (secure-by-default production workloads), and Chronicle's ability to ingest and correlate petabytes of security telemetry at flat cost.

---

## Product Portfolio

| Category | Product(s) | NIST Mapping |
|----------|-----------|--------------|
| SIEM | Chronicle SIEM | Detect |
| SOAR | Chronicle SOAR (Siemplify) | Respond |
| XDR / MDR | Mandiant MDR | Detect, Respond |
| Threat Intelligence | Mandiant Threat Intelligence | Detect |
| CTI / APT Research | Mandiant Advantage | Detect |
| DRPS | Mandiant Digital Threat Monitoring | Identify |
| DFIR | Mandiant Consulting | Respond |
| EASM | Mandiant Attack Surface Management | Identify |
| IAM | Cloud Identity / Google Workspace IAM | Protect |
| ZTNA | BeyondCorp Enterprise | Protect |
| App Proxy | Identity-Aware Proxy (IAP) | Protect |
| CNAPP | Security Command Center (SCC) | Identify, Protect |
| CSPM | SCC Premium + DSPM | Identify |
| WAF | Cloud Armor | Protect |
| DDoS | Cloud Armor (Shield Standard/Advanced) | Protect |
| DLP | Cloud DLP (Sensitive Data Protection) | Protect |
| Secrets | Secret Manager | Protect |
| Supply Chain | Binary Authorization | Protect |
| AI Security | Defender for AI / Model Armor | Protect |
| AI SOC | Security AI Workbench (Gemini) | Detect, Respond |

---

## Strengths

- **Mandiant threat intelligence** — deepest CTI in industry from 500+ IR engagements/year; 300+ adversary groups tracked
- **Chronicle SIEM** — flat-cost petabyte log ingestion; search at Google-scale; YARAl detection language
- **BeyondCorp** — invented Zero Trust; BeyondCorp Enterprise is production-proven at Google scale
- **AI integration** — Gemini/Sec-PaLM security models integrated across Chronicle, SCC, Mandiant
- **Cloud-native advantage** — SCC, IAP, Binary Authorization are deeply integrated with GCP infrastructure
- **VirusTotal** — largest public malware/URL intelligence community database

---

## Weaknesses

- **Endpoint security** — no native EDR/EPP; Chronicle can ingest CrowdStrike/MDE but Google competes with neither
- **Network security** — Cloud IDS/NGFW for GCP; no enterprise hardware NGFW; no SD-WAN
- **Email security** — Google Workspace Gmail has built-in security; no enterprise SEG vs. Proofpoint/Mimecast
- **PAM** — no native PAM product
- **OT/ICS** — no OT security products
- **GCP-centric** — SCC and most controls are GCP-native; multi-cloud support is partial
- **Chronicle SOAR maturity** — Siemplify (2022) integration still maturing vs. Palo Alto XSOAR

---

## Licensing Model

| Product | Model | Approx. Cost |
|---------|-------|--------------|
| Chronicle SIEM | Flat-rate per GB/month capacity tiers | ~$15-$30K/month for mid-enterprise |
| Chronicle SOAR | Per playbook execution or enterprise license | ~$100-$300K/year |
| Mandiant MDR | Capacity-based (endpoints + environment) | ~$150-$500K/year |
| Mandiant Threat Intelligence | Per seat + API access | ~$50-$200K/year |
| SCC Standard | Included with GCP | Free |
| SCC Premium | Per asset/month | ~$0.06/asset/month |
| BeyondCorp Enterprise | Per user/month | ~$6/user/month |
| Cloud Armor Advanced | Per policy + per GB | Variable, typically $3K-$30K/year |

---

## NIST CSF Coverage

| Function | Coverage | Notes |
|----------|----------|-------|
| Govern | Weak | SCC compliance dashboards; no GRC platform |
| Identify | Good (GCP) | SCC CSPM + Mandiant ASM; limited for on-prem/multi-cloud |
| Protect | Good (cloud-native) | BeyondCorp + Cloud Armor + VPC Controls + DLP; weak for endpoint/network |
| Detect | Very Strong | Chronicle scale + Mandiant Intel = unmatched threat detection capability |
| Respond | Strong | Mandiant MDR + SOAR + Mandiant Consulting IR team |
| Recover | Partial | GCP Backup/DR (infrastructure); no security-native recovery |

---

## The Mandiant Acquisition Value

The $5.4B acquisition (2022) brought:
1. **BreachView** — access to telemetry from real breach investigations (anonymized)
2. **Frontline Intelligence** — threat intel derived from hands-on IR, not just sensors
3. **Expert human analysts** — 600+ frontline security consultants
4. **Named adversary research** — APT tracking unmatched by any vendor except possibly Crowdstrike/NSA-derived intel

Google can validate Chronicle detections against Mandiant's real-world IR data — this is structurally difficult for pure-SaaS vendors to replicate.

---

## Key Integrations

- Chronicle ingests: CrowdStrike, MDE, Palo Alto, Zscaler, Okta, AWS CloudTrail, Azure Sentinel
- BeyondCorp integrates with: Okta, Ping, ADFS for identity; CrowdStrike/MDE for device posture
- SCC integrates with: AWS Security Hub, Azure Defender (multi-cloud findings)
- VirusTotal: open API + enterprise threat intel enrichment

---

## Recent Developments (2023-2025)

- **Gemini for Security** — Gemini 1.5 integrated into Chronicle, SCC, Mandiant (2024)
- **Security AI Workbench** — foundation for all Google AI security products
- **Model Armor** — LLM prompt injection and output filtering for AI workloads
- **Wiz acquisition** (announced June 2024, ~$23B) — *pending regulatory approval* — would add the leading CNAPP/CSPM to GCP security portfolio
- **Chronicle SOAR** — Siemplify integration completing (2023-2024)

---

## Analyst Position

- **Gartner MQ:** Leader in SIEM (Chronicle), Challenger in SSE
- **Forrester Wave:** Leader in Threat Intelligence, IaaS Platform Security
- **IDC:** Leader in cloud security
