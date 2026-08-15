# Search Patterns and Query Craft

`research-sources.md` covers *where* to look. This file covers *how* to search.

Search quality is the ceiling on research quality. Searching with the wrong words returns nothing even when pointed at the right source — because people describe their pain in their own words, not in yours.

## Contents

- [A. Firecrawl first](#a-firecrawl-first)
- [B. Operator craft](#b-operator-craft)
- [C. Intent-organized pattern library](#c-intent-organized-pattern-library)
- [D. Query budget and stopping rules](#d-query-budget-and-stopping-rules)
- [E. Search log](#e-search-log)
- [Query generator](#query-generator)

---

## A. Firecrawl first

When `firecrawl_search` is available, it is the primary research tool — not a fallback. Measured: it reaches Reddit and the review sites, which the plain web fetcher cannot touch at all.

**`includeDomains` is the highest-leverage parameter in this workflow.** It converts the two richest veins from unreachable to fully mineable:

```
firecrawl_search(
  query: '"<profession>" "anyone else" <process>',
  includeDomains: ["reddit.com"],
  limit: 8,
  highlights: true
)
```

```
firecrawl_search(
  query: '"switched from" <category> software too expensive',
  includeDomains: ["capterra.com", "g2.com", "trustradius.com"]
)
```

Practical notes:

- **`highlights: true`** returns the matching passage, not just the title. Often you get the quote you need without opening the page.
- Result descriptions frequently carry **upvote counts and review snippets** — repeat-count evidence without a second request.
- **Throttle to about 2-3 concurrent calls.** Measured: firing a large parallel batch returns HTTP 429 and roughly twenty queries are lost. Small parallel batches run cleanly. This is the one place where "search in parallel" needs a limit — parallelize in waves of two or three rather than all at once, or you'll spend the budget on retries.
- `categories: ["research"]` narrows to research-affiliated sites; useful for industry statistics, rarely for pain.
- Firecrawl supports the standard operators below, so combine them with `includeDomains` rather than choosing between them.

Without Firecrawl, veins 1 and 2 are largely closed. Say so in the report instead of quietly producing a thinner list.

---

## B. Operator craft

| Operator | Example | Why it works |
|---|---|---|
| `"exact phrase"` | `"still doing this by hand"` | Forces adjacency and order; prevents scattered word matches |
| `site:` | `site:reddit.com <profession>` | Isolates a source when domain filters aren't available |
| `inurl:` | `inurl:reviews <product>` | Jumps straight to the review section rather than the marketing page |
| `intitle:` | `intitle:"<vertical> software"` | Pages dedicated to the topic, not ones mentioning it in passing |
| `OR` | `frustrated OR "fed up" OR nightmare` | Sweeps a whole emotional register in one query |
| `-` (exclude) | `<vertical> software -"best of" -sponsored` | Strips listicles and affiliate content, which otherwise dominate |
| `after:` / `before:` | `<vertical> mandate after:2025-01-01` | Essential for regulation — old mandates are already solved |
| `filetype:pdf` | `filetype:pdf "<vertical>" inspection checklist` | Regulator guidance and association bulletins are PDFs and invisible to normal search |

**A good query is never one word.** It combines an intent, a role or vertical term, and a register word:

```
"independent auto shop" ("anyone else" OR "am I the only one") parts ordering
"<vertical> software" ("switched from" OR "canceled") -"best of" -sponsored
```

---

## C. Intent-organized pattern library

Grouped by **intent**, not by site. The reason: starting from "what do I want to learn?" leads you to the right source on your own; starting from "which site should I search?" makes you scan the same site six times.

Placeholders: `<vertical>` `<role>` `<competitor>` `<jobtitle>` `<city>`

### C1. Find the pain

```
"<role>" "biggest problem" OR "biggest headache"
"<role>" ("anyone else" OR "am I the only one")
"<role>" (rant OR vent OR "fed up" OR "losing my mind")
"<vertical>" "wish there was a way"
"<role>" "what nobody tells you about"
"<vertical>" ("waste of time" OR "takes forever")
"<role>" "spent all day" OR "spent 3 hours"
"<vertical>" "drives me crazy"
"<role>" "worst part of the job"
site:reddit.com "<role>" "does anyone"
```

Best paired with `includeDomains: ["reddit.com"]`.

### C2. Find today's workaround

Proof the pain is real: if people are already spending effort, it exists.

```
"<vertical>" "still using excel" OR "still on paper"
"<vertical>" "spreadsheet" "keep track"
"<role>" "we do it manually"
"<vertical>" "whiteboard" OR "sticky notes" OR "legal pad"
"<role>" "how do you guys handle"
"<role>" "how do you track"
"<vertical>" "double entry" OR "entering it twice"
"<vertical>" "copy and paste" every
"<role>" "our process is"
"<vertical>" "we hired someone just to"
```

That last one is the bridge to Vein 5 — it names a problem that already has a salary attached.

### C3. Find payment evidence

The ★★★★ tier. Note the query shapes: generic job searches return career-advice articles, so target listing pages and pair a title with the vertical and a tool word.

```
"<jobtitle>" "<vertical>" spreadsheet responsibilities
site:indeed.com "<jobtitle>" "<vertical>"
site:linkedin.com/jobs "<jobtitle>" "<vertical>"
"<vertical>" hiring "data entry" OR "operations coordinator"
"<vertical>" job "manual" "tracking" salary
"<vertical>" "we're looking for someone to" track OR manage OR enter
"<competitor>" pricing per user
"<vertical> software" cost per month small business
"<vertical>" "how much do you pay for" software
"<vertical>" fined OR penalty OR violation <regulation>
"<vertical>" consultant hourly rate
```

### C4. Find the incumbents

```
"<vertical> software" pricing
best "<vertical>" software small business
"<vertical>" software comparison -"best of" -sponsored
site:g2.com "<vertical>" software
site:capterra.com "<vertical>"
site:reddit.com "<vertical>" "what do you use for"
site:reddit.com "<role>" "what software"
"<vertical>" "alternatives to <competitor>"
intitle:"<vertical> management software"
"<vertical>" software recommendations forum
```

A `"what do you use for"` thread with many comments is a finished competitor map — tool names plus why each is disliked. One such thread does half of Vein 4's work.

### C5. Find the incumbent's blind spot

Your entry point.

```
"<competitor>" "switched from" OR "switched to"
site:capterra.com "<competitor>" "switched from"
"<competitor>" review cons complaints
"<competitor>" ("canceled" OR "cancelled") subscription
"<competitor>" "too expensive" OR "price increase"
"<competitor>" "doesn't support" OR "can't do"
"<competitor>" "support is terrible" OR "no response"
"<competitor>" "feature request" ignored
"<competitor>" alternative cheaper
site:reddit.com "<competitor>" "finally left" OR "moving away from"
"<vertical> software" "none of them" OR "they all"
```

**Capterra's "Switched from" field is structured churn data** — it names the abandoned product outright. Search it specifically; there is no more direct route to a wedge in public data.

On review sites: filter to **1-2 stars**, sort by **recency**, read the **Cons** field. The last six months of low-star reviews are the wounds that are still open.

### C6. Regulation and mandates

```
"<vertical>" new regulation after:2025-01-01
"<vertical>" compliance deadline
"<vertical>" "must comply by" OR "effective date"
"<vertical>" fine penalty enforcement
filetype:pdf "<vertical>" compliance guide
filetype:pdf "<vertical>" inspection checklist
site:federalregister.gov "<vertical>"
site:eur-lex.europa.eu "<vertical>"
"<vertical>" association compliance bulletin
"<vertical>" state licensing renewal requirements
"<vertical>" "reporting requirement" small business
```

An inspection or audit checklist is a software requirements document written by a regulator. Treat it as such.

### C7. Field and local

```
"<vertical>" "<city>" reviews complaints
"<vertical>" google reviews "never showed up" OR "no one answered"
site:bizbuysell.com "<vertical>"
"<vertical>" business for sale "can't keep up"
"<vertical>" business for sale reason burnout
youtube "<role>" "day in the life"
youtube "<role>" "what I wish I knew"
"<role>" "before you start this business"
```

Maps and Yelp reviews aren't readable via search — use browser automation if available, otherwise record the vein as inaccessible.

---

## D. Query budget and stopping rules

### Per-vein targets

| Vein | Queries | Expected pains |
|---|---|---|
| 1 — Practitioner communities | 10-14 | 5+ |
| 2 — Review sites | 8-12 | 5+ |
| 3 — Regulation | 5-8 | 3+ |
| 4 — Incumbents | 8-12 | 5+ |
| 5 — Job postings | 5-8 | 3+ |
| 6 — Field and local | 5-8 | 5+ |
| **Total** | **40-60** | **30-40** |

**Run queries in parallel.** Sequential searching costs the user's patience and buys no additional information.

### Stopping rules

1. **Two-attempt rule.** If two different approaches to a source both fail, stop and substitute. Ten queries against a blocked source burns a sixth of the budget for nothing.
2. **Saturation.** No new pain across five consecutive searches in a vein means that vein is done.
3. **Target reached.** At 30-40 raw pains, move to filtering.
4. **Hard ceiling.** Past 60 queries, stop and work with what you have. More searching yields noise, not better problems.
5. **Short vein.** If a vein falls far below target, **don't force it — record it.** "Vein 5 produced one posting" is worth immeasurably more than three invented ones.

### Two rounds, always

Round one uses outsider vocabulary and returns mediocre results. **Stop after round one and harvest the jargon:** what do practitioners call themselves, what do they call the process, which product names keep recurring, which abbreviations appear?

Run round two with those words. Round two is almost always sharply better — reserve about a third of the budget for it.

---

## E. Search log

Record what each query returned. It makes the report's sources traceable and stops the next session from repeating the same searches.

```
| # | Query | Vein | Result | New pains |
|---|-------|------|--------|-----------|
| 1 | "independent auto shop" "anyone else" parts | 1 | r/serviceadvisors, 4 threads | 3 |
| 2 | site:capterra.com "Tekmetric" "switched from" | 2 | 6 churn reviews | 2 |
| 3 | site:indeed.com "service advisor" auto repair | 5 | 2 postings w/ salary | 1 |
```

The `New pains` column is the saturation counter — five consecutive zeros in a vein means it's exhausted.

Keep the log as a working note; generate the report's bibliography from it rather than publishing the log itself.

---

## Query generator

Hand-writing 40-60 queries every run is tedious and leaves coverage to chance — dropping a synonym or a whole vein is easy.

`scripts/query_gen.py` takes this library, fills it with your vertical and synonyms, groups by intent, and prints a ready search-log table:

```bash
python scripts/query_gen.py "auto repair shop" \
  --synonyms "independent mechanic,service advisor,auto shop owner" \
  --competitors "Tekmetric,Shop-Ware,Mitchell1" \
  --city "Austin" --format md
```

Useful flags: `--intent 1,2,5` for a single group, `--limit N` for per-group caps (default 12, matching the budget), `--limit 0` for the full cross-product.

The script generates nothing this file doesn't define. To add a pattern, add it here first, then to the script.
