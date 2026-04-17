# Cybersecurity Category Analysis

Deep-dive per category: purpose, core functions, vendor landscape, spend estimates, maturity, and market trends. Companion to [TECH-STACK.md](TECH-STACK.md).

> **Spend estimates:** Annual cost for enterprise ~5,000 employees / ~8,000–10,000 endpoints. Actual negotiated pricing typically 20–40% below list.  
> **Maturity scale:** Emerging → Growth → Maturing → Mature → Commoditizing

---

## GOVERN

### GRC — Governance, Risk & Compliance

**Purpose:** Central platform for managing security policies, risk registers, compliance programs, and audit evidence. Translates board-level risk appetite into operational controls and demonstrates compliance to regulators.

**Core Modules / Functions:**
- Policy library and lifecycle management (creation → approval → version control)
- Risk register and risk scoring (qualitative and quantitative)
- Control framework mapping (ISO 27001, NIST CSF, SOC 2, PCI-DSS, local regs)
- Evidence collection and attestation workflow
- Audit management (planning, fieldwork, findings, remediation tracking)
- Regulatory reporting and dashboard

**Key Vendors:**
Archer (RSA), ServiceNow GRC, MetricStream, OneTrust, LogicGate, IBM OpenPages, SAP GRC, Diligent HighBond, AuditBoard, Vanta, Drata, Hyperproof, Secureframe

**Gartner MQ:** No dedicated GRC MQ; covered in Integrated Risk Management (IRM) MQ — Archer, ServiceNow, MetricStream are Leaders

**Market Maturity:** Mature  
Established market segmented by tier: enterprise (Archer, ServiceNow, IBM), cloud-native/SMB (Vanta, Drata, Secureframe). Cloud-native compliance automation is the growth segment.

**Estimated Annual Spend:** $80K–$500K  
- Cloud-native (Vanta/Drata): $15K–$60K  
- Mid-enterprise (LogicGate): $50K–$150K  
- Enterprise (Archer, ServiceNow): $150K–$500K+

**Consolidation Signal:** Standalone; GRC is not being absorbed by security platform vendors (Microsoft, CrowdStrike, Palo Alto) — structural gap. OneTrust acquired Tugboat Logic 2021.

**2025 Market Trend:** AI-assisted risk assessment and automated evidence collection (GRC vendors using LLMs to pre-populate controls based on configuration scans). Regulatory pressure (DORA, NIS2, SEC Cybersecurity Rules) driving enterprise investment.

---

### TPRM — Third-Party Risk Management

**Purpose:** Continuously assess and monitor security posture of vendors, suppliers, and partners. Answers: are our third parties introducing risk into our environment?

**Core Modules / Functions:**
- Vendor onboarding and tiering (criticality classification)
- Security questionnaire distribution and response management
- Outside-in security rating / continuous monitoring (attack surface scanning)
- Dark web monitoring for vendor credential exposure
- Contract and SLA tracking
- Risk remediation workflow and exception management

**Key Vendors:**
BitSight, SecurityScorecard, ProcessUnity (+ CyberGRX), Prevalent, RiskRecon (Mastercard), UpGuard, Panorays, Aravo, Venminder, OneTrust Vendor Risk

**Gartner MQ:** Covered under IRM; no standalone TPRM MQ. Gartner's IT Vendor Risk Management (VRM) guidance references BitSight and SecurityScorecard.

**Market Maturity:** Maturing  
Growing rapidly post-supply chain attacks (SolarWinds, MOVEit). Converging two models: questionnaire-based (Prevalent) and continuous monitoring (BitSight, SecurityScorecard). ProcessUnity acquisition of CyberGRX (2023) merged both approaches.

**Estimated Annual Spend:** $30K–$150K  
- Point tools (BitSight, SecurityScorecard): $20K–$80K  
- Full TPRM platforms (ProcessUnity, Prevalent): $50K–$150K

**Consolidation Signal:** Partially absorbing into GRC platforms (Archer TPRM module, ServiceNow Vendor Risk).

**2025 Market Trend:** Regulatory mandates (DORA supply chain requirements, NIS2 Article 21) driving mandatory third-party risk programs in financial services and critical infrastructure. AI-driven vendor scoring replacing static questionnaires.

---

### Security Awareness Training

**Purpose:** Reduces human-layer risk through phishing simulations, security education, and behavioral measurement. Addresses the fact that 68–90% of breaches involve a human element.

**Core Modules / Functions:**
- Phishing simulation engine (email, SMS, vishing)
- Training content library (videos, micro-learning, gamified)
- User risk scoring and behavioral analytics
- Automated training assignment based on failure/risk score
- Compliance tracking and reporting (HIPAA, PCI, ISO 27001 awareness)
- Manager/CISO dashboards and board reporting

**Key Vendors:**
KnowBe4, Proofpoint Security Awareness, SANS Security Awareness, Cofense, Mimecast Awareness, Hoxhunt, Terranova (Fortra), Ninjio

**Gartner MQ:** Security Awareness Computer-Based Training MQ — KnowBe4 is consistent Leader.

**Market Maturity:** Mature  
Market leader KnowBe4 dominates. Trend toward "human risk management" platforms that quantify individual risk scores rather than just track training completion.

**Estimated Annual Spend:** $15K–$60K  
- Per-user pricing: $15–$30/user/year  
- 5,000 employees: $75K–$150K (negotiated: $40K–$80K)

**Consolidation Signal:** Partial — email security vendors (Proofpoint, Mimecast) bundling awareness training. Microsoft Defender Attack Simulator provides basic phishing simulation for M365 customers at no added cost.

**2025 Market Trend:** AI-generated spear phishing simulations (hyper-personalized attacks); real-time nudges when users take risky actions vs. scheduled training campaigns.

---

### Policy Management

**Purpose:** Manages security policy creation, distribution, acknowledgment, and enforcement. Ensures employees know and comply with security requirements.

**Core Modules / Functions:**
- Policy authoring and approval workflow
- Version control and audit trail
- Employee acknowledgment tracking
- Regulatory framework mapping
- Exception request and approval management
- Integration with GRC for evidence collection

**Key Vendors:**
ServiceNow Policy & Compliance, Purview Compliance Manager (MS), OneTrust, Sprinto, Strike Graph, Scrut Automation, Hyperproof

**Market Maturity:** Mature (overlaps heavily with GRC)

**Estimated Annual Spend:** Often bundled with GRC — standalone: $10K–$50K

**Consolidation Signal:** Absorbing into GRC platforms. Cloud-native compliance automation (Vanta, Drata, Scrut) effectively converging policy + GRC + evidence for SMB/cloud-native orgs.

---

## IDENTIFY

### Asset Management / CAASM

**Purpose:** Continuous discovery and inventory of all IT assets — endpoints, servers, cloud workloads, identities, network devices, OT, and shadow IT. You cannot protect what you cannot see.

**Core Modules / Functions:**
- Agentless and agent-based asset discovery
- Asset classification and tagging (criticality, owner, data sensitivity)
- Software inventory (applications and versions)
- Relationship mapping (which assets talk to which)
- Control gap analysis (which assets have EDR, patch, etc.)
- Change detection and alerting

**Key Vendors:**
Axonius, JupiterOne, Noetic Cyber, runZero, ServiceNow CMDB, Tanium, Lansweeper, Microsoft Defender for Endpoint (managed assets), CrowdStrike Falcon Discover, Qualys CSAM

**Gartner MQ:** No dedicated MQ. Covered under Cyber Asset Attack Surface Management (CAASM).

**Market Maturity:** Growth → Maturing  
Axonius emerged as the leader of the CAASM category. Traditional CMDBs (ServiceNow) are too static for modern environments. Agent-less approaches (Axonius, JupiterOne, runZero) growing rapidly.

**Estimated Annual Spend:** $50K–$200K  
- runZero: ~$10K–$50K  
- Axonius (enterprise): $80K–$200K+

