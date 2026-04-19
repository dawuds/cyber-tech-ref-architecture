"""
Security Tool Consolidation Workbook Generator
Produces: consolidation-analysis.xlsx with 6 sheets + charts
"""

import xlsxwriter
import os

OUTPUT = os.path.join(os.path.dirname(__file__), "consolidation-analysis.xlsx")

# ── Palette ──────────────────────────────────────────────────────────────────
RED    = "#FF6B6B"   # Retire / Perimeter-era / Gap
AMBER  = "#FFB347"   # Consolidate / Evaluate
GREEN  = "#6BCB77"   # Retain / Advancing
BLUE   = "#4D96FF"   # Over-covered
GREY   = "#D3D3D3"   # N/A
WHITE  = "#FFFFFF"
DARK   = "#1A1A2E"
MID    = "#16213E"
HEADER = "#0F3460"
ACCENT = "#E94560"

# ── Tool Inventory Data ───────────────────────────────────────────────────────
TOOLS = [
    # num, name, vendor, category, nist, zt_pillar, deploy, lic_k, opex_k, contract, zt_align, redundancy, rec
    (1,  "Splunk Enterprise Security", "Cisco/Splunk",    "SIEM",          "Detect",   "Visibility",   "on-prem", 480, 120, "2026-03", "Neutral",       "Partial", "Retain"),
    (2,  "Exabeam UEBA",               "Exabeam",         "UEBA",          "Detect",   "Visibility",   "SaaS",    180,  45, "2025-09", "Neutral",       "Yes",     "Retire"),
    (3,  "CrowdStrike Falcon Complete", "CrowdStrike",    "EDR/XDR",       "Detect",   "Device",       "agent",   320,  30, "2026-06", "Advancing",     "No",      "Retain"),
    (4,  "Carbon Black EDR (legacy)",   "Broadcom",       "EDR",           "Detect",   "Device",       "agent",    95,  60, "2025-07", "Neutral",       "Yes",     "Retire"),
    (5,  "Cisco AnyConnect VPN",        "Cisco",          "VPN",           "Protect",  "Network",      "agent",    65,  40, "2025-12", "Perimeter-era", "Partial", "Replace"),
    (6,  "Zscaler ZIA",                 "Zscaler",        "SSE/SWG",       "Protect",  "Network",      "SaaS",    180,  25, "2027-01", "Advancing",     "No",      "Retain"),
    (7,  "Okta Workforce Identity",     "Okta",           "IAM/SSO/MFA",   "Protect",  "Identity",     "SaaS",    145,  20, "2026-04", "Advancing",     "Partial", "Retain"),
    (8,  "RSA SecurID (on-prem MFA)",   "RSA Security",   "MFA",           "Protect",  "Identity",     "on-prem",  85,  75, "2025-11", "Perimeter-era", "Yes",     "Retire"),
    (9,  "CyberArk Privilege Cloud",    "CyberArk",       "PAM",           "Protect",  "Identity",     "SaaS",    220,  35, "2026-09", "Advancing",     "No",      "Retain"),
    (10, "Qualys VMDR",                 "Qualys",         "VM",            "Identify", "Device",       "SaaS",     95,  25, "2025-10", "Neutral",       "Yes",     "Retain"),
    (11, "Tenable.io",                  "Tenable",        "VM",            "Identify", "Device",       "SaaS",     60,  20, "2025-06", "Neutral",       "Yes",     "Retire"),
    (12, "Palo Alto PA-3200 NGFW",      "Palo Alto",      "NGFW",          "Protect",  "Network",      "hardware", 180,  55, "2027-06", "Neutral",       "No",      "Retain"),
    (13, "Forescout NAC",               "Forescout",      "NAC",           "Protect",  "Device",       "on-prem",  95,  45, "2025-08", "Perimeter-era", "Partial", "Replace"),
    (14, "Varonis",                     "Varonis",        "DSPM/DAG",      "Identify", "Data",         "hybrid",  140,  30, "2026-02", "Advancing",     "No",      "Retain"),
    (15, "McAfee DLP (endpoint)",       "Trellix",        "DLP",           "Protect",  "Data",         "agent",    75,  65, "2025-05", "Neutral",       "Yes",     "Retire"),
    (16, "Microsoft M365 E3",           "Microsoft",      "Email/Endpoint","Protect",  "Device",       "SaaS",    200,  15, "rolling", "Advancing",     "Partial", "Upgrade to E5"),
    (17, "Proofpoint TAP",              "Proofpoint",     "Email Security","Protect",  "Application",  "SaaS",    120,  15, "2026-01", "Neutral",       "Partial", "Retain"),
    (18, "Archer GRC",                  "OpenPages/IBM",  "GRC",           "Govern",   "—",            "on-prem", 120,  40, "2026-11", "Neutral",       "No",      "Retain"),
    (19, "Rapid7 InsightIDR",           "Rapid7",         "DFIR",          "Respond",  "Visibility",   "SaaS",     85,  30, "2025-09", "Neutral",       "Yes",     "Retire"),
    (20, "PagerDuty",                   "PagerDuty",      "Case Mgmt",     "Respond",  "—",            "SaaS",     35,   5, "rolling", "Neutral",       "Partial", "Retain"),
    (21, "Cofense PhishMe",             "Cofense",        "Sec Awareness", "Govern",   "—",            "SaaS",     35,  10, "2026-03", "Neutral",       "No",      "Retain"),
    (22, "AWS Security Hub+GuardDuty",  "AWS",            "CNAPP/CSPM",    "Detect",   "Application",  "SaaS",     45,  20, "PAYG",    "Advancing",     "Partial", "Retain"),
]

