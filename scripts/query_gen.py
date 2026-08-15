#!/usr/bin/env python3
"""Global Problem Hunter - search query generator.

Takes the pattern library from references/search-patterns.md, fills it with a
vertical and its synonyms, groups by intent, and prints a ready-to-run query
list (or a search-log table).

Why this exists: hand-writing 40-60 queries every run leaves coverage to
chance. Dropping a synonym or skipping a whole vein is easy to do and hard to
notice. The script guarantees the shape of the sweep; you still decide which
queries are worth running.

It invents nothing. The source of truth is search-patterns.md - add a pattern
there first, then here.

Usage:
    python query_gen.py "auto repair shop" \\
        --synonyms "independent mechanic,service advisor,auto shop owner" \\
        --competitors "Tekmetric,Shop-Ware,Mitchell1" \\
        --city "Austin" --format md

Firecrawl note: queries tagged [FIRECRAWL] work best via firecrawl_search with
includeDomains, because those domains are unreachable by plain web fetch.

Standard library only.
"""

import argparse
import sys

# ---------------------------------------------------------------------------
# Pattern library - mirrors search-patterns.md section C
#
# Placeholders:
#   {v}  -> vertical / role (repeated across synonyms)
#   {c}  -> competitor name
#   {city} -> city, for the local vein
#
# "domains" marks the group's preferred Firecrawl includeDomains, printed as a
# hint so the researcher does not have to remember which vein needs which.
# ---------------------------------------------------------------------------
PATTERNS = {
    1: {
        "name": "Find the pain",
        "note": "What operators say to each other",
        "vein": "V1",
        "domains": ["reddit.com"],
        "general": [
            '"{v}" "biggest problem" OR "biggest headache"',
            '"{v}" ("anyone else" OR "am I the only one")',
            '"{v}" (rant OR vent OR "fed up" OR "losing my mind")',
            '"{v}" "wish there was a way"',
            '"{v}" "what nobody tells you about"',
            '"{v}" ("waste of time" OR "takes forever")',
            '"{v}" "spent all day" OR "spent 3 hours"',
            '"{v}" "drives me crazy"',
            '"{v}" "worst part of the job"',
        ],
        "domain_scoped": [
            '"{v}" "does anyone"',
            '"{v}" "how do you guys"',
        ],
    },
    2: {
        "name": "Find today's workaround",
        "note": "Proof the pain is real - effort is already being spent",
        "vein": "V1",
        "domains": ["reddit.com"],
        "general": [
            '"{v}" "still using excel" OR "still on paper"',
            '"{v}" spreadsheet "keep track"',
            '"{v}" "we do it manually"',
            '"{v}" "whiteboard" OR "sticky notes" OR "legal pad"',
            '"{v}" "double entry" OR "entering it twice"',
            '"{v}" "copy and paste" every',
            '"{v}" "we hired someone just to"',
        ],
        "domain_scoped": [
            '"{v}" "how do you handle"',
            '"{v}" "how do you track"',
        ],
    },
    3: {
        "name": "Find payment evidence",
        "note": "4-star evidence: is a salary being paid for this work",
        "vein": "V5",
        "domains": ["indeed.com", "linkedin.com", "glassdoor.com"],
        "general": [
            '"{v}" hiring "data entry" OR "operations coordinator"',
            '"{v}" job "manual" tracking salary',
            '"{v}" "we\'re looking for someone to" track OR manage OR enter',
            '"{v} software" cost per month small business',
            '"{v}" "how much do you pay for" software',
            '"{v}" fined OR penalty OR violation',
            '"{v}" consultant hourly rate',
        ],
        "domain_scoped": [
            '"{v}" "data entry" responsibilities spreadsheet',
            '"{v}" "operations coordinator"',
            '"{v}" scheduling coordinator manual',
        ],
    },
    4: {
        "name": "Find the incumbents",
        "note": "Market exists + the payment band",
        "vein": "V4",
        "domains": ["g2.com", "capterra.com", "trustradius.com"],
        "general": [
            '"{v} software" pricing',
            'best "{v}" software small business',
            '"{v}" software comparison -"best of" -sponsored',
            'intitle:"{v} management software"',
            '"{v}" software recommendations forum',
        ],
        "domain_scoped": [
            '"{v}" software',
            '"{v}" pricing plans',
        ],
        "reddit": [
            '"{v}" "what do you use for"',
            '"{v}" "what software"',
        ],
    },
    5: {
        "name": "Find the incumbent's blind spot",
        "note": "Your entry point - churn reasons",
        "vein": "V2",
        "domains": ["capterra.com", "g2.com", "trustradius.com"],
        "competitor_general": [
            '"{c}" "switched from" OR "switched to"',
            '"{c}" review cons complaints',
            '"{c}" ("canceled" OR "cancelled") subscription',
            '"{c}" "too expensive" OR "price increase"',
            '"{c}" "doesn\'t support" OR "can\'t do"',
            '"{c}" "support is terrible" OR "no response"',
            '"{c}" alternative cheaper',
        ],
        "competitor_domain": [
            '"{c}" "switched from"',
            '"{c}" cons',
        ],
        "competitor_reddit": [
            '"{c}" "finally left" OR "moving away from"',
        ],
        "general": [
            '"{v} software" "none of them" OR "they all"',
        ],
    },
    6: {
        "name": "Regulation and mandates",
        "note": "Obligation equals budget",
        "vein": "V3",
        "domains": [],
        "general": [
            '"{v}" new regulation after:2025-01-01',
            '"{v}" compliance deadline',
            '"{v}" "must comply by" OR "effective date"',
            '"{v}" fine penalty enforcement',
            'filetype:pdf "{v}" compliance guide',
            'filetype:pdf "{v}" inspection checklist',
            'site:federalregister.gov "{v}"',
            'site:eur-lex.europa.eu "{v}"',
            '"{v}" association compliance bulletin',
            '"{v}" state licensing renewal requirements',
            '"{v}" "reporting requirement" small business',
        ],
    },
    7: {
        "name": "Field and local",
        "note": "Customer reviews, exits, trade video",
        "vein": "V6",
        "domains": [],
        "general": [
            '"{v}" "{city}" reviews complaints',
            '"{v}" google reviews "never showed up" OR "no one answered"',
            'site:bizbuysell.com "{v}"',
            '"{v}" business for sale "can\'t keep up"',
            '"{v}" business for sale reason burnout',
            'youtube "{v}" "day in the life"',
            'youtube "{v}" "what I wish I knew"',
            '"{v}" "before you start this business"',
        ],
    },
}