**Consolidation Signal:** Partially absorbing into EDR platforms (CrowdStrike Falcon Discover, Defender for Endpoint). However, multi-source correlation (Axonius connecting 800+ data sources) is difficult to replicate.

**2025 Market Trend:** Asset intelligence becoming the foundation for exposure management. Integration with VM and ASM platforms to create continuous exposure context.

---

### Vulnerability Management

**Purpose:** Continuously scans, prioritizes, and tracks vulnerabilities across endpoints, servers, cloud workloads, and applications. Enables risk-based patch prioritization based on exploitability, asset criticality, and compensating controls.

**Core Modules / Functions:**
- Authenticated and unauthenticated scanning
- CVE correlation and CVSS scoring
- Exploit intelligence integration (EPSS, KEV, threat intel)
- Asset criticality context for risk-based prioritization
- Patch management workflow integration
- Compliance scanning (CIS benchmarks, STIG)
- Cloud workload and container scanning
- Reporting and SLA tracking

**Key Vendors:**
Tenable One / Nessus, Qualys VMDR, Rapid7 InsightVM, Microsoft Defender VM, CrowdStrike Falcon Spotlight, Wiz (cloud), AWS Inspector, Snyk (developer/code)

**Gartner MQ:** Vulnerability Assessment MQ — Tenable and Qualys are perennial Leaders.

**Market Maturity:** Mature → Commoditizing (traditional scanning)  
Cloud-native vulnerability management (Wiz, Orca, Defender for Cloud) is Growth phase. Traditional scan-based VM is commoditizing — pricing pressure and feature convergence.

**Estimated Annual Spend:** $50K–$250K  
- Tenable.io at ~$35/asset/year × 8,000 assets = $280K (negotiated: $150K–$180K)  
- Qualys VMDR: comparable pricing  
- CrowdStrike Spotlight: included in higher Falcon tiers

**Consolidation Signal:** VM absorbing into XDR (CrowdStrike Spotlight), CNAPP (Wiz, Prisma Cloud), and exposure management platforms (Tenable One). Standalone VM declining in favor of integrated exposure platforms.

**2025 Market Trend:** Shift from CVE-centric VM to exposure management (CTEM methodology). Vendors bundling VM + ASM + threat intel into single exposure platform (Tenable One, Qualys Enterprise TruRisk).

---

### Attack Surface Management (ASM / EASM)

**Purpose:** Discovers and monitors internet-facing assets continuously from an attacker's perspective — including unknown, unmanaged, and shadow IT assets. Identifies exposed services, misconfigured assets, and vulnerabilities before attackers do.

**Core Modules / Functions:**
- Internet-wide asset discovery (domains, IPs, certificates, cloud assets)
- Shadow IT and subsidiary discovery
- Port and service exposure analysis
- Certificate expiration monitoring
- Technology fingerprinting (identifying software and versions)
- Risk scoring based on exposure and exploitability
- Dark web and breach data correlation

**Key Vendors:**
Palo Alto Cortex Xpanse, Microsoft Defender EASM, CrowdStrike Falcon Surface, Google Mandiant ASM, Tenable ASM, Censys, Cycognito, IBM Randori, Fortinet FortiRecon, NetSPI, Searchlight Cyber

**Gartner:** Covered under EASM market guide. No standalone MQ yet (expected 2025-2026).

**Market Maturity:** Growth → Maturing  
Category coined circa 2021. Rapid consolidation: Microsoft acquired RiskIQ (2021), Palo Alto acquired Expanse (2021), IBM acquired Randori (2022). Remaining pure-play: Censys, Cycognito.

**Estimated Annual Spend:** $50K–$150K  
Platform ASM (bundled with XDR/TI): often included in higher tiers  
Pure-play ASM: Censys ~$50K–$150K, Cycognito $80K–$200K

**Consolidation Signal:** Strong — rapidly absorbing into larger platforms. Palo Alto Xpanse feeds into Cortex. Microsoft EASM feeds into Sentinel. Likely to be a standard feature of XDR/exposure platforms within 2–3 years.

**2025 Market Trend:** Convergence of EASM + CAASM into unified attack surface intelligence. Active validation (confirming exposures are genuinely exploitable vs. theoretical). Supply chain surface discovery (subsidiaries, acquired companies).

---

### Threat Intelligence (CTI)

**Purpose:** Aggregates, analyzes, and operationalizes threat data — IOCs, TTPs, threat actor profiles, dark web intelligence — to inform defensive decisions and enable proactive detection.

**Core Modules / Functions:**
- Indicator of Compromise (IOC) ingestion and management (IPs, domains, hashes, URLs)
- Threat actor profiling (TTPs mapped to MITRE ATT&CK)
- Dark web and underground forum monitoring
- Strategic intelligence reporting (threat landscape, sector-specific)
- SIEM/SOAR/EDR integration for automated IOC matching
- Intelligence sharing (STIX/TAXII, ISACs, MISP)
- Malware analysis (sandbox, reverse engineering)

**Key Vendors:**
Recorded Future (Mastercard), Mandiant TI (Google), CrowdStrike Falcon Intelligence, Microsoft Defender TI, Cisco Talos, MISP (open-source), OpenCTI (open-source), Anomali, EclecticIQ, ThreatConnect, Intel 471, Flashpoint, VirusTotal (Google)

**Gartner MQ:** Security Threat Intelligence MQ — Recorded Future, Mandiant are Leaders.

**Market Maturity:** Maturing  
High-end CTI (Recorded Future, Mandiant) remains premium. Commoditization at IOC level — many SIEMs and XDR platforms bundle basic IOC feeds. Human intelligence (HUMINT) on threat actors remains the differentiator.

**Estimated Annual Spend:** $30K–$400K  
- Open-source (MISP + OpenCTI): minimal cost  
- Mid-tier (Anomali, EclecticIQ): $50K–$150K  
- Premium (Recorded Future, Mandiant TI): $150K–$400K+  
- Included in platform (CrowdStrike Falcon Intelligence): bundled in enterprise tiers

**Consolidation Signal:** Strong — CTI absorbing into SIEM, XDR, and SOAR platforms. Standalone CTI market shrinking as vendors bundle IOC feeds. Human intelligence and strategic reporting remain standalone.

**2025 Market Trend:** AI-powered intelligence synthesis (Recorded Future AI, Mandiant Threat Intelligence AI). Nation-state attribution improving. Supply chain threat intelligence (tracking software component risks) emerging.

---

### Identity Governance (IGA)

**Purpose:** Manages identity lifecycle — who should have access to what, and does what they have match what they need? Automates provisioning/deprovisioning, access certification, role mining, and SoD enforcement.

**Core Modules / Functions:**
- Joiner-Mover-Leaver automation (HR-driven provisioning)
- Access certification / recertification campaigns
- Role management and role mining (AI-assisted)
- Segregation of Duties (SoD) policy enforcement
- Access request and approval workflow
- Entitlement analytics and outlier detection
- Application connector library (AD, SAP, Salesforce, custom)

**Key Vendors:**
SailPoint, Saviynt, Omada, Microsoft Entra ID Governance, IBM Security Verify Governance, One Identity Manager, ConductorOne, Radiant Logic

**Gartner MQ:** Identity Governance and Administration MQ — SailPoint is consistent Leader.

**Market Maturity:** Mature  
Large enterprise market well-served. Mid-market underserved by complex legacy IGA tools (SailPoint, IBM) — creating opportunity for modern SaaS alternatives (Saviynt, ConductorOne).

**Estimated Annual Spend:** $150K–$600K  
- SailPoint: $200K–$600K+ (complex implementation)  
- Saviynt: $100K–$300K  
- Microsoft Entra ID Governance: included in Entra P2 / $6/user/month

**Consolidation Signal:** Moderate — Microsoft Entra ID Governance absorbing IGA for Microsoft shops. Deep identity analytics and complex SoD (financial services) require specialist tools.