# ── Scoring Data ──────────────────────────────────────────────────────────────
# num, name, uniqueness(1-5), cost_eff(1-5), platform_abs(1-5), zt_align(1-5), ops_overhead(1-5), removal_risk(1-5), score, band, rec
SCORES = [
    (2,  "Exabeam UEBA",              1, 2, 5, 3, 3, 2, 21, "Retire / Consolidate Now",    "Retire"),
    (8,  "RSA SecurID",               1, 1, 5, 1, 1, 2, 21, "Retire / Consolidate Now",    "Retire"),
    (15, "McAfee DLP",                1, 1, 5, 3, 1, 2, 20, "Retire / Consolidate Now",    "Retire"),
    (4,  "Carbon Black EDR",          1, 2, 5, 3, 2, 2, 20, "Retire / Consolidate Now",    "Retire"),
    (11, "Tenable.io",                1, 3, 4, 3, 4, 2, 17, "Consolidate 6–12m",           "Consolidate"),
    (5,  "Cisco AnyConnect VPN",      2, 3, 4, 1, 3, 3, 17, "Consolidate 6–12m",           "Replace"),
    (19, "Rapid7 InsightIDR",         2, 3, 4, 3, 3, 2, 16, "Consolidate 6–12m",           "Consolidate"),
    (13, "Forescout NAC",             2, 2, 3, 1, 2, 3, 15, "Consolidate 6–12m",           "Replace"),
    (10, "Qualys VMDR",               3, 3, 3, 3, 3, 3, 10, "Evaluate at Renewal",         "Retain"),
    (1,  "Splunk ES",                 3, 2, 2, 3, 2, 4,  9, "Evaluate at Renewal",         "Retain"),
    (6,  "Zscaler ZIA",               4, 3, 2, 5, 4, 3,  7, "Retain",                      "Retain"),
    (7,  "Okta Workforce",            4, 3, 2, 5, 4, 4,  6, "Retain",                      "Retain"),
    (9,  "CyberArk PAM",              5, 3, 2, 5, 3, 4,  5, "Retain",                      "Retain"),
    (3,  "CrowdStrike Falcon",        4, 3, 2, 5, 4, 4,  5, "Retain",                      "Retain"),
    (12, "Palo Alto PA NGFW",         4, 3, 2, 3, 2, 4,  5, "Retain",                      "Retain"),
    (14, "Varonis",                   4, 3, 2, 4, 3, 3,  5, "Retain",                      "Retain"),
    (17, "Proofpoint TAP",            3, 3, 3, 3, 4, 3,  5, "Retain",                      "Retain"),
    (16, "Microsoft M365 E3",         4, 4, 5, 4, 5, 4,  4, "Retain",                      "Upgrade to E5"),
    (22, "AWS Security Hub",          4, 5, 3, 4, 5, 3,  4, "Retain",                      "Retain"),
    (18, "Archer GRC",                4, 3, 1, 3, 2, 4,  3, "Retain",                      "Retain"),
    (21, "Cofense PhishMe",           4, 4, 2, 3, 4, 2,  3, "Retain",                      "Retain"),
    (20, "PagerDuty",                 3, 4, 3, 3, 5, 2,  3, "Retain",                      "Retain"),
]

# ── Scenario Data ─────────────────────────────────────────────────────────────
SCENARIOS = {
    "Current State": {
        "tools": 22, "vendors": 18, "annual_cost": 3780,
        "zt_identity": 2, "zt_device": 2, "zt_network": 1, "zt_app": 2, "zt_data": 1, "zt_visibility": 2,
        "coverage_gaps": 6, "perimeter_tools": 3,
    },
    "Scenario A\n(12 months)": {
        "tools": 16, "vendors": 14, "annual_cost": 3030,
        "zt_identity": 2, "zt_device": 2, "zt_network": 1, "zt_app": 2, "zt_data": 2, "zt_visibility": 3,
        "coverage_gaps": 5, "perimeter_tools": 2,
    },
    "Scenario B\n(24 months)": {
        "tools": 14, "vendors": 14, "annual_cost": 3190,
        "zt_identity": 3, "zt_device": 3, "zt_network": 2, "zt_app": 2, "zt_data": 2, "zt_visibility": 3,
        "coverage_gaps": 2, "perimeter_tools": 0,
    },
    "Scenario C\n(36 months)": {
        "tools": 12, "vendors": 11, "annual_cost": 2350,
        "zt_identity": 3, "zt_device": 3, "zt_network": 2, "zt_app": 3, "zt_data": 2, "zt_visibility": 4,
        "coverage_gaps": 0, "perimeter_tools": 0,
    },
}

# ── Heatmap Data ──────────────────────────────────────────────────────────────
# (function, pillar) → status: G=green, Y=yellow, R=red, B=blue, -=na
HEATMAP = {
    ("Govern",   "Identity"): "-", ("Govern",   "Device"): "-",   ("Govern",   "Network"): "-",
    ("Govern",   "App"):      "-", ("Govern",   "Data"):   "-",   ("Govern",   "Visibility"): "-",

    ("Identify", "Identity"): "-", ("Identify", "Device"): "B",   ("Identify", "Network"): "-",
    ("Identify", "App"):      "-", ("Identify", "Data"):   "G",   ("Identify", "Visibility"): "Y",

    ("Protect",  "Identity"): "B", ("Protect",  "Device"): "B",   ("Protect",  "Network"): "B",
    ("Protect",  "App"):      "G", ("Protect",  "Data"):   "B",   ("Protect",  "Visibility"): "-",

    ("Detect",   "Identity"): "-", ("Detect",   "Device"): "G",   ("Detect",   "Network"): "-",
    ("Detect",   "App"):      "Y", ("Detect",   "Data"):   "-",   ("Detect",   "Visibility"): "G",

    ("Respond",  "Identity"): "G", ("Respond",  "Device"): "-",   ("Respond",  "Network"): "Y",
    ("Respond",  "App"):      "-", ("Respond",  "Data"):   "-",   ("Respond",  "Visibility"): "G",

    ("Recover",  "Identity"): "R", ("Recover",  "Device"): "R",   ("Recover",  "Network"): "R",
    ("Recover",  "App"):      "R", ("Recover",  "Data"):   "R",   ("Recover",  "Visibility"): "R",
}
HEATMAP_LABEL = {"G": "Covered", "Y": "Single/At Risk", "R": "GAP", "B": "Over-covered", "-": "N/A"}
HEATMAP_COLOR = {"G": GREEN, "Y": AMBER, "R": RED, "B": BLUE, "-": GREY}

# ─────────────────────────────────────────────────────────────────────────────

def make_fmt(wb, bold=False, bg=None, font_color=WHITE, size=11, align="left",
             border=False, wrap=False, num_format=None):
    props = {"font_name": "Calibri", "font_size": size, "font_color": font_color,
             "align": align, "valign": "vcenter", "bold": bold, "text_wrap": wrap}
    if bg:
        props["bg_color"] = bg
    if border:
        props["border"] = 1
        props["border_color"] = "#CCCCCC"
    if num_format:
        props["num_format"] = num_format
    return wb.add_format(props)

