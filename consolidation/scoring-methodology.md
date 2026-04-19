# Consolidation Scoring Methodology

**Purpose:** Produce an objective, defensible prioritization of which tools to retain, consolidate, replace, or retire — tied to business outcomes, not just cost.

---

## Outcome Themes (The "Why")

Every tool decision must be justified against one or more outcome themes. These are the business reasons the exercise exists — not just "save money."

| Theme | What It Means | Key Question |
|-------|--------------|-------------|
| **Cost Optimization** | Reduce total security spend without degrading coverage | "Are we paying twice for the same capability?" |
| **Zero Trust Advancement** | Replace perimeter-era tools with identity-aware, least-privilege equivalents | "Does this tool belong in a ZT architecture or does it assume network trust?" |
| **Platform Consolidation** | Reduce tool sprawl; improve signal quality by unifying telemetry | "Can a platform we already own absorb this?" |
| **Operational Efficiency** | Reduce analyst fatigue, integration overhead, and alert noise | "How many FTEs does this tool require to run well?" |
| **Risk Reduction** | Close coverage gaps identified in threat/risk assessment | "What threats are we not detecting because tools don't talk to each other?" |
| **Compliance Alignment** | Ensure controls map cleanly to regulatory requirements | "Does this tool generate evidence we need for audits?" |

---

## The Scoring Model

Each tool is scored across 6 dimensions. Scores run 1–5. The final **Consolidation Priority Score** determines sequencing.

### Dimension 1: Capability Uniqueness (1–5)
*Does any other tool in the estate deliver this capability?*

| Score | Meaning |
|-------|---------|
| 1 | Full overlap — 2+ other tools do exactly this |
| 2 | Significant overlap — one other tool covers 70%+ of this capability |
| 3 | Partial overlap — another tool covers this partially |
| 4 | Minor overlap — small functional overlap only |
| 5 | Unique — no other tool in estate covers this |

### Dimension 2: Cost Efficiency (1–5)
*Is the cost proportionate to the value delivered?*

| Score | Guidance |
|-------|---------|
| 1 | Very high cost per capability delivered; cheaper alternatives exist |
| 2 | Above-market cost; vendor has limited leverage at renewal |
| 3 | Market-rate pricing |
| 4 | Good value; platform bundle pricing or negotiated discount |
| 5 | Exceptional value — platform module at near-zero marginal cost (e.g., E5 bundled feature) |

**Calculation helper:** `cost efficiency = annual_license_usd ÷ number_of_distinct_capabilities`  
A $200K tool delivering 2 capabilities scores lower than a $200K tool delivering 8.

### Dimension 3: Platform Absorption Potential (1–5)
*How readily can a platform you already own absorb this tool?*

| Score | Meaning |
|-------|---------|
| 1 | No platform in the estate covers this; requires net-new investment |
| 2 | Platform covers this weakly; significant gap to fill |
| 3 | Platform covers this adequately; feature parity with current tool |
| 4 | Platform covers this well; some loss of edge features |
| 5 | Platform covers this fully or better; immediate replacement candidate |

### Dimension 4: Zero Trust Alignment (1–5)
*Does this tool advance Zero Trust maturity?*

| Score | Meaning |
|-------|---------|
| 1 | Perimeter-era tool; directly contradicts ZT principles (e.g. implicit trust VPN) |
| 2 | Legacy architecture; compatible with ZT only with significant re-engineering |
| 3 | Neutral — provides security value but ZT-agnostic |
| 4 | ZT-compatible; integrates with identity/device posture signals |
| 5 | ZT-native — enforces continuous verification, least privilege, microsegmentation |

### Dimension 5: Operational Overhead (1–5)
*Inverse of effort to operate — higher score = lower overhead.*

| Score | Meaning |
|-------|---------|
| 1 | Requires dedicated FTE(s); frequent maintenance; complex integrations |
| 2 | Significant analyst time; multiple integrations to maintain |
| 3 | Moderate effort; occasional tuning; standard integrations |
| 4 | Low effort; mostly SaaS-managed; minimal integration |
| 5 | Near-zero opex; fully managed SaaS; out-of-box integrations |

### Dimension 6: Removal Risk (1–5, inverted)
*Higher score = higher risk = harder to consolidate away. Inverted for priority calculation.*

| Score | Meaning |
|-------|---------|
| 5 | Critical — regulatory dependency; no replacement ready; operational essential |
| 4 | High — significant gap if removed; 6–12 month transition needed |
| 3 | Medium — partial coverage exists; 3–6 month transition |
| 2 | Low — full coverage elsewhere; can retire after 30-day parallel run |
| 1 | Trivial — already unused or redundant; immediate retirement possible |

---

## Scoring Matrix

```
CONSOLIDATION PRIORITY SCORE =
    (5 - Capability Uniqueness)      ← low uniqueness = high consolidation priority
  + (5 - Cost Efficiency)            ← low cost efficiency = high consolidation priority
  + Platform Absorption Potential    ← high absorption = high consolidation priority
  + (5 - ZT Alignment)              ← low ZT alignment = high consolidation priority
  + (5 - Operational Overhead inv.) ← high overhead = high consolidation priority
  - Removal Risk                     ← high risk = reduce priority (do later)

Range: 0 (retain without question) to 25 (retire immediately)
```