**2025 Market Trend:** AI-driven access recommendations reducing manual review fatigue. Convergence of IGA + PAM (Saviynt, CyberArk). Non-human identity (service accounts, APIs) expanding IGA scope.

---

### CIEM — Cloud Infrastructure Entitlement Management

**Purpose:** Discovers and right-sizes excessive cloud permissions across AWS IAM, Azure RBAC, and GCP IAM. Identifies unused entitlements, overprivileged roles, and toxic permission combinations.

**Core Modules / Functions:**
- Multi-cloud permission discovery (AWS, Azure, GCP, OCI)
- Effective permission analysis (net permissions after policy inheritance)
- Unused permission detection and right-sizing recommendations
- Toxic combination detection (e.g., S3 full access + no MFA)
- JIT (Just-in-Time) access for cloud resources
- Anomalous access detection
- Compliance reporting (CIS benchmarks, NIST)

**Key Vendors:**
Microsoft Entra Permissions Management, Tenable Cloud Security (Ermetic), Sonrai Security, Wiz CIEM, Palo Alto Prisma Cloud CIEM, CrowdStrike Falcon CIEM, Orca Security, Sysdig

**Gartner:** Covered under CNAPP and IAM governance; no standalone MQ.

**Market Maturity:** Growth  
Standalone CIEM market rapidly consolidating into CNAPP. Ermetic → Tenable (2023), Sonrai remaining independent. Most organizations get CIEM through their CNAPP vendor.

**Estimated Annual Spend:** $30K–$120K standalone; typically included in CNAPP platform

**Consolidation Signal:** Strong — absorbing into CNAPP platforms. Standalone CIEM vendors (Sonrai) under pressure.

**2025 Market Trend:** Non-human identity (service accounts, CI/CD pipelines, Lambda functions) driving CIEM scope expansion. Cloud identity governance converging with IGA.

---

## PROTECT

### IAM / SSO / MFA

**Purpose:** Core identity platform — directory services, authentication (SSO, MFA, passwordless), and authorization. In Zero Trust, identity is the new perimeter: every access decision flows through IAM.

**Core Modules / Functions:**
- Directory services (user, group, device objects)
- Single Sign-On (SAML 2.0, OIDC, OAuth 2.0)
- Multi-Factor Authentication (TOTP, push, FIDO2/passkey, hardware key)
- Conditional Access policies (device compliance, location, risk score)
- B2B federation and external identity
- Customer Identity (CIAM) for public-facing apps
- Lifecycle management (HR sync, deprovisioning)
- Adaptive authentication (risk-based step-up)

**Key Vendors:**
Microsoft Entra ID, Okta, Google Cloud Identity, Ping Identity (Thales), Cisco Duo (MFA), JumpCloud, OneLogin (One Identity), Auth0 (Okta), HYPR (passwordless), Yubico

**Gartner MQ:** Access Management MQ — Microsoft and Okta are consistent Leaders.

**Market Maturity:** Mature  
Highly competitive. Microsoft Entra ID dominates Microsoft-centric environments. Okta leads independent market. FIDO2/passkey adoption is the major 2024-2025 shift.

**Estimated Annual Spend:** $120K–$400K  
- Microsoft Entra P2: ~$9/user/month = $540K/year for 5,000 users (negotiated significantly lower for M365 E5 bundle)  
- Okta: ~$8/user/month = $480K/year (Workforce Identity Cloud)  
- Cisco Duo: ~$9/user/month = $540K/year (Duo Business/Beyond)

**Consolidation Signal:** Stable standalone category. Vendors expanding scope: Okta adding governance, Microsoft adding Permissions Management, CrowdStrike adding ITDR.

**2025 Market Trend:** Passkey/FIDO2 mainstream adoption eliminating passwords. Identity threat detection (ITDR) converging with IAM. Non-human identity (API keys, service accounts) expanding IAM scope.

---

### PAM — Privileged Access Management

**Purpose:** Secures, controls, and monitors privileged accounts — admin credentials, service accounts, SSH keys, API tokens. Reduces blast radius from compromised admin accounts. Critical for ransomware protection.

**Core Modules / Functions:**
- Credential vaulting and password rotation
- Session recording and monitoring
- Just-in-Time (JIT) access (time-limited, approval-gated)
- Privileged session manager (proxy-based isolation)
- Least-privilege enforcement
- Privileged access workstations (PAW) policy
- Service account discovery and vaulting
- SIEM integration for audit trail

**Key Vendors:**
CyberArk, BeyondTrust, Delinea (Centrify + Thycotic), Microsoft Entra PIM, CrowdStrike Falcon Privileged Access, ARCON, HashiCorp Vault (DevOps PAM), Teleport (open-source), One Identity Safeguard

**Gartner MQ:** Privileged Access Management MQ — CyberArk is the consistent Leader.

**Market Maturity:** Mature  
CyberArk dominates large enterprises. Delinea (merger of Centrify and Thycotic) serves mid-market. HashiCorp Vault and Teleport serving DevOps/cloud-native PAM use cases.

**Estimated Annual Spend:** $80K–$400K  
- CyberArk Enterprise: typically $150K–$400K+ (implementation + license)  
- Delinea: $80K–$200K  
- Microsoft Entra PIM: included in Entra P2 (minimal incremental cost for Azure AD admin roles)

**Consolidation Signal:** Moderate. Microsoft Entra PIM handles Azure/M365 privileges. CrowdStrike expanding into identity threat detection. Core PAM for on-prem/hybrid remains specialist territory.

**2025 Market Trend:** JIT and just-enough-access (JEA) replacing permanent privileged accounts. DevOps PAM (machine identities, CI/CD pipelines, IaC) expanding scope beyond human accounts.

---

### NGFW / IPS

**Purpose:** Network security enforcement — stateful packet inspection, application identification (L7), IDS/IPS, TLS inspection, and threat prevention. Enforces network segmentation and prevents lateral movement.

**Core Modules / Functions:**
- Stateful firewall (L3/L4 policy enforcement)
- Application identification and control (App-ID)
- Intrusion Detection / Prevention System (IDS/IPS)
- TLS/SSL inspection (decrypt, inspect, re-encrypt)
- URL filtering and web categories
- Antivirus and anti-malware
- DNS security
- SD-WAN integration
- Threat intelligence integration

**Key Vendors:**
Palo Alto Networks NGFW, Fortinet FortiGate, Check Point Quantum, Cisco Secure Firewall (Firepower), Juniper SRX, AWS Network Firewall, Azure Firewall, Google Cloud IDS, Sophos XGS, Barracuda

**Gartner MQ:** Network Firewalls MQ — Palo Alto Networks and Fortinet consistently in Leaders quadrant.

**Market Maturity:** Mature → Commoditizing (physical appliance)  
Cloud-native NGFW (Azure Firewall, AWS Network Firewall) growing. Physical appliance refresh cycles slowing. SASE/SSE eating into traditional NGFW for remote access.

**Estimated Annual Spend:** $50K–$500K  
- Mid-enterprise physical NGFW (Fortinet, Palo Alto): $50K–$200K hardware + $30K–$100K/year licenses  
- Cloud NGFW (Azure/AWS): consumption-based, $20K–$100K/year

**Consolidation Signal:** Physical NGFW declining for perimeter; SSE/SASE replacing for remote workforce. Internal segmentation NGFW (East-West) stable.

**2025 Market Trend:** AI-powered threat prevention (Palo Alto Precision AI, Cisco Hypershield). Cloud-delivered NGFW (FWaaS) via SASE growing. Physical perimeter NGFW increasingly positioned for data center East-West segmentation only.

---

### ZTNA / SSE / SASE

**Purpose:** Cloud-delivered convergence of secure access (ZTNA) and security services (CASB, SWG, DLP) delivered from the cloud edge. Replaces VPN and consolidates network security inspection points.

