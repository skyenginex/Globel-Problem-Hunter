  # Global Problem Hunter

A Claude skill that takes a team from *"what should we build?"* to *"we're solving one of these ten problems"* — with evidence, not guesses.

It ranks candidate verticals, mines the chosen one for real and cited pain, then scores and reports the ten most solvable and most monetizable problems as an Obsidian problem index.

Built for founders, indie hackers, and small teams doing pre-MVP discovery, hackathon scoping, or looking for a wedge into an existing market. Scoped to **US and Western European B2B SaaS**.

---

## What makes it different

Most idea-generation tools generate *ideas*. This one hunts *problems*, and it refuses to let you skip the evidence.

**Problems, not ideas.** Every pain is written in one shape:

> **[Who]**, **[in what situation]**, **[struggles with what]**; today they solve it by **[how]**.

That last clause is load-bearing. If nobody can say how they cope today, the problem probably isn't real. Answers like *spreadsheet*, *whiteboard*, *paper binder*, or *we hired someone for it* are the strongest signals available — a human is already spending effort, so the pain is real and already has a budget line.

**The seam requirement.** In the US and Western Europe nothing is unserved; every vertical already has three to ten incumbents. So the skill never asks "is this space empty?" (it isn't) but "**where is the seam?**" Five seams a small team can realistically enter through:

| Seam | What it looks like |
|---|---|
| Underserved sub-vertical | Incumbents serve "field service"; nobody serves pool cleaners, whose workflow the generic tool actively fights |
| Workflow adjacency | Incumbents own the core record and ignore the ugly step before or after it |
| Price tier gap | Incumbents start at $200/seat; the 3-person shop is priced out and on a spreadsheet |
| Regulatory shift | A new mandate creates a compliance job no existing tool covers yet |
| Platform shift | A new channel, API, or device incumbents' architecture predates |

A problem with no nameable seam **cannot enter the top ten**, regardless of score. Entering a well-served market without one means losing on someone else's terms with less money and fewer people.

**Multiplication, not addition.** Ranking is Solvability × Monetizability, not the sum. A problem scoring 2 on one axis is dead even if it scores 10 on the other — summed it reaches 12 and sits mid-table, multiplied it reaches 20 and sinks, which is where it belongs.

**The evidence ladder.** Not all evidence is equal, so every raw pain is rated ★ to ★★★★:

| Strength | Evidence type |
|---|---|
| ★★★★ | A job posting (**a salary is being paid** for this work) · a paying customer of an incumbent complaining · a documented penalty |
| ★★★ | The same pain across 3+ independent sources · an incumbent pricing page · an in-force mandate with a deadline |
| ★★ | A single community post, review, or stated business-exit reason |
| ★ | Blog post, trend article, vendor-published report |
| ✗ | Your own inference — enters the report tagged `⚠️ unverified` |

**A problem with no ★★★★ evidence cannot score above 7 on monetizability.** No salary, no paying complainer, no penalty means willingness to pay is unproven, however good the story sounds.

**Persona discipline.** The subtlest failure mode is collecting eight real, well-sourced pains that all belong to the wrong person. Customer complaints ("they gave me an appointment and nobody showed") are valuable but can't enter the list raw — they must be translated into the operator's gap ("shops can't confirm dispatch, so no-shows aren't caught") before they count.

---

## How it works

### Stage 0 — Context

Asks where the team has unfair access or insider knowledge, their technical strength, what to rule out, and whether they can reach these buyers at all. In a crowded market, insider access is often the only real advantage — so this is not a formality.

### Stage 1 — Rank verticals

Narrows to 8–12 candidates and scores each on five criteria: **reachability, pain intensity, willingness to pay, technical fit, wedge availability**. Presents a table and **lets you choose** — the decision depends on the team's motivation and access, which the skill doesn't have.

Two hard overrides: reachability of 1 eliminates regardless of total (you can't validate a problem for people you can't reach), and wedge availability of 1 does the same.

### Stage 2 — Mine the vertical for pain

Six veins, each answering a different question. Research fed by one vein inherits that vein's blind spots.

| # | Vein | Question | Target |
|---|---|---|---|
| 1 | Practitioner communities | What do operators say to each other? | 5+ |
| 2 | Review sites | What do paying customers hate? | 5+ |
| 3 | Regulation | What are they *required* to do? | 3+ |
| 4 | Incumbents | What's sold, at what price, missing what? | 5+ |
| 5 | Job postings | What work is someone paying a salary for? | 3+ |
| 6 | Field and local | What breaks in daily operations? | 5+ |

Target is **30–40 raw pains** before any filtering, within a **40–60 query budget**.

### Stage 3 — Score and report

Scores survivors, ranks by the product, names the seam for each, and writes one Obsidian note per problem plus an index note — YAML frontmatter for Dataview queries, `[[wikilinks]]` both directions for graph view.

---

## Requirements

**Firecrawl (`firecrawl_search`) is strongly recommended.** Measured in testing:

| Source | Without Firecrawl | With Firecrawl |
|---|---|---|
| Reddit | **Completely closed** — every URL returns 403, `site:reddit.com` search returns essentially nothing | Fully mineable via `includeDomains: ["reddit.com"]` |
| G2 / Capterra / TrustRadius | Limited | Fully mineable, including pricing and churn fields |

`includeDomains` is the single highest-leverage parameter in the whole workflow — it converts the two richest veins from unreachable to fully mineable. Without it, veins 1 and 2 are largely closed and the skill will say so in the report rather than quietly producing a thinner list.

Everything else (regulator sites, vendor pages, job boards, trade forums) works with ordinary web search and fetch.

Browser automation is optional — only Google Maps and Yelp reviews need it.

---

## Files

```
global-problem-hunter/
├── SKILL.md                            entry point: the three stages, wedge framing, defaults
├── references/
│   ├── vertical-scoring.md             5-criterion rubric + ~50 candidate verticals (US/EU)
│   ├── research-sources.md             the six veins, subreddit discovery, access table,
│   │                                   persona discipline, evidence ladder, record format
│   ├── search-patterns.md              operator craft, ~90 patterns grouped by intent,
│   │                                   query budget, stopping rules, search log
│   └── problem-scoring.md              solvability × monetizability rubric, seam gate,
│                                       "they'll pay" and "they won't pay" signals
├── assets/
│   ├── problem-report-template.md      the per-problem Obsidian note
│   └── index-template.md               the 00 - Problem Index note
├── scripts/
│   └── query_gen.py                    generates the query sweep from the pattern library
└── evals/
    └── evals.json                      4 test prompts with assertions
```

Claude reads `SKILL.md` on trigger and pulls the reference files as each stage needs them — you don't have to load anything yourself.

---

## The query generator

Hand-writing 40–60 queries every run leaves coverage to chance; dropping a synonym or skipping a vein is easy to do and hard to notice.

```bash
python scripts/query_gen.py "auto repair shop" \
  --synonyms "independent mechanic,service advisor,auto shop owner" \
  --competitors "Tekmetric,Shop-Ware,Mitchell1" \
  --city "Austin" --format md
```

Produces a search-log table grouped by intent, with the right `includeDomains` hint per group.

| Flag | Purpose |
|---|---|
| `--synonyms` | Insider terms practitioners actually use — every vertical has an outsider word and an insider word, and the insider one finds the real communities |
| `--competitors` | Unlocks the churn queries. Run C4 first to discover incumbent names, then re-run with them |
| `--city` | For the local/field vein |
| `--intent 1,2,5` | Only these intent groups |
| `--limit N` | Per-group cap (default 12, matching the budget). `--limit 0` for the full cross-product |
| `--format md` | Markdown search-log table instead of plain lines |

Two implementation details that matter: queries are ordered **term-major** so that cutting at the limit leaves many *distinct patterns* rather than one pattern repeated across synonyms, and source pools are **interleaved round-robin** so the Reddit and review-site queries always get a share of the cap instead of being crowded out by the general pool.

The script invents nothing — `search-patterns.md` is the source of truth. Add a pattern there first, then to the script.

**Two rounds, always.** Round one uses outsider vocabulary and returns mediocre results. Stop, harvest the jargon practitioners actually use, and run round two with those words. Round two is almost always sharply better — reserve about a third of the budget for it.

---

## Operating rules worth knowing

These exist because each one was a real failure in testing:

- **Two-attempt rule.** If a source resists two different approaches, stop and substitute. Ten queries against a blocked source burns a sixth of the budget for nothing.
- **Saturation.** No new pain across five consecutive searches in a vein means that vein is done.
- **Throttle Firecrawl to 2–3 concurrent calls.** Large parallel batches return 429 and lose roughly twenty queries. Parallelize in small waves.
- **Never fake an empty vein.** "Vein 5 produced one posting" is worth immeasurably more than three invented ones. Honest gaps beat fabricated coverage.
- **Preserve quotes verbatim.** *"I close the shop for a full day every month just to count parts"* is evidence. *"Users are frustrated with inventory tracking"* is not.
- **Show the arithmetic** on any market-size estimate, and flag the assumption.

---

## Validation is online

This market can't be validated by walking into a shop, so every problem report names a concrete online path: which subreddit or community to post the question in, which job title to cold-DM, which reviewer who left a 2-star review to contact.

Each report ships with six interview questions that **ask about the past, never about the idea**. "Would you use this?" produces polite lies; "walk me through the last time this happened" produces facts.

Ten reports without ten conversations are ten hypotheses.

---

## Tested

Stage 2 was run live against US independent auto repair shops:

- **38 raw pains**, all six veins producing evidence
- Real profession subreddits found and mined — `r/serviceadvisors`, `r/partscounter`, `r/Justrolledintotheshop` — with verbatim quotes and working URLs
- Capterra's **"Switched from"** field yielded named churn: Tekmetric customers arriving from Manager SE, RO Writer, and ALLDATA, with stated reasons — the most direct route to a wedge that exists in public data
- ★★★★ salary evidence found: Service Advisor $65k–150k, Parts Specialist $30–45/hr at named shops
- Inaccessible sources (Google Maps, Yelp) reported honestly rather than fabricated

10 of 10 assertions passed. The one fix that came out of it — the Firecrawl throttling rule — is now in the skill.

---

## Related

A sibling skill, `pazar-problem-avcisi`, does the same job for the **Turkish market** in Turkish. It shares the core design — multiplication scoring, evidence ladder, persona discipline, two-attempt rule — but swaps the sources (Ekşi Sözlük, Şikayetvar, GİB, chambers of commerce), drops the seam requirement (localization is usually the wedge there), and keeps validation face-to-face, since reaching users in person is realistic in that market and is the strongest filter available.