### Priority Bands

| Score | Band | Action |
|-------|------|--------|
| 20–25 | **Retire / Consolidate Now** | Immediate action; present to leadership in next cycle |
| 14–19 | **Consolidate in 6–12 months** | Plan migration; time to platform; leverage contract renewal |
| 8–13 | **Evaluate at renewal** | Reassess at next contract milestone; monitor platform absorption |
| 0–7 | **Retain** | Strategic tool; not a consolidation candidate in current planning horizon |

---

## Outcome Mapping: Tool Decision → Business Outcome

For each consolidation recommendation, link back to the outcome theme. This is the language executives and boards respond to.

| Tool Decision | Cost Optimization | ZT Advancement | Platform Consolidation | Risk Reduction |
|--------------|:-----------------:|:--------------:|:---------------------:|:--------------:|
| Retire redundant UEBA (absorbed into SIEM) | ✓ Save $180K | | ✓ Single telemetry | |
| Replace legacy VPN with ZTNA | ✓ Lower opex | ✓ Eliminate implicit trust | ✓ Platform SSE | ✓ Reduce attack surface |
| Retire standalone CASB (absorbed into SSE) | ✓ Save $120K | ✓ Inline enforcement | ✓ Zscaler/Cloudflare | |
| Consolidate dual VM tools onto one | ✓ Save $95K | | ✓ Fewer consoles | |
| Replace perimeter IDS with NDR | | ✓ East-west visibility | | ✓ Lateral movement detection |

---

## Coverage Heatmap: How to Visualize Gaps

After scoring all tools, plot them on a NIST CSF × ZTA pillar grid. Color-code:
- **Red** — no coverage (gap)
- **Amber** — single tool, high removal risk
- **Yellow** — single tool, medium removal risk
- **Green** — covered by retained/platform tool
- **Blue** — over-covered (consolidation candidate)

```
              Identity  Device  Network  Application  Data  Visibility
Govern           -        -        -          -         -       -
Identify         G        G        Y          Y         R       Y
Protect          B        G        B          G         Y       -
Detect           G        G        G          Y         Y       G
Respond          G        -        Y          -         -       G
Recover          R        -        -          -         -       -
```

Legend: G=Green, Y=Yellow, R=Red (gap), B=Blue (over-covered)

---

## ZTA Maturity Delta

For each consolidation scenario, calculate the change in ZTA maturity by pillar using the CISA ZTMM 4-stage scale (Traditional → Initial → Advanced → Optimal):

| ZTA Pillar | Current Maturity | Post-Consolidation | Delta | Driven By |
|-----------|-----------------|-------------------|-------|-----------|
| Identity | Initial | Advanced | +1 | Add IGA; retire legacy RADIUS |
| Device | Initial | Advanced | +1 | Consolidate on CrowdStrike; retire Carbon Black |
| Network | Traditional | Initial | +1 | Deploy ZTNA; retire VPN |
| Application | Initial | Initial | 0 | No change in this scenario |
| Data | Traditional | Initial | +1 | Deploy DSPM; basic DLP classification |
| Visibility | Initial | Advanced | +1 | Consolidated SIEM telemetry |

---

## Presenting to Stakeholders

### For the CFO / Board
Lead with the financial case. Show:
1. **Current total cost** (license + opex) by tool
2. **Projected savings** from consolidation (Year 1, Year 3)
3. **Investment required** (migration cost, new platform licenses)
4. **Net savings** with payback period

### For the CISO / Security Leadership
Lead with the risk and maturity case:
1. Coverage heatmap — where are the gaps today?
2. ZTA maturity delta — what does the org achieve by consolidating?
3. Threat coverage — which ATT&CK techniques become better covered?

### For the CIO / Architecture Team
Lead with operational efficiency and technical debt:
1. Integration complexity reduction (fewer APIs, fewer connectors)
2. Alert fatigue reduction (unified telemetry → better fidelity)
3. Vendor management reduction (fewer relationships, fewer contracts)

### For Procurement / Finance
Lead with commercial leverage:
1. Contract end dates (where can we exit vs. where are we locked)
2. Vendor consolidation discount opportunity (multi-product deals with fewer vendors)
3. Platform licensing efficiency (marginal-cost modules vs. standalone pricing)

---

## Common Pitfalls

1. **Evaluating tools in isolation** — always score against the full inventory; a tool looks different when you see everything it overlaps with
2. **Treating license cost as total cost** — a $50K tool that needs a full-time analyst costs $200K+
3. **Ignoring integration dependencies** — some tools feed data into other tools; retirement creates upstream blind spots
4. **Over-indexing on features** — a platform module with 80% feature parity is often the right answer; don't let feature comparison stall a cost/consolidation decision
5. **Forgetting contract timing** — the best consolidation plan is worthless if your replacement isn't ready before a forced renewal locks you in for 3 more years
6. **Not sequencing for ZT dependencies** — you cannot retire VPN before ZTNA is fully deployed and tested; map the dependency graph first