**Core Modules / Functions:**
- **ZTNA:** Identity + device-aware application access (replaces VPN)
- **SWG (Secure Web Gateway):** URL filtering, malware inspection for internet traffic
- **CASB:** Cloud app visibility and control (sanctioned and shadow IT)
- **DLP:** Data exfiltration prevention across all traffic
- **Firewall-as-a-Service (FWaaS):** Cloud-native stateful inspection
- **SD-WAN:** Branch-to-cloud optimized routing (full SASE)
- **Remote Browser Isolation (RBI):** Rendering web content in cloud sandbox
- **Digital Experience Monitoring:** End-to-end user experience visibility

**Key Vendors:**
Zscaler (ZIA+ZPA), Palo Alto Prisma Access, Cloudflare One, Netskope, Microsoft Global Secure Access, Google BeyondCorp Enterprise, Cato Networks, Versa Networks, Cisco Umbrella/Secure Connect, iboss, Forcepoint ONE, Skyhigh Security

**Gartner MQ:** Security Service Edge (SSE) MQ — Netskope, Palo Alto, Zscaler, Skyhigh in Leaders. SASE MQ: Cato Networks, Palo Alto, Versa, Zscaler.

**Market Maturity:** Growth → Maturing (ZTNA/SSE); Early Growth (true SASE)  
Fastest-growing enterprise security category 2022-2025. ZTNA replacing VPN for remote access. Full SASE (SSE + SD-WAN) adoption lagging behind SSE.

**Estimated Annual Spend:** $200K–$800K  
- Zscaler Business/Transformation: $20–$60/user/year = $100K–$300K for 5,000 users  
- Palo Alto Prisma Access: comparable  
- Microsoft Global Secure Access (P1/P2 add-on): significantly lower if already in M365 E5

**Consolidation Signal:** Absorbing: CASB, SWG, legacy VPN, basic DLP being absorbed into SSE platforms.

**2025 Market Trend:** AI-driven traffic inspection. Network DLP moving to SSE layer. Browser security (Cloudflare, Talon Security) emerging as adjacent category. SASE and endpoint EDR integration deepening.

---

### CASB — Cloud Access Security Broker

**Purpose:** Visibility and control over cloud application usage — both sanctioned apps and shadow IT. Provides DLP, threat detection, and compliance enforcement for SaaS/IaaS environments.

**Core Modules / Functions:**
- Shadow IT discovery (cloud app usage visibility)
- SaaS security posture management (SSPM)
- Real-time inline inspection (forward proxy)
- API-based out-of-band inspection (for sanctioned apps)
- Cloud DLP (detecting sensitive data in cloud)
- Malware detection in cloud storage
- User behavior analytics in SaaS apps
- Compliance reporting (GDPR, HIPAA)

**Key Vendors:**
Microsoft Defender for Cloud Apps, Netskope, Zscaler CASB, Palo Alto Prisma Access CASB, Symantec CloudSOC (Broadcom), Skyhigh Security, Cisco Umbrella CASB

**Gartner MQ:** CASB MQ retired in 2022 — merged into SSE MQ.

**Market Maturity:** Mature → Commoditizing (standalone)  
Standalone CASB effectively dead. Functionality absorbed into SSE platforms. Organizations get CASB from their SSE vendor (Zscaler, Netskope, Microsoft, Palo Alto).

**Estimated Annual Spend:** Rarely purchased standalone; bundled into SSE ($0 incremental if using SSE).

**Consolidation Signal:** Complete absorption into SSE. Standalone CASB category eliminated from Gartner MQ 2022.

---

### DLP — Data Loss Prevention

**Purpose:** Detects and prevents unauthorized transfer or exfiltration of sensitive data (PII, PCI, PHI, IP) across endpoints, network, email, and cloud channels.

**Core Modules / Functions:**
- Data discovery and classification (content inspection, ML-based)
- Endpoint DLP (file copy, print, USB, clipboard)
- Network DLP (web, email, FTP inspection)
- Cloud DLP (SaaS/IaaS monitoring via CASB)
- Email DLP (attachment inspection, recipient analysis)
- Policy engine (regex, exact data match, ML classifiers)
- Incident management and workflow
- Encryption enforcement (rights management integration)

**Key Vendors:**
Microsoft Purview DLP, Palo Alto Enterprise DLP, Forcepoint DLP, Symantec DLP (Broadcom), Zscaler DLP, Netskope DLP, Google Cloud DLP, Amazon Macie, Digital Guardian (Fortra), Nightfall AI (API-native SaaS DLP)

**Gartner MQ:** Data Loss Prevention MQ (Enterprise) — Forcepoint and Microsoft are Leaders.

**Market Maturity:** Maturing  
Traditional network DLP (Symantec, Forcepoint) declining as traffic moves to cloud. Cloud-delivered DLP (SSE-embedded) is growth. AI-native SaaS DLP (Nightfall) emerging for collaboration tool DLP.

**Estimated Annual Spend:** $50K–$300K  
- Microsoft Purview DLP: included in M365 E5 compliance add-on (~$12/user/month)  
- Forcepoint DLP: $30K–$150K  
- Enterprise standalone DLP: $100K–$300K+

**Consolidation Signal:** Strong — absorbing into SSE (Zscaler, Netskope DLP), CASB, and email security platforms. Endpoint DLP increasingly part of XDR agents.

---

### Email Security

**Purpose:** Defends email against phishing, BEC (Business Email Compromise), malware delivery, spam, and account takeover. Email is the #1 initial access vector in most breach reports.

**Core Modules / Functions:**
- Anti-spam and anti-phishing filtering
- Malware scanning (attachments + links)
- URL rewriting and time-of-click protection
- Impersonation detection (display name spoofing, lookalike domains)
- BEC detection (AI-behavioral, no malware signature needed)
- Outbound DLP
- Email authentication (DMARC/DKIM/SPF enforcement)
- Phishing incident response (automated remediation from mailboxes)
- Email continuity and archiving

**Key Vendors:**
Proofpoint, Mimecast, Microsoft Defender for Office 365, Google Workspace (Advanced Protection), Abnormal Security (BEC specialist), Cisco Secure Email, Barracuda, Cofense, Avanan (Check Point), Agari (Fortra)

**Gartner MQ:** Email Security MQ — Microsoft and Proofpoint are Leaders.

**Market Maturity:** Mature  
Well-established category. Microsoft Defender for O365 (included in M365) displacing Proofpoint/Mimecast in some accounts. Abnormal Security growing rapidly in BEC detection (AI-native approach).

**Estimated Annual Spend:** $50K–$200K  
- Microsoft Defender for O365 Plan 2: ~$5/user/month = $300K/year (often bundled in M365 E5)  
- Proofpoint Email Protection + TAP: ~$20–$35/user/year = $100K–$175K  
- Abnormal Security: ~$25–$40/user/year = $125K–$200K

**Consolidation Signal:** Microsoft displacing standalone gateways for M365 shops. Specialist BEC vendors (Abnormal) maintaining share for advanced use cases.

**2025 Market Trend:** AI-powered BEC detection (no malware, pure behavioral); QR code phishing bypassing traditional filters; integration with SOAR for automated mailbox remediation.

---

### Endpoint Protection (EPP / NGAV)

**Purpose:** Prevents malware, ransomware, and exploitation on endpoints via AI/ML-based behavioral analysis. The prevention layer that stops known and unknown malware before execution.

**Core Modules / Functions:**
- Static analysis (ML on file attributes without execution)
- Behavioral analysis (runtime execution monitoring)
- Exploit prevention (memory protection, anti-injection)
- Ransomware-specific protection (rollback, shadow copy protection)
- Device control (USB, peripheral blocking)
- Application control / whitelisting
- Script and macro blocking (PowerShell, Office macros)
- Quarantine and automated remediation