def build(vertical, synonyms, competitors, city, intents, limit=12):
    """Fill patterns and return an intent-grouped dict.

    Ordering is TERM-MAJOR: every pattern with the primary term first, then
    every pattern with synonym 1, and so on. This matters because when the
    list is cut at `limit`, what survives is MANY DISTINCT PATTERNS rather
    than one pattern repeated across five synonyms - coverage, not repetition.

    Pools (general / domain-scoped / reddit / competitor) are then interleaved
    round-robin so each source type gets a share of the cap. Concatenating
    instead would let the general pool eat the entire limit and silently drop
    the Reddit and review-site queries, which are the richest two veins.
    """
    terms = [vertical] + [s.strip() for s in synonyms if s.strip()]
    comps = [c.strip() for c in competitors if c.strip()]

    out = {}

    for iid, grp in PATTERNS.items():
        if intents and iid not in intents:
            continue

        pool_general, pool_domain, pool_reddit, pool_comp = [], [], [], []

        for term in terms:
            for pat in grp.get("general", []):
                if "{city}" in pat and not city:
                    continue
                pool_general.append(pat.format(v=term, city=city or ""))
            for pat in grp.get("domain_scoped", []):
                pool_domain.append(pat.format(v=term, city=city or ""))
            for pat in grp.get("reddit", []):
                pool_reddit.append(pat.format(v=term, city=city or ""))

        # Competitor queries interleave ACROSS competitors, not one competitor
        # at a time. Under the cap, knowing that three incumbents each have
        # churn complaints beats knowing twelve things about the first one -
        # the goal here is finding which incumbent is bleeding, and that is a
        # comparison across products.
        comp_pats = (grp.get("competitor_general", [])
                     + grp.get("competitor_domain", [])
                     + grp.get("competitor_reddit", []))
        comp_pools = [[pat.format(c=comp) for pat in comp_pats] for comp in comps]
        j = 0
        while comp_pools:
            for cp in list(comp_pools):
                if j < len(cp):
                    pool_comp.append(cp[j])
                else:
                    comp_pools.remove(cp)
            j += 1

        merged = []
        pools = [p for p in (pool_general, pool_domain, pool_reddit, pool_comp) if p]
        i = 0
        while pools:
            for p in list(pools):
                if i < len(p):
                    merged.append(p[i])
                else:
                    pools.remove(p)
            i += 1

        seen, unique = set(), []
        for q in merged:
            if q not in seen:
                seen.add(q)
                unique.append(q)

        trimmed = 0
        if limit and len(unique) > limit:
            trimmed = len(unique) - limit
            unique = unique[:limit]

        if unique:
            out[iid] = {
                "name": grp["name"],
                "note": grp["note"],
                "vein": grp["vein"],
                "domains": grp.get("domains", []),
                "queries": unique,
                "trimmed": trimmed,
            }

    return out


