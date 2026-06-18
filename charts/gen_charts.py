#!/usr/bin/env python3
"""Generate cost-comparison bar charts for the 12-institution scenarios.

Scenario G: HK$1,000,000 into 03070 + 03466 (1:1), lump-sum (2 trades).
Scenario H: HK$80,000 x 12 monthly DCA into 03466 only (12 trades, ~HK$960k).
Both use standard published online rates (promos noted separately in README).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# (label, year1_total, year2plus_annual)  — HK$, standard online rates
# Scenario G — lump-sum, 2 ETFs, ~16 dividend payouts/yr
DATA_G = [
    ("Futu 富途",        940,  490),
    ("ICBC(Asia) 工银",  1715, 365),
    ("Wing Lung 永隆",   2505, 605),
    ("CCB Asia 建行亚洲", 2505, 605),
    ("SC 渣打",          2585, 485),
    ("BEA 东亚",         2685, 785),
    ("DBS 星展",         2835, 735),
    ("CNCBI 中信国际",   3285, 685),
    ("HSBC 汇丰",        3385, 785),
    ("Hang Seng 恒生",   3385, 785),
    ("NCB 南商",         3385, 785),
    ("BOCHK 中银香港",   5800, 3200),
]

# Scenario H — monthly DCA (12 trades x HK$80k), single ETF 03466, 12 payouts/yr.
# At HK$80k/trade no commission minimum binds -> commission = pure rate x turnover.
# Year-2+ ICBC = Wealth a/c (custody waived); see README for the sub-Wealth case.
DATA_H = [
    ("Futu 富途",        940,  360),
    ("ICBC(Asia) 工银",  1675, 335),
    ("Wing Lung 永隆",   2320, 480),
    ("CCB Asia 建行亚洲", 2320, 480),
    ("SC 渣打",          2390, 360),
    ("BEA 东亚",         2500, 660),
    ("DBS 星展",         2590, 600),
    ("CNCBI 中信国际",   3070, 560),
    ("HSBC 汇丰",        3170, 660),
    ("Hang Seng 恒生",   3170, 660),
    ("NCB 南商",         3170, 660),
    ("BOCHK 中银香港",   5410, 2900),
]

# Use a CJK-capable font if available, else fall back (labels still ok in EN).
for f in ["PingFang HK", "PingFang SC", "Heiti SC", "Arial Unicode MS", "STHeiti"]:
    try:
        matplotlib.font_manager.findfont(f, fallback_to_default=False)
        plt.rcParams["font.family"] = f
        break
    except Exception:
        continue
plt.rcParams["axes.unicode_minus"] = False


def bar(data, values_idx, title, fname, unit="HK$/yr"):
    rows = sorted(data, key=lambda r: r[values_idx])
    labels = [r[0] for r in rows]
    vals = [r[values_idx] for r in rows]
    colors = []
    for i, v in enumerate(vals):
        if i == 0:
            colors.append("#2e8b57")        # cheapest -> green
        elif i <= 2:
            colors.append("#66b573")        # next cheapest -> light green
        elif v == max(vals):
            colors.append("#c0392b")        # most expensive -> red
        else:
            colors.append("#4a86c5")        # mid -> blue
    fig, ax = plt.subplots(figsize=(9.5, 6.2))
    y = range(len(labels))
    ax.barh(list(y), vals, color=colors, edgecolor="white")
    ax.set_yticks(list(y))
    ax.set_yticklabels(labels, fontsize=11)
    ax.invert_yaxis()                        # cheapest at top
    ax.set_xlabel(unit, fontsize=11)
    ax.set_title(title, fontsize=13, fontweight="bold", pad=12)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    xmax = max(vals)
    for i, v in enumerate(vals):
        ax.text(v + xmax * 0.012, i, f"{v:,}", va="center", fontsize=10, fontweight="bold")
    ax.set_xlim(0, xmax * 1.16)
    fig.tight_layout()
    fig.savefig(fname, dpi=150, bbox_inches="tight")
    print("wrote", fname)


bar(DATA_G, 1, "First-Year Total Cost  首年总费用  (HK$1M, 03070+03466, lump-sum)",
    "charts/scenarioG_year1.png")
bar(DATA_G, 2, "Annual Cost from Year 2  第二年起每年费用  (custody + dividend 存仓+收股息)",
    "charts/scenarioG_year2.png")

bar(DATA_H, 1, "First-Year Total Cost  首年总费用  (HK$80k×12 monthly DCA → 03466)",
    "charts/scenarioH_year1.png")
bar(DATA_H, 2, "Annual Cost from Year 2  第二年起每年费用  (custody + dividend 存仓+收股息)",
    "charts/scenarioH_year2.png")
print("done")