**Key Vendors:**
CrowdStrike Falcon Prevent, Microsoft Defender Antivirus, SentinelOne Singularity, Palo Alto Cortex XDR (NGAV), Trellix Endpoint, Broadcom/Symantec Endpoint Security, ESET, Sophos Intercept X, Malwarebytes

**Gartner MQ:** Endpoint Protection Platforms MQ — CrowdStrike, SentinelOne, Microsoft in Leaders quadrant.

**Market Maturity:** Mature → Commoditizing  
EPP now table-stakes functionality — almost always bundled with EDR. Standalone NGAV market effectively absorbed into EDR/XDR platforms. Windows Defender included with Windows at no cost is displacing third-party AV for basic protection.

**Estimated Annual Spend:** Often bundled with EDR — see XDR/EDR pricing.

**Consolidation Signal:** Complete — standalone EPP absorbed into EDR/XDR. The EPP+EDR bundle is now the market standard.

---

### Application Security (SAST / DAST / SCA / IAST)

**Purpose:** Finds security vulnerabilities in application code and open-source dependencies throughout the SDLC. Shifts security left — finding issues at development time rather than in production.

**Core Modules / Functions:**
- **SAST:** Static code analysis for vulnerabilities (SQL injection, XSS, hardcoded credentials)
- **SCA:** Open-source dependency scanning for known CVEs and license risk
- **DAST:** Dynamic testing of running applications (black-box scanning)
- **IAST:** Runtime instrumentation for contextual vulnerability detection
- **Secret Scanning:** Credentials and API keys in code/git history
- **IaC Security:** Misconfiguration scanning (Terraform, CloudFormation, Kubernetes)
- **Container Security:** Image scanning for vulnerabilities
- **API Discovery:** Identifying undocumented APIs in code
- **IDE Integration:** Real-time developer feedback
- **CI/CD Pipeline Integration:** Gate checks in GitHub Actions, Jenkins, GitLab CI

**Key Vendors:**
Veracode, Checkmarx, Snyk, GitHub Advanced Security, GitLab Security, Semgrep, SonarQube (open-source), Black Duck (Synopsys), Invicti, Contrast Security, Palo Alto Prisma Cloud Code, Apiiro

**Gartner MQ:** Application Security Testing MQ — Checkmarx, Veracode, Synopsys in Leaders. Emerging: ASPM (Application Security Posture Management).

**Market Maturity:** Maturing  
Developer-first tools (Snyk, Semgrep, GitHub) growing rapidly. Traditional SAST vendors (Veracode, Checkmarx) modernizing to compete. ASPM emerging as coordination layer across all AppSec tools.

**Estimated Annual Spend:** $30K–$200K  
- Snyk: $25K–$100K (developer count-based)  
- GitHub Advanced Security: ~$49/developer/month  
- Checkmarx/Veracode: $80K–$200K+  
- SonarQube Community: free; Enterprise: $30K–$150K

**Consolidation Signal:** Moderate — consolidating toward developer platforms (GitHub, GitLab bundling security). ASPM emerging to correlate across tools. CNAPP vendors adding code security (Palo Alto Prisma Cloud Code, Wiz Code).

**2025 Market Trend:** AI-assisted code remediation (GitHub Copilot security fixes, Snyk DeepCode AI). ASPM as the coordination layer. Non-human identity / API secrets the fastest-growing finding type.

---

### WAF / API Security

**Purpose:** Protects web applications and APIs from OWASP Top 10 attacks (SQLi, XSS, CSRF), bot attacks, DDoS, and API abuse. API security extends protection to REST/GraphQL/gRPC endpoints including shadow API discovery.

**Core Modules / Functions:**
- OWASP Top 10 rule enforcement
- Rate limiting and DDoS mitigation
- Bot detection and management
- API discovery (finding undocumented/shadow APIs)
- API schema validation (enforce expected request/response format)
- API abuse detection (credential stuffing, scraping)
- SSL/TLS termination
- Custom rule engine
- IP reputation and geo-blocking

**Key Vendors:**
Cloudflare WAF, AWS WAF, Azure WAF, F5 Advanced WAF, Imperva, Akamai App & API Protector, Salt Security, Noname Security (Akamai, acquired 2024), Traceable AI, Wallarm

**Gartner MQ:** Web Application and API Protection (WAAP) MQ — Cloudflare, Imperva, F5, Akamai in Leaders.

**Market Maturity:** Mature (WAF); Growth (API security)  
Traditional WAF is mature and CDN-integrated. API security is a growth sub-category driven by API sprawl and shadow API risks.

**Estimated Annual Spend:** $30K–$200K  
- Cloudflare WAF (Teams/Enterprise): $20K–$100K  
- AWS WAF: $5/million requests + rules (typically $10K–$50K)  
- Salt Security / Traceable (API-focused): $80K–$200K

**Consolidation Signal:** WAF absorbing into CDN platforms (Cloudflare, Akamai, CloudFront). API security maturing but being absorbed into CNAPP (Palo Alto Prisma Cloud WAAS, Wiz).

---

### CNAPP — Cloud-Native Application Protection Platform

**Purpose:** Unified cloud security platform spanning the full cloud attack surface: code (IaC, SCA), CI/CD pipelines, deployed workload configuration (CSPM), running workload protection (CWPP), cloud entitlements (CIEM), and runtime detection.

**Core Modules / Functions:**
- **CSPM:** Cloud Security Posture Management — configuration compliance and misconfiguration detection
- **CWPP:** Cloud Workload Protection — container, VM, serverless runtime protection
- **CIEM:** Cloud entitlement management (over-privileged IAM)
- **DSPM:** Data Security Posture Management — finding sensitive data in cloud storage
- **IaC Security:** Scanning Terraform/CloudFormation before deployment
- **Container Image Scanning:** CVE detection in Docker/OCI images
- **Kubernetes Security Posture Management (KSPM)**
- **Runtime Threat Detection:** Behavioral anomalies in running workloads
- **API Security Posture:** Discovering APIs exposed by cloud workloads

**Key Vendors:**
Wiz, Palo Alto Prisma Cloud, Microsoft Defender for Cloud, Orca Security, Aqua Security, Sysdig, Fortinet Lacework, CrowdStrike Falcon Cloud Security, Google SCC, AWS Security Hub, Tenable Cloud Security, Cisco Panoptica

**Gartner MQ:** Cloud-Native Application Protection Platform MQ (2024) — Wiz, Palo Alto, Orca in Leaders.

**Market Maturity:** Growth → Maturing  
Fastest-growing cybersecurity category 2021-2025. Wiz disrupted the market with agentless approach. Market growing 25%+ annually. Google pending acquisition of Wiz ($32B, 2025) signals maturation.

**Estimated Annual Spend:** $100K–$500K  
- Wiz: $100K–$300K mid-enterprise; $300K–$500K+ large  
- Prisma Cloud (credits): $100K–$400K  
- Microsoft Defender for Cloud: included in Azure Defender plan (~$15/server/month)  
- AWS Security Hub: minimal cost ($0.001/finding) but finding volume drives cost

**Consolidation Signal:** Major consolidation underway. Lacework → Fortinet (2024), Wiz → Google (pending 2025). Platform vendors (MS, CrowdStrike, Palo Alto) competing directly.

**2025 Market Trend:** DSPM (Data Security Posture Management) adding sensitive data discovery layer. AI/LLM model and pipeline discovery added to CNAPP scope. Runtime eBPF-based detection gaining over agent approaches.

---

### MDM / UEM

**Purpose:** Manages and enforces security policies on mobile and desktop endpoints — enrollment, configuration profiles, compliance enforcement, remote wipe, and application management.

**Core Modules / Functions:**
- Device enrollment (zero-touch for corporate, BYOD enrollment)
- Configuration profile management (Wi-Fi, VPN, restrictions)
- Application management (deploy, update, remove apps)
- Compliance enforcement (block non-compliant from corporate resources)
- Remote wipe and lock (selective or full)
- OS patch management visibility
- Certificate lifecycle management
- Conditional access integration (with IAM/ZTNA)

