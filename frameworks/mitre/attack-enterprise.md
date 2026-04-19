# MITRE ATT&CK Enterprise — Technology Countermeasure Mapping

**Version:** ATT&CK v15 (2024)  
**Source:** https://attack.mitre.org/  
**Scope:** Enterprise matrix (Windows, macOS, Linux, Cloud, Containers, SaaS)

---

## On This Page
- [Purpose](#purpose) — what this mapping enables
- [Tactic → Technology Mapping](#tactic--technology-mapping) — all 14 tactics with primary/supporting categories and key technique IDs
- [Coverage Heat Map by Technology Category](#coverage-heat-map-by-technology-category) — which categories cover which tactics
- [Detection Engineering: ATT&CK + CAR + Sigma](#detection-engineering-attck--car--sigma) — workflow from gap analysis to validated detection
- [References](#references)

## At a Glance
- **All 14 ATT&CK Enterprise tactics** mapped to primary and supporting technology categories with specific technique IDs (T-numbers)
- **Highest-coverage investments**: SIEM (12 tactics), EDR/XDR (8 tactics), Email Security (critical for Initial Access T1566), PAM (Credential Access T1003 + Privilege Escalation T1068)
- **T1566 Phishing** and **T1078 Valid Accounts** are the two most exploited initial access vectors — Email Security + MFA + IAM are non-negotiable first investments
- **T1486 Ransomware** and **T1562.001 Disable Security Tools** are the highest-impact techniques — Backup/Recovery and EDR tamper-protection address both
- **Detection engineering flow**: ATT&CK Navigator gap analysis → CAR analytics library → Sigma rules → CALDERA automated emulation → tune

## Summary

ATT&CK Enterprise is the most widely used adversary behaviour framework in the industry — a structured taxonomy of how real attackers operate, organised into 14 tactics (the strategic goal) and hundreds of specific techniques (the how). This document maps every tactic to the security technology categories that defend against it, making ATT&CK directly usable for technology selection, budget justification, and SOC gap analysis.

The mapping works in both directions. Starting from an ATT&CK tactic, you can identify which technology categories you need to cover it. Starting from a technology category, you can identify which tactics it defends against — useful for demonstrating coverage breadth to auditors or justifying procurement decisions to a CFO. The coverage heat map consolidates both views into a single table.

Two techniques deserve priority attention above all others: **T1566 Phishing** and **T1078 Valid Accounts** are the initial access vectors behind the majority of enterprise breaches. Any security programme that has not addressed these first is not correctly prioritised. On the impact side, **T1486** (ransomware) has a single reliable mitigation that no detection tool can replicate: immutable backup. These three technique investments — email security, MFA, and immutable backup — deliver more breach prevention per dollar than almost any other combination.

---

## Purpose

Maps all 14 ATT&CK Enterprise tactics to the security technology categories that defend against them. Enables:
- **SOC coverage gap analysis** — which tactics have weak or missing defensive coverage
- **Technology selection justification** — which products to buy and why, grounded in adversary behavior
- **Detection engineering roadmap** — prioritize rules and analytics by tactic frequency
- **Purple team scope** — which techniques to emulate per technology under test

---

## Tactic → Technology Mapping

### 1. Reconnaissance (TA0043)
*Attacker gathers information about the target before the attack.*

Key techniques: T1589 (gather victim identity info), T1590 (gather victim network info), T1591 (gather victim org info), T1596 (search open technical databases)

| Defense Layer | Technology Category | Implementation |
|--------------|-------------------|----------------|
| **Primary** | [Threat Intelligence](../../technologies/categories/identify/threat-intelligence.yaml) | Monitor dark web, paste sites, breach data for exposed employee/infra info |
| **Primary** | [Attack Surface Management](../../technologies/categories/identify/attack-surface-management.yaml) | Discover what is visible to external attackers before they do |
| **Supporting** | [DRPS](../../technologies/categories/identify/attack-surface-management.yaml) | Brand monitoring, domain squatting detection |

**Key insight:** Recon is largely pre-attack — defenses are intelligence-driven (know what attackers know about you).

---

### 2. Resource Development (TA0042)
*Attacker establishes infrastructure for the attack (domains, accounts, malware).*

Key techniques: T1583 (acquire infrastructure), T1584 (compromise infrastructure), T1585 (establish accounts), T1587 (develop capabilities)

| Defense Layer | Technology Category | Implementation |
|--------------|-------------------|----------------|
| **Primary** | [Threat Intelligence](../../technologies/categories/identify/threat-intelligence.yaml) | Track adversary infrastructure; identify C2 domains before use |
| **Supporting** | [Email Security](../../technologies/categories/protect/email-security.yaml) | DMARC/DKIM/SPF prevents domain impersonation |
| **Supporting** | [Attack Surface Management](../../technologies/categories/identify/attack-surface-management.yaml) | Detect lookalike domains targeting your brand |

---

### 3. Initial Access (TA0001)
*Attacker gains first foothold in the target environment.*

Key techniques: T1566 (phishing — #1 initial access vector), T1190 (exploit public-facing app), T1133 (external remote services — VPN/RDP), T1195 (supply chain compromise), T1199 (trusted relationship abuse)

| Defense Layer | Technology Category | Implementation |
|--------------|-------------------|----------------|
| **Primary** | [Email Security](../../technologies/categories/protect/email-security.yaml) | Anti-phishing, URL rewriting, attachment sandboxing |
| **Primary** | [WAF/API Security](../../technologies/categories/protect/waf-api-security.yaml) | Block exploitation of public-facing web apps |
| **Primary** | [ZTNA/SSE/SASE](../../technologies/categories/protect/ztna-sse-sase.yaml) | Replace VPN/RDP with broker-based access (no public RDP) |
| **Supporting** | [Vulnerability Management](../../technologies/categories/identify/vulnerability-management.yaml) | Patch public-facing systems before exploitation |
| **Supporting** | [Supply Chain Security](../../technologies/categories/emerging/supply-chain-security.yaml) | Verify software and hardware supply chain integrity |
| **Supporting** | [NGFW/IPS](../../technologies/categories/protect/ngfw-ips.yaml) | Block known exploit signatures at perimeter |

**Key insight:** T1566 Phishing accounts for ~30-40% of initial access in breach reports. Email security + security awareness training are the highest-ROI initial access controls.

---

### 4. Execution (TA0002)
*Attacker runs malicious code on the target system.*

Key techniques: T1059 (command/scripting interpreter — PowerShell, bash, Python), T1203 (exploitation for client execution), T1204 (user execution — malicious links/files), T1648 (serverless execution)

| Defense Layer | Technology Category | Implementation |
|--------------|-------------------|----------------|
| **Primary** | [Endpoint Protection](../../technologies/categories/protect/endpoint-protection.yaml) | NGAV blocks malicious execution; behavioral prevention |
| **Primary** | [XDR/EDR](../../technologies/categories/detect/xdr-edr.yaml) | Detects LOLBaS (living off the land) script execution |
| **Supporting** | [Application Security](../../technologies/categories/protect/application-security.yaml) | RASP prevents exploitation-triggered code execution |
| **Supporting** | [CNAPP](../../technologies/categories/protect/cnapp.yaml) | Container runtime prevention (serverless, ECS, Lambda) |

**Key insight:** T1059 (scripting interpreters) is the most frequent execution technique. EDR behavioral detection (not signature-based AV) is the primary control — PowerShell encoded commands, WMI execution, and process injection all require behavioral analysis.

---

### 5. Persistence (TA0003)
*Attacker maintains access across restarts, credential changes, or interruptions.*

Key techniques: T1098 (account manipulation), T1053 (scheduled task/job), T1133 (external remote services), T1543 (create/modify system process), T1078 (valid accounts)

| Defense Layer | Technology Category | Implementation |
|--------------|-------------------|----------------|
| **Primary** | [PAM](../../technologies/categories/protect/pam.yaml) | Detect new privileged account creation; credential rotation breaks persistence |
| **Primary** | [XDR/EDR](../../technologies/categories/detect/xdr-edr.yaml) | Alert on scheduled task creation, registry run key modification |
| **Primary** | [IGA](../../technologies/categories/identify/identity-governance.yaml) | Detect unauthorized account creation; access reviews find stale accounts |
| **Supporting** | [SIEM](../../technologies/categories/detect/siem.yaml) | Correlate persistence events across endpoints |
| **Supporting** | [Vulnerability Management](../../technologies/categories/identify/vulnerability-management.yaml) | Identify misconfigured services enabling persistence |

---

### 6. Privilege Escalation (TA0004)
*Attacker gains higher-level permissions (local admin → domain admin → root).*

Key techniques: T1548 (abuse elevation control — sudo/UAC bypass), T1134 (access token manipulation), T1068 (exploitation for privilege escalation), T1078.003 (local accounts)

| Defense Layer | Technology Category | Implementation |
|--------------|-------------------|----------------|
| **Primary** | [Endpoint Protection](../../technologies/categories/protect/endpoint-protection.yaml) | Block UAC bypass, token impersonation attempts |
| **Primary** | [XDR/EDR](../../technologies/categories/detect/xdr-edr.yaml) | Detect process injection, token manipulation at kernel level |
| **Primary** | [PAM](../../technologies/categories/protect/pam.yaml) | Least privilege enforcement — no standing local admin; JIT elevation |
| **Supporting** | [UEBA](../../technologies/categories/detect/ueba.yaml) | Baseline normal privilege patterns; alert on anomalous escalation |
| **Supporting** | [Vulnerability Management](../../technologies/categories/identify/vulnerability-management.yaml) | Patch local privilege escalation CVEs promptly |

**Key insight:** Removing local admin rights (via PAM endpoint privilege management — CyberArk EPM, BeyondTrust) eliminates most privilege escalation paths.

---

### 7. Defense Evasion (TA0005)
*Attacker avoids detection and security controls.*

Key techniques: T1070 (indicator removal — log clearing), T1027 (obfuscated files/info), T1562 (impair defenses — disable AV), T1055 (process injection), T1197 (BITS jobs), T1564 (hide artifacts)

| Defense Layer | Technology Category | Implementation |
|--------------|-------------------|----------------|
| **Primary** | [XDR/EDR](../../technologies/categories/detect/xdr-edr.yaml) | Behavioral detection (not signature-based) — process injection, hollowing |
| **Primary** | [SIEM](../../technologies/categories/detect/siem.yaml) | Alert on log clearing (T1070.001), security tool disabling |
| **Supporting** | [Endpoint Protection](../../technologies/categories/protect/endpoint-protection.yaml) | Tamper protection prevents AV/EDR disabling |
| **Supporting** | [CNAPP](../../technologies/categories/protect/cnapp.yaml) | Immutable container images prevent runtime modification |

**Key insight:** T1562.001 (Disable or Modify Tools) — attackers frequently try to kill EDR agents. Tamper protection in CrowdStrike, SentinelOne, and MDE prevents this. EDR with kernel-level protection is critical.

---

### 8. Credential Access (TA0006)
*Attacker steals credentials to enable lateral movement and persistence.*

Key techniques: T1110 (brute force), T1003 (OS credential dumping — LSASS/Mimikatz), T1555 (credentials from password stores), T1558 (Kerberoasting/AS-REP Roasting), T1606 (forge web credentials)

| Defense Layer | Technology Category | Implementation |
|--------------|-------------------|----------------|
| **Primary** | [IAM/SSO/MFA](../../technologies/categories/protect/iam-sso-mfa.yaml) | MFA prevents credential replay; FIDO2 is phishing-resistant |
| **Primary** | [PAM](../../technologies/categories/protect/pam.yaml) | Vault credentials — never expose to attacker; auto-rotation breaks stolen creds |
| **Primary** | [XDR/EDR](../../technologies/categories/detect/xdr-edr.yaml) | Detect LSASS access, Mimikatz patterns at process level |
| **Primary** | [UEBA](../../technologies/categories/detect/ueba.yaml) | Anomalous authentication patterns (impossible travel, off-hours access) |
| **Supporting** | [Deception](../../technologies/categories/detect/deception.yaml) | Honey credentials trigger alerts when used — zero false positives |

**Key insight:** Kerberoasting (T1558.003) is one of the most common AD attacks — targets service accounts with weak passwords. CyberArk, SentinelOne Singularity Identity, and Microsoft Defender for Identity all detect this pattern specifically.

---

### 9. Discovery (TA0007)
*Attacker maps the environment — users, systems, network, security tools.*

Key techniques: T1087 (account discovery), T1083 (file/directory discovery), T1482 (domain trust discovery), T1526 (cloud service discovery), T1018 (remote system discovery)

| Defense Layer | Technology Category | Implementation |
|--------------|-------------------|----------------|
| **Primary** | [NDR](../../technologies/categories/detect/ndr.yaml) | Detect network scanning patterns — port scans, SMB enumeration |
| **Primary** | [Deception](../../technologies/categories/detect/deception.yaml) | Honey shares, fake accounts, fake systems — any enumeration access = alert |
| **Supporting** | [UEBA](../../technologies/categories/detect/ueba.yaml) | Baseline normal directory query volume; alert on mass enumeration |
| **Supporting** | [CNAPP](../../technologies/categories/protect/cnapp.yaml) | Cloud resource enumeration detection (GuardDuty, SCC) |

**Key insight:** Deception technology provides the highest-confidence detection for discovery — attackers enumerating fake accounts or accessing honey shares have already bypassed perimeter controls, and any interaction is malicious by definition.

---

### 10. Lateral Movement (TA0008)
*Attacker moves through the environment to reach target systems.*

Key techniques: T1550.002 (Pass-the-Hash), T1550.003 (Pass-the-Ticket), T1021 (remote services — RDP, SMB, WinRM, SSH), T1570 (lateral tool transfer)

| Defense Layer | Technology Category | Implementation |
|--------------|-------------------|----------------|
| **Primary** | [NDR](../../technologies/categories/detect/ndr.yaml) | Detect east-west lateral movement — SMB/RDP anomalies, new connections |
| **Primary** | [PAM](../../technologies/categories/protect/pam.yaml) | Vaulted credentials break Pass-the-Hash; JIT prevents standing lateral access |
| **Primary** | [NGFW/IPS](../../technologies/categories/protect/ngfw-ips.yaml) | Microsegmentation blocks lateral movement paths |
| **Supporting** | [XDR/EDR](../../technologies/categories/detect/xdr-edr.yaml) | Process-level detection of PsExec, WMI remote execution |
| **Supporting** | [ZTNA/SSE/SASE](../../technologies/categories/protect/ztna-sse-sase.yaml) | ZTA: users connect to apps, not networks — lateral movement eliminated |

**Key insight:** NDR is the primary detection tool for lateral movement — it sees east-west traffic that endpoints cannot. Combined with PAM (breaking credential reuse) and microsegmentation (blocking pathways), lateral movement becomes detectable and containable.

---

### 11. Collection (TA0009)
*Attacker gathers data of interest — staging before exfiltration.*

Key techniques: T1005 (data from local system), T1039 (data from network shared drive), T1114 (email collection), T1557 (adversary-in-the-middle), T1560 (archive collected data)

| Defense Layer | Technology Category | Implementation |
|--------------|-------------------|----------------|
| **Primary** | [DLP](../../technologies/categories/protect/dlp.yaml) | Detect large-scale data staging, unusual file copy volumes |
| **Primary** | [Email Security](../../technologies/categories/protect/email-security.yaml) | Block bulk email export (Exchange/O365 PowerShell abuse) |
| **Supporting** | [NDR](../../technologies/categories/detect/ndr.yaml) | Detect internal data staging (unusual SMB share access volumes) |
| **Supporting** | [UEBA](../../technologies/categories/detect/ueba.yaml) | Anomalous data access volume vs. user baseline |

---

### 12. Command & Control (TA0011)
*Attacker communicates with compromised systems.*

Key techniques: T1071 (application layer protocol — HTTP/S, DNS, SMTP), T1092 (communication via removable media), T1095 (non-application layer protocol), T1573 (encrypted channel), T1105 (ingress tool transfer)

| Defense Layer | Technology Category | Implementation |
|--------------|-------------------|----------------|
| **Primary** | [NDR](../../technologies/categories/detect/ndr.yaml) | Detect C2 beaconing patterns — regular intervals, small payloads, unusual DNS |
| **Primary** | [Threat Intelligence](../../technologies/categories/identify/threat-intelligence.yaml) | Block known C2 domains/IPs at DNS + firewall level |
| **Primary** | [NGFW/IPS](../../technologies/categories/protect/ngfw-ips.yaml) | Egress filtering + IPS signatures for C2 protocols |
| **Supporting** | [SIEM](../../technologies/categories/detect/siem.yaml) | Correlate DNS queries, HTTP beaconing patterns |
| **Supporting** | [ZTNA/SSE/SASE](../../technologies/categories/protect/ztna-sse-sase.yaml) | DNS-layer blocking (Umbrella, Zscaler DNS) stops C2 domain resolution |

**Key insight:** DNS-based C2 (T1071.004) is increasingly common — attackers tunnel C2 traffic over DNS queries. Zscaler/Umbrella DNS security and NDR with DNS inspection are the primary controls.

---

### 13. Exfiltration (TA0010)
*Attacker moves target data out of the organization.*

Key techniques: T1041 (exfil over C2 channel), T1048 (exfil over alternative protocol — FTP, SCP, RDP clipboard), T1567 (exfil over web service — Google Drive, Dropbox, GitHub), T1537 (exfil to cloud storage), T1020 (automated exfiltration)

| Defense Layer | Technology Category | Implementation |
|--------------|-------------------|----------------|
| **Primary** | [DLP](../../technologies/categories/protect/dlp.yaml) | Block data leaving via web upload, email, USB — last line of defense |
| **Primary** | [CASB](../../technologies/categories/protect/casb.yaml) | Block uploads to unsanctioned cloud storage (T1567) |
| **Primary** | [NDR](../../technologies/categories/detect/ndr.yaml) | Detect large outbound transfers, unusual protocol usage |
| **Supporting** | [NGFW/IPS](../../technologies/categories/protect/ngfw-ips.yaml) | Egress filtering to sanctioned destinations only |
| **Supporting** | [ZTNA/SSE/SASE](../../technologies/categories/protect/ztna-sse-sase.yaml) | All traffic via Zscaler/Prisma — inline DLP on all egress |

---

### 14. Impact (TA0040)
*Attacker disrupts operations, destroys data, or causes financial harm.*

Key techniques: T1486 (data encrypted for impact — ransomware), T1490 (inhibit system recovery), T1489 (service stop), T1531 (account access removal), T1485 (data destruction)

| Defense Layer | Technology Category | Implementation |
|--------------|-------------------|----------------|
| **Primary** | [Backup & Recovery](../../technologies/categories/recover/backup-recovery.yaml) | Immutable backups = ransomware recovery without paying |
| **Primary** | [XDR/EDR](../../technologies/categories/detect/xdr-edr.yaml) | Detect mass file encryption behavior; automated rollback (SentinelOne) |
| **Primary** | [BCP/DR](../../technologies/categories/recover/bcp-dr.yaml) | Tested DR plan enables recovery within RTO after destructive attack |
| **Supporting** | [PAM](../../technologies/categories/protect/pam.yaml) | Prevent lateral movement needed for enterprise-wide ransomware deployment |
| **Supporting** | [CNAPP](../../technologies/categories/protect/cnapp.yaml) | Prevent cloud resource deletion (S3 bucket, VM snapshot destruction) |

**Key insight:** T1490 (Inhibit System Recovery) — ransomware operators specifically target backup systems before deploying ransomware. Immutable backup (S3 Object Lock, Veeam Hardened Repository, Rubrik immutability) that cannot be deleted even by domain admin is the critical control.

---

## Coverage Heat Map by Technology Category

Which technology categories provide the broadest ATT&CK tactic coverage:

| Technology Category | Tactics Covered | Coverage Breadth |
|--------------------|-----------------|-----------------|
| XDR/EDR | Execution, Persistence, PrivEsc, DefEvasion, CredAccess, LateralMov, Impact | Very Broad (7) |
| SIEM | All tactics (via log correlation) | Broad (all 14, correlation depth) |
| NDR | Discovery, LateralMov, C2, Exfil, Collection | Broad (5, deep coverage) |
| PAM | Persistence, PrivEsc, CredAccess, LateralMov | Focused (4, deep) |
| IAM/SSO/MFA | CredAccess, Persistence, InitialAccess | Focused (3, high impact) |
| DLP | Collection, Exfil | Narrow (2, critical) |
| Deception | Discovery, LateralMov, CredAccess | Narrow (3, high fidelity) |
| Email Security | InitialAccess, Collection | Narrow (2, #1 vector) |
| NGFW/IPS | InitialAccess, LateralMov, C2, Exfil | Moderate (4) |
| ZTNA/SSE | InitialAccess, LateralMov, C2, Exfil | Moderate (4) |
| Threat Intelligence | Recon, ResourceDev, C2 | Narrow (3, proactive) |
| Backup/Recovery | Impact | Narrow (1, critical) |

---

## Detection Engineering: ATT&CK + CAR + Sigma

**Practical workflow for detection-rule development:**

1. **Prioritize tactics** with highest attack frequency (Initial Access, Execution, Persistence, CredAccess)
2. **Map techniques** using ATT&CK Navigator; identify gaps in existing SIEM/XDR rules
3. **Reference MITRE CAR** analytics for the specific techniques — CAR provides data sources needed and query templates
4. **Convert CAR to Sigma rules** for cross-SIEM portability (Sigma → SPL, KQL, YARA-L)
5. **Validate with CALDERA** — run the technique emulation and confirm detection fires
6. **Tune** — adjust thresholds, add exclusions, iterate

---

## References

- ATT&CK Enterprise matrix: https://attack.mitre.org/matrices/enterprise/
- ATT&CK Navigator: https://mitre-attack.github.io/attack-navigator/
- MITRE CAR: https://car.mitre.org/
- Sigma rules (open-source): https://github.com/SigmaHQ/sigma
- CALDERA: https://caldera.mitre.org/
- Verizon DBIR 2024 (ATT&CK technique frequency data): https://www.verizon.com/business/resources/reports/dbir/
