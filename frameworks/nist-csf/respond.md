# NIST CSF 2.0 — Respond (RS)

Takes action regarding a detected cybersecurity incident — containment, eradication, communication, and analysis.

## Purpose

Response determines whether an incident becomes a breach, a breach becomes a crisis. Respond answers: *What do we do when we detect an attack?* Speed, coordination, and automation are the key variables.

## Technology Categories

| Category | Description |
|----------|-------------|
| [SOAR](../../technologies/categories/respond/soar.yaml) | Automated playbook execution and tool orchestration |
| [IR Case Management](../../technologies/categories/respond/case-management.yaml) | Incident tracking, evidence management, stakeholder coordination |
| [DFIR](../../technologies/categories/respond/dfir.yaml) | Digital forensics, root cause analysis, legal evidence collection |

## Key Outcomes (NIST CSF 2.0 Categories)

- **RS.MA** — Incident Management: incidents contained and communicated
- **RS.AN** — Incident Analysis: forensic analysis to understand impact and root cause
- **RS.CO** — Incident Response Reporting & Communication
- **RS.MI** — Incident Mitigation: containment and eradication actions

## Vendor Architecture Coverage

**Strong:** Google Mandiant (IR services), Microsoft Sentinel SOAR, Palo Alto XSOAR, CrowdStrike (OverWatch/Complete MDR)  
**Partial:** IBM SOAR, ServiceNow SecOps, Splunk SOAR, Cisco XDR  
**Weak:** Zscaler (no native response tools), AWS (EventBridge automation only)

## Key Architecture Note: SOAR Consolidation

Standalone SOAR is effectively dead as an independent category. Splunk SOAR (Phantom), Google Chronicle SOAR (Siemplify), and Palo Alto XSOAR (Demisto) are all platform-embedded. New entrants Tines and Torq offer simpler, no-code automation for teams without dedicated SOAR engineers.

## MDR / Managed Response

Many organizations supplement internal Respond capabilities with **Managed Detection & Response (MDR)** services:
- CrowdStrike Falcon Complete
- Microsoft Defender Experts
- Google Mandiant MDR
- SentinelOne Vigilance
- Rapid7 MDR