def print_plain(out):
    total = 0
    for iid, g in out.items():
        extra = f"  (+{g['trimmed']} trimmed by --limit)" if g["trimmed"] else ""
        print(f"\n### C{iid}. {g['name']}  [{g['vein']}]{extra}")
        print(f"# {g['note']}")
        if g["domains"]:
            print(f"# [FIRECRAWL] includeDomains: {g['domains']}")
        for q in g["queries"]:
            print(q)
        total += len(g["queries"])
    print(f"\n# --- TOTAL: {total} queries ---", file=sys.stderr)


def print_md(out):
    total = 0
    print("# Generated search queries\n")
    print("Use this as your search log: fill in `New pains` as you run each "
          "query. Five consecutive zeros in a group means that vein is "
          "saturated - move on.\n")
    for iid, g in out.items():
        extra = f" *(+{g['trimmed']} trimmed)*" if g["trimmed"] else ""
        print(f"## C{iid}. {g['name']} — `{g['vein']}`{extra}\n")
        print(f"*{g['note']}*\n")
        if g["domains"]:
            doms = ", ".join(f"`{d}`" for d in g["domains"])
            hint = ("— Reddit and the review sites are unreachable by plain "
                    "web fetch, so domain-scoped Firecrawl search is the only "
                    "route to this vein."
                    if any(d in ("reddit.com", "g2.com", "capterra.com",
                                 "trustradius.com") for d in g["domains"])
                    else "— domain scoping filters out the career-advice and "
                         "listicle noise these sites otherwise return.")
            print(f"> **Firecrawl:** run these with `includeDomains: [{doms}]` "
                  f"{hint}\n")
        print("| # | Query | Run | New pains |")
        print("|---|-------|-----|-----------|")
        for i, q in enumerate(g["queries"], 1):
            print(f"| {i} | `{q.replace('|', chr(92) + '|')}` |  |  |")
        print()
        total += len(g["queries"])
    print(f"\n**Total: {total} queries.** Budget is 40-60; stop a vein after "
          "five consecutive searches with no new pain.")


def main():
    p = argparse.ArgumentParser(
        description="Search query generator for global-problem-hunter.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("vertical", help='Vertical or role, e.g. "auto repair shop"')
    p.add_argument("--synonyms", default="",
                   help="Comma-separated insider terms practitioners actually use")
    p.add_argument("--competitors", default="",
                   help="Comma-separated incumbent product names")
    p.add_argument("--city", default="",
                   help="City for the local/field vein")
    p.add_argument("--intent", default="",
                   help="Only these intent groups, e.g. '1,2,5'. Empty = all")
    p.add_argument("--limit", type=int, default=12,
                   help="Per-group query cap (default 12, matching the "
                        "40-60 budget). 0 = uncapped")
    p.add_argument("--format", choices=["plain", "md"], default="plain",
                   help="Output format (default: plain)")

    a = p.parse_args()

    intents = set()
    if a.intent:
        try:
            intents = {int(x.strip()) for x in a.intent.split(",") if x.strip()}
        except ValueError:
            p.error("--intent must be comma-separated numbers, e.g. 1,2,4")

    out = build(a.vertical, a.synonyms.split(","), a.competitors.split(","),
                a.city, intents, a.limit)

    if not out:
        print("No queries generated - check the --intent filter.", file=sys.stderr)
        return 1

    print_md(out) if a.format == "md" else print_plain(out)

    if not a.competitors.strip():
        print("\n# NOTE: no --competitors given, so the churn queries (C5) are\n"
              "# thin. Run C4 first to find incumbent names, then re-run with\n"
              "# --competitors. Capterra's 'Switched from' field is the most\n"
              "# direct route to a wedge in public data.", file=sys.stderr)
    if not a.synonyms.strip():
        print("# NOTE: no --synonyms given. Round one finds the insider terms;\n"
              "# re-run with them for round two. Round two is almost always\n"
              "# sharply more productive.", file=sys.stderr)

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        try:
            sys.stdout.close()
        except Exception:
            pass
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(130)