**Key Vendors:**
Microsoft Intune, Jamf (Apple), Omnissa Workspace ONE (former VMware EUC), Google Endpoint Management, Kandji, Mosyle, Ivanti Neurons UEM, ManageEngine MDM+

**Gartner MQ:** Unified Endpoint Management MQ — Microsoft and Jamf (Apple) are Leaders.

**Market Maturity:** Mature  
Dominated by Microsoft Intune for Windows orgs and Jamf for Apple fleets. Workspace ONE (Omnissa) strong in mixed environments. MDM is often bundled — Microsoft Intune included in M365 E3/E5.

**Estimated Annual Spend:** $30K–$150K  
- Microsoft Intune: ~$8/device/month (or bundled in M365)  
- Jamf Pro: ~$10/device/month  
- Omnissa Workspace ONE: comparable

**Consolidation Signal:** Stable standalone category but deeply integrated with IAM conditional access. ZTNA making MDM compliance enforcement critical.

---

### OT / ICS / IoT Security

**Purpose:** Secures operational technology, industrial control systems (SCADA, PLCs, DCS), and IoT devices — environments where traditional IT security tools cannot operate. Passive monitoring is the dominant approach to avoid disrupting industrial processes.

**Core Modules / Functions:**
- Passive OT/IoT asset discovery (agentless, protocol-aware)
- OT protocol analysis (Modbus, DNP3, BACnet, EtherNet/IP, PROFINET)
- Baseline and anomaly detection
- Vulnerability management for ICS components
- Network segmentation visibility (IT/OT/DMZ zones)
- Threat detection (TTPs from MITRE ATT&CK for ICS)
- Remote access security for OT environments
- Incident response support for industrial incidents

**Key Vendors:**
Claroty, Dragos, Nozomi Networks, Microsoft Defender for IoT, Tenable OT Security, Armis, Forescout, Cisco Cyber Vision, Palo Alto Industrial OT Security

**Gartner MQ:** OT Security MQ (2024) — Claroty, Dragos, Nozomi in Leaders. Also: Cyber-Physical Systems Protection Platforms MQ.

**Market Maturity:** Growth → Maturing  
Critical infrastructure regulations (NERC CIP, IEC 62443, NACSA Act 854 in Malaysia) driving mandatory adoption. Market growing rapidly post-Colonial Pipeline, Oldsmar water plant attacks.

**Estimated Annual Spend:** $100K–$500K  
- Claroty: $80K–$300K depending on number of assets/sensors  
- Dragos: $150K–$500K+ (includes threat intelligence and IR retainer)  
- Nozomi Networks: $100K–$300K

**Consolidation Signal:** Moderate. IT/OT convergence accelerating. Microsoft Defender for IoT gaining enterprise OT share. Armis expanding from IoT to OT via acquisitions.

**2025 Market Trend:** IT/OT network convergence creating security visibility requirements. IEC 62443 compliance becoming contractual requirement for critical infrastructure. AI-based anomaly detection improving over rule-based approaches.

---

## DETECT

### SIEM — Security Information & Event Management

**Purpose:** Central nervous system of the SOC — aggregates, normalizes, and correlates security telemetry from all sources for threat detection, compliance reporting, and forensic investigation.

**Core Modules / Functions:**
- Log ingestion and normalization (syslog, API, agent-based)
- Event correlation (rule-based and ML-based)
- Alert generation and triage
- Threat hunting (ad-hoc query and saved searches)
- Compliance reporting (PCI DSS, ISO 27001, NIST)
- UEBA (increasingly embedded)
- Dashboards and metrics
- Long-term log retention and archival
- SOAR integration / built-in playbooks

**Key Vendors:**
Microsoft Sentinel, Google Chronicle SIEM, Splunk Enterprise Security (Cisco), Exabeam (+ LogRhythm merged 2024), Elastic SIEM, Securonix, Sumo Logic, FortiSIEM, IBM QRadar (on-prem; SaaS → Palo Alto 2024)

**Gartner MQ:** SIEM MQ 2025 — Microsoft Sentinel and Google Chronicle are Leaders.

**Market Maturity:** Mature → Consolidating  
Market undergoing significant consolidation. IBM QRadar SaaS → Palo Alto (2024), Splunk → Cisco (2024), Exabeam + LogRhythm merged (2024). Cloud-native SIEMs (Sentinel, Chronicle) displacing on-prem (Splunk, QRadar).

**Estimated Annual Spend:** $80K–$400K  
- Microsoft Sentinel: ~$2.46–$5.20/GB ingested; at 100GB/day = ~$90K–$190K/year  
- Splunk Enterprise Security: $50K–$200K + Splunk platform license (total $150K–$500K)  
- Google Chronicle: consumption-based; comparable to Sentinel  
- Exabeam/Securonix: $100K–$300K

**Consolidation Signal:** SIEM absorbing UEBA (standalone UEBA largely dead) and beginning to absorb SOAR. XDR platforms (Defender XDR, Falcon LogScale) competing with SIEM for SOC budget.

**2025 Market Trend:** AI Copilots for threat investigation (Copilot for Security, CrowdStrike Charlotte AI, Google SecLM). SIEM vs. XDR debate: orgs choosing platforms that bundle both. Detection-as-code (YARA-L, Sigma rules) becoming standard.

---

### XDR / EDR

**Purpose:** EDR provides deep endpoint telemetry for threat detection, investigation, and response. XDR extends across endpoint, identity, email, network, and cloud for correlated, cross-domain detection and automated response.

**Core Modules / Functions:**
- Process creation and execution monitoring
- File, registry, and network activity recording
- Behavioral detection engine (ML-based TTPs)
- Attack timeline reconstruction (process trees, causality graphs)
- Remote isolation (network disconnect, process kill)
- Threat hunting (query across historical telemetry)
- Cross-domain correlation (endpoint + identity + cloud + email)
- Managed threat hunting (human + AI overlay)
- Automated response playbooks

**Key Vendors:**
CrowdStrike Falcon Insight XDR, Microsoft Defender XDR, SentinelOne Singularity XDR, Palo Alto Cortex XDR, Google Chronicle + Mandiant, Cisco XDR, Trellix XDR, FortiEDR, ESET Inspect

**Gartner MQ:** EDR MQ and EPP MQ — SentinelOne and CrowdStrike consistently in Leaders.

**Market Maturity:** Mature → Consolidating  
One of the most competitive enterprise security markets. CrowdStrike, Microsoft, and SentinelOne dominate. Trellix (McAfee+FireEye) declining. Platform consolidation (XDR absorbing NDR, identity, cloud detection) accelerating.

**Estimated Annual Spend:** $150K–$600K  
- CrowdStrike Falcon Enterprise (EDR+XDR): $18–$35/endpoint/year = $144K–$280K (8,000 endpoints); negotiated = $100K–$200K  
- SentinelOne Singularity Complete: ~$160/endpoint/year = $1.28M list; negotiated = $600K–$800K  
- Microsoft Defender XDR: included in M365 E5 (significant bundling discount)

**Consolidation Signal:** XDR absorbing: NDR (telemetry integration), UEBA (behavioral baselines), deception (SentinelOne), identity threat detection (ITDR). Next: SIEM (Falcon LogScale, Defender XDR).

**2025 Market Trend:** Autonomous response (AI-driven action without analyst approval). Non-endpoint XDR telemetry (cloud workloads, network, SaaS) expanding. MDR (Managed Detection & Response) growing as XDR delivery model.

---

### NDR — Network Detection & Response

**Purpose:** Monitors network traffic for threats that bypass perimeter controls — east-west lateral movement, C2 communication, insider threats, and encrypted traffic anomalies. Provides network visibility that endpoint agents cannot see.