REC_COLOR = {
    "Retire":       RED,
    "Replace":      AMBER,
    "Consolidate":  AMBER,
    "Retain":       GREEN,
    "Upgrade to E5": BLUE,
}

ALIGN_COLOR = {
    "Advancing":     GREEN,
    "Neutral":       "#B8B8B8",
    "Perimeter-era": RED,
}

BAND_COLOR = {
    "Retire / Consolidate Now": RED,
    "Consolidate 6–12m":        AMBER,
    "Evaluate at Renewal":      "#FFD700",
    "Retain":                   GREEN,
}


# ════════════════════════════════════════════════════════════════════════════
# SHEET 1 — Tool Inventory
# ════════════════════════════════════════════════════════════════════════════

def sheet_inventory(wb):
    ws = wb.add_worksheet("1. Tool Inventory")
    ws.set_tab_color(HEADER)
    ws.freeze_panes(2, 0)
    ws.set_zoom(90)

    # Column widths
    widths = [4, 32, 22, 18, 12, 14, 12, 14, 10, 14, 13, 16, 14, 18]
    for i, w in enumerate(widths):
        ws.set_column(i, i, w)

    # Formats
    title_fmt  = make_fmt(wb, bold=True, bg=HEADER, size=14, align="center")
    hdr_fmt    = make_fmt(wb, bold=True, bg=MID, size=10, border=True)
    sub_fmt    = make_fmt(wb, bold=True, bg="#E8F4F8", font_color=DARK, size=9, border=True)
    base_fmt   = make_fmt(wb, bg=WHITE, font_color=DARK, size=10, border=True)
    alt_fmt    = make_fmt(wb, bg="#F5F9FC", font_color=DARK, size=10, border=True)
    cost_fmt   = make_fmt(wb, bg=WHITE, font_color=DARK, size=10, border=True, num_format='$#,##0')
    cost_alt   = make_fmt(wb, bg="#F5F9FC", font_color=DARK, size=10, border=True, num_format='$#,##0')
    bold_cost  = make_fmt(wb, bold=True, bg="#EBF5EB", font_color=DARK, size=10, border=True, num_format='$#,##0')

    # Title row
    ws.merge_range("A1:N1", "Acme Financial Corp — Security Tool Inventory  |  April 2025  |  22 Tools  |  $3.78M Total Annual Cost", title_fmt)
    ws.set_row(0, 28)

    # Headers
    headers = ["#", "Tool Name", "Vendor", "Category", "NIST\nFunction", "ZT Pillar",
               "Deploy\nType", "Licence\n($K/yr)", "Opex\n($K/yr)", "Total\n($K/yr)",
               "Contract\nEnd", "ZT\nAlignment", "Redundancy", "Recommendation"]
    ws.set_row(1, 36)
    for c, h in enumerate(headers):
        ws.write(1, c, h, hdr_fmt)

    total_lic = total_opex = total_cost = 0

    for i, row in enumerate(TOOLS):
        r = i + 2
        (num, name, vendor, cat, nist, zt, deploy,
         lic_k, opex_k, contract, zt_align, redundancy, rec) = row

        total_cost_row = lic_k + opex_k
        total_lic += lic_k
        total_opex += opex_k
        total_cost += total_cost_row

        is_alt = (i % 2 == 1)
        bf = alt_fmt if is_alt else base_fmt
        cf = cost_alt if is_alt else cost_fmt

        ws.set_row(r, 20)
        ws.write(r, 0,  num,               bf)
        ws.write(r, 1,  name,              bf)
        ws.write(r, 2,  vendor,            bf)
        ws.write(r, 3,  cat,               bf)
        ws.write(r, 4,  nist,              bf)
        ws.write(r, 5,  zt,                bf)
        ws.write(r, 6,  deploy,            bf)
        ws.write(r, 7,  lic_k * 1000,      cf)
        ws.write(r, 8,  opex_k * 1000,     cf)
        ws.write(r, 9,  total_cost_row * 1000, cf)
        ws.write(r, 10, contract,          bf)

        # ZT Alignment with colour
        zt_bg = ALIGN_COLOR.get(zt_align, WHITE)
        ws.write(r, 11, zt_align, make_fmt(wb, bg=zt_bg, font_color=WHITE if zt_bg != "#B8B8B8" else DARK, size=10, border=True))

        # Redundancy
        red_bg = RED if redundancy == "Yes" else (AMBER if redundancy == "Partial" else GREEN)
        ws.write(r, 12, redundancy, make_fmt(wb, bg=red_bg, font_color=WHITE, size=10, border=True))

        # Recommendation with colour
        rec_bg = REC_COLOR.get(rec, WHITE)
        ws.write(r, 13, rec, make_fmt(wb, bg=rec_bg, font_color=WHITE, size=10, border=True, bold=True))

    # Totals row
    r_tot = len(TOOLS) + 2
    ws.set_row(r_tot, 22)
    ws.merge_range(r_tot, 0, r_tot, 6, "TOTAL ANNUAL COST", sub_fmt)
    ws.write(r_tot, 7, total_lic  * 1000, bold_cost)
    ws.write(r_tot, 8, total_opex * 1000, bold_cost)
    ws.write(r_tot, 9, total_cost * 1000, bold_cost)
    ws.merge_range(r_tot, 10, r_tot, 13, f"22 tools | 18 vendors | $3.78M total", sub_fmt)

    # Legend
    r_leg = r_tot + 2
    ws.merge_range(r_leg, 0, r_leg, 13, "LEGEND", make_fmt(wb, bold=True, bg=DARK, size=10))
    legends = [
        ("ZT Alignment", [("Advancing", GREEN), ("Neutral", "#B8B8B8"), ("Perimeter-era", RED)]),
        ("Recommendation", [("Retain", GREEN), ("Retire", RED), ("Replace / Consolidate", AMBER), ("Upgrade", BLUE)]),
        ("Redundancy", [("Yes — full overlap", RED), ("Partial overlap", AMBER), ("No — unique", GREEN)]),
    ]
    r_leg += 1
    for label, items in legends:
        ws.write(r_leg, 0, label, make_fmt(wb, bold=True, bg="#F0F0F0", font_color=DARK, size=9))
        for j, (text, color) in enumerate(items):
            ws.write(r_leg, j + 1, text, make_fmt(wb, bg=color, font_color=WHITE, size=9, border=True))
        r_leg += 1


