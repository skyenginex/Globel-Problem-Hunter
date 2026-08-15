# Pain Research: The Six Veins

The goal is to find the vertical's **stated** pain. The moment you start generating guesses, this skill's value drops to zero — the team already had guesses; what they need is evidence.

This file covers *where* to look. *How* to search is in `search-patterns.md`. Read both; a source list is useless without the right query shapes, and query shapes are useless pointed at the wrong sources.

## Contents

- [The six veins at a glance](#the-six-veins-at-a-glance)
- [Vein 1 — Practitioner communities](#vein-1--practitioner-communities)
- [Vein 2 — Review sites](#vein-2--review-sites)
- [Vein 3 — Regulation](#vein-3--regulation)
- [Vein 4 — Incumbents](#vein-4--incumbents)
- [Vein 5 — Job postings](#vein-5--job-postings)
- [Vein 6 — Field and local](#vein-6--field-and-local)
- [Measured access table](#measured-access-table)
- [Persona discipline: whose pain is it?](#persona-discipline-whose-pain-is-it)
- [Evidence ladder](#evidence-ladder)
- [Raw pain record format](#raw-pain-record-format)
- [Saturation: when to stop](#saturation-when-to-stop)
- [Common traps](#common-traps)

---

## The six veins at a glance

| # | Vein | Question it answers | Target |
|---|---|---|---|
| 1 | Practitioner communities | What do operators say to each other? | 5+ pains |
| 2 | Review sites | What do paying customers hate? | 5+ pains |
| 3 | Regulation | What are they *required* to do? | 3+ pains |
| 4 | Incumbents | What's sold, at what price, missing what? | 5+ pains |
| 5 | Job postings | What work is someone paying a salary for? | 3+ pains |
| 6 | Field and local | What breaks in daily operations? | 5+ pains |

**Total target: 30-40 raw pains.** Filter afterward, never during collection.

An empty vein is itself a finding — usually it means weak reachability or genuinely no pain there. Record it. It closes the "did we even look?" argument later.

---

## Vein 1 — Practitioner communities

The richest vein. In a community of peers, people describe their work problems with a candor they show nowhere else — anonymity plus the sense of talking to people who do the same job produces admissions like "honestly we still track this on a whiteboard."

### Subreddit discovery protocol

Finding the right sub is half the work. Five steps, in order:

1. **Reddit's own search** — `reddit.com/subreddits/search?q=<profession>`. Lists communities with subscriber counts.
2. **Organic discovery via search** — `site:reddit.com "<profession>" "anyone else"`. Surfaces the sub without knowing its name, and often lands you somewhere you'd never have guessed: `r/serviceadvisors`, `r/msp`, `r/InventoryManagement`, `r/talesfromthepharmacy`.
3. **Neighborhood tracing** — from one good post, check the sub's "related communities" sidebar and which other subs the poster is active in. Trade communities cluster.
4. **The sub's own wiki/sidebar** — most profession subs list sibling communities.
5. **Liveness test — skip the dead ones.** Subscriber count plus posts in the last 30 days. A 200k-subscriber sub with three posts a month is dead; an 8k-subscriber sub with fifteen posts a day is a goldmine. **Activity matters, not size.**

### Profession → community map (starting point)

Verify each before relying on it — subs get renamed, merged, and abandoned.

| Domain | Communities to check |
|---|---|
| General SMB | `r/smallbusiness`, `r/Entrepreneur`, `r/EntrepreneurRideAlong`, `r/sweatystartup` |
| Auto | `r/AutoRepair`, `r/MechanicAdvice`, `r/serviceadvisors`, `r/Justrolledintotheshop` |
| Trades | `r/Plumbing`, `r/electricians`, `r/HVAC`, `r/Construction`, `r/Contractor` |
| Field service | `r/fieldservice`, `r/pooloperators`, `r/lawncare`, `r/Pestcontrol` |
| Accounting | `r/Accounting`, `r/Bookkeeping`, `r/taxpros`, `r/CPA` |
| Legal | `r/LawFirm`, `r/paralegal` |
| Healthcare admin | `r/Dentistry`, `r/optometry`, `r/veterinaryprofession`, `r/medicalbilling` |
| Restaurants | `r/restaurantowners`, `r/KitchenConfidential`, `r/bartenders` |
| IT services | `r/msp`, `r/sysadmin`, `r/ITManagers` |
| Logistics | `r/logistics`, `r/Truckers`, `r/FreightBrokers`, `r/supplychain` |
| Property | `r/PropertyManagement`, `r/realtors`, `r/Landlord` |
| Manufacturing | `r/Machinists`, `r/manufacturing`, `r/Welding` |
| Agencies/creative | `r/agency`, `r/freelance`, `r/graphic_design` |
| E-commerce | `r/ecommerce`, `r/shopify`, `r/FulfillmentByAmazon` |

Beyond Reddit: industry Discord and Slack communities, trade association forums, Facebook groups, and vertical-specific forums (often decades old, poorly indexed, and therefore unmined by competitors).

### Golden phrase patterns

Pain gets expressed in recognizable shapes. Search these inside a community:

| Pattern | What it finds |
|---|---|
| `"anyone else"` | Shared pain — the poster hopes they're not alone |
| `"am I the only one"` | Same, sharper |
| `"how do you guys handle"` | Unsolved process — people are still looking for a method |
| `"what do you use for"` | **A prepared competitor map** — the comments list the tools |
| `"is there a tool"` / `"is there software"` | Direct product demand |
| `"rant"` / `"vent"` | Highest emotional density |
| `"spent 3 hours"` / `"took me all day"` | Quantified time loss — raw material for the monetization math |
| `"switching from"` / `"finally left"` | Churn reason from an incumbent |
| `"still using excel"` / `"still on paper"` | Undigitized process — the cleanest opportunity |
| `"clients keep"` / `"customers always"` | Recurring customer-caused problem |
| `"my boss makes me"` | Manual work someone is being paid to do (links to Vein 5) |

**Sort tactics:** *Top → All time* surfaces structural, persistent pain (unsolved for years). *New* surfaces fresh pain (a new mandate, a recent price hike, an incumbent's bad release). Scan both.

### Reading the signal correctly

Reddit's real power is the numbers around the text:

- **Upvotes are a poll.** A complaint with 400 upvotes is 400 people saying "yes, me too." That is a survey result you didn't have to run.
- **"Same here" comments are repeat evidence.** Fill the `REPEAT` field from them.
- **A `"what do you use for X"` thread with 80 comments is a finished competitor map** — tool names *and* why each is disliked. One such thread does half of Vein 4's work. Never skip it.
- **An unanswered "is there a tool for X" post is also data** — it suggests the solution genuinely doesn't exist.

---

## Vein 2 — Review sites

The highest-yield vein per unit of effort, because a low-star review comes from someone who **paid money and is still unhappy**. That single text carries the problem, proof of willingness to pay, and the incumbent's exact failure point.

**Where:** G2, Capterra, TrustRadius, GetApp, Software Advice, Trustpilot, and app store reviews.

**How to mine it:**

- Filter to **1-2 star** reviews. Five stars is marketing, three stars is ambivalence, one and two stars are data.
- Sort by **recency**. Reviews from the last six months describe wounds that are still open; older ones may have been fixed.
- Read the **"Cons"** field specifically — it's a structured complaint field, which is rare and valuable.
- **Capterra's "Switched from" field is structured churn data.** It literally names the product the reviewer abandoned. This tells you which incumbent is bleeding customers and why — the single most direct route to a wedge that exists anywhere in public data.
- Pricing is displayed on comparison pages. Collect it; it's the multiplier in every market-size estimate and it reveals the price tier gap seam.

Also mine reviews of **adjacent-category** products, not just direct competitors. The pain that makes someone rate a scheduling tool poorly is often not about scheduling.

---

## Vein 3 — Regulation

When a business "might want" something, selling is hard. When it "will be penalized without" it, selling happens on its own. New mandates are the fastest path from problem to revenue because the budget is already allocated.

**US sources:** the Federal Register, agency rule pages (OSHA, DOL, DOT/FMCSA, FDA, EPA), state legislature and licensing board sites, state privacy law trackers, industry association compliance bulletins.

**EU sources:** EUR-Lex, national implementation of EU directives (they differ by country and the gap is often the opportunity), e-invoicing mandate rollouts, the European Accessibility Act, NIS2 scope, CSRD/sustainability reporting reaching SMEs through supply chains.

**Cross-cutting:** industry association newsletters usually explain a mandate more clearly than the regulator does, and inspection or audit checklists are effectively a software requirements document written by the government.

**Narrow the date.** A three-year-old mandate has been solved. The opportunity is in the last 12-24 months, where compliance is still incomplete and incumbents haven't shipped support yet.

**Watch for the supply-chain ripple:** large-company obligations cascade to small suppliers who have no tooling and no compliance staff. That's a frequent, under-served seam.

---

## Vein 4 — Incumbents

The beginner's reflex — "no competitors, great!" — is wrong. Absence of competition usually means either no market or a graveyard of previous attempts. What you're hunting is not emptiness but the **incumbents' shared blind spot**.

- **Pricing pages** — the market's payment band. Look at which features sit in which tier: whatever is gated to the top tier is what customers want most. The gap below the cheapest tier is the price tier seam.
- **Feature lists** — what everyone does is table stakes; what nobody does is opportunity.
- **Changelogs and release notes** — the last six months of shipped features is a list of what customers demanded loudly enough.
- **Their job postings** — reveal where they're investing and, by omission, where they're weak. "Hiring integration engineers" says integrations are currently a weakness.
- **G2/Capterra comparison pages** — pre-built competitive matrices.
- **Their own community and support forums** — feature requests sitting unanswered for years are seams with a queue of demand already attached.

---

## Vein 5 — Job postings

`problem-scoring.md` treats "someone is being paid a salary to do this" as the strongest monetization evidence. Job postings are where that evidence lives, and almost nobody looks.

A posting reveals three things at once:

1. **Which work is manual** — the responsibilities list is an inventory of un-automated processes.
2. **Which tools are used** — "proficient in Excel," "experience with [incumbent]," "must be comfortable with data entry" names the current solution outright.
3. **What it costs** — the salary range is the **price ceiling** of the problem. A tool that removes half of a $50k/year role can justify a few hundred dollars a month without argument.

**Where:** Indeed, LinkedIn Jobs, Glassdoor, ZipRecruiter, industry-specific job boards, and companies' own careers pages.

**Query craft matters here.** Generic queries return career-advice articles rather than postings. Target listing pages and pair a job title with the vertical and a tool word — patterns are in `search-patterns.md` C3.

**Titles that signal manual process:** data entry clerk, operations coordinator, scheduling coordinator, dispatcher, billing specialist, AR/AP clerk, order entry, inventory clerk, compliance administrator, intake coordinator.

**A repeated posting is its own signal:** the same role posted three times in six months means either the work is unbearable (high turnover) or the process is broken. Both are opportunities.

---

## Vein 6 — Field and local

For local service businesses, the fastest route to the operator's problem is reading **their customers' complaints**.

### Google and Yelp reviews

A customer complaint is a description of the operator's process gap:

- "They gave me an appointment and nobody showed" → no dispatch confirmation loop
- "Called four times, no one picked up" → no call handling or callback system
- "Been waiting three weeks for a part, nobody updates me" → no parts tracking or proactive notification
- "The price changed after they started" → no documented estimate-and-approval flow

Method: pick a metro area, scan 15-20 businesses in the vertical, read the 1-3 star reviews, and extract recurring themes. **A complaint appearing across eight different businesses is a sector problem, not one bad operator** — that distinction is the whole point of the exercise.

### Business-for-sale listings

BizBuySell and similar marketplaces. Why are people exiting? Stated reasons — "can't find staff," "grew faster than I can manage," "burned out on scheduling" — point straight at structural breaking points. "**Can't keep up with demand**" is especially valuable: demand exists but operations won't scale, which is exactly what software fixes.

### Video and social

Trade YouTube channels ("day in the life," "what I wish I knew before starting"), TikTok trade creators, and Instagram business accounts. These are the only sources that show the daily routine as it actually happens and reveal how long each task takes. Comment sections double as complaint lists.

---

## Measured access table

Measured in this environment, not assumed. Re-verify if behavior changes.

| Source | Status | Route |
|---|---|---|
| **Reddit** | Reachable **via Firecrawl search only** | `firecrawl_search` with `includeDomains: ["reddit.com"]`. Plain web fetch returns 403 on every reddit URL, and plain web search returns essentially no reddit results. |
| **G2 / Capterra / TrustRadius** | Reachable via Firecrawl; pricing and "Switched from" fields visible in results | `firecrawl_search` with `includeDomains` |
| Job boards (Indeed, LinkedIn) | Reachable, but generic queries return career-advice articles | Target listing pages; pair title + vertical + tool word |
| Vendor sites, pricing pages, changelogs | Reachable | Standard fetch |
| Regulator sites, Federal Register, EUR-Lex | Reachable | Standard fetch; `filetype:pdf` for guidance documents |
| Trade forums and association sites | Reachable | Standard fetch |
| Google Maps / Yelp reviews | Dynamic, not readable by search | Browser automation if available; otherwise skip and record |
| Business-for-sale listing detail pages | Often blocked | Search snippets confirm existence; full text may not load |
| Facebook / Instagram | Closed | Search snippets only |

**Firecrawl's `includeDomains` is the single highest-leverage parameter in this workflow.** It converts Reddit and the review sites from unreachable to fully mineable. When Firecrawl is available, prefer it for veins 1 and 2 without exception.

**Throttle to 2-3 concurrent Firecrawl calls.** Measured: a large simultaneous batch returns 429 and loses roughly twenty queries. Parallelize in small waves, not all at once.

**Two-attempt rule.** If two different approaches to a source both fail, stop. Writing ten more queries against a blocked source burns roughly a sixth of the query budget for nothing. Switch to a substitute or mark the vein "inaccessible" and move on. Honestly reporting an empty vein beats a fabricated full one.

---

## Persona discipline: whose pain is it?

The subtlest failure mode: collecting eight real, well-sourced pains that all belong to the **wrong person**.

Two kinds of pain:

- **Operator pain** — felt by the person who would buy. "We write appointments in a book and lose them." Directly usable.
- **Customer pain** — felt by that person's customer. "They gave me an appointment and nobody showed." Not directly usable.

Customer pain isn't worthless — Vein 6 is built on it — but it **cannot enter the list raw.** Translate it first:

```
Customer pain:  "Been waiting three weeks for a part, nobody updates me"
        ↓ translate: what's missing inside the business?
Operator pain:  "Shop owners can't track pending parts orders or proactively
                 update customers; today the service advisor asks the parts
                 guy and calls back if they remember."
```

If a complaint can't be translated — because it points to bad faith or lack of skill rather than a missing system ("they replaced parts that didn't need replacing") — it isn't usable for a software product. Drop it.

**Check question:** for each pain, ask "if this person described this to me in their own words, would they buy the product?" If the answer isn't the target buyer, translate it or cut it.

That's what the `WHO SAYS IT` field is for. If it says "customer" and no translation was done, the record is incomplete.

---

## Evidence ladder

Not all evidence is equal. A job posting and a blog post sitting in the same table misleads the reader. Rate every raw pain:

| Strength | Evidence type |
|---|---|
| ★★★★ | Job posting (**a salary is being paid** for this work) · a paying customer of an incumbent complaining · a documented penalty or enforcement action |
| ★★★ | Same pain repeated across 3+ independent sources · incumbent pricing page (proves the payment band) · an in-force mandate with a deadline |
| ★★ | A single community post · one review · one Google review · a stated business-exit reason |
| ★ | Blog post · trend article · vendor-published "state of the industry" report |
| ✗ | Your own inference — enters the report tagged **`⚠️ unverified`** |

**Rule:** a problem with no ★★★★ evidence cannot score above 7 on monetizability. No salary, no paying complainer, no penalty means willingness to pay is unproven — however interesting the problem sounds.

Vendor-published research deserves specific suspicion: it's produced to sell the vendor's product and its numbers are chosen accordingly. Treat it as ★, never as a market-size source.

This ladder feeds `problem-scoring.md` directly and appears in the **Strength** column of `assets/problem-report-template.md`.

---

## Raw pain record format

Record this for every pain. Re-finding a source later is the most time-expensive part of research.

```
PAIN: <one sentence, in the practitioner's own words>
VEIN: <1-6>
SOURCE: <URL or platform + date>
QUOTE: "<verbatim quote if available>"
WHO SAYS IT: <role — and if "customer," include the translation>
REPEAT: <how many independent sources voiced this>
SIGNAL: <upvotes / review count / salary figure, if applicable>
STRENGTH: <★ to ★★★★>
```

**Repeat count outweighs the quality of any single source.** An ordinary pain voiced independently in three places beats one person's extremely detailed account — the latter may be specific to them.

**Keep quotes verbatim.** "Users are frustrated with inventory tracking" is worthless next to "I close the shop for a full day every month just to count parts."

---

## Saturation: when to stop

Two failure modes — quitting early and never quitting. One rule prevents both.

**Saturation test:** if a vein yields no new pain across five consecutive searches, it's exhausted. Move on.

Alongside that:

- Stop a vein once it hits its target count in the table above.
- Stop entirely at 30-40 raw pains; more doesn't improve the outcome.
- Hard ceiling of 60 queries. Past that you're collecting noise, not problems.
- If a vein falls far short, **don't force it — record it.**

Query budget and the search log format are in `search-patterns.md`.

---

## Common traps

- **Starting with AI.** "AI-powered X" is a solution shape, not a problem. Pain first, technology second.
- **Generalizing from your own life.** Founder-life problems point at the founder market — crowded, cheap, and the worst payers in software.
- **Drowning in blog posts.** "5 trends in the industry for 2026" is written for SEO and contains no real pain. First-hand complaint text always wins; that's the ★ versus ★★★★ gap.
- **Dismissing a pain because a solution exists.** "X already does this" doesn't kill a problem — X being expensive, bloated, badly supported, or aimed at bigger companies is a doorway. That's the whole wedge concept.
- **Silently skipping a blocked source.** Skipping Vein 1 because Reddit resisted one query loses the richest vein. Use Firecrawl; if that fails too, substitute and disclose.
- **Confusing your persona.** See above. This is the most common way good research produces a useless list.
- **Summarizing quotes.** Once you paraphrase, the evidence stops being evidence.
- **Taking vendor market-size numbers at face value.** Build your own estimate from a business count and a price band, and show the arithmetic.
