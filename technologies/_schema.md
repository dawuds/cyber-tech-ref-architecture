# Technology Category Schema

Each category YAML file follows this structure:

```yaml
id: string                    # kebab-case unique identifier
name: string                  # short display name
full_name: string             # expanded name
nist_primary: string          # primary NIST CSF 2.0 function
nist_secondary: [string]      # additional NIST functions addressed
description: string           # what this category does
related_categories: [string]  # related category ids
market_notes: string          # consolidation trends, status notes (optional)
vendor_framework_coverage:
  microsoft_mcra: string|null
  palo_alto_zta: string|null
  zscaler_zte: string|null
  google_csa: string|null
  crowdstrike_falcon: string|null
  cisa_ztmm: string|null
  aws_sra: string|null
  cisco_security: string|null
products:
  - name: string
    vendor: string
    platform: string          # parent platform if a module (optional)
    type: SaaS|on-prem|hybrid|open-source
    notes: string             # one-line differentiator or status note (optional)
```

## NIST CSF 2.0 Functions
- **Govern** — Organizational risk strategy, policies, roles, supply chain risk
- **Identify** — Asset inventory, vulnerability discovery, threat intelligence, risk assessment
- **Protect** — Access control, data security, network protection, resilient infrastructure
- **Detect** — Continuous monitoring, anomaly detection, threat detection
- **Respond** — Incident response, containment, communication, analysis
- **Recover** — Recovery planning, restoration, post-incident improvements

## Vendor Reference Architectures
| ID | Name | Source |
|----|------|--------|
| microsoft_mcra | Microsoft Cyber Reference Architecture | learn.microsoft.com/security/adoption/mcra |
| palo_alto_zta | Palo Alto Zero Trust Architecture | paloaltonetworks.com/zero-trust |
| zscaler_zte | Zscaler Zero Trust Exchange | zscaler.com/products-and-solutions/zero-trust-exchange-zte |
| google_csa | Google Cloud Security Architecture | cloud.google.com/security |
| crowdstrike_falcon | CrowdStrike Falcon Platform | crowdstrike.com/platform |
| cisa_ztmm | CISA Zero Trust Maturity Model v2.0 | cisa.gov/zero-trust-maturity-model |
| aws_sra | AWS Security Reference Architecture | docs.aws.amazon.com/prescriptive-guidance/security-reference-architecture |
| cisco_security | Cisco Security Reference Architecture | cisco.com/site/us/en/products/security/cisco-security-reference-architecture |
