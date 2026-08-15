---
name: global-problem-hunter
description: Three-stage idea finder for global (US and Western European) SaaS markets — ranks candidate verticals, mines a chosen vertical for real, evidenced pain, then scores and reports the 10 most solvable and most monetizable problems as an Obsidian problem index. Use this skill whenever the user says anything like "find us a market", "what should we build", "help us pick a niche", "find startup ideas", "market research for a new product", "build a problem pool", "which problem should we solve", "find a profitable problem", "validate a SaaS idea", or "we need a B2B SaaS idea". Also trigger when the user never says "market" or "problem" at all and just says something like "we don't know what to build, we need a product idea" or "we've been going in circles for weeks". Built for founders, indie hackers, and small teams doing pre-MVP discovery, hackathon or competition scoping, or picking a wedge into an existing market.
---

# Global Problem Hunter

This skill takes a team from "what should we build?" to "we're solving one of these 10 problems." The goal is not to generate ideas — it is to **find problems**. Ideas are cheap; an evidenced problem is expensive.

Output: one Obsidian note per problem plus an index note linking them.

## Core principle: problems, not ideas

The most common failure is starting with "let's build an app that…". This skill blocks that. Every problem is written in one shape:

> **[Who]**, **[in what situation]**, **[struggles with what]**; today they solve it by **[how]**.

*Example:* "Independent auto repair shops, when ordering parts mid-job, can't tell customers when the car will be ready; today they call the supplier and guess."

The "today they solve it by" clause is the load-bearing part. If there is no answer, the problem probably isn't real or nobody cares. Answers like spreadsheets, WhatsApp/SMS, a paper binder, a whiteboard, or "we hired someone to do it" are the strongest possible signals: a human is already spending effort, so the pain is real and already has a budget line.

## Scope defaults

- **Market:** United States and Western Europe. Highest willingness to pay, most mature SaaS buying habits, and by far the richest public evidence.
- **Buyer:** B2B, small to mid-sized businesses. Consumer markets have far weaker payment signals and are out of scope unless the user asks.
- **Language:** research and reports in English.
- **Team assumption:** 2-4 person software team, limited budget, a few months of runway. "Solvability" is scored against *that* team, not against a funded startup.

If the user names a different market, buyer, or team size, follow them instead.

## The wedge problem (read this before Stage 1)

In a small or emerging market, being early is enough. In the US and Western Europe, almost nothing is unserved — every vertical already has three to ten established tools. A small team that enters without a wedge loses on features, sales, and budget.