**Core Modules / Functions:**
- Network traffic capture and metadata analysis
- Behavioral baseline modeling (normal vs. anomalous)
- Encrypted traffic analysis (without decryption)
- Lateral movement detection
- C2 communication identification
- Protocol anomaly detection
- East-West (data center) traffic analysis
- Cloud traffic analysis (VPC flow logs, cloud-native)
- SIEM/XDR integration (feeding alerts and context)
- Threat hunting across network telemetry

**Key Vendors:**
ExtraHop Reveal(x), Darktrace (acquired by Thoma Bravo 2024), Vectra AI, Corelight, Cisco Secure Network Analytics (Stealthwatch), Palo Alto Cortex NDR, Gigamon, Awake Security (Arista), IronNet, Amazon GuardDuty (cloud NDR), Zeek (open-source), Suricata (open-source IDS/IPS)

**Gartner MQ:** First-ever NDR MQ published May 2025 — Vectra AI, Darktrace, ExtraHop, Corelight recognized as Leaders.

**Market Maturity:** Growth → Maturing  
Category formalized with inaugural Gartner MQ (May 2025). Major M&A: Darktrace acquired by Thoma Bravo ($5.3B, July 2024). Market growing at 9.6% CAGR to ~$5.8B by 2030.

**Estimated Annual Spend:** $80K–$300K  
- ExtraHop Reveal(x) 360: $80K–$200K  
- Darktrace: $100K–$300K (AI Analyst licensing)  
- Vectra AI: $100K–$250K  
- Corelight: $80K–$200K (sensor-based + cloud feeds)  
- Open-source (Zeek + ELK): $20K–$60K (operational cost)

**Consolidation Signal:** Moderate. XDR vendors integrating network telemetry (Falcon Network + NDR, Defender network protection). Standalone NDR maintains value for east-west visibility.

**2025 Market Trend:** Encrypted traffic analysis without decryption (JA3/JA4 fingerprinting, behavioral ML). Cloud NDR (VPC flow analysis, cloud-native) competing with on-prem sensors. Integration with SIEM and XDR for alert correlation.

---

### UEBA — User & Entity Behavior Analytics

**Purpose:** Establishes behavioral baselines for users and entities and detects anomalous deviations — insider threats, compromised accounts, and privilege escalation not caught by rule-based detection.

**Core Modules / Functions:**
- User behavioral profiling (peer group comparison, time-based baselines)
- Entity analytics (devices, applications, service accounts)
- Risk scoring (cumulative, time-decaying)
- Insider threat detection
- Compromised account detection (credential theft behavioral indicators)
- Data exfiltration behavioral indicators
- Anomalous access pattern detection

**Key Vendors:**
Exabeam (UEBA heritage), Microsoft Sentinel UEBA, Securonix, Splunk UBA, Gurucul, Palo Alto Cortex XDR (embedded), FortiInsight

**Gartner MQ:** UEBA MQ retired. Now covered within SIEM MQ.

**Market Maturity:** Mature → Commoditizing as standalone  
Standalone UEBA market effectively dead. Exabeam and Securonix maintain UEBA as core differentiator within their SIEM platforms. All major SIEM and XDR platforms now embed behavioral analytics.

**Estimated Annual Spend:** Rarely purchased standalone — bundled in SIEM or XDR costs.

**Consolidation Signal:** Complete absorption into SIEM and XDR. Standalone UEBA category eliminated from Gartner MQ.

**2025 Market Trend:** AI-driven behavioral analysis replacing rules. ITDR (Identity Threat Detection & Response) emerging as the next evolution — combining UEBA with identity-specific detection (CrowdStrike, SentinelOne).

---

### Deception Technology

**Purpose:** Plants fake assets (honeypots, honeytokens, decoy credentials) throughout the environment to detect adversaries during lateral movement. Provides high-fidelity, near-zero false-positive alerts.

**Core Modules / Functions:**
- Honeypot deployment (fake servers, services, endpoints)
- Honeytoken distribution (fake credentials, API keys, files)
- Active Directory decoys (fake AD accounts, SPNs)
- Network breadcrumbs (leading attackers to decoys)
- Alert generation on any decoy interaction
- Attacker profiling and TTP capture
- Integration with SIEM/SOAR for automated response

**Key Vendors:**
SentinelOne Singularity Ranger Deception (Attivo), Thinkst Canary, Illusive Networks (Proofpoint), Zscaler Deception, Acalvio, FortiDeceptor, Smokescreen

**Gartner MQ:** No MQ. Covered under Deception Technology market guide.

**Market Maturity:** Niche / Growth  
Small but growing market. Thinkst Canary is the simplest to deploy and widely adopted for its ease-of-use. SentinelOne Attivo focused on identity deception (AD decoys). Market consolidating into XDR and ZTNA platforms.

**Estimated Annual Spend:** $20K–$80K  
- Thinkst Canary: ~$7,500/year (10 canaries + tokens)  
- SentinelOne Ranger Deception: bundled in Singularity tiers  
- Enterprise deception platforms: $50K–$150K

**Consolidation Signal:** Absorbing into XDR (SentinelOne Attivo), SOAR, and ZTNA (Zscaler Deception). Thinkst Canary maintains strong standalone position due to simplicity.

---

## RESPOND

### SOAR — Security Orchestration, Automation & Response

**Purpose:** Automates security operations workflows — alert triage, enrichment, containment, and remediation — via playbooks. Reduces mean time to respond (MTTR) and analyst alert fatigue.

**Core Modules / Functions:**
- Playbook authoring and execution (visual and code-based)
- Alert ingestion and deduplication
- Automated enrichment (IP reputation, user context, threat intel lookup)
- Automated containment actions (block IP, isolate endpoint, disable user)
- Case management integration
- Human approval gates for high-risk actions
- Metrics tracking (MTTD, MTTR, case volume)
- Multi-tool orchestration (API-based integration fabric)

**Key Vendors:**
Microsoft Sentinel SOAR, Splunk SOAR (Phantom), Palo Alto Cortex XSOAR, Google Chronicle SOAR (Siemplify), IBM Security SOAR, ServiceNow SecOps, Tines, Torq, Swimlane, D3 Security

**Gartner MQ:** SOAR MQ retired 2022 — merged into Security Operations Platform coverage.

**Market Maturity:** Mature → Consolidating (standalone); Growth (embedded)  
Standalone SOAR effectively dead: Phantom → Splunk, Siemplify → Google, Demisto → Palo Alto, Resilient → IBM. New entrants Tines and Torq take no-code/low-code approach growing rapidly.

**Estimated Annual Spend:** Often bundled in SIEM (Sentinel SOAR = Logic Apps consumption costs); standalone: $50K–$200K  
- Splunk SOAR: $50K–$150K  
- Palo Alto XSOAR: $80K–$250K  
- Tines/Torq: $30K–$100K

**Consolidation Signal:** Near-complete absorption into SIEM and XDR platforms. Tines/Torq growing as developer-friendly automation alternatives.

**2025 Market Trend:** AI-generated playbooks (Copilot for Security generating SOAR playbooks). No-code automation (Tines, Torq) reducing playbook engineering overhead. Hyperautomation — automating full incident response lifecycle.

---

### IR Case Management

**Purpose:** Tracks and coordinates security incidents through full lifecycle — detection to closure. Manages evidence, communications, timelines, regulatory notifications, and lessons learned.

**Core Modules / Functions:**
- Incident creation and classification (severity, type, MITRE ATT&CK mapping)
- Task assignment and workflow
- Evidence and artifact management
- Timeline reconstruction
- Communication log (internal, stakeholder, regulatory)
- SLA tracking and escalation
- Lessons learned and post-incident review
- Regulatory notification tracking (GDPR 72hr, etc.)

**Key Vendors:**
ServiceNow Security Incident Response, Palo Alto Cortex XSOAR (case management), TheHive (open-source), IBM Security SOAR, Jira Service Management, PagerDuty, D3 Security, Atlassian Opsgenie

