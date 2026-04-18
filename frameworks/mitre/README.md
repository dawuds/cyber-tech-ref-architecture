# MITRE Security Frameworks — Overview

MITRE maintains a family of interconnected cybersecurity knowledge bases. Together they form a complete offensive/defensive intelligence stack — from how attackers operate (ATT&CK), to how defenders counter them (D3FEND), to how to verify detections work (CALDERA, CAR), to specialized domains (ATLAS for AI/ML, ENGAGE for deception).

## Framework Family

| Framework | Purpose | Use in Architecture |
|-----------|---------|-------------------|
| [ATT&CK Enterprise](attack-enterprise.md) | Adversary tactics and techniques knowledge base | Detection coverage mapping, SOC gap analysis |
| [D3FEND](d3fend-overview.md) | Defensive countermeasure knowledge graph | Technology category → defensive technique mapping |
| ENGAGE | Cyber deception framework | Deception technology playbooks |
| ATLAS | Adversarial ML/AI attack taxonomy | AI/LLM security category guidance |
| CAR | Cyber Analytics Repository — detection rules | SIEM/XDR detection engineering |
| CALDERA | Automated adversary emulation | Purple team, SOAR testing |
| MITRE Navigator | ATT&CK coverage heatmap tool | SOC coverage visualization |

## How These Frameworks Relate to This Architecture

```
MITRE ATT&CK (Adversary view)
        ↕  each technique has countermeasures
MITRE D3FEND (Defender view)
        ↕  defensive techniques map to products
Technology Categories (this repo)
        ↕  categories map to NIST CSF functions
NIST CSF 2.0 (Governance spine)
```

ATT&CK tells you **what attackers do**. D3FEND tells you **what defenses counter each technique**. This repo maps those defenses to **which product categories implement them**. NIST CSF provides **organizational structure** for accountability and governance.

## ATT&CK Technique → Technology Quick Reference

Most frequently exploited ATT&CK techniques and primary defensive technology:

| Technique | ID | Primary Defense Category |
|-----------|-----|--------------------------|
| Phishing | T1566 | Email Security |
| Valid Accounts | T1078 | IAM/SSO/MFA + UEBA |
| Exploit Public-Facing App | T1190 | WAF/API Security + VM |
| Credential Dumping | T1003 | EDR/XDR + PAM |
| Lateral Movement (Pass-the-Hash) | T1550 | PAM + NDR + UEBA |
| Data Encrypted for Impact (Ransomware) | T1486 | EDR/XDR + Backup/Recovery |
| Exfiltration over Web | T1041 | DLP + CASB + NDR |
| Command & Control (Beaconing) | T1071 | NDR + Threat Intelligence |
| Living off the Land (LOLBaS) | T1059 | EDR behavioral detection |
| Supply Chain Compromise | T1195 | Supply Chain Security + CNAPP |

## MITRE Coverage Assessment

Organizations use **MITRE ATT&CK Navigator** to visualize detection coverage. Each product in the stack provides coverage over specific techniques:

| Technology Category | ATT&CK Coverage Breadth | Coverage Type |
|--------------------|------------------------|---------------|
| XDR/EDR | Very broad (8-10 tactics) | Behavioral + signature detection |
| SIEM | Broad (correlates across all tactics) | Log-based correlation |
| NDR | Network tactics (Lateral, C2, Exfil) | Traffic analysis |
| Email Security | Initial Access (phishing) | Pre-delivery + attachment |
| IAM/SSO/MFA | Credential Access, Privilege Escalation | Authentication controls |
| PAM | Privilege Escalation, Lateral Movement | Privileged account controls |
| DLP | Collection, Exfiltration | Data movement |
| Deception | Discovery, Lateral Movement, C2 | High-fidelity alerts on decoy access |
| WAF/API Security | Initial Access (web exploits) | Request inspection |
| CNAPP | Execution, Persistence (cloud) | Cloud workload controls |

## References

- MITRE ATT&CK: https://attack.mitre.org/
- MITRE D3FEND: https://d3fend.mitre.org/
- MITRE ENGAGE: https://engage.mitre.org/
- MITRE ATLAS: https://atlas.mitre.org/
- MITRE CAR: https://car.mitre.org/
- MITRE CALDERA: https://caldera.mitre.org/
- ATT&CK Navigator: https://mitre-attack.github.io/attack-navigator/
