# NIST CSF 2.0 — Detect (DE)

Enables timely discovery and analysis of cybersecurity events and anomalies that could indicate an attack is occurring or has occurred.

## Purpose

Detection is the race against time — the faster threats are identified, the lower the blast radius. Detect answers: *How do we know when something bad is happening?* Modern detection is continuous, AI-driven, and integrated across telemetry sources.

## Technology Categories

| Category | Description |
|----------|-------------|
| [SIEM](../../technologies/categories/detect/siem.yaml) | Telemetry aggregation, correlation, and alert generation |
| [XDR / EDR](../../technologies/categories/detect/xdr-edr.yaml) | Cross-domain and endpoint threat detection and investigation |
| [NDR](../../technologies/categories/detect/ndr.yaml) | Network traffic analysis and lateral movement detection |
| [UEBA](../../technologies/categories/detect/ueba.yaml) | Behavioral baselines for users and entities |
| [Deception](../../technologies/categories/detect/deception.yaml) | High-fidelity detection via decoy assets |

## Key Outcomes (NIST CSF 2.0 Categories)

- **DE.CM** — Continuous Monitoring: environment monitored for anomalies and indicators
- **DE.AE** — Adverse Event Analysis: data correlated and analyzed to understand attacks

## Vendor Architecture Coverage

**Strong:** Microsoft Sentinel (SIEM/XDR), Google Chronicle (SIEM/SOAR), CrowdStrike Falcon (XDR), Palo Alto Cortex (XDR)  
**Partial:** Zscaler (traffic anomalies within ZTE), AWS GuardDuty (cloud-native), Cisco XDR

## Architecture Trends

- **SIEM → XDR convergence:** XDR platforms are absorbing SIEM use cases; some organizations run both. Pure SIEM without XDR is declining in enterprise.
- **UEBA absorption:** Standalone UEBA largely absorbed into SIEM (Exabeam, Securonix) and XDR (Microsoft, CrowdStrike).
- **AI/ML-driven detection:** Human-written detection rules being supplemented by AI models (Google SecLM, CrowdStrike Charlotte AI, Microsoft Copilot for Security).
- **MITRE ATT&CK alignment:** Detection coverage mapped to ATT&CK techniques is now standard practice for SOC maturity assessment.
