# Problem Scoring Rubric

Every surviving pain is scored on two axes, 1-10 each. Ranking is by the **product** (Solvability × Monetizability, max 100).

Multiplication rather than addition, because a problem scoring 2 on one axis is dead even if it scores 10 on the other. Summed, it reaches 12 and sits mid-table; multiplied, it reaches 20 and sinks — which is where it belongs. A brilliant business idea you cannot build and a buildable idea nobody pays for are equally useless.

---

## Axis A — Solvability (1-10)

*"Can a 2-4 person team ship this in a few months by writing software?"*

Five sub-questions, then a holistic score:

**A1. Data dependency.** Does the product need a pre-existing dataset to work? A product powered by data the user enters is valuable on day one; a product that needs external data is an empty box until that data arrives. This is where most AI-flavored ideas quietly fail.

**A2. Integration load.** How many external systems must it connect to? Zero integrations scores full marks. Each accounting, payments, carrier, or industry-API integration adds calendar time *and* bureaucracy — partner applications, sandbox access, certification. In this market that bureaucracy is often longer than the engineering.

**A3. Network effects.** Is the product valuable to a single user, or worthless until both sides show up? Marketplace and matching ideas score 1-3 here. A product that can't deliver value to user one will never see user two.

**A4. Regulation and liability.** What happens if it's wrong? Patient data, financial transactions, statutory filings, safety records — all lower the score. Where an error means a fine or a lawsuit, MVP quality isn't enough, and enterprise buyers will demand SOC 2 before signing.

**A5. Time to demo.** How many weeks to something demonstrable? A practical constraint for any team with a deadline, and a proxy for how quickly you can start learning from real users.

### Bands

- **9-10** — Valuable to a single user, no integrations, CRUD plus workflow plus reporting. Demoable in weeks.
- **7-8** — One well-documented integration, or a modest calculation/logic engine.
- **5-6** — Several integrations, or genuine complexity: scheduling optimization, multi-tenant permissions, offline sync, real-time collaboration.
- **3-4** — Network effects required, or an ML component without available training data, or a heavy compliance burden.
- **1-2** — Hardware, gated data access, or not legal without a license.

---

## Axis B — Monetizability (1-10)

*"Will someone pay for this? Who, how much, how often?"*

**B1. Who pays?** Is the person feeling the pain the same person who controls the budget? When they're the same, the sales cycle is short — this is why owner-operated small businesses are attractive. When they differ (staff suffers, owner pays), a persuasion layer appears and the cycle lengthens.

**B2. Today's cost.** What is the problem costing right now? Hours lost × loaded hourly cost, missed jobs, penalties paid, extra staff employed, consultants retained. **If you can compute this number, pricing follows automatically** — a problem costing $60k/year makes $500/month trivial to defend. If you can't compute it, you don't understand the problem well enough yet.

**B3. Buying habit.** Does this audience already buy software? Convincing someone already paying for an industry tool is far easier than convincing someone who has never paid for software. "We already use [incumbent]" is good news, not bad.

**B4. Frequency.** Daily, monthly, or annual? Daily problems sustain subscriptions. Annual problems (tax filings, license renewals) can carry high pain but produce one-off purchases and brutal churn.

**B5. Market size.** How many businesses have this pain? Rough TAM: *business count × plausible monthly price × 12*. If you can't find the count, flag the estimate and show your arithmetic.

**B6. Expansion path.** Does revenue grow as the customer grows — more seats, locations, volume, or a natural upsell? In this market, per-customer revenue that stays flat forever makes the economics hard, because acquisition costs are high.

### Bands

- **9-10** — B2B, measurable dollar loss, payer is the sufferer, daily use, existing software budget, seat or volume expansion.
- **7-8** — B2B with a weak buying habit, or clear but unquantified pain.
- **5-6** — Budget exists but purchasing is slow: approval chains, enterprise procurement, public sector.
- **3-4** — Consumer, low price tolerance, free-tier expectations.
- **1-2** — No identifiable payer, or no model beyond ads/commission (both require scale you won't have).

**Evidence gate:** a problem with no ★★★★ evidence cannot exceed **7** on this axis. No salary being paid, no paying customer complaining, no penalty for non-compliance means willingness to pay remains unproven regardless of how compelling the story is. Ladder in `research-sources.md`.

---

## The seam multiplier

Solvability and monetizability describe the problem. In a mature market, a third question decides whether *you* can win it: **what seam do you enter through?**

This isn't a numeric axis — it's a gate. Name the seam for every problem in the top 10:

1. **Underserved sub-vertical** — incumbents serve the category; nobody serves this specific niche whose workflow differs
2. **Workflow adjacency** — incumbents own the core record and ignore the ugly step before or after it
3. **Price tier gap** — incumbents start well above what the smallest operators can pay
4. **Regulatory shift** — a new obligation no existing tool covers yet
5. **Platform shift** — a new channel, API, or device incumbents' architecture predates

**If you cannot name a seam, the problem doesn't belong in the top 10** — no matter how well it scores. In this market, entering without a seam means losing on someone else's terms with less money and fewer people.

Record the seam in the report's frontmatter. It becomes the positioning sentence later.

---

## Ranking and interpretation

| Product | Interpretation |
|---|---|
| 70-100 | Finalist. Take it straight to user conversations. |
| 45-69 | Strong candidate. Rises if the weaker axis can be shored up. |
| 25-44 | Keep in the pool, but not a priority. |
| Under 25 | Keep it listed **with the reason it was cut** — writing down why prevents the same idea resurfacing in three weeks. |

## Score honestly

Inflating scores so the report looks impressive is the most expensive mistake available here: the team spends months on a weak problem and finds out only after the code is written. Don't hesitate to score low — **if all ten problems land above 80, the rubric wasn't applied.**

Write a **one-sentence rationale** next to every score. A score without a rationale can't be argued with, and a table that can't answer "why a 7?" in a team meeting is decoration.

## "They'll pay" signals

Concrete findings that raise the monetizability score. State which ones you found:

- Someone is **already employing staff** for this work — the strongest signal; a salary is being paid
- Someone is **already paying another product** and complaining about it
- There are documented cases of **fines or losses** caused by the problem
- People spend **regular, patient manual effort** on it (spreadsheets, whiteboards, paper, copy-paste)
- **Consultants or agencies** sell this as a service by the hour
- Incumbents' **pricing pages** show an established band for adjacent functionality

None of these present means the problem may be interesting, but monetizability stays at or below 5.

## "They won't pay" counter-signals

Equally worth naming, because they're easy to miss when a problem sounds good:

- The pain is real but **occasional** — an annual annoyance, not an operating cost
- The workaround is **free and adequate** — a spreadsheet that genuinely works is a formidable competitor
- The buyer is **fragmented and tiny** — thousands of one-person operations with no budget and no shared channel to reach them
- The workflow is **already bundled** into software they must buy anyway; a standalone tool competes with "free with the thing I already own"
- Switching means **migrating years of historical data**, and nobody will
