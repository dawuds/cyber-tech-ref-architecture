# MITRE D3FEND — Defensive Countermeasure Mapping

**Version:** D3FEND v1.0 (2023)  
**Source:** https://d3fend.mitre.org/  
**Relationship:** D3FEND is ATT&CK's counterpart — ATT&CK describes offensive techniques, D3FEND describes defensive techniques that counter them.

---

## On This Page
- [Overview](#overview) — what D3FEND is and how it differs from NIST CSF and ATT&CK
- [D3FEND Defensive Technique Categories](#d3fend-defensive-technique-categories) — Harden, Detect, Isolate, Deceive, Evict, Restore with technology mappings
- [D3FEND ↔ ATT&CK ↔ Technology Triangle](#d3fend--attck--technology-category-triangle) — technique-to-countermeasure-to-product mapping
- [D3FEND and Zero Trust Architecture](#d3fend-and-zero-trust-architecture) — how D3FEND categories map to ZTA principles
- [Using D3FEND for Security Program Design](#using-d3fend-for-security-program-design) — 5-step gap-to-product workflow
- [MITRE ENGAGE (Deception Framework)](#mitre-engage-deception-framework) — operationalising the Deceive category
- [MITRE ATLAS (Adversarial ML)](#mitre-atlas-adversarial-ml) — AI/ML-specific attack taxonomy
- [References](#references)

## At a Glance
- **D3FEND is technology-centric**: it describes what a defensive tool *does* to digital artifacts to prevent or detect an attack — the missing link between ATT&CK techniques and product selection
- **6 defensive categories**: Harden, Detect, Isolate, Deceive, Evict, Restore — map directly to NIST CSF Protect / Detect / Respond / Recover functions
- **5-step program design**: ATT&CK gap → D3FEND countermeasure → technology category → vendor selection → CALDERA validation
- **D3FEND and Zero Trust**: Harden (Credential Hardening = MFA) + Isolate (Network Isolation = microsegmentation) map 1:1 to core ZT principles
- **MITRE ATLAS** extends the framework to AI/ML attack surface: prompt injection → AI/LLM Security category; model poisoning → Supply Chain Security; training data exfiltration → DLP

## Summary

ATT&CK tells you what attackers do. D3FEND tells you what defenders should do about it. Without D3FEND, the gap between "we have an ATT&CK coverage gap in Credential Access" and "here is the specific technology purchase that closes it" requires manual expert knowledge to bridge. D3FEND formalises that bridge as a knowledge graph: for each ATT&CK offensive technique, D3FEND identifies the countermeasure technique, the digital artifact being protected, and the technology category that implements the countermeasure.

The most direct use of this document is the 5-step programme design workflow: identify an ATT&CK gap with Navigator, find the D3FEND countermeasure, map to the technology category, select a product, then validate with CALDERA emulation. This creates a traceable, auditable chain from "threat" to "product purchase" to "validated detection" — the kind of evidence that both regulators and CFOs find credible.

D3FEND also serves as the architectural bridge to Zero Trust. The Harden category maps directly to ZT's "verify explicitly" principle (Credential Hardening = MFA, Platform Hardening = device compliance). The Isolate category maps to "least privilege" and "assume breach" (Network Isolation = microsegmentation, Credential Isolation = PAM). Understanding D3FEND through the ZT lens makes security architecture decisions far more coherent — every control has both a threat-model justification (D3FEND) and an architecture justification (ZT).

---

## Overview

D3FEND (Detection, Denial, and Disruption Framework Empowering Network Defense) is a knowledge graph of cybersecurity countermeasures. Unlike NIST CSF (which is organizational) or ATT&CK (which is adversary-centric), D3FEND is **technology-centric** — it describes specific actions a defensive technology takes and links them to the attacks they counter.

**Structure:** D3FEND defines `Digital Artifacts` (things that exist in the environment), `Offensive Techniques` (ATT&CK), and `Defensive Techniques` (what defenders do to those artifacts to prevent or detect attack).

---

## D3FEND Defensive Technique Categories

### 1. Harden
*Reduce the attack surface and make the environment harder to exploit.*

| D3FEND Technique | Description | Technology Category |
|-----------------|-------------|---------------------|
| Application Configuration Hardening | Disable unnecessary features, secure defaults | [GRC](../../technologies/categories/govern/grc.yaml), Config management |
| Credential Hardening | Enforce strong passwords, MFA, certificate auth | [IAM/SSO/MFA](../../technologies/categories/protect/iam-sso-mfa.yaml) |
| Message Hardening | Email authentication (DMARC, SPF, DKIM) | [Email Security](../../technologies/categories/protect/email-security.yaml) |
| Platform Hardening | OS/firmware hardening, secure boot | [Endpoint Protection](../../technologies/categories/protect/endpoint-protection.yaml) |
| Network Traffic Filtering | NGFW policies, allow-lists | [NGFW/IPS](../../technologies/categories/protect/ngfw-ips.yaml) |
| Software Supply Chain Hardening | SBOM, dependency verification, image signing | [Supply Chain Security](../../technologies/categories/emerging/supply-chain-security.yaml) |
| Credential Encryption | Vault credentials; no plaintext secrets | [PAM](../../technologies/categories/protect/pam.yaml), [Secrets Management](../../technologies/categories/protect/secrets-management.yaml) |
| Segment Network | Isolate zones; restrict east-west | [NGFW/IPS](../../technologies/categories/protect/ngfw-ips.yaml), [ZTNA](../../technologies/categories/protect/ztna-sse-sase.yaml) |

### 2. Detect
*Identify adversary activity in progress.*

| D3FEND Technique | Description | Technology Category |
|-----------------|-------------|---------------------|
| File System Analysis | Detect malicious file creation/modification | [XDR/EDR](../../technologies/categories/detect/xdr-edr.yaml) |
| Network Traffic Analysis | Detect C2, lateral movement, exfil in traffic | [NDR](../../technologies/categories/detect/ndr.yaml) |
| Process Analysis | Detect malicious process behavior, injection | [XDR/EDR](../../technologies/categories/detect/xdr-edr.yaml) |
| User Behavioral Analysis | Detect anomalous user actions vs. baseline | [UEBA](../../technologies/categories/detect/ueba.yaml) |
| Identifier Analysis | Detect credential abuse, account enumeration | [SIEM](../../technologies/categories/detect/siem.yaml) |
| Platform Monitoring | Detect cloud API misuse, config drift | [CNAPP](../../technologies/categories/protect/cnapp.yaml) |
| Message Analysis | Detect phishing, BEC, malware attachments | [Email Security](../../technologies/categories/protect/email-security.yaml) |
| System Call Analysis | Detect kernel-level abuse, rootkits | [XDR/EDR](../../technologies/categories/detect/xdr-edr.yaml) |

### 3. Isolate
*Contain attacker activity to limit blast radius.*

| D3FEND Technique | Description | Technology Category |
|-----------------|-------------|---------------------|
| Network Isolation | Quarantine compromised systems, microsegment | [NGFW/IPS](../../technologies/categories/protect/ngfw-ips.yaml), [SOAR](../../technologies/categories/respond/soar.yaml) |
| Execution Isolation | Sandboxing, containerization of untrusted code | [Endpoint Protection](../../technologies/categories/protect/endpoint-protection.yaml) |
| Encrypted Tunnels | mTLS for workload-to-workload (prevents MITM) | Service mesh, [ZTNA](../../technologies/categories/protect/ztna-sse-sase.yaml) |
| Credential Isolation | Restrict credential scope; prevent reuse | [PAM](../../technologies/categories/protect/pam.yaml) |
| Application Isolation | Browser isolation (RBI) for risky web content | [ZTNA/SSE/SASE](../../technologies/categories/protect/ztna-sse-sase.yaml) |

### 4. Deceive
*Mislead the attacker to gain intelligence and delay/detect them.*

| D3FEND Technique | Description | Technology Category |
|-----------------|-------------|---------------------|
| Decoy Environment | Honeynets, fake systems attract attackers | [Deception Technology](../../technologies/categories/detect/deception.yaml) |
| Decoy Object | Honey files, honey credentials, honey tokens | [Deception Technology](../../technologies/categories/detect/deception.yaml) |
| Decoy User Credential | Fake accounts that trigger alert when used | [Deception Technology](../../technologies/categories/detect/deception.yaml) |
| Decoy Network Resource | Honey shares, fake DNS records | [Deception Technology](../../technologies/categories/detect/deception.yaml) |
| Biometric Authentication | High-assurance identity that can't be faked | [IAM/SSO/MFA](../../technologies/categories/protect/iam-sso-mfa.yaml) |

### 5. Evict
*Remove the attacker from the environment.*

| D3FEND Technique | Description | Technology Category |
|-----------------|-------------|---------------------|
| Credential Eviction | Rotate compromised credentials, revoke sessions | [PAM](../../technologies/categories/protect/pam.yaml), [IAM/SSO/MFA](../../technologies/categories/protect/iam-sso-mfa.yaml) |
| Process Eviction | Terminate malicious processes, isolate endpoint | [XDR/EDR](../../technologies/categories/detect/xdr-edr.yaml), [SOAR](../../technologies/categories/respond/soar.yaml) |
| File Eviction | Delete/quarantine malicious files | [Endpoint Protection](../../technologies/categories/protect/endpoint-protection.yaml) |
| Account Eviction | Disable/delete compromised accounts | [IGA](../../technologies/categories/identify/identity-governance.yaml), [SOAR](../../technologies/categories/respond/soar.yaml) |

### 6. Restore
*Recover systems and data to known-good state.*

| D3FEND Technique | Description | Technology Category |
|-----------------|-------------|---------------------|
| Backup Integrity Checking | Verify backup before restore | [Backup & Recovery](../../technologies/categories/recover/backup-recovery.yaml) |
| System Restore | Rollback to known-good state | [Backup & Recovery](../../technologies/categories/recover/backup-recovery.yaml) |
| Operational Continuity | Failover to alternate systems | [BCP/DR](../../technologies/categories/recover/bcp-dr.yaml) |
| Credential Rotation | Re-credential all accounts post-incident | [PAM](../../technologies/categories/protect/pam.yaml) |

---

## D3FEND ↔ ATT&CK ↔ Technology Category Triangle

```
ATT&CK Technique           D3FEND Countermeasure      Technology Category
─────────────────          ─────────────────────      ───────────────────
T1566 Phishing         →   Message Analysis        →   Email Security
T1003 Credential Dump  →   Credential Hardening    →   PAM + EDR
T1486 Ransomware       →   System Restore          →   Backup & Recovery
T1021 Remote Services  →   Network Isolation       →   NGFW + ZTNA
T1078 Valid Accounts   →   User Behavioral Analysis→   UEBA + IAM
T1190 Web Exploit      →   Network Traffic Filter  →   WAF/API Security
T1570 Lateral Tool     →   Network Traffic Analysis→   NDR
T1041 Exfil over C2    →   Outbound Traffic Filter →   DLP + CASB
T1195 Supply Chain     →   SW Supply Chain Harden  →   Supply Chain Security
```

---

## D3FEND and Zero Trust Architecture

D3FEND's Harden + Isolate categories map directly to Zero Trust principles:

| ZTA Principle | D3FEND Category | Technology |
|--------------|-----------------|-----------|
| Never trust, always verify | Credential Hardening, User Behavioral Analysis | IAM/MFA, UEBA |
| Least privilege access | Credential Isolation, Network Isolation | PAM, NGFW |
| Assume breach | Process Analysis, Network Traffic Analysis | EDR, NDR |
| Verify explicitly | Platform Monitoring, Identifier Analysis | CNAPP, SIEM |

---

## Using D3FEND for Security Program Design

**Step 1: ATT&CK Navigator assessment** — map current detections to ATT&CK techniques; identify gaps  
**Step 2: D3FEND mapping** — for each uncovered ATT&CK technique, find the D3FEND countermeasures  
**Step 3: Technology mapping** — find the technology category that implements each countermeasure  
**Step 4: Vendor selection** — select products within the category that best cover the countermeasure  
**Step 5: Validate** — run CALDERA emulation and verify the D3FEND countermeasure detects/blocks the ATT&CK technique  

---

## MITRE ENGAGE (Deception Framework)

MITRE ENGAGE extends D3FEND's "Deceive" category with operationalization guidance:

**ENGAGE Activities:**
- **Expose** — Observe adversary behavior in deception environment
- **Affect** — Manipulate adversary operations (waste their time with fake data)
- **Elicit** — Learn adversary TTPs from deception interactions

**Technology:** ENGAGE operationalizes the [Deception Technology](../../technologies/categories/detect/deception.yaml) category — Attivo Networks (SentinelOne), Illusive Networks (Armis), TrapX, Acalvio, OpenCanary (open-source).

---

## MITRE ATLAS (Adversarial ML)

ATLAS maps AI/ML-specific attack techniques — the "ATT&CK for AI":

| ATLAS Tactic | Example Technique | Countermeasure Category |
|-------------|------------------|------------------------|
| ML Attack Staging | Acquire public ML artifacts | [Supply Chain Security](../../technologies/categories/emerging/supply-chain-security.yaml) |
| ML Model Access | Craft adversarial data | [AI/LLM Security](../../technologies/categories/emerging/ai-llm-security.yaml) |
| Reconnaissance | Search model repositories | [Threat Intelligence](../../technologies/categories/identify/threat-intelligence.yaml) |
| Initial Access (LLM) | Prompt injection | [AI/LLM Security](../../technologies/categories/emerging/ai-llm-security.yaml) |
| Persistence (LLM) | Model backdoor via poisoning | [Supply Chain Security](../../technologies/categories/emerging/supply-chain-security.yaml) |
| Exfiltration (LLM) | Extract training data | [DLP](../../technologies/categories/protect/dlp.yaml), [AI/LLM Security](../../technologies/categories/emerging/ai-llm-security.yaml) |

---

## References

- D3FEND knowledge graph: https://d3fend.mitre.org/
- D3FEND ontology (OWL): https://github.com/mitre/d3fend-ontology
- MITRE ENGAGE: https://engage.mitre.org/
- MITRE ATLAS: https://atlas.mitre.org/
- MITRE CAR: https://car.mitre.org/