# ════════════════════════════════════════════════════════════════════════════
# SHEET 2 — Scoring Results
# ════════════════════════════════════════════════════════════════════════════

def sheet_scoring(wb):
    ws = wb.add_worksheet("2. Scoring Results")
    ws.set_tab_color(ACCENT)
    ws.freeze_panes(3, 0)
    ws.set_zoom(90)

    widths = [4, 32, 13, 14, 16, 13, 14, 14, 11, 26, 18]
    for i, w in enumerate(widths):
        ws.set_column(i, i, w)

    title_fmt = make_fmt(wb, bold=True, bg=ACCENT, size=14, align="center")
    hdr_fmt   = make_fmt(wb, bold=True, bg=MID, size=10, border=True)
    sub_fmt   = make_fmt(wb, bold=True, bg="#F5E6E8", font_color=DARK, size=9, border=True, align="center")
    base_fmt  = make_fmt(wb, bg=WHITE, font_color=DARK, size=10, border=True, align="center")
    alt_fmt   = make_fmt(wb, bg="#FFF5F5", font_color=DARK, size=10, border=True, align="center")
    name_fmt  = make_fmt(wb, bg=WHITE, font_color=DARK, size=10, border=True)
    name_alt  = make_fmt(wb, bg="#FFF5F5", font_color=DARK, size=10, border=True)

    ws.merge_range("A1:K1", "Consolidation Priority Scoring  |  Score = (5-U)+(5-CE)+PA+(5-ZTA)+(5-OO)-RR  |  Range: 0 (Retain) → 25 (Retire Now)", title_fmt)
    ws.set_row(0, 28)

    # Sub-header explaining dimensions
    ws.merge_range("A2:B2", "Dimension Reference", sub_fmt)
    dims = ["U = Capability\nUniqueness", "CE = Cost\nEfficiency", "PA = Platform\nAbsorption", "ZTA = ZT\nAlignment", "OO = Ops\nOverhead", "RR = Removal\nRisk"]
    for j, d in enumerate(dims):
        ws.write(1, j+2, d, sub_fmt)
    ws.merge_range("I2:J2", "Score = 0–25", sub_fmt)
    ws.write(1, 10, "Action", sub_fmt)
    ws.set_row(1, 36)

    headers = ["#", "Tool Name", "Uniqueness\n(1–5)", "Cost Eff.\n(1–5)", "Platform\nAbsorption", "ZT Align\n(1–5)", "Ops O/H\n(1–5)", "Removal\nRisk", "Priority\nScore", "Priority Band", "Recommendation"]
    ws.set_row(2, 38)
    for c, h in enumerate(headers):
        ws.write(2, c, h, hdr_fmt)

    for i, row in enumerate(SCORES):
        r = i + 3
        (num, name, u, ce, pa, zta, oo, rr, score, band, rec) = row
        is_alt = (i % 2 == 1)
        bf = alt_fmt if is_alt else base_fmt
        nf = name_alt if is_alt else name_fmt

        ws.set_row(r, 20)
        ws.write(r, 0,  num,  bf)
        ws.write(r, 1,  name, nf)
        ws.write(r, 2,  u,    bf)
        ws.write(r, 3,  ce,   bf)
        ws.write(r, 4,  pa,   bf)
        ws.write(r, 5,  zta,  bf)
        ws.write(r, 6,  oo,   bf)
        ws.write(r, 7,  rr,   bf)

        # Score with gradient colour
        score_bg = RED if score >= 20 else (AMBER if score >= 14 else (GREEN if score <= 7 else "#FFD700"))
        ws.write(r, 8, score, make_fmt(wb, bold=True, bg=score_bg, font_color=WHITE, size=11, border=True, align="center"))

        band_bg = BAND_COLOR.get(band, WHITE)
        ws.write(r, 9, band, make_fmt(wb, bg=band_bg, font_color=WHITE, size=9, border=True))

        rec_bg = REC_COLOR.get(rec, WHITE)
        ws.write(r, 10, rec, make_fmt(wb, bold=True, bg=rec_bg, font_color=WHITE, size=10, border=True))

    # Band legend
    r_leg = len(SCORES) + 4
    ws.merge_range(r_leg, 0, r_leg, 10, "PRIORITY BAND DEFINITIONS", make_fmt(wb, bold=True, bg=DARK, size=10))
    r_leg += 1
    bands = [
        ("20–25", "Retire / Consolidate Now",  RED,    "Immediate action; quick wins available; perimeter-era tools"),
        ("14–19", "Consolidate 6–12 months",   AMBER,  "Plan migration; align with contract renewal; platform alternative ready"),
        ("8–13",  "Evaluate at Renewal",        "#FFD700", "Reassess at contract milestone; monitor platform absorption progress"),
        ("0–7",   "Retain",                     GREEN,  "Strategic tool; no consolidation candidate in current planning horizon"),
    ]
    for score_range, label, color, desc in bands:
        ws.write(r_leg, 0, score_range, make_fmt(wb, bold=True, bg=color, font_color=WHITE, size=10, border=True, align="center"))
        ws.write(r_leg, 1, label,       make_fmt(wb, bold=True, bg=color, font_color=WHITE, size=10, border=True))
        ws.merge_range(r_leg, 2, r_leg, 10, desc, make_fmt(wb, bg="#F8F8F8", font_color=DARK, size=10, border=True))
        r_leg += 1


# ════════════════════════════════════════════════════════════════════════════
# SHEET 3 — Coverage Heatmap
# ════════════════════════════════════════════════════════════════════════════

