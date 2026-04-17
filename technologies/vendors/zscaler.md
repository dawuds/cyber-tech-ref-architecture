# Zscaler — Vendor Profile

**Type:** Platform Vendor (Security-native, SSE/SASE)  
**HQ:** San Jose, CA, USA  
**Security Revenue:** ~$2.4B (FY2025)  
**Architecture Reference:** [Zscaler Zero Trust Exchange](../../architectures/zscaler-zte.md)

---

## Overview

Zscaler is the defining pure-play Zero Trust and SSE (Security Service Edge) vendor. Founded in 2007, Zscaler was built cloud-native from day one — the entire platform is delivered from Zscaler's globally distributed cloud fabric (150+ PoPs), with no on-premises software.

Zscaler's architecture is fundamentally different from NGFW-based or agent-first vendors: **all traffic is proxied inline through Zscaler cloud.** This provides complete visibility and enforcement for all internet/SaaS and private application access, but creates blind spots for traffic that doesn't pass through the proxy.

---

## Product Portfolio

| Category | Product(s) | NIST Mapping |
|----------|-----------|--------------|
| SWG | ZIA (Secure Web Gateway) | Protect |
| CASB (inline + API) | ZIA CASB | Protect |
| FWaaS | ZIA Cloud Firewall | Protect |
| URL/DNS Filtering | ZIA URL + DNS | Protect |
| DLP (web/cloud) | ZIA DLP | Protect |
| Browser Isolation | ZIA RBI (Remote Browser Isolation) | Protect |
| Email Security | Zscaler Email Security | Protect |
| Sandbox | Zscaler Sandbox | Detect |
| Deception | ZDP (Zscaler Deception — Smokescreen) | Detect |
| ZTNA | ZPA (Zscaler Private Access) | Protect |
| Privileged Remote Access | ZPA Privileged Remote Access | Protect |
| CSPM | ZCP / ZSCP Posture Control | Identify |
| DSPM | ZCP Data Security Posture | Identify |
| VM (cloud) | ZCP Vulnerability Assessment | Identify |
| Risk Scoring | Risk360 | Govern |
| Digital Experience | ZDX (Zscaler Digital Experience) | Identify |
| AI Copilot | Zscaler AI Copilot | Detect |

---

## Strengths

- **SSE/SASE leadership** — Gartner MQ Leader in SSE; widely regarded as the gold standard for ZTNA + SWG
- **Zero Trust architecture** — users connect to apps, never to the network; lateral movement eliminated by design
- **Scale** — 150+ PoPs globally; processes 500B+ transactions/day; low-latency cloud delivery
- **TLS inspection** — full SSL/TLS decryption and inspection as baseline capability (no traffic escapes inspection)
- **Risk360** — unique risk quantification feature connecting security events to business risk in dollar terms
- **Proxy telemetry depth** — richer web/SaaS telemetry than any firewall-based product (full URL, user, app, content inspection)

---

## Weaknesses

- **Endpoint blind spots** — no native EDR; device posture signals come from integrated CrowdStrike/MDE
- **East-west / non-web traffic** — proxy-only architecture; encrypted east-west traffic in data center bypasses Zscaler
- **SOC tooling** — no native SIEM or SOAR; log export to third-party SIEM required
- **Identity provider** — ZPA requires external IdP (Okta, Entra, Ping); Zscaler is not an IdP
- **OT/ICS** — Privileged Remote Access covers remote OT access; no industrial protocol inspection
- **MDR / services** — no managed detection and response service; response entirely dependent on SIEM integration

---

## Licensing Model

Module-based, capacity/user tiers.

| Product | Model | Approx. Annual Cost |
|---------|-------|---------------------|
| ZIA Business | Per user/year | ~$60-90/user/year |
| ZIA Transformation | Per user/year (advanced features) | ~$100-140/user/year |
| ZPA Business | Per user/year | ~$60-90/user/year |
| ZPA Transformation | Per user/year (AI + advanced) | ~$100-140/user/year |
| ZDX | Per user/year add-on | ~$20-40/user/year |
| ZCP Posture Control | Per workload/month | ~$10-20/workload/month |
| Risk360 | Included in Transformation bundles | — |
| Deception | Per decoy unit | ~$50-100K/year |

Bundled **Zscaler Business** or **Zscaler Transformation** packages provide ZIA + ZPA together at discount.

---

## NIST CSF Coverage

| Function | Coverage | Notes |
|----------|----------|-------|
| Govern | Weak | Risk360 is good; no GRC/compliance management platform |
| Identify | Partial | SaaS discovery, CSPM, DSPM for cloud; blind to unproxied assets |
| Protect | Very Strong | Complete internet/SaaS/private access control; best ZTNA/SSE |
| Detect | Partial | Sandbox + deception on proxied traffic; no SIEM/XDR |
| Respond | Weak | No native SOAR, no MDR; integration to third-party required |
| Recover | Absent | No backup or DR |

---

## Integration Architecture

Zscaler requires three components to function:
1. **Zscaler Client Connector** (agent) on managed devices — or PAC file/explicit proxy for unmanaged
2. **App Connectors** — lightweight software deployed near private applications (on-prem or cloud)
3. **Identity Provider** — Okta, Entra ID, Ping, or SAML/OIDC-compatible IdP

Key third-party integrations:
- **CrowdStrike** — Falcon Zero Trust Assessment score feeds ZPA access decisions
- **Microsoft Entra** — identity signals; Entra Conditional Access integration
- **SentinelOne, MDE** — device compliance signals for ZPA policies
- **Splunk, Sentinel, Chronicle** — log export for SIEM analysis

---

## Recent Developments (2023-2025)

- **AI-powered threat detection** — AI inline threat analysis within proxy (2024)
- **Zscaler AI Copilot** — natural language configuration assistant and security query
- **Risk360** expansion — financial quantification of risk added to base license tiers
- **DSPM** — data security posture management for cloud storage (2023)
- **ZPA AI-driven segmentation** — ML-based application segmentation recommendations
- **Avalor acquisition** (2024, ~$350M) — data fabric for security analytics; integrates into Risk360

---

## Analyst Position

- **Gartner MQ:** Leader in SSE (Security Service Edge) — consistently #1 or #2
- **Forrester Wave:** Leader in Zero Trust Platform, Cloud Security
- **Gartner Peer Insights:** Customers Choice for SSE multiple years