So the question is never "is this space empty?" (it isn't) but "**where is the seam?**" Five seams that a small team can realistically enter through:

1. **Underserved sub-vertical.** The incumbent serves "field service"; nobody serves pool cleaners specifically, and pool cleaners have workflows the generic tool actively fights.
2. **Workflow adjacency.** The incumbent owns the core record but ignores the ugly step before or after it — quoting, handoff, reconciliation, the customer-facing part.
3. **Price tier gap.** Incumbents start at $200/seat and target 50-person companies. The 3-person shop is priced out and using a spreadsheet.
4. **Regulatory shift.** A new mandate creates a compliance job that no existing tool covers yet. This is the fastest path to revenue because the budget already exists.
5. **Platform shift.** A new channel, API, device, or integration surface that incumbents haven't adopted because their architecture predates it.

Carry this framing through all three stages. In Stage 3 every problem report must name which seam it enters through — a problem with no identifiable seam is a problem you will lose.

## Stage 0 — Gather context

Before researching, ask the user briefly (use AskUserQuestion if available, in a single turn):

1. Where does the team have **unfair access or insider knowledge**? Past jobs, an industry a family member works in, a community they're already part of. In a crowded market this is often the only real advantage.
2. What is the team's technical strength? (web, mobile, data/ML, infra, integrations)
3. Anything to rule out? Industries they refuse, regulatory burden they can't carry, geographies they can't serve.
4. Distribution reality: can they reach these buyers at all? Existing audience, community membership, cold outbound tolerance.

If the user says "just pick for me," proceed with defaults and state the assumptions at the top of your output.

Also confirm the Obsidian vault path in this stage. If the user hasn't said, propose a `Problems/` folder in the current project and confirm.

## Stage 1 — Rank verticals

Narrow from unbounded space to 8-12 candidate verticals, scored and presented for the user to choose from.

Read `references/vertical-scoring.md` for the candidate pool and the five-criterion rubric (reachability, pain intensity, willingness to pay, technical fit, wedge availability).

Keep research shallow here — one or two searches per vertical. You're looking for signs of life: number of businesses, software spend, a recent regulatory change, whether people are visibly complaining.

Present a table: vertical | five scores | total | one-sentence rationale. Surface the top three, but **let the user choose.** The decision depends on the team's motivation and access, which you don't have. Frame the options so a decision is possible: "X ranks first because…; but Y is closer to your insider access, which matters more than two points in this table."

## Stage 2 — Mine the vertical for pain

This is where the real work happens. Target: the vertical's **stated** pain, not your guesses about it.

Read both files before starting:
- `references/research-sources.md` — *where* to look: the six veins, subreddit discovery, the measured access table, evidence ladder
- `references/search-patterns.md` — *how* to search: operator craft, intent-organized pattern library, query budget

### The six veins

Each vein answers a different question. Research fed by one vein inherits that vein's blind spots.

1. **Practitioner communities** — Reddit profession subs, Discord/Slack communities, trade forums. People describe their work problems here with a candor they show nowhere else. Richest single vein.
2. **Review sites** — G2, Capterra, TrustRadius. Low-star reviews are written by people who *paid* and are still unhappy: problem, willingness to pay, and incumbent failure point in one text. Capterra's **"Switched from"** field is structured churn data — it names the product they abandoned.
3. **Regulation** — new mandates and compliance obligations. Obligation equals budget.
4. **Incumbents** — pricing pages, feature lists, changelogs, their own job postings. Competitors existing is good news; it proves the market. Their common blind spot is your seam.
5. **Job postings** — if someone is paying a salary to do this manually, the problem is real and the salary is your price ceiling. Strongest monetization evidence there is.
6. **Field and local** — Google reviews of actual businesses, "business for sale" listings and their stated reasons, trade YouTube channels. The operator won't say what's broken; their customer will.

**Target: 30-40 raw pains**, at least 3-5 per vein, before filtering. Filtering early means the best problem never makes the list.

### Generate queries, don't hand-write them

Hand-writing 40-60 queries leaves coverage to chance — skipping a synonym or a whole vein is easy.

```bash
python scripts/query_gen.py "<vertical>" \
  --synonyms "<insider terms practitioners actually use>" \
  --competitors "<incumbent product names>" \
  --format md
```

It expands the pattern library across synonyms, groups by intent, and prints a search log table. Run it once for discovery; once you've found the incumbent names in intent group C4, run it again with `--competitors` to unlock the churn queries.

### While researching

- **Search in parallel, but in waves of two or three.** Sequential searching costs the user's patience and buys nothing — yet Firecrawl returns 429 on large simultaneous batches, and a rate-limited query is a lost query. Small waves are both fast and reliable.
- **Use Firecrawl search where available.** Measured: it reaches Reddit, G2, and Capterra, which the plain web fetcher cannot. `includeDomains` is the highest-leverage parameter in this whole workflow. Full access table in `references/research-sources.md`.
- **Two-attempt rule.** If a source resists two different approaches, stop and move to a substitute. Writing ten queries against a blocked source burns a sixth of the budget for nothing.
- **Do two rounds.** After round one, stop and harvest the jargon: what do practitioners call themselves, what do they call the process, which product names recur? Run round two with those words. Round two is almost always more productive — reserve about a third of the budget for it.
- **Keep persona discipline.** Is this pain felt by the person who would *buy*, or by *their customer*? Customer complaints are valuable but cannot enter the list raw — translate them into the operator's gap first. See `research-sources.md`.
- **Rate every pain** on the evidence ladder (★ to ★★★★). It feeds scoring directly.
- **Preserve quotes verbatim.** The most persuasive line in the final report is never your summary; it's a practitioner's own words.

**Stopping rule:** if a vein produces no new pain across five consecutive searches, it's exhausted — move on. Stop entirely past 60 queries. If a vein comes up far short, **don't force it — record it.** "Vein 5 yielded one posting" is worth immeasurably more than three invented ones.

### Filtering raw pains

Eliminate these first:

- **Regulatory walls** — patient data, financial licensing, anything where a small team can't carry the compliance burden.
- **Network-effect plays** — marketplaces. Two-sided markets are where small teams die, because a working product with one side is worth nothing.
- **Hardware dependencies** — manufacturing and supply chain will eat the entire timeline.
- **No identifiable seam** — if the incumbents already do this well and cheaply, you will lose. Say so and move on.

## Stage 3 — Score and report the top 10

Score surviving pains with the rubric in `references/problem-scoring.md`. Two axes:

- **Solvability (1-10):** can *this* team ship it in *this* time by writing software?
- **Monetizability (1-10):** will someone actually pay, how much, how often?

Rank by the **product**, not the sum — a problem near zero on one axis is dead regardless of the other, and multiplying puts it where it belongs.

Apply the evidence ladder when scoring: **a problem with no ★★★★ evidence cannot score above 7 on monetizability.** No salary being paid, no paying customer complaining, no penalty for non-compliance means willingness to pay is still unproven.

Take the top 10 and write one Obsidian note each.

### Obsidian output

```
Problems/
├── 00 - Problem Index.md
├── 01 - <problem-slug>.md
├── 02 - <problem-slug>.md
└── ...
```

Templates are in `assets/problem-report-template.md` and `assets/index-template.md`. Fill them as given — consistent structure is what makes ten notes comparable side by side, and it feeds directly into the next phase's decision matrix.

Two Obsidian specifics:
- **YAML frontmatter** (vertical, scores, seam, date, status) so the vault is queryable with Dataview later.
- **`[[wikilinks]]`** both ways: each problem links to the index, the index links to each problem. Clustering in graph view helps the team grasp the space fast.

Write to the real vault path. If a device bridge is available (`device_commit_files`), actually put the files on the user's disk — showing files in chat isn't enough, Obsidian has to be able to open them.

### Validation is online

This market can't be validated by walking into a shop. Every problem report must therefore name a **concrete online validation path**: which subreddit or community to post the question in, which job title to cold-DM on LinkedIn, which Slack/Discord to join, which review-site reviewer to contact.

Ask about the past, never about the idea. "Would you use this?" produces polite lies. "Walk me through the last time this happened" produces facts.

### Honesty rule

Never invent data. When estimating market size, show the arithmetic ("X businesses × $Y/month × 12 = $Z") and flag the assumption. Invented numbers send the team down the wrong path, and they're the first thing an investor or judge will probe.

If an unsourced claim must appear, mark it `⚠️ unverified`.

## Wrapping up

Give the user:
1. The list of files written to the vault
2. A one-sentence summary of the top 3 and why they rose
3. **The next step:** who to contact where, for the highest-ranked problem. Ten reports without ten conversations are ten hypotheses.
