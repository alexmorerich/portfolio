# User Manual — HK Bank & Broker Cost Comparison
# 使用手册 —— 香港银行与券商成本对比

> **Companion to [`README.md`](README.md).** The README is the **data** (10 verified scenarios A–J + charts); this manual is the **operating layer** — how the fees work, how to read a scenario, and how to pick an institution for *your* situation (even one no scenario covers).
> **配合 [`README.md`](README.md) 使用。** README 是**数据**（10 个已核实场景 A–J + 图表）；本手册是**操作层** —— 费用如何运作、如何读懂场景、以及如何为*你自己的*情况（即使没有对应场景）选机构。
>
> **Last updated / 更新:** 2026-06-18 · **Not financial advice / 非投资建议.**

---

## Language / 语言
- [English](#english)
- [中文](#中文)

---

# English

## 1. What this is & who it's for

This repo answers one question precisely: **"For a given Hong Kong stock/ETF investing plan, which of these 13 institutions costs the least — in Year 1 and in every year after?"**

- **Institutions covered:** 7 banks (HSBC, BOCHK, Standard Chartered, ICBC Asia, CNCBI, DBS HK, Wing Lung) + 6 brokers (Futu 富途, uSMART 盈立, Tiger 老虎, Valuable Capital 华盛, Longbridge 长桥, Snowball 尊嘉). Scenarios G–I also include BEA, CCB Asia, Hang Seng, NCB.
- **Who it's for:** retail investors comparing where to run a dividend-ETF or buy-and-hold plan in HK; mainland-China investors opening offshore HK accounts; anyone sizing the *true* all-in cost (not just the headline commission).
- **What it is NOT:** stock picking, return forecasting, or tax advice. It compares **fees only**, holding the investment plan fixed.

## 2. How to use it in 60 seconds

1. Open the **[Scenario quick-reference table](README.md#-scenario-quick-reference--场景速查表)** in the README.
2. Find the row whose **trade size, frequency, and holding type** look like yours.
3. Read its "Cheapest" cell for Year 1 and for the long-term hold.
4. If nothing matches exactly, use the **[decision framework](#5-decision-framework--pick-by-your-profile)** below — it generalizes the rules so you can reason about any plan.

**The one-sentence answer most people need:** for **small, frequent ETF buys**, a **near-zero-commission broker** (Snowball/尊嘉 cheapest on commission) beats every bank; for a **long-term hold after you stop trading**, anything with **$0 custody** wins (all 6 brokers, plus SC and ICBC-Wealth among banks); the banks' fat **commission minimums** and **custody fees** are what make them expensive. (Brokers still charge a dividend-collection fee of ~0.2%/min HK$30 — see §3 — so none is truly "fee-free".)

## 3. The five fee types — anatomy of an HK securities bill

Every cost in this repo is one of these five. Knowing which one *binds* in your plan tells you who wins.

| # | Fee | When charged | Typical size | Who it hurts |
|---|---|---|---|---|
| 1 | **Commission** 佣金 | every **buy** and **sell** | banks 0.138%–0.25%, **min HK$50–100**; brokers ~0–0.03% | small trades (the **minimum** becomes a huge effective %) |
| 2 | **Platform fee** 平台费 | every order — **brokers only** | HK$1 (尊嘉) · HK$12 (uSMART) · HK$15 (Futu/华盛/长桥/Tiger) | high-frequency buyers (paid per order) |
| 3 | **Custody / safekeeping** 托管费 | **annually, while you hold** | banks HK$120–2,000/yr; **brokers $0** | long-term holders who stopped trading |
| 4 | **Dividend collection** 代收股息费 | **each dividend payout** | banks 0.5%, **min HK$30** (BOCHK HK$75, ICBC HK$20); brokers **0.2%/min HK$30** (+ possible registrar 过户费 ~HK$1.5/lot) | many small dividends (monthly-pay ETFs) |
| 5 | **Gov/exchange levies** 政府征费 | every trade — **same everywhere** | ~0.0085% + CCASS (≈HK$2–3/small trade); **stamp duty 0.1%** | nobody differentially — but **stamp duty hits stocks, NOT ETFs** |

**The single most important mechanic — a minimum is a percentage in disguise.**
A HK$100 commission minimum on a **HK$10,000** trade = **1.0% effective**. The same min on a **HK$100,000** trade = **0.1%**. So the *same fee schedule* makes a bank cheap for big trades and ruinous for small ones. This is why the answer flips between scenarios.

## 4. The three rules of thumb (with the math)

| Rule | When it applies | Winner | The math |
|---|---|---|---|
| **Small trades → minimums dominate** | trade ≤ ~HK$30k | low-/no-minimum houses: **brokers**, then **Wing Lung** (min HK$4.88), **DBS** (no min) | HK$100 min ÷ HK$10k = **1%**; vs Wing Lung 0.18% true rate |
| **Big trades → rates dominate** | trade ≥ ~HK$60k | **ICBC** (0.138%, or **0.1% ≥HK$1M**); brokers still cheaper | no minimum binds, so 0.138% ≪ 0.25% — ICBC ≈ half the big banks |
| **Long hold → custody dominates** | you stop trading and just hold | **$0-custody** houses: all **brokers**, plus **SC** & **ICBC-Wealth** | commission is over; custody HK$0 vs HK$2,000/yr (BOCHK) compounds yearly |

**Corollary for dividends:** if you hold a **monthly-paying** ETF, the **dividend minimum** decides (12+ payouts × each bank's min). ICBC's HK$20 wins; BOCHK's HK$75 is worst. If you hold a **semi-annual** payer (e.g. 02800), the two big payouts clear every minimum, so the dividend fee is ~equal and **custody** breaks the tie.

## 5. Decision framework — pick by your profile

Answer four questions, then read the table.

**Q1. Trade size?** small (≤HK$30k) · medium (HK$30–60k) · large (≥HK$60k)
**Q2. How often do you buy?** one-off lump sum · monthly DCA · frequent
**Q3. Holding period?** trade often · buy-and-hold for years
**Q4. What do you hold?** ETF (no stamp duty) · individual stock (0.1% stamp duty) · gold/USD (no dividend fee)

| Your profile | Cheapest Year 1 | Cheapest to hold | Avoid | Scenario |
|---|---|---|---|---|
| Small monthly ETF DCA (≤HK$20k/trade) | **Snowball 尊嘉** → all brokers; banks: Wing Lung/DBS | brokers, SC, ICBC-Wealth (all $0 custody) | HK$100-min banks (HSBC/CNCBI/BOCHK) | **I, J** |
| Large trades (≥HK$60k) | **Futu**; banks: **ICBC** (0.138%) | SC/Futu/ICBC-Wealth | 0.25% banks (HSBC/Hang Seng/NCB) | **E, H** |
| Big lump sum ≥HK$1M, then hold | **Futu**; banks: **ICBC-Wealth** | **ICBC-Wealth** (0.1% ≥1M + $0 custody) | BOCHK | **G, F** |
| Monthly-paying ETF (12+ dividends/yr) | Futu; banks: **ICBC** (div min HK$20) | ICBC-Wealth | **BOCHK** (div min HK$75 + HK$2,000 custody) | **G, H** |
| Buy-and-hold one position, stop trading | SC / Wing Lung (low entry) | **SC** or **ICBC-Wealth** (unconditional $0 custody) | custody-charging banks | **B, C, D** |
| Individual HK stocks (not ETF) | factor **+0.1% stamp duty** each buy | SC (custody) | — (stamp duty is equal everywhere) | **C, D** |
| Sanctions-resilient (gold + USD + stock) | **ICBC-Wealth** | **ICBC-Wealth** | — | **F** |

**Two caveats baked into the small-trade cases:**
- **Board lots.** A HK$10k order is below one board lot of many ETFs (02800 ≈ HK$12,500/lot). Execute via a **Monthly Stock Investment Plan / 月供股票计划** (pools odd/fractional lots) or the odd-lot market. This also unlocks **monthly-plan $0-commission promos** (BOCHK, HSBC, and brokers).
- **Broker tiered plans.** Tiger's HK$15/order is the *fixed* plan; its *tiered* plan is **HK$30/order at ≤5 orders/month** — pick the fixed plan for monthly DCA.

## 6. Institution profiles

### Brokers (all $0 custody, no stamp duty on ETFs)
| Broker | Edge | Trap / caveat |
|---|---|---|
| **Snowball 尊嘉** | **$0 commission + HK$1/order** platform — cheapest *commission* for tiny/frequent trades | still charges dividend 0.2%/min HK$30 **+ 登记过户费 HK$1.5/lot (min HK$31.9)** per payout; smaller franchise — verify |
| **Futu 富途** | market-leading app/community; standing **$0-commission-forever** promo + HK$15 platform | platform fee per order adds up on high frequency |
| **uSMART 盈立** | **HK$12/order** (免佣 plan) — cheapest platform fee after 尊嘉; AI/grid tools | tiered plans; check which plan you're on |
| **Longbridge 长桥** | **lifetime $0 commission** + HK$15 platform (tiered to HK$3) | dividend fee not published — verify |
| **Valuable Capital 华盛** | Sina-backed; 0.03%/min HK$3 + HK$15; frequent new-account promos | standard, not the cheapest |
| **Tiger 老虎** | Nasdaq-listed; strong options/global tools; 0.029% + HK$15 (fixed) | **tiered plan = HK$30 at ≤5 orders/mo** — use fixed |

### Banks
| Bank | Edge | Trap / caveat |
|---|---|---|
| **ICBC Asia 工银** | lowest bank **rate** (0.138%, **0.1% ≥HK$1M**); **div min HK$20**; **$0 custody** if Wealth/turnover | **HK$88 commission min** kills small trades; custody waiver needs HK$1M (Wealth) or HK$200k turnover |
| **Standard Chartered 渣打** | **unconditional $0 custody** — best for long holds; min HK$50 | 0.20% rate mediocre for big trades |
| **Wing Lung 永隆** | tiny commission **min HK$4.88** → best bank for small trades | HK$120/yr custody |
| **DBS 星展** | **no commission minimum** (0.20%) → great for small trades | 0.025%/yr custody (~HK$250 on HK$1M) |
| **CNCBI 中信国际** | diamond tier 0.15% | 0.25% standard rate; HK$200 custody |
| **HSBC 汇丰** | largest network, convenience | 0.25% + HK$100 min + HK$300/yr custody — pricey |
| **BOCHK 中银香港** | monthly-plan **$0-commission promo** | **worst by default**: HK$2,000/yr custody + HK$75 div min |

## 7. Scenario index (A–J)

| Scenario | Setup | Teaches |
|---|---|---|
| **A** | 2 ETFs, HK$40k/mo DCA | small-trade baseline; minimums bind |
| **B** | single ETF, long-term hold | custody waiver is the whole game |
| **C** | 1 ETF + 2 bank stocks, HK$500k | stamp duty on stocks; custody for the hold |
| **D** | one holding, HK$500k | stock vs ETF; monthly ETF → ICBC min HK$20 |
| **E** | one holding, HK$800k (~HK$66k/trade) | trade size flips ranking to ICBC |
| **F** | HK$3M anti-sanctions (gold+USD+stock) | ICBC-Wealth: 0.1% tier + no dividend fee on gold/USD |
| **G** | 12 institutions, HK$1M (03070+03466), lump-sum | broker vs bank; dividend-min driven |
| **H** | 12 institutions, HK$1M into 03466, **HK$80k×12** | **big trades → rate decides** (ICBC) |
| **I** | 12 institutions, HK$1M into 02800, **HK$16.7k×60** | **small trades → minimums bind** (mirror of H) |
| **J** | 13 institutions (7 banks + 6 brokers), HK$1M into 02800, **HK$10k×100** | **extreme small-trade**: zero-fee brokers crush banks |

## 8. Methodology & assumptions

- **Fees are verified** against each institution's official online schedule (banks: latest 2026 schedules; brokers: June 2026 pages — see README [Sources](README.md#sources--数据来源)). Broker fees are **promo-driven**; standing $0-commission offers are common.
- **"Year 1"** = the first 12 monthly buys + custody on the (growing) balance + the year's dividends + government levies. For DCA plans that run multiple years, **commission repeats every year of the build** — the README states cumulative commission separately.
- **"Steady-state / Year N+"** = fully invested, **buying stopped**, so only custody + dividend remain.
- **Dividends:** 02800 ≈ 2.9% yield, **semi-annual** (2 big payouts → % beats the minimum). Monthly-paying ETFs (e.g. 03466) → 12 small payouts → the **minimum** binds.
- **Stamp duty:** 0.1% on **stocks**; **ETFs are exempt** — most scenarios use ETFs, so stamp duty is HK$0.
- **Promotions** (Futu $0-forever, BOCHK monthly-plan $0, new-account offers) are noted **separately**, not baked into the headline standard-rate numbers, so the comparison stays apples-to-apples.
- **Rounding:** totals are shown with `~` and rounded to the nearest ~HK$5–10; they are cost *estimates*, not quotes.

## 9. Maintaining this repo

**Regenerate the charts** (after editing fee data):
```bash
python3 charts/gen_charts.py      # writes charts/scenario*_*.png
```
Requires `matplotlib`; a CJK font (PingFang/Heiti/Arial Unicode) renders the Chinese labels — it falls back gracefully if none is installed.

**Add a new scenario:**
1. Add a `DATA_X` list in `charts/gen_charts.py` as `(label, year1_total, steady_state_annual)` triples, plus two `bar(...)` calls.
2. Run the generator to produce `charts/scenarioX_*.png`.
3. Add the scenario section to `README.md` in **both** English and 中文 (mirror the structure of Scenario I/J).
4. Add a row to the **quick-reference table** at the top.
5. Update **[Sources](README.md#sources--数据来源)** if new institutions/fees were used.

**Update a fee:** change it in the README fee table(s) **and** the matching `DATA_*` triple, then regenerate charts. Keep EN and 中文 in sync.

## 10. Glossary

| Term | 中文 | Meaning |
|---|---|---|
| Commission | 佣金 | broker/bank charge to execute a trade, a % with a minimum |
| Platform fee | 平台费 | flat per-order fee charged by brokers on top of (or instead of) commission |
| Custody / safekeeping | 托管费 | annual fee for holding securities in your account |
| Dividend collection | 代收股息费 | handling fee deducted from each cash dividend |
| Stamp duty | 印花税 | 0.1% government tax on **stock** trades; **ETFs exempt** |
| Levies | 征费 | small SFC/AFRC/HKEX/CCASS fees, identical at every institution |
| DCA | 月供 / 定投 | dollar-cost averaging — buying a fixed amount on a schedule |
| Board lot | 一手 | the minimum tradable share quantity; sub-lot buys use odd-lot market or a monthly plan |
| Wealth tier | 理财金 / 财富管理 | premium account status that often waives custody (e.g. ICBC needs ~HK$1M) |
| Withholding tax | 预扣税 | a **tax** on dividends set by the holding + your residency — **not** a bank fee, equal across institutions |

## 11. Disclaimers

- **Educational cost estimate — not** financial, tax, or investment advice.
- Fees and promotions **change**; confirm with each institution before acting.
- **Withholding tax ≠ handling fee.** Dividend withholding is a tax (e.g. ~10% on mainland H-shares at fund level, 20% via Stock Connect for individuals); it's identical across institutions and doesn't affect which is cheapest. PRC tax residents may have offshore self-reporting duties — **consult a tax professional.**

---

# 中文

## 1. 这是什么、给谁用

本仓库精确回答一个问题：**「对于给定的港股/ETF 投资计划，这 13 家机构里哪家最省 —— 首年、以及之后每一年？」**

- **覆盖机构：** 7 家银行（汇丰、中银香港、渣打、工银亚洲、中信国际、星展香港、永隆）+ 6 家券商（富途、盈立、老虎、华盛、长桥、尊嘉）。场景 G–I 另含东亚、建行亚洲、恒生、南商。
- **适用人群：** 比较在港跑分红 ETF 或长揸计划的散户；开离岸港股账户的内地投资者；任何想算清**全包真实成本**（而非只看标称佣金）的人。
- **不是什么：** 不选股、不预测收益、不提供税务建议。它**只比费用**，投资计划固定不变。

## 2. 60 秒上手

1. 打开 README 里的**[场景速查表](README.md#-scenario-quick-reference--场景速查表)**。
2. 找到**交易额、频率、持仓类型**与你相似的那一行。
3. 读它的「最省」格 —— 看首年和长期持有各自的赢家。
4. 若无完全匹配，用下面的**[决策框架](#5-决策框架--按你的画像选)** —— 它把规则一般化，任何计划都能推理。

**多数人需要的一句话答案：** **小额、高频买入** → **近零佣金券商**（尊嘉佣金最省）胜过所有银行；**停止交易后的长期持有** → 任何 **$0 托管**的（6 家券商，加银行里的渣打、工银理财金）都赢；银行贵就贵在**高佣金最低收费**与**托管费**。（券商仍收约 0.2%/最低 HK$30 的代收股息费 —— 见 §3 —— 故无一真正「零费」。）

## 3. 五种费用 —— 港股账单解剖

本仓库每一笔成本都属于以下五种之一。知道你的计划里哪一种**咬住**，就知道谁赢。

| # | 费用 | 何时收 | 典型大小 | 伤到谁 |
|---|---|---|---|---|
| 1 | **佣金** | 每次**买**和**卖** | 银行 0.138%–0.25%，**最低 HK$50–100**；券商 ~0–0.03% | 小额交易（**最低收费**变成极高实际百分比） |
| 2 | **平台费** | 每单 —— **仅券商** | HK$1（尊嘉）· HK$12（盈立）· HK$15（富途/华盛/长桥/老虎） | 高频买入者（按单收） |
| 3 | **托管费** | **持有期间，按年** | 银行 HK$120–2,000/年；**券商 $0** | 已停止交易的长期持有者 |
| 4 | **代收股息费** | **每次派息** | 银行 0.5%，**最低 HK$30**（中银 HK$75、工银 HK$20）；券商 **0.2%/最低 HK$30**（另或有登记过户费 ~HK$1.5/手） | 多次小额派息（月派 ETF） |
| 5 | **政府/交易所征费** | 每笔 —— **各家相同** | ~0.0085% + 中央结算（小额约 HK$2–3/笔）；**印花税 0.1%** | 不区分高下 —— 但**印花税只打股票，不打 ETF** |

**最重要的机制 —— 最低收费是伪装的百分比。**
HK$100 佣金最低收费摊在 **HK$10,000** 交易上 = **实际 1.0%**；同样的最低收费摊在 **HK$100,000** 上 = **0.1%**。所以*同一张费率表*，大额时让银行便宜、小额时让它惨烈。这就是为什么各场景答案会翻转。

## 4. 三条经验法则（附算式）

| 法则 | 适用 | 赢家 | 算式 |
|---|---|---|---|
| **小额拼最低收费** | 每笔 ≤ ~HK$3 万 | 低/无最低收费的：**券商**，其次**永隆**（最低 HK$4.88）、**星展**（无最低） | HK$100 最低 ÷ HK$1 万 = **1%**；对比永隆真实 0.18% |
| **大额拼费率** | 每笔 ≥ ~HK$6 万 | **工银**（0.138%，或 **≥HK$100 万 0.1%**）；券商仍更省 | 无最低收费咬住，故 0.138% ≪ 0.25% —— 工银约为大行一半 |
| **长揸拼托管** | 停止交易、只持有 | **$0 托管**的：全部**券商**，加**渣打**与**工银理财金** | 佣金已付完；托管 HK$0 对比 HK$2,000/年（中银）逐年累积 |

**股息推论：** 若持**月派** ETF，**股息最低收费**决定胜负（12+ 次 × 各家最低）。工银 HK$20 胜、中银 HK$75 最差。若持**半年派**（如 02800），两次大额派息超过所有最低收费，故股息费近似相等，**托管**打破平手。

## 5. 决策框架 —— 按你的画像选

回答四个问题，再读表。

**Q1. 交易额？** 小（≤HK$3 万）· 中（HK$3–6 万）· 大（≥HK$6 万）
**Q2. 多久买一次？** 一次性 · 月供 · 频繁
**Q3. 持有期？** 频繁交易 · 长揸数年
**Q4. 持有什么？** ETF（免印花税）· 个股（0.1% 印花税）· 黄金/美元（无股息费）

| 你的画像 | 首年最省 | 长期持有最省 | 避免 | 场景 |
|---|---|---|---|---|
| 小额月供 ETF（≤HK$2 万/笔） | **尊嘉** → 全部券商；银行：永隆/星展 | 券商、渣打、工银理财金（全 $0 托管） | HK$100 最低收费银行（汇丰/中信/中银） | **I, J** |
| 大额交易（≥HK$6 万） | **富途**；银行：**工银**（0.138%） | 渣打/富途/工银理财金 | 0.25% 银行（汇丰/恒生/南商） | **E, H** |
| 大额一次性 ≥HK$100 万后持有 | **富途**；银行：**工银理财金** | **工银理财金**（≥100 万 0.1% + $0 托管） | 中银香港 | **G, F** |
| 月派 ETF（年 12+ 次派息） | 富途；银行：**工银**（股息最低 HK$20） | 工银理财金 | **中银香港**（股息最低 HK$75 + HK$2,000 托管） | **G, H** |
| 长揸单一持仓、停止交易 | 渣打 / 永隆（入场低） | **渣打**或**工银理财金**（无条件 $0 托管） | 收托管费的银行 | **B, C, D** |
| 个股（非 ETF） | 每次买入计 **+0.1% 印花税** | 渣打（托管） | —（印花税各家相同） | **C, D** |
| 抗制裁（黄金+美元+股票） | **工银理财金** | **工银理财金** | — | **F** |

**小额场景内置的两个提醒：**
- **一手门槛。** HK$1 万订单常不足一手（02800 约 HK$12,500/手）。须经**月供股票计划**（凑碎股/零股）或碎股市场执行 —— 这也解锁**月供 $0 佣金推广**（中银、汇丰及券商）。
- **券商阶梯计划。** 老虎 HK$15/单是*固定*计划；其*阶梯*计划在 **≤5 单/月时为 HK$30/单** —— 月供请选固定计划。

## 6. 机构画像

### 券商（全部 $0 托管、ETF 免印花税）
| 券商 | 优势 | 陷阱 / 提醒 |
|---|---|---|
| **尊嘉 Snowball** | **$0 佣金 + HK$1/单**平台费 —— 小额/高频*佣金*最省 | 仍收代收股息费 0.2%/最低 HK$30 **+ 登记过户费 HK$1.5/手（最低 HK$31.9）**/次；体量较小 —— 须核实 |
| **富途 Futu** | App/社区龙头；常设**终身 $0 佣金**推广 + HK$15 平台费 | 平台费按单收，高频累积 |
| **盈立 uSMART** | **HK$12/单**（免佣计划）—— 仅次于尊嘉；AI/网格工具 | 阶梯计划；确认所在计划 |
| **长桥 Longbridge** | **终身 $0 佣金** + HK$15 平台费（可低至 HK$3） | 股息费未公布 —— 须核实 |
| **华盛 Valuable** | 新浪系；0.03%/最低 HK$3 + HK$15；常有开户优惠 | 标准档，非最省 |
| **老虎 Tiger** | 纳斯达克上市；期权/全球工具强；0.029% + HK$15（固定） | **阶梯计划 ≤5 单/月为 HK$30** —— 用固定计划 |

### 银行
| 银行 | 优势 | 陷阱 / 提醒 |
|---|---|---|
| **工银亚洲** | 银行最低**费率**（0.138%，**≥HK$100 万 0.1%**）；**股息最低 HK$20**；达标即 **$0 托管** | **HK$88 佣金最低**杀小额；免托管需 HK$100 万（理财金）或 HK$20 万周转 |
| **渣打** | **无条件 $0 托管** —— 长揸最佳；最低 HK$50 | 0.20% 费率对大额一般 |
| **永隆** | 佣金**最低 HK$4.88** → 小额最佳银行 | HK$120/年 托管 |
| **星展** | **无佣金最低收费**（0.20%）→ 小额佳 | 0.025%/年托管（HK$100 万约 HK$250） |
| **中信国际** | 钻石档 0.15% | 标准 0.25%；HK$200 托管 |
| **汇丰** | 网点最广、方便 | 0.25% + 最低 HK$100 + HK$300/年托管 —— 贵 |
| **中银香港** | 月供计划 **$0 佣金推广** | **默认最差**：HK$2,000/年托管 + HK$75 股息最低 |

## 7. 场景索引（A–J）

| 场景 | 设定 | 教什么 |
|---|---|---|
| **A** | 两只 ETF，HK$4 万/月供 | 小额基线；最低收费咬住 |
| **B** | 单只 ETF，长揸 | 免托管是全部关键 |
| **C** | 1 ETF + 2 银行股，HK$50 万 | 个股印花税；持有拼托管 |
| **D** | 全仓单一，HK$50 万 | 股票 vs ETF；月派 ETF → 工银最低 HK$20 |
| **E** | 全仓单一，HK$80 万（~HK$6.6 万/笔） | 交易额翻转排名至工银 |
| **F** | HK$300 万抗制裁（黄金+美元+股） | 工银理财金：0.1% 档 + 黄金/美元无股息费 |
| **G** | 12 机构，HK$100 万（03070+03466），一次性 | 券商 vs 银行；股息最低收费主导 |
| **H** | 12 机构，HK$100 万买 03466，**HK$8 万×12** | **大额 → 拼费率**（工银） |
| **I** | 12 机构，HK$100 万买 02800，**HK$1.67 万×60** | **小额 → 拼最低收费**（H 的镜像） |
| **J** | 13 机构（7 行 + 6 券商），HK$100 万买 02800，**HK$1 万×100** | **极端小额**：零费券商压倒银行 |

## 8. 方法与假设

- **费用均已核实**，对照各机构官方网上费率表（银行：2026 最新；券商：2026 年 6 月页面 —— 见 README [数据来源](README.md#sources--数据来源)）。券商费率**受促销驱动**，常设 $0 佣金推广普遍。
- **「首年」** = 首 12 笔月供 + 当年（增长中）余额的托管 + 当年股息 + 政府征费。多年期月供计划中，**建仓的每一年都重复佣金** —— README 另列累计佣金。
- **「稳态 / 第 N 年起」** = 满仓、**停止买入**，故只剩托管 + 股息。
- **股息：** 02800 约 2.9% 股息率、**半年派**（2 次大额 → 百分比超过最低收费）。月派 ETF（如 03466）→ 12 次小额 → **最低收费**咬住。
- **印花税：** **股票** 0.1%；**ETF 豁免** —— 多数场景用 ETF，故印花税为 HK$0。
- **促销**（富途终身 $0、中银月供 $0、开户优惠）**单独注明**，不并入标准费率的标题数字，使对比同口径。
- **取整：** 总额以 `~` 标示、就近取整至约 HK$5–10；为成本*估算*，非报价。

## 9. 维护本仓库

**重新生成图表**（改完费率数据后）：
```bash
python3 charts/gen_charts.py      # 输出 charts/scenario*_*.png
```
需 `matplotlib`；中文标签需 CJK 字体（PingFang/Heiti/Arial Unicode），无字体时优雅回退。

**新增场景：**
1. 在 `charts/gen_charts.py` 加一个 `DATA_X` 列表，元素为 `(标签, 首年总额, 稳态年额)` 三元组，再加两个 `bar(...)` 调用。
2. 运行生成器产出 `charts/scenarioX_*.png`。
3. 在 `README.md` 用**英文与中文双语**加场景章节（仿场景 I/J 结构）。
4. 在顶部**速查表**加一行。
5. 若用了新机构/费率，更新 **[数据来源](README.md#sources--数据来源)**。

**更新费率：** 同时改 README 费率表**与**对应 `DATA_*` 三元组，再重新生成图表。保持中英同步。

## 10. 术语表

| 术语 | 英文 | 含义 |
|---|---|---|
| 佣金 | Commission | 执行交易的收费，按百分比并设最低 |
| 平台费 | Platform fee | 券商在佣金之外（或代替）按单收的固定费 |
| 托管费 | Custody | 在账户内持有证券的年费 |
| 代收股息费 | Dividend collection | 从每次现金股息中扣的手续费 |
| 印花税 | Stamp duty | **股票**交易的 0.1% 政府税；**ETF 豁免** |
| 征费 | Levies | 证监会/财汇局/港交所/结算的小额费，各家相同 |
| 月供 / 定投 | DCA | 按计划定期定额买入 |
| 一手 | Board lot | 最小可交易股数；不足一手走碎股市场或月供计划 |
| 理财金 / 财富管理 | Wealth tier | 常可免托管的高端账户档（如工银需约 HK$100 万） |
| 预扣税 | Withholding tax | 股息上由持仓 + 你的税务身份决定的**税** —— 非银行费、各家相同 |

## 11. 免责声明

- **教育性成本估算 —— 非**投资、税务或财务建议。
- 费率与促销会**变动**；行动前请向各机构确认。
- **预扣税 ≠ 手续费。** 股息预扣是税（如内地 H 股基金层面约 10%、港股通个人 20%）；各家相同，不影响谁最省。内地税务居民对境外收益或有自行申报义务 —— **请咨询专业税务师。**

---

*Generated with [Claude Code](https://claude.com/claude-code).*