def sheet_heatmap(wb):
    ws = wb.add_worksheet("3. Coverage Heatmap")
    ws.set_tab_color("#9B59B6")
    ws.set_zoom(100)

    FUNCTIONS = ["Govern", "Identify", "Protect", "Detect", "Respond", "Recover"]
    PILLARS   = ["Identity", "Device", "Network", "App", "Data", "Visibility"]

    ws.set_column(0, 0, 14)
    for c in range(1, 7):
        ws.set_column(c, c, 18)
    ws.set_column(7, 7, 30)

    title_fmt  = make_fmt(wb, bold=True, bg=HEADER, size=14, align="center")
    fn_fmt     = make_fmt(wb, bold=True, bg=MID, font_color=WHITE, size=11, border=True)
    pillar_fmt = make_fmt(wb, bold=True, bg=MID, font_color=WHITE, size=11, border=True, align="center")
    na_fmt     = make_fmt(wb, bg=GREY, font_color="#888888", size=10, border=True, align="center")

    ws.merge_range("A1:H1", "Security Coverage Heatmap  —  NIST CSF Function × Zero Trust Pillar  |  Current State (Before Consolidation)", title_fmt)
    ws.set_row(0, 28)

    # Pillar headers
    ws.write(1, 0, "NIST CSF\nFunction", pillar_fmt)
    ws.set_row(1, 36)
    for c, p in enumerate(PILLARS):
        ws.write(1, c + 1, p, pillar_fmt)
    ws.write(1, 7, "Key tools covering this function", pillar_fmt)

    key_tools = {
        "Govern":   "Archer GRC, Cofense PhishMe",
        "Identify":  "Qualys VMDR, Tenable.io, Varonis",
        "Protect":   "Okta, CyberArk, Zscaler ZIA, Palo Alto NGFW, Proofpoint, M365",
        "Detect":    "Splunk ES, CrowdStrike Falcon, AWS GuardDuty",
        "Respond":   "Splunk SOAR (planned), Rapid7, PagerDuty",
        "Recover":   "⚠ NO COVERAGE — critical gap",
    }

    for row_i, func in enumerate(FUNCTIONS):
        r = row_i + 2
        ws.set_row(r, 30)
        ws.write(r, 0, func, fn_fmt)
        for col_i, pillar in enumerate(PILLARS):
            status = HEATMAP.get((func, pillar), "-")
            label  = HEATMAP_LABEL[status]
            color  = HEATMAP_COLOR[status]
            if status == "-":
                ws.write(r, col_i + 1, "N/A", na_fmt)
            else:
                cell_fmt = make_fmt(wb, bg=color, font_color=WHITE, size=10, border=True, align="center", bold=(status=="R"))
                ws.write(r, col_i + 1, label, cell_fmt)
        ws.write(r, 7, key_tools.get(func, ""), make_fmt(wb, bg="#FAFAFA", font_color=DARK, size=9, border=True, wrap=True))

    # Legend
    r_leg = len(FUNCTIONS) + 3
    ws.merge_range(r_leg, 0, r_leg, 7, "LEGEND", make_fmt(wb, bold=True, bg=DARK, size=11))
    r_leg += 1
    legends = [
        (BLUE,  "Over-covered",    "2+ tools cover this; consolidation candidate"),
        (GREEN, "Covered",         "Single tool provides adequate coverage"),
        (AMBER, "Single / At Risk","One tool; medium removal risk if retired"),
        (RED,   "GAP",             "No coverage — urgent investment needed"),
        (GREY,  "N/A",             "Not applicable to this function/pillar combination"),
    ]
    for color, label, desc in legends:
        ws.write(r_leg, 0, label, make_fmt(wb, bold=True, bg=color, font_color=WHITE, size=10, border=True))
        ws.merge_range(r_leg, 1, r_leg, 7, desc, make_fmt(wb, bg="#F8F8F8", font_color=DARK, size=10, border=True))
        r_leg += 1

    # Post-consolidation note
    r_leg += 1
    ws.merge_range(r_leg, 0, r_leg, 7,
        "Post-Scenario B (24 months): Recover gaps closed (Veeam added); over-coverage in Identity and Device resolved; Network moves from Perimeter-era to Initial ZT maturity",
        make_fmt(wb, bg="#EBF5EB", font_color=DARK, size=10, border=True, wrap=True))
    ws.set_row(r_leg, 36)


# ════════════════════════════════════════════════════════════════════════════
# SHEET 4 — Scenario Comparison
# ════════════════════════════════════════════════════════════════════════════

