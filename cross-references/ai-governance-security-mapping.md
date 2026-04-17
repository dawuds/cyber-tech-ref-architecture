# AI Governance → Cybersecurity Technology Mapping

**Source:** [AI-Governance repository](https://github.com/dawuds/AI-Governance) — `controls/framework-map.json`  
**Scope:** AI governance controls mapped to cybersecurity technology categories and NIST CSF functions

---

## Purpose

AI governance frameworks (EU AI Act, NIST AI RMF, ISO 42001) define requirements for responsible AI development and deployment. These requirements create **direct cybersecurity technology needs** — security tools must be deployed specifically to meet AI governance obligations. This mapping connects AI governance controls to the security technology categories in this reference architecture.

---

## AI Governance Frameworks Covered

| Framework | Jurisdiction | Status |
|-----------|-------------|--------|
| **NIST AI RMF** | USA | Voluntary; widely adopted as enterprise baseline |
| **EU AI Act** | European Union | Mandatory for high-risk AI systems; phased enforcement 2024-2026 |
| **ISO/IEC 42001** | International | AI Management System standard; certification available |
| **Malaysia NGAIGE** | Malaysia | National Guidelines on AI Governance and Ethics |

---

## AI Governance Control → Security Technology Mapping

### 1. AI Governance Structure
*NIST AI RMF: GOVERN-1.1, GOVERN-1.2 | EU AI Act: Art. 9, 17 | ISO 42001: 5.1-5.3*

**Cybersecurity technology need:** GRC platform to document AI governance framework, assign accountability, and track compliance.

**Technology category:** [GRC](../technologies/categories/govern/grc.yaml)  
**NIST CSF function:** Govern  
**Relevant products:** ServiceNow GRC, Archer, OneTrust AI Governance module

---

### 2. AI Policy Framework
*NIST AI RMF: GOVERN-1.1, GOVERN-1.3 | EU AI Act: Art. 9 | ISO 42001: A.2.2*

**Cybersecurity technology need:** Policy management system to create, version, and distribute AI acceptable use policies; security awareness training for AI-specific risks.

**Technology categories:** [Policy Management](../technologies/categories/govern/policy-management.yaml), [Security Awareness](../technologies/categories/govern/security-awareness.yaml)  
**NIST CSF function:** Govern  
**Relevant products:** Confluence/SharePoint (policy), KnowBe4 (AI-specific training content)

---

### 3. AI Risk Assessment
*NIST AI RMF: MAP-1.1, MAP-1.2 | EU AI Act: Art. 6, 7, 9 | ISO 42001: 6.1, 6.1.2*

**Cybersecurity technology need:** Risk management platform to conduct and document AI system risk assessments; attack surface management to identify AI API exposure.

**Technology categories:** [GRC](../technologies/categories/govern/grc.yaml), [Attack Surface Management](../technologies/categories/identify/attack-surface-management.yaml)  
**NIST CSF function:** Govern, Identify  
**Relevant products:** OneTrust, ServiceNow, Cortex Xpanse (API exposure), Mandiant ASM

---

### 4. AI Risk Classification
*NIST AI RMF: MAP-1.1, MAP-1.5 | EU AI Act: Art. 6, 7 | ISO 42001: 6.1.2*

**Cybersecurity technology need:** Asset management system to catalog AI systems with risk classification tags; GRC to manage EU AI Act high-risk system compliance obligations.

**Technology categories:** [Asset Management](../technologies/categories/identify/asset-management.yaml), [GRC](../technologies/categories/govern/grc.yaml)  
**NIST CSF function:** Govern, Identify

---

### 5. Data Quality Governance
*NIST AI RMF: MAP-2.1, MAP-2.2 | EU AI Act: Art. 10 | ISO 42001: A.7.2, A.7.3*

**Cybersecurity technology need:** Data classification and DLP to ensure training data quality and prevent sensitive data from entering AI training pipelines without governance.

**Technology categories:** [DLP](../technologies/categories/protect/dlp.yaml), [CNAPP](../technologies/categories/protect/cnapp.yaml) (data security posture)  
**NIST CSF function:** Protect  
**Relevant products:** Microsoft Purview (data governance), Varonis, BigID

---

### 6. Data Privacy Protection
*NIST AI RMF: MAP-2.3 | EU AI Act: Art. 10 | ISO 42001: A.7.4, A.8.4*

**Cybersecurity technology need:** DLP to prevent PII/sensitive data from being used as AI training data without consent; DSPM to discover sensitive data in AI training datasets.

**Technology categories:** [DLP](../technologies/categories/protect/dlp.yaml), [CNAPP/DSPM](../technologies/categories/protect/cnapp.yaml)  
**NIST CSF function:** Protect  
**Relevant products:** Wiz (DSPM), Varonis, Cyera, Microsoft Purview

---

### 7. Model Documentation
*NIST AI RMF: MAP-1.1, MAP-1.6 | EU AI Act: Art. 11, 13 | ISO 42001: A.5.3, A.6.2.4*

**Cybersecurity technology need:** Software asset management and CMDB to track AI models as software assets; supply chain security to verify model provenance.

**Technology categories:** [Asset Management](../technologies/categories/identify/asset-management.yaml), [Supply Chain Security](../technologies/categories/emerging/supply-chain-security.yaml)  
**NIST CSF function:** Identify

---

### 8. AI System Testing
*NIST AI RMF: MEASURE-1.1, MEASURE-2.1 | EU AI Act: Art. 9, 15 | ISO 42001: A.6.2.3*

**Cybersecurity technology need:** Application security testing (DAST/SAST) for AI systems; adversarial ML testing for robustness against adversarial inputs; AI red-teaming.

**Technology categories:** [Application Security](../technologies/categories/protect/application-security.yaml), [AI/LLM Security](../technologies/categories/emerging/ai-llm-security.yaml)  
**NIST CSF function:** Identify, Protect  
**Relevant products:** Giskard (AI testing), Microsoft PyRIT (AI red-teaming), Adversarial Robustness Toolbox

---

### 9. Deployment Validation
*NIST AI RMF: MANAGE-1.1 | EU AI Act: Art. 9 | ISO 42001: 8.1*

**Cybersecurity technology need:** CI/CD security gates to validate model deployment; container security for model serving infrastructure; CNAPP for AI workload posture.

**Technology categories:** [Application Security](../technologies/categories/protect/application-security.yaml), [CNAPP](../technologies/categories/protect/cnapp.yaml)  
**NIST CSF function:** Protect  
**Relevant products:** Wiz, Prisma Cloud, Snyk (pipeline gates)

---

### 10. AI Transparency & Disclosure
*NIST AI RMF: MAP-1.5, GOVERN-1.5 | EU AI Act: Art. 13, 50 | ISO 42001: A.4.3, A.4.4*

**Cybersecurity technology need:** Audit logging to record AI system decisions; GRC for disclosure management; model monitoring for explainability outputs.

**Technology categories:** [GRC](../technologies/categories/govern/grc.yaml), [SIEM](../technologies/categories/detect/siem.yaml)  
**NIST CSF function:** Govern, Detect

---

### 11. Human Oversight Mechanism
*NIST AI RMF: GOVERN-1.4, MANAGE-2.2 | EU AI Act: Art. 14 | ISO 42001: A.3.2*

**Cybersecurity technology need:** SOAR for AI-triggered security decisions (human review required before execution); ZTNA for controlling who can override AI decisions.

**Technology categories:** [SOAR](../technologies/categories/respond/soar.yaml), [ZTNA/SSE/SASE](../technologies/categories/protect/ztna-sse-sase.yaml)  
**NIST CSF function:** Respond

---

### 12. Bias Detection & Mitigation
*NIST AI RMF: MAP-2.3, MEASURE-2.6 | EU AI Act: Art. 10 | ISO 42001: A.7.5*

**Cybersecurity technology need:** Data governance tools for dataset auditing; GRC for bias risk documentation and remediation tracking.

**Technology categories:** [GRC](../technologies/categories/govern/grc.yaml)  
**NIST CSF function:** Govern, Identify

---

### 13. Security Testing for AI
*NIST AI RMF: MANAGE-2.3 | EU AI Act: Art. 15 | ISO 42001: A.8.2*

**Cybersecurity technology need:** AI-specific security testing — prompt injection testing, model extraction/inversion testing, adversarial input testing, LLM jailbreak detection.

**Technology categories:** [AI/LLM Security](../technologies/categories/emerging/ai-llm-security.yaml), [Application Security](../technologies/categories/protect/application-security.yaml)  
**NIST CSF function:** Identify, Protect  
**Relevant products:**
- **Prompt injection testing:** Garak (open-source LLM vulnerability scanner)
- **Red-teaming:** Microsoft PyRIT, Adversa AI
- **Runtime protection:** Lakera Guard, Prompt Security, Rebuff

---

### 14. Access Control for AI Systems
*NIST AI RMF: MANAGE-2.1 | EU AI Act: Art. 15 | ISO 42001: A.8.1*

**Cybersecurity technology need:** IAM with fine-grained controls for who can access AI models/APIs; PAM for administrative access to AI infrastructure; CIEM for cloud AI service permissions.

**Technology categories:** [IAM/SSO/MFA](../technologies/categories/protect/iam-sso-mfa.yaml), [PAM](../technologies/categories/protect/pam.yaml), [CIEM](../technologies/categories/identify/ciem.yaml)  
**NIST CSF function:** Protect  
**Relevant products:** Okta (API access governance), CyberArk (AI infra admin), Wiz/Tenable (cloud AI CIEM)

---

### 15. AI Incident Response
*NIST AI RMF: MANAGE-3.1, MANAGE-4.1 | EU AI Act: Art. 72 | ISO 42001: A.9.3*

**Cybersecurity technology need:** IR case management for AI-specific incidents (model compromise, data poisoning, adversarial attacks); SOAR playbooks for AI incident containment.

**Technology categories:** [IR Case Management](../technologies/categories/respond/case-management.yaml), [SOAR](../technologies/categories/respond/soar.yaml)  
**NIST CSF function:** Respond  
**Relevant products:** ServiceNow, Jira (case management), Palo Alto XSOAR (AI incident playbooks)

---

### 16. Continuous Monitoring of AI
*NIST AI RMF: MANAGE-3.2, MEASURE-1.3 | EU AI Act: Art. 72 | ISO 42001: A.9.1, A.9.2*

**Cybersecurity technology need:** Dedicated AI/LLM security monitoring for model drift, anomalous outputs, prompt injection attempts; SIEM integration for AI system events; AI-specific threat detection.

**Technology categories:** [AI/LLM Security](../technologies/categories/emerging/ai-llm-security.yaml), [SIEM](../technologies/categories/detect/siem.yaml), [XDR/EDR](../technologies/categories/detect/xdr-edr.yaml)  
**NIST CSF function:** Detect  
**Relevant products:**
- **LLM monitoring:** Lakera Guard, Protect AI LLM Guard, Microsoft Defender for AI
- **Model monitoring:** Arize AI, WhyLabs, Fiddler AI
- **SIEM integration:** Sentinel (Defender for AI), Chronicle

---

## AI/LLM Security Technology Category

The emerging [AI/LLM Security](../technologies/categories/emerging/ai-llm-security.yaml) category addresses AI governance technical requirements:

| Threat | Security Control | Products |
|--------|----------------|---------|
| Prompt injection | Runtime content filtering | Lakera Guard, Protect AI, Rebuff |
| Model extraction | API rate limiting + monitoring | Cloudflare AI Gateway, Azure APIM |
| Training data poisoning | Data quality governance + provenance | Great Expectations, DVC |
| Jailbreaking | Output filtering + safety classifiers | Anthropic Claude safety, OpenAI moderation |
| Model inversion/membership inference | Differential privacy + access controls | IBM Differential Privacy Library |
| Supply chain / model tampering | Model signing, SBOM for ML | Sigstore, ONNX model hashing |
| Shadow AI (unsanctioned LLM use) | CASB + SWG (Generative AI categorization) | Netskope, Zscaler ZIA, Microsoft Purview |

---

## NIST CSF 2.0 Coverage for AI Governance

| NIST Function | AI Governance Controls Addressed |
|--------------|----------------------------------|
| **Govern** | AI governance structure, policy framework, risk classification, accountability, audit |
| **Identify** | AI system inventory, risk assessment, model documentation, data quality assessment |
| **Protect** | Access control for AI, data privacy protection, deployment validation, security testing |
| **Detect** | Continuous monitoring, AI anomaly detection, audit logging |
| **Respond** | AI incident response, human oversight, SOAR playbooks |
| **Recover** | AI system recovery procedures (subset of general IR/DR) |

---

## References

- Source: [AI-Governance/controls/framework-map.json](https://github.com/dawuds/AI-Governance/blob/main/controls/framework-map.json)
- NIST AI RMF: https://www.nist.gov/system/files/documents/2023/01/26/AI-RMF-1.0.pdf
- EU AI Act: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689
- ISO/IEC 42001:2023: https://www.iso.org/standard/81230.html
- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
