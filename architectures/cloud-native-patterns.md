# Cloud-Native Security Architecture Patterns

**Scope:** Infrastructure-level security patterns for cloud environments  
**Applies to:** AWS, Azure, GCP (patterns are cloud-agnostic unless noted)

---

## On This Page
- [Overview](#overview) — how cloud-native security differs from traditional
- [Pattern 1: Multi-Account / Landing Zone](#pattern-1-multi-account--landing-zone-architecture) — AWS Organizations, Azure Management Groups, GCP Folder Hierarchy
- [Pattern 2: Hub-Spoke Network Topology](#pattern-2-hub-spoke-network-topology) — centralised NGFW/NDR with spoke VPCs
- [Pattern 3: Workload Identity](#pattern-3-workload-identity-no-credentials-in-code) — IRSA, Azure WIF, GCP Workload Identity
- [Pattern 4: Secrets Management](#pattern-4-secrets-management-in-cloud-native-sidecarcsi) — Vault sidecar, ESO, CSI driver
- [Pattern 5: Service Mesh Security](#pattern-5-service-mesh-security-mtls-zero-trust-for-east-west) — mTLS east-west, Istio/Linkerd/Consul
- [Pattern 6: eBPF-Based Security Telemetry](#pattern-6-ebpf-based-security-telemetry) — Falco, Cilium, Tetragon
- [Pattern 7: Immutable Infrastructure](#pattern-7-immutable-infrastructure) — golden image pipeline, IaC enforcement
- [Pattern 8: Cloud Security Posture Guardrails](#pattern-8-cloud-security-posture-guardrails-preventive--detective) — shift-left IaC + continuous CSPM
- [Pattern 9: GenAI / LLM Workload Security](#pattern-9-genai--llm-workload-security) — AI gateway, prompt injection, output filtering
- [Pattern 10: Multi-Cloud SIEM Aggregation](#pattern-10-multi-cloud-siem-aggregation) — OCSF normalisation, per-SIEM connectors

## At a Glance
- **Pattern 1 is foundational** — multi-account/landing zone isolation is required before any other pattern is meaningful
- **Workload identity** (IRSA / Azure WIF / GCP Workload Identity) eliminates static credentials entirely — the single highest-ROI cloud security change
- **Service mesh mTLS** provides zero-trust east-west security between microservices without network architecture changes
- **Immutable infrastructure** eliminates configuration drift and attacker persistence — all changes must flow through version-controlled IaC pipelines
- **eBPF-based tools** (Falco, Cilium, Tetragon) provide kernel-level telemetry with near-zero overhead — the foundation of cloud-native runtime detection

## Summary

Securing cloud-native infrastructure requires a different mental model from traditional IT security. The network perimeter dissolves; infrastructure is ephemeral and changes continuously; workload identity replaces network location as the primary trust signal. Applying traditional security controls to cloud-native environments either fails entirely or creates friction that slows delivery without improving security. This document captures ten architectural patterns — proven design decisions that address the specific security challenges of cloud environments across AWS, Azure, and GCP.

The patterns are sequenced deliberately. Pattern 1 (Multi-Account/Landing Zone) is the prerequisite for everything else: without account-level blast-radius isolation, every subsequent control is weaker. Patterns 3 (Workload Identity) and 7 (Immutable Infrastructure) deliver the highest security ROI per implementation effort — eliminating static credentials and configuration drift respectively address two of the most common root causes of cloud security incidents. The later patterns (service mesh mTLS, eBPF telemetry, GenAI security) are advanced controls for organisations that have already addressed the foundational patterns.

Each pattern includes cloud-provider-specific implementation examples — YAML manifests, SCP policy JSON, architecture diagrams — and cross-references to the relevant technology category YAML. This is not a theoretical framework; it is a set of concrete architectural decisions with specific implementation paths. Use it as a design checklist when building new cloud environments or as an audit checklist when reviewing existing ones.

---

## Overview

Cloud-native security differs from traditional security in three fundamental ways:
1. **Infrastructure is code** — security policies are deployed as IaC, not manual configuration
2. **Scale is dynamic** — workloads scale up/down; security must scale with them automatically
3. **Identity replaces network** — in cloud, IAM is the primary security boundary, not network perimeter

These patterns document the architectural decisions that enable secure cloud deployments at scale.

---

## Pattern 1: Multi-Account / Landing Zone Architecture

**The foundational pattern for all cloud security.**

Organizations must structure cloud accounts to enforce security isolation, prevent blast radius, and enable centralized security management.

### AWS Pattern: Security OU + Control Tower

```
AWS ORGANIZATIONS
├── Management Account (minimal — billing + org only)
├── Security OU
│   ├── Security Tooling Account (GuardDuty admin, Security Hub, Inspector)
│   └── Log Archive Account (S3 + CloudTrail + VPC Flow — immutable)
├── Infrastructure OU
│   ├── Network Account (Transit Gateway, NGFW, Route53)
│   └── Shared Services Account (AD, build tools)
├── Workload OUs
│   ├── Production OU
│   │   ├── App Account 1
│   │   └── App Account 2
│   ├── Development OU
│   └── Sandbox OU (budget limits + SCPs for safety)
└── Suspended OU (decommissioned accounts held here)
```

**Security controls per account type:**
- **Management:** MFA required; no workloads; only OU management and billing
- **Security Tooling:** GuardDuty delegated admin; Security Hub aggregator; member accounts cannot disable security services
- **Log Archive:** S3 Object Lock + Vault Lock; even root cannot delete; immutable forensic record
- **Workload accounts:** SCPs enforce guardrails (no public S3, no IAM users, enforce IMDSv2)

### Azure Pattern: Management Group Hierarchy + Landing Zones

```
Root Management Group
├── Platform Management Group
│   ├── Identity Subscription (AD Domain Services, Entra Connect)
│   ├── Management Subscription (Monitor, Sentinel, Defender for Cloud)
│   └── Connectivity Subscription (Azure Firewall, Virtual WAN, ExpressRoute)
├── Landing Zones Management Group
│   ├── Corp (connected to hub network)
│   │   ├── Production Subscriptions
│   │   └── Dev/Test Subscriptions
│   └── Online (internet-facing, isolated)
└── Sandbox Management Group (isolated development)
```

**Key controls:**
- Azure Policy at Management Group level enforces: encryption, allowed regions, mandatory tags
- Defender for Cloud enabled at subscription level via Azure Policy
- Azure Sentinel deployed in Management subscription; diagnostics from all subscriptions aggregated

### GCP Pattern: Organization + Folder Hierarchy (Security Foundations Blueprint)

```
GCP ORGANIZATION
├── Folders
│   ├── bootstrap (terraform infrastructure management)
│   ├── common (shared security services)
│   │   ├── project: audit-logs (Cloud Storage + BigQuery for logs)
│   │   ├── project: scc-notifications (Security Command Center alerts)
│   │   └── project: kms (Cloud KMS for encryption)
│   ├── production
│   │   ├── project: prod-app-1
│   │   └── project: prod-data-1
│   ├── non-production
│   └── network
│       ├── project: interconnect (Cloud Interconnect)
│       └── project: dns-hub (DNS policies)
```

---

## Pattern 2: Hub-Spoke Network Topology

**Centralize security inspection; spoke VPCs/VNets connect to a hub with firewall/NDR.**

```
                    [Internet]
                        ↓
               [Hub VPC / VNet]
               ┌─────────────────┐
               │  NGFW (cloud)   │ ← AWS Network Firewall / Azure Firewall / Cloud NGFW
               │  Egress proxy   │ ← Forward proxy for outbound inspection
               │  NDR sensors    │ ← Packet capture + traffic analysis
               │  Bastion / Jump │ ← Privileged access entry point
               └────────┬────────┘
           ┌────────────┼────────────┐
       [Spoke 1]    [Spoke 2]    [Spoke 3]
       Production    Dev/Test     Shared Services
```

**Implementation:**
- **AWS:** Transit Gateway (routes all spoke traffic through Security VPC with Network Firewall + Palo Alto VM-Series)
- **Azure:** Azure Virtual WAN with Azure Firewall Premium in hub; or hub VNet with Azure Firewall
- **GCP:** Shared VPC with Cloud NGFW (Palo Alto engine) as choke point

**Key design decisions:**
- Egress traffic forced through hub NGFW/proxy → DNS security, URL filtering, TLS inspection
- East-west traffic between spokes flows through NGFW → prevents lateral movement
- NDR sensor sees all inter-spoke traffic at hub

---

## Pattern 3: Workload Identity (No Credentials in Code)

**Applications must authenticate to cloud services without static credentials.**

```
❌ WRONG:
ENV: AWS_ACCESS_KEY_ID=AKIAXXXXXXXX
     AWS_SECRET_ACCESS_KEY=xxxxxxxxxx

✅ RIGHT (cloud-native workload identity):
[EC2 Instance] → [IAM Role attached to instance] → [STS AssumeRole] → [S3 access]
[EKS Pod] → [IAM Role for Service Account (IRSA)] → [STS AssumeRoleWithWebIdentity] → API
[Lambda] → [Execution role] → [access AWS services without credentials]
```

### AWS: IAM Roles for Service Accounts (IRSA)

```yaml
# EKS pod uses IRSA — no static credentials
apiVersion: v1
kind: ServiceAccount
metadata:
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::123456789:role/my-app-role
```

### Azure: Workload Identity Federation

```bash
# Azure AD Workload Identity for AKS pods
# Azure issues OIDC tokens; no secrets in pods
az aks update --enable-oidc-issuer --enable-workload-identity
```

### GCP: Workload Identity for GKE

```yaml
# GKE service account binds to GCP service account
# No key files; automatic OIDC token injection
apiVersion: v1
kind: ServiceAccount
metadata:
  annotations:
    iam.gke.io/gcp-service-account: app@my-project.iam.gserviceaccount.com
```

**Supporting technology:** [Secrets Management](../technologies/categories/protect/secrets-management.yaml) — HashiCorp Vault (for non-cloud-native or multi-cloud), AWS Secrets Manager, Azure Key Vault, Google Secret Manager for application secrets that can't use workload identity.

---

## Pattern 4: Secrets Management in Cloud-Native (Sidecar/CSI)

**Inject secrets at runtime without environment variables or static files.**

### Option A: Vault Agent Sidecar (Kubernetes)

```yaml
# Vault injects secrets into pod without exposing in environment
spec:
  template:
    metadata:
      annotations:
        vault.hashicorp.com/agent-inject: "true"
        vault.hashicorp.com/agent-inject-secret-db: "secret/data/db-password"
    spec:
      containers:
      - name: app
        # Secret written to /vault/secrets/db-password at runtime
```

### Option B: Kubernetes External Secrets Operator (ESO)

```yaml
# ESO syncs external secret (AWS SM, Azure KV) → K8s Secret
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
spec:
  secretStoreRef:
    name: aws-secretsmanager
    kind: ClusterSecretStore
  data:
  - secretKey: database-password
    remoteRef:
      key: prod/db-password
```

### Option C: CSI Secret Store Driver

```yaml
# Secrets mounted as files via CSI; no K8s Secret created
spec:
  volumes:
  - name: secrets
    csi:
      driver: secrets-store.csi.k8s.io
      readOnly: true
      volumeAttributes:
        secretProviderClass: "azure-kvname"
```

---

## Pattern 5: Service Mesh Security (mTLS Zero Trust for East-West)

**Enforce mutual TLS between all services — no implicit trust between microservices.**

```
Traditional east-west:
[Service A] ──HTTP──► [Service B]  (no authentication — trust the network)

Service mesh with mTLS:
[Service A] ──mTLS──► [Sidecar A] ──[Encrypted+Authenticated]──► [Sidecar B] ──► [Service B]
                 ↑ certificate from mesh CA              ↑ verifies Service A identity
```

**Technology:**

| Service Mesh | mTLS | Policy | Observability |
|-------------|------|--------|--------------|
| **Istio** (CNCF) | Auto mTLS | AuthorizationPolicy + PeerAuthentication | Kiali, Grafana, Jaeger |
| **Linkerd** (CNCF) | Auto mTLS (simpler) | Server + Route policies | Viz dashboard |
| **Consul Connect** (HashiCorp) | mTLS + intentions | Consul ACLs | Consul UI |
| **AWS App Mesh** | mTLS | IAM policy binding | X-Ray |

**Integration with security tools:**
- mTLS certificates issued by mesh CA; can be federated to SPIFFE/SPIRE for cross-cluster
- Traffic policies enforced by mesh complement NGFW (east-west microsegmentation)
- Istio telemetry feeds into SIEM (service-to-service communication patterns)

---

## Pattern 6: eBPF-Based Security Telemetry

**Collect kernel-level security telemetry without agents — using eBPF probes.**

eBPF (extended Berkeley Packet Filter) runs sandboxed programs in the Linux kernel without modifying kernel source. Security tools use eBPF to:
- Observe all system calls, network connections, file access — zero overhead vs. kernel modules
- Enforce security policies at kernel level (block specific syscalls)
- Collect telemetry without user-space agent

**Security tools using eBPF:**

| Tool | Function | Use Case |
|------|---------|---------|
| **Falco** (CNCF) | Runtime threat detection via syscall inspection | Detect container escapes, privilege escalation |
| **Cilium** (CNCF) | eBPF-based CNI + network policy + security observability | Replace iptables; enforce K8s NetworkPolicy at kernel |
| **Tetragon** (Isovalent/Cilium) | Process execution + network + file eBPF enforcement | Block and alert on kernel-level events |
| **Tracee** (Aqua Security) | Runtime security using eBPF | Container forensics, threat detection |
| **Wiz Runtime** | eBPF-based cloud workload detection | Kubernetes runtime threats without kernel modules |

**Relation to technology categories:** eBPF-based tools feed telemetry into [XDR/EDR](../technologies/categories/detect/xdr-edr.yaml) and [CNAPP](../technologies/categories/protect/cnapp.yaml) platforms; Cilium provides network policy enforcement at [NGFW/IPS](../technologies/categories/protect/ngfw-ips.yaml) function level.

---

## Pattern 7: Immutable Infrastructure

**Servers are never patched in place — replaced with new images. Eliminates configuration drift and persistence.**

```
Traditional (mutable):
[Server] → patch → patch → patch → configuration drift → unknown state

Immutable:
[Golden Image] → [CI/CD pipeline scans image (Trivy/Wiz/Inspector)] 
    → [Deploy new image] → [Terminate old] → [No direct SSH access to running instance]
```

**Security benefits:**
- Eliminates configuration drift — known state at all times
- Attackers cannot persist changes (next deployment reverts)
- Forces all changes through version control (IaC) → audit trail

**Implementation:**
- **Build:** Packer (image build) + Trivy/Grype (vulnerability scan) + OPA (policy gate)
- **Deploy:** Terraform/Pulumi IaC; all infrastructure as code in Git
- **Verify:** AWS Config / Azure Policy / GCP Org Policy — detect manual changes
- **Enforce:** Block direct SSH/RDP to production (PAM jump server for any emergency access)

---

## Pattern 8: Cloud Security Posture Guardrails (Preventive + Detective)

**Two-layer approach: prevent misconfigurations at deploy time; detect drift continuously.**

### Layer 1: Preventive (Shift-Left)

```
[Developer pushes IaC]
    ↓
[Pre-commit: Checkov/tfsec scan] → fail if S3 bucket is public, SG 0.0.0.0/0, etc.
    ↓ 
[CI/CD pipeline: OPA/Conftest policy] → organization-wide rules enforced
    ↓
[Cloud: AWS SCPs / Azure Policy / GCP Org Policy] → prevent prohibited actions via API
```

**Tools:** Checkov (open-source IaC scanner), tfsec, Snyk IaC, Wiz Code (IaC scanning), Prisma Cloud IaC

### Layer 2: Detective (Continuous)

```
[Deployed resources]
    ↓ continuously scanned by
[CSPM (Wiz / Defender for Cloud / Security Hub)]
    ↓
[Alert: EC2 in production has public IP + SSH open + no MFA on console]
    ↓
[SOAR playbook: notify owner → auto-remediate if critical]
```

**SCPs / Guardrails examples (AWS):**

```json
// Deny public S3 buckets
{
  "Sid": "DenyS3PublicAccess",
  "Effect": "Deny",
  "Action": "s3:PutBucketPublicAccessBlock",
  "Condition": {
    "StringEquals": {"s3:PublicAccessBlockConfiguration/BlockPublicAcls": "false"}
  }
}

// Enforce IMDSv2 (prevent SSRF metadata attacks)
// Require MFA for sensitive actions
// Deny root account actions
// Restrict to approved AWS regions (data residency)
```

---

## Pattern 9: GenAI / LLM Workload Security

**Specific security architecture for AI/ML inference workloads.**

```
[User/Application] 
    ↓ API request with prompt
[AI Gateway layer]          ← Rate limiting, cost control, PII detection in prompts
    ↓ sanitized prompt
[LLM Inference endpoint]    ← Access controlled via IAM; no public endpoint
    ↓ model response
[Output filter]             ← Block harmful content, PII leakage, prompt injection indicators
    ↓ safe response
[Logging to SIEM]           ← All prompts + responses logged (with PII redaction)
[User receives response]
```

**Security controls:**

| Control | Tool | Purpose |
|---------|------|---------|
| LLM API gateway | Cloudflare AI Gateway, Azure APIM | Rate limiting, cost control, request logging |
| Prompt injection detection | Lakera Guard, Protect AI | Block prompt injection / jailbreaks |
| PII detection in prompts | Microsoft Presidio, AWS Comprehend | Prevent sensitive data entering LLM |
| Output filtering | LLM safety classifiers | Block harmful/policy-violating outputs |
| Access control | IAM (role-based LLM access) | Only authorized apps/users access model endpoints |
| Fine-tuning data security | DSPM for training data | Prevent PII in fine-tuning datasets |
| Model provenance | Model signing (Sigstore) | Verify model integrity before deployment |

**Reference:** [AI/LLM Security category](../technologies/categories/emerging/ai-llm-security.yaml), [AI Governance cross-reference](../cross-references/ai-governance-security-mapping.md)

---

## Pattern 10: Multi-Cloud SIEM Aggregation

**Collect security signals from all clouds into a single SIEM.**

```
AWS
  CloudTrail → ──────────────────────────────────┐
  GuardDuty findings → CloudWatch → Kinesis →    │
  VPC Flow Logs → S3 → Lambda/Firehose → ────────┤
                                                  │
Azure                                             ├──► [SIEM]
  Activity Log → Event Hub → ────────────────────┤    (Sentinel / Splunk /
  Defender alerts → → → → → ────────────────────┤     Chronicle)
  AAD Audit Logs → → → → → → ────────────────────┤
                                                  │
GCP                                               │
  Cloud Audit Logs → Pub/Sub → → → → → → → → →──┘
  SCC findings → → → → → → → → → → → → → → →──┘
```

**Implementation options:**

| SIEM | AWS | Azure | GCP |
|------|-----|-------|-----|
| **Microsoft Sentinel** | AWS S3 connector + CloudTrail | Native | GCP connector |
| **Google Chronicle** | AWS connector | Azure connector | Native |
| **Splunk** | AWS Add-on for Splunk | Azure Add-on | GCP Add-on |
| **Amazon Security Lake** | Native (OCSF) | Azure → OCSF → Security Lake | GCP → OCSF |

**Amazon Security Lake + OCSF:** OpenCybersecurity Schema Framework normalizes all cloud logs to a common schema — 50+ sources including AWS, Azure, GCP, CrowdStrike, Okta, and more.

---

## References

- AWS Security Reference Architecture: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/
- AWS Control Tower: https://aws.amazon.com/controltower/
- Azure Landing Zones: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/
- GCP Security Foundations Blueprint: https://github.com/terraform-google-modules/terraform-example-foundation
- CNCF Falco: https://falco.org/
- CNCF Cilium: https://cilium.io/
- OpenCybersecurity Schema Framework (OCSF): https://schema.ocsf.io/
- SPIFFE/SPIRE (workload identity): https://spiffe.io/
- Checkov (IaC scanning): https://www.checkov.io/