def sheet_scenarios(wb):
    ws = wb.add_worksheet("4. Scenario Comparison")
    ws.set_tab_color(GREEN)
    ws.set_zoom(95)

    ws.set_column(0, 0, 26)
    for c in range(1, 5):
        ws.set_column(c, c, 22)

    title_fmt = make_fmt(wb, bold=True, bg=HEADER, size=14, align="center")
    scen_fmt  = make_fmt(wb, bold=True, bg=MID, font_color=WHITE, size=11, border=True, align="center", wrap=True)
    metric_fmt= make_fmt(wb, bold=True, bg="#E8EAF6", font_color=DARK, size=10, border=True)
    base_fmt  = make_fmt(wb, bg=WHITE, font_color=DARK, size=11, border=True, align="center")
    alt_fmt   = make_fmt(wb, bg="#F5F9FC", font_color=DARK, size=11, border=True, align="center")
    cost_fmt  = make_fmt(wb, bg=WHITE, font_color=DARK, size=11, border=True, align="center", num_format='$#,##0"K"')
    cost_alt  = make_fmt(wb, bg="#F5F9FC", font_color=DARK, size=11, border=True, align="center", num_format='$#,##0"K"')
    saving_fmt= make_fmt(wb, bold=True, bg="#EBF5EB", font_color="#1B5E20", size=12, border=True, align="center", num_format='$#,##0"K"')
    worse_fmt = make_fmt(wb, bg="#FFF3E0", font_color="#E65100", size=11, border=True, align="center", num_format='$#,##0"K"')

    ws.merge_range("A1:E1", "Consolidation Scenario Comparison  |  Acme Financial Corp  |  April 2025", title_fmt)
    ws.set_row(0, 28)

    # Scenario headers
    ws.write(1, 0, "Metric", metric_fmt)
    ws.set_row(1, 42)
    scenarios = list(SCENARIOS.keys())
    for c, s in enumerate(scenarios):
        ws.write(1, c + 1, s, scen_fmt)

    METRICS = [
        ("── OPERATIONAL ──", None),
        ("Tool Count",          "tools"),
        ("Vendor Count",        "vendors"),
        ("Perimeter-era Tools", "perimeter_tools"),
        ("Coverage Gaps (Red Cells)", "coverage_gaps"),
        ("── FINANCIAL ──", None),
        ("Annual Cost ($K)",    "annual_cost"),
        ("Saving vs. Current ($K)", "__saving"),
        ("── ZT MATURITY (1=Traditional, 4=Optimal) ──", None),
        ("Identity Pillar",     "zt_identity"),
        ("Device Pillar",       "zt_device"),
        ("Network Pillar",      "zt_network"),
        ("Application Pillar",  "zt_app"),
        ("Data Pillar",         "zt_data"),
        ("Visibility",          "zt_visibility"),
    ]

    base_cost = SCENARIOS["Current State"]["annual_cost"]
    ZT_COLOR = {1: "#FFCDD2", 2: "#FFE082", 3: "#C8E6C9", 4: "#81C784"}

    for i, (label, key) in enumerate(METRICS):
        r = i + 2
        ws.set_row(r, 22)
        if key is None:
            ws.merge_range(r, 0, r, 4, label, make_fmt(wb, bold=True, bg=DARK, font_color=WHITE, size=10))
            continue

        ws.write(r, 0, label, metric_fmt)
        is_alt = (i % 2 == 1)
        bf = alt_fmt if is_alt else base_fmt
        cf = cost_alt if is_alt else cost_fmt

        for c, scen_name in enumerate(scenarios):
            scen = SCENARIOS[scen_name]
            if key == "__saving":
                val = base_cost - scen["annual_cost"]
                if val > 0:
                    ws.write(r, c + 1, val, saving_fmt)
                elif val == 0:
                    ws.write(r, c + 1, "—", bf)
                else:
                    ws.write(r, c + 1, abs(val), worse_fmt)
            elif key == "annual_cost":
                ws.write(r, c + 1, scen[key], cf)
            elif key.startswith("zt_"):
                val = scen[key]
                zt_bg = ZT_COLOR.get(val, WHITE)
                labels = {1: "Traditional", 2: "Initial", 3: "Advanced", 4: "Optimal"}
                ws.write(r, c + 1, f"{val} — {labels[val]}",
                         make_fmt(wb, bg=zt_bg, font_color=DARK, size=10, border=True, align="center"))
            else:
                # Colour based on direction
                val = scen[key]
                cur_val = SCENARIOS["Current State"][key]
                if scen_name == "Current State":
                    fmt = bf
                elif key in ("tools", "vendors", "perimeter_tools", "coverage_gaps"):
                    fmt = make_fmt(wb, bg=GREEN if val < cur_val else (AMBER if val == cur_val else RED),
                                   font_color=WHITE, size=11, border=True, align="center")
                else:
                    fmt = bf
                ws.write(r, c + 1, val, fmt)


# ════════════════════════════════════════════════════════════════════════════
# SHEET 5 — Execution Roadmap
# ════════════════════════════════════════════════════════════════════════════

def sheet_roadmap(wb):
    ws = wb.add_worksheet("5. Execution Roadmap")
    ws.set_tab_color(AMBER)
    ws.set_zoom(95)

    ws.set_column(0, 0, 14)
    ws.set_column(1, 1, 40)
    ws.set_column(2, 2, 22)
    ws.set_column(3, 3, 20)
    ws.set_column(4, 4, 14)
    ws.set_column(5, 5, 30)

    title_fmt  = make_fmt(wb, bold=True, bg=HEADER, size=14, align="center")
    hdr_fmt    = make_fmt(wb, bold=True, bg=MID, size=10, border=True)
    qtr_fmt    = make_fmt(wb, bold=True, bg="#2C3E50", font_color=WHITE, size=11, border=True)
    exit_fmt   = make_fmt(wb, bg=RED,   font_color=WHITE, size=10, border=True)
    deploy_fmt = make_fmt(wb, bg=GREEN, font_color=WHITE, size=10, border=True)
    eval_fmt   = make_fmt(wb, bg=AMBER, font_color=WHITE, size=10, border=True)
    base_fmt   = make_fmt(wb, bg=WHITE, font_color=DARK,  size=10, border=True)
    saving_fmt = make_fmt(wb, bold=True, bg="#EBF5EB", font_color="#1B5E20", size=10, border=True, num_format='$#,##0"K"')

    ws.merge_range("A1:F1", "Contract-Aligned Execution Plan  |  Sequenced by Contract End Date  |  No Forced Early Terminations", title_fmt)
    ws.set_row(0, 28)

    headers = ["Quarter", "Action", "Tool Exited / Deployed", "Replaces / Enables", "Net Saving", "Notes"]
    ws.set_row(1, 30)
    for c, h in enumerate(headers):
        ws.write(1, c, h, hdr_fmt)

    ROADMAP = [
        ("2025 Q2", "EXIT",   "McAfee DLP (endpoint)",         "Activate M365 E5 Purview DLP",            55,  "Contract May-25; E5 upgrade $85K offset"),
        ("2025 Q2", "EXIT",   "Tenable.io",                     "Consolidate on Qualys VMDR",               80,  "Contract Jun-25; no migration needed"),
        ("2025 Q3", "EXIT",   "Carbon Black EDR (legacy)",      "CrowdStrike already deployed",            155,  "Contract Jul-25; 30-day parallel run"),
        ("2025 Q3", "EXIT",   "Forescout NAC",                  "CrowdStrike device posture + Okta CA",    140,  "Contract Aug-25; ZT device maturity +1"),
        ("2025 Q3", "EXIT",   "Rapid7 InsightIDR",              "Splunk SOAR module activated",             75,  "Contract Sep-25; $40K SOAR add-on"),
        ("2025 Q3", "EXIT",   "Exabeam UEBA",                   "Splunk ML UEBA (already licensed)",       225,  "Contract Sep-25; no new investment"),
        ("2025 Q4", "EXIT",   "RSA SecurID",                    "Okta MFA fully validated as primary",     160,  "Contract Nov-25; Okta already live"),
        ("2025 Q4", "DEPLOY", "Zscaler ZPA (ZTNA)",             "Parallel with VPN; begin pilot",           0,   "$120K new; enables VPN exit"),
        ("2025 Q4", "DEPLOY", "SailPoint IGA (basic)",          "Fill IGA gap; MAS TRM compliance",         0,   "$120K new; access certification automated"),
        ("2026 Q1", "EXIT",   "Cisco AnyConnect VPN",           "ZPA pilot validated; VPN decommissioned", 105,  "Contract Dec-25; ZT network maturity +1"),
        ("2026 Q1", "DEPLOY", "Veeam Hardened Repository",      "Fill Recover gap; ransomware resilience",  0,   "$95K new; closes last red cell"),
        ("2026 Q2", "DEPLOY", "Wiz CNAPP",                      "Cloud posture; AWS CSPM augmentation",     0,   "$180K new; CNAPP depth for AWS"),
        ("2026 Q2", "EVAL",   "Splunk ES renewal decision",     "Evaluate Sentinel migration (Scenario C)", 0,   "Mar-26 renewal; Sentinel saves ~$230K/yr"),
        ("2026 Q3", "EXIT",   "Splunk ES (if Scenario C)",      "Microsoft Sentinel migration",            230,  "Conditional on Sentinel migration go-ahead"),
    ]

    ACTION_FMT = {"EXIT": exit_fmt, "DEPLOY": deploy_fmt, "EVAL": eval_fmt}

    for i, (qtr, action, tool, replaces, saving, notes) in enumerate(ROADMAP):
        r = i + 2
        ws.set_row(r, 22)
        # Quarter — merge if same as previous
        if i == 0 or ROADMAP[i-1][0] != qtr:
            ws.write(r, 0, qtr, qtr_fmt)
        else:
            ws.write(r, 0, "", qtr_fmt)
        ws.write(r, 1, tool,     ACTION_FMT.get(action, base_fmt))
        ws.write(r, 2, action,   ACTION_FMT.get(action, base_fmt))
        ws.write(r, 3, replaces, base_fmt)
        if saving > 0:
            ws.write(r, 4, saving * 1000, saving_fmt)
        else:
            ws.write(r, 4, "Investment", make_fmt(wb, bg="#FFF3E0", font_color="#E65100", size=10, border=True))
        ws.write(r, 5, notes, base_fmt)

    # Summary totals
    r_tot = len(ROADMAP) + 3
    ws.merge_range(r_tot, 0, r_tot, 5, "SCENARIO B FINANCIAL SUMMARY (24-month horizon)", make_fmt(wb, bold=True, bg=DARK, size=11))
    r_tot += 1
    summary = [
        ("Gross savings from tool retirements", "$995K"),
        ("New tool investment required",         "$515K"),
        ("Net annual saving (Year 2+)",          "$590K"),
        ("Scenario C additional saving (Splunk → Sentinel)", "$230K/yr"),
        ("Full Scenario C annual saving (Year 3+)",           "$1.43M/yr"),
    ]
    for label, val in summary:
        ws.write(r_tot, 0, label, make_fmt(wb, bg="#F5F5F5", font_color=DARK, size=10, border=True))
        ws.merge_range(r_tot, 1, r_tot, 5, val, make_fmt(wb, bold=True, bg="#EBF5EB", font_color="#1B5E20", size=11, border=True))
        r_tot += 1


