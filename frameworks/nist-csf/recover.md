# NIST CSF 2.0 — Recover (RC)

Restores assets and operations impaired by a cybersecurity incident, enabling timely return to normal function and incorporation of lessons learned.

## Purpose

Recovery is the least invested-in function and the most painful to discover gaps in during an actual incident. Recover answers: *How do we get back to normal after an attack?* Ransomware has made this function business-critical — organizations without strong Recover capabilities face paying ransoms or accepting prolonged outages.

## Technology Categories

| Category | Description |
|----------|-------------|
| [Backup & Recovery](../../technologies/categories/recover/backup-recovery.yaml) | Data protection, immutable backup, and ransomware recovery |
| [BCP / DR](../../technologies/categories/recover/bcp-dr.yaml) | Business continuity planning and disaster recovery orchestration |

## Key Outcomes (NIST CSF 2.0 Categories)

- **RC.RP** — Incident Recovery Plan Execution: recovery executed per plan; communications managed
- **RC.CO** — Incident Recovery Communication: stakeholders coordinated during and after recovery

## Vendor Architecture Coverage

**Strong:** None — Recover is the most underserved function in all major vendor architectures  
**Partial:** AWS (AWS Backup), Microsoft (Azure Backup, built into M365)  
**Weak/None:** Palo Alto, Zscaler, CrowdStrike, Google (beyond Mandiant IR), Cisco

## Architecture Note: The Recover Gap

Backup and DR vendors (Veeam, Rubrik, Cohesity, Commvault) are not typically marketed as cybersecurity vendors, but they are essential to NIST Recover. This creates an organizational gap: security teams often don't own or influence backup/DR decisions, and IT/infra teams don't engage with the CISO on recovery objectives.

**Key questions for any Recover assessment:**
1. Are backups immutable and air-gapped from production?
2. What is the tested RTO and RPO for critical systems?
3. Is there a clean room recovery environment isolated from the potentially compromised network?
4. Has the recovery plan been tested against a ransomware scenario?