**Market Maturity:** Mature  
Most organizations adapt existing ITSM tools (ServiceNow, Jira) for IR. Security-specific case management often bundled with SOAR.

**Estimated Annual Spend:** Often bundled with SOAR or ITSM — standalone: $20K–$80K

---

### DFIR — Digital Forensics & Incident Response

**Purpose:** Investigates security incidents — collecting evidence, analyzing malware, reconstructing attack timelines, and supporting legal/regulatory proceedings and attribution.

**Core Modules / Functions:**
- Disk imaging and forensic acquisition
- Memory forensics (live memory analysis)
- Malware analysis (static and dynamic)
- Network forensics (packet capture analysis)
- Timeline reconstruction and event correlation
- Cloud forensics (cloud-native evidence collection)
- Mobile device forensics
- Legal chain-of-custody management
- Threat actor attribution

**Key Vendors:**
Google Mandiant (services), CrowdStrike Services (OverWatch/Complete), Cado Security (cloud DFIR), Magnet Forensics (AXIOM), Cellebrite (mobile), OpenText EnCase, Exterro FTK, Velociraptor (open-source), KAPE (open-source), Palo Alto Unit 42 (services)

**Market Maturity:** Mature (traditional); Growth (cloud DFIR)  
Services-heavy. Traditional disk forensics mature. Cloud DFIR (Cado Security) growing as incidents shift to cloud environments.

**Estimated Annual Spend:** $100K–$500K+ (IR retainer)  
- Mandiant IR retainer: $150K–$500K/year  
- CrowdStrike Falcon Complete MDR: $200K–$600K/year  
- Cado Security platform: $50K–$150K

---

## RECOVER

### Backup & Recovery

**Purpose:** Protects data availability through backup, replication, and recovery. Modern platforms add ransomware-specific protections: immutable backups, anomaly detection (detecting encryption), and clean room recovery.

**Core Modules / Functions:**
- Agent and agentless backup (VMs, databases, file systems)
- Immutable backup (WORM storage, air-gapped copies)
- Incremental forever and changed block tracking
- Ransomware anomaly detection (sudden entropy change, mass encryption)
- Instant recovery (mount backup as VM for fast RTO)
- Cloud backup (SaaS applications, cloud VMs)
- Cyber vault (isolated recovery environment)
- DR orchestration (failover/failback automation)
- Data governance (retention policies, legal hold)

**Key Vendors:**
Veeam, Rubrik, Cohesity (merged Veritas 2024), Commvault, Zerto (HPE), AWS Backup, Azure Backup, Google Cloud Backup & DR, Druva, Acronis Cyber Protect

**Gartner MQ:** Enterprise Backup and Recovery Solutions MQ — Veeam, Rubrik, Cohesity in Leaders.

**Market Maturity:** Mature  
Veeam dominates VM backup. Rubrik and Cohesity repositioned as "data security" platforms to differentiate from pure backup. Ransomware recovery capabilities now table-stakes.

**Estimated Annual Spend:** $80K–$400K  
- Veeam Data Platform: $50K–$200K  
- Rubrik Security Cloud: $100K–$400K  
- Cloud backup (Druva): $15–$25/user/month = $75K–$125K for 5,000 users

**Consolidation Signal:** Moderate. Backup vendors acquiring security features (Commvault acquired TrapX 2022). Hyperscaler backup (AWS Backup, Azure Backup) growing for cloud-native workloads.

**2025 Market Trend:** Cyber vault (air-gapped clean room recovery) becoming standard enterprise requirement post-ransomware. AI-driven anomaly detection identifying ransomware before backup corruption spreads.

---

### BCP / DR Planning

**Purpose:** Plans, tests, and executes business continuity and disaster recovery — ensuring critical functions survive and recover from disruptions. Encompasses BIA, recovery plan documentation, crisis communications, and DR orchestration.

**Core Modules / Functions:**
- Business Impact Analysis (BIA) — RTO/RPO definition
- Recovery plan authoring and version control
- Crisis communication planning and templates
- Tabletop exercise management
- DR testing and validation workflows
- Regulatory reporting (DORA, operational resilience)
- Vendor and dependency mapping
- Emergency notification

**Key Vendors:**
Fusion Risk Management, Castellan, Quantivate, OnSolve, Everbridge, Archer (BCP module), IBM OpenPages (BCP), SAP GRC (BCP)

**Market Maturity:** Mature  
Niche but regulated market. DORA (EU Digital Operational Resilience Act) and FCA operational resilience requirements driving mandatory investment in financial services.

**Estimated Annual Spend:** $30K–$150K

**Consolidation Signal:** BCP absorbing into GRC platforms (Archer, ServiceNow). Operational resilience regulations creating new demand for dedicated platforms (Fusion Risk).

---

## EMERGING

### AI / LLM Security

**Purpose:** Addresses security risks specific to AI/ML deployments — prompt injection, jailbreaks, data poisoning, model theft, and sensitive data exposure via LLM outputs. Also: securing AI infrastructure and pipelines.

**Core Modules / Functions:**
- Prompt injection detection (input filtering)
- Output filtering and content safety (response moderation)
- Sensitive data detection in LLM context windows
- Jailbreak and adversarial input detection
- Model scanning for embedded malware or backdoors
- AI pipeline security (data poisoning, model supply chain)
- LLM usage monitoring and audit trail
- Compliance reporting (EU AI Act, NIST AI RMF)

**Key Vendors:**
Microsoft Azure AI Content Safety, Google Cloud Model Armor, Palo Alto AI-SPM, Guardrails AI (OSS), NVIDIA NeMo Guardrails (OSS), Lakera Guard, HiddenLayer, Protect AI, Robust Intelligence, Wiz AI Security

**Gartner:** No MQ yet. Gartner Hype Cycle for AI Security 2024 covers this space.

**Market Maturity:** Emerging  
Most vendors are <3 years old. Platform vendors (Microsoft, Palo Alto, Wiz) adding AI security features to existing tools. Pure-play vendors (Lakera, HiddenLayer) at early stage.

**Estimated Annual Spend:** $10K–$80K (most organizations building rather than buying)

**2025 Market Trend:** EU AI Act compliance requirements driving governance investment. OWASP LLM Top 10 (v2 2024) becoming the reference taxonomy. AI-SPM (AI Security Posture Management) emerging as the CSPM equivalent for AI.

---

### Supply Chain Security / SBOM

**Purpose:** Secures the software development and distribution supply chain — verifying provenance of code, open-source components, and build artifacts. SBOM (Software Bill of Materials) provides the inventory foundation.

**Core Modules / Functions:**
- SBOM generation (CycloneDX, SPDX formats)
- Dependency vulnerability scanning (SCA)
- Package integrity and provenance verification (Sigstore, SLSA)
- Build pipeline security (CI/CD artifact signing)
- Malicious package detection (typosquatting, dependency confusion)
- Open-source license compliance
- Continuous monitoring for new CVEs in deployed SBOMs
- Vendor SBOM intake and verification

**Key Vendors:**
Snyk (SCA + supply chain), Black Duck (Synopsys), Chainguard (hardened images), Socket Security, GitHub Dependency Review, Anchore, FOSSA, Sigstore (OSS), in-toto (OSS)

**Market Maturity:** Growth  
EO 14028 (2021) mandated SBOM for US government software. EU CRA (Cyber Resilience Act) driving European adoption. Standards (SPDX, CycloneDX) mature; tooling still maturing.

**Estimated Annual Spend:** $10K–$80K (SCA tools often cover supply chain); dedicated SBOM tooling: $20K–$60K

**2025 Market Trend:** Regulatory pressure (EU CRA enforcement 2027) accelerating enterprise SBOM adoption. SLSA (Supply-chain Levels for Software Artifacts) framework gaining traction. AI-generated code supply chain risks emerging.