# ════════════════════════════════════════════════════════════════════════════
# SHEET 6 — Dashboard (Charts)
# ════════════════════════════════════════════════════════════════════════════

def sheet_dashboard(wb):
    ws = wb.add_worksheet("6. Dashboard")
    ws.set_tab_color(ACCENT)
    ws.set_zoom(85)

    title_fmt = make_fmt(wb, bold=True, bg=HEADER, size=16, align="center")
    ws.merge_range("A1:P1", "Executive Dashboard  —  Security Tool Consolidation  |  Acme Financial Corp  |  April 2025", title_fmt)
    ws.set_row(0, 32)

    lbl_fmt  = make_fmt(wb, bold=True, bg=MID, font_color=WHITE, size=10, border=True, align="center")
    val_fmt  = make_fmt(wb, bold=True, bg=WHITE, font_color=DARK, size=20, border=True, align="center")
    desc_fmt = make_fmt(wb, bg="#F0F0F0", font_color="#666666", size=9, border=True, align="center")

    # ── KPI Row ──────────────────────────────────────────────────────────────
    ws.set_row(1, 24)
    ws.set_row(2, 40)
    ws.set_row(3, 20)

    kpis = [
        ("A2:C2", "B3", "C4", "Current Tools",    "22",     "#1A1A2E"),
        ("D2:F2", "E3", "F4", "Redundant Tools",  "6",      RED),
        ("G2:I2", "H3", "I4", "Perimeter-era",    "3",      RED),
        ("J2:L2", "K3", "L4", "Quick Win Saving", "$750K",  GREEN),
        ("M2:O2", "N3", "O4", "3-Year Saving",    "$1.43M", GREEN),
    ]
    for hdr_range, val_cell, desc_cell, label, value, color in kpis:
        ws.merge_range(hdr_range, label, lbl_fmt)
        ws.write(val_cell, value, make_fmt(wb, bold=True, bg=WHITE, font_color=color, size=22, border=True, align="center"))
        ws.write(desc_cell, "vs current state", desc_fmt)

    # ── Chart data (hidden rows, used only for charts) ────────────────────
    # Cost by Scenario — row 6
    ws.write("A6", "Scenario");      ws.write("B6", "Annual Cost ($K)")
    ws.write("A7", "Current State"); ws.write("B7", 3780)
    ws.write("A8", "Scenario A");    ws.write("B8", 3030)
    ws.write("A9", "Scenario B");    ws.write("B9", 3190)
    ws.write("A10","Scenario C");    ws.write("B10",2350)

    # Recommendation split — row 12
    ws.write("A12","Recommendation"); ws.write("B12","Count")
    ws.write("A13","Retain");         ws.write("B13",13)
    ws.write("A14","Retire");         ws.write("B14", 5)
    ws.write("A15","Replace");        ws.write("B15", 2)
    ws.write("A16","Consolidate");    ws.write("B16", 1)
    ws.write("A17","Upgrade to E5");  ws.write("B17", 1)

    # ZT Maturity — row 19
    ws.write("A19","Pillar");         ws.write("B19","Current"); ws.write("C19","Scenario B"); ws.write("D19","Scenario C")
    zt_data = [
        ("Identity",   2, 3, 3),
        ("Device",     2, 3, 3),
        ("Network",    1, 2, 2),
        ("Application",2, 2, 3),
        ("Data",       1, 2, 2),
        ("Visibility", 2, 3, 4),
    ]
    for i, (p, cur, b, c) in enumerate(zt_data):
        ws.write(19 + i, 0, p); ws.write(19 + i, 1, cur)
        ws.write(19 + i, 2, b); ws.write(19 + i, 3, c)

    # ── Chart 1: Cost by Scenario (column) ──────────────────────────────
    chart1 = wb.add_chart({"type": "column"})
    chart1.add_series({
        "name": "Annual Cost",
        "categories": "='6. Dashboard'!$A$7:$A$10",
        "values":     "='6. Dashboard'!$B$7:$B$10",
        "fill":       {"colors": [ACCENT, AMBER, AMBER, GREEN]},
        "data_labels": {"value": True, "num_format": '$#,##0"K"'},
    })
    chart1.set_title({"name": "Annual Cost by Scenario ($K)"})
    chart1.set_x_axis({"name": ""})
    chart1.set_y_axis({"name": "Cost ($K)", "min": 0, "max": 4500})
    chart1.set_style(11)
    chart1.set_size({"width": 380, "height": 260})
    ws.insert_chart("C6", chart1, {"x_offset": 5, "y_offset": 5})

    # ── Chart 2: Recommendation split (pie) ──────────────────────────────
    chart2 = wb.add_chart({"type": "pie"})
    chart2.add_series({
        "name": "Tools by Recommendation",
        "categories": "='6. Dashboard'!$A$13:$A$17",
        "values":     "='6. Dashboard'!$B$13:$B$17",
        "points": [
            {"fill": {"color": GREEN}},
            {"fill": {"color": RED}},
            {"fill": {"color": AMBER}},
            {"fill": {"color": AMBER}},
            {"fill": {"color": BLUE}},
        ],
        "data_labels": {"percentage": True, "category": True},
    })
    chart2.set_title({"name": "Tools by Recommendation"})
    chart2.set_style(10)
    chart2.set_size({"width": 380, "height": 260})
    ws.insert_chart("I6", chart2, {"x_offset": 5, "y_offset": 5})

    # ── Chart 3: ZT Maturity progression (clustered column) ──────────────
    chart3 = wb.add_chart({"type": "column"})
    for col_idx, (series_name, col_letter, color) in enumerate([
        ("Current",    "B", ACCENT),
        ("Scenario B", "C", AMBER),
        ("Scenario C", "D", GREEN),
    ]):
        chart3.add_series({
            "name":       series_name,
            "categories": "='6. Dashboard'!$A$20:$A$25",
            "values":     f"='6. Dashboard'!${col_letter}$20:${col_letter}$25",
            "fill":       {"color": color},
        })
    chart3.set_title({"name": "ZT Maturity by Pillar (1=Traditional → 4=Optimal)"})
    chart3.set_x_axis({"name": "ZT Pillar"})
    chart3.set_y_axis({"name": "Maturity Stage", "min": 0, "max": 4})
    chart3.set_style(11)
    chart3.set_legend({"position": "bottom"})
    chart3.set_size({"width": 520, "height": 280})
    ws.insert_chart("C20", chart3, {"x_offset": 5, "y_offset": 5})

    # Hide the raw data rows used for charts
    for r in range(5, 26):
        ws.set_row(r, None, None, {"hidden": True})

    # ── Summary table ─────────────────────────────────────────────────────
    ws.set_row(27, 24)
    ws.merge_range("A28:P28", "CONSOLIDATION SUMMARY", make_fmt(wb, bold=True, bg=DARK, size=12))
    ws.set_row(28, 20)

    summary_headers = ["",          "Current", "Scen A\n12m", "Scen B\n24m", "Scen C\n36m"]
    summary_data    = [
        ("Tool count",          22,    16,    14,    12),
        ("Vendor count",        18,    14,    14,    11),
        ("Annual cost ($K)",  3780,  3030,  3190,  2350),
        ("Saving vs today ($K)",  0,   750,   590,  1430),
        ("Coverage gaps",        6,     5,     2,     0),
        ("Perimeter-era tools",  3,     2,     0,     0),
    ]

    for c, h in enumerate(summary_headers):
        ws.write(28, c, h, make_fmt(wb, bold=True, bg=MID, font_color=WHITE, size=10, border=True, align="center", wrap=True))

    for i, (metric, cur, a, b, c_val) in enumerate(summary_data):
        r = 29 + i
        ws.set_row(r, 22)
        ws.write(r, 0, metric, make_fmt(wb, bold=True, bg="#E8EAF6", font_color=DARK, size=10, border=True))
        ws.write(r, 1, cur, make_fmt(wb, bg=WHITE, font_color=DARK, size=11, border=True, align="center"))

        for col_idx, val in enumerate([a, b, c_val]):
            improving = (metric in ("Tool count", "Vendor count", "Annual cost ($K)", "Coverage gaps", "Perimeter-era tools"))
            if improving:
                bg = GREEN if val < cur else (AMBER if val == cur else RED)
            else:
                bg = GREEN if val > cur else (AMBER if val == cur else RED)
            ws.write(r, col_idx + 2, val, make_fmt(wb, bold=True, bg=bg, font_color=WHITE, size=11, border=True, align="center"))


# ════════════════════════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════════════════════════

def main():
    wb = xlsxwriter.Workbook(OUTPUT, {"strings_to_numbers": False})
    wb.set_properties({"title": "Security Tool Consolidation Analysis — Acme Financial Corp",
                       "author": "Security Architecture Team",
                       "subject": "Tool Rationalisation",
                       "comments": "Generated from cyber-tech-ref-architecture/consolidation/"})

    sheet_inventory(wb)
    sheet_scoring(wb)
    sheet_heatmap(wb)
    sheet_scenarios(wb)
    sheet_roadmap(wb)
    sheet_dashboard(wb)

    wb.close()
    size_kb = os.path.getsize(OUTPUT) // 1024
    print(f"Generated: {OUTPUT}  ({size_kb} KB)")
    print("Sheets: 1.Tool Inventory | 2.Scoring Results | 3.Coverage Heatmap | 4.Scenario Comparison | 5.Execution Roadmap | 6.Dashboard")


if __name__ == "__main__":
    main()
