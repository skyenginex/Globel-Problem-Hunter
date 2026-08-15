# Vertical Scoring Rubric and Candidate Pool

## How to use this

Pick 8-12 verticals from the pool below that fit the team's context, score each on five criteria, total, and rank. The pool is a starting point — if the team has insider access to something not listed, **add it**. Access is worth more than the two or three points it might lose elsewhere in the table.

## Five criteria (1-5 each)

### 1. Reachability — can we get 10 of these people to talk to us?

The hardest filter. You cannot validate a problem for people you can't reach, and an unvalidated problem produces a product that dies the day the code is finished. In this market reachability is *online* reachability.

- **5** — The team is already inside: past job, family business, member of the community. Or there's an active, welcoming subreddit/Discord where practitioners answer questions from strangers.
- **3** — Reachable with effort: identifiable job titles on LinkedIn, active trade forums, review-site reviewers who can be contacted, conferences.
- **1** — Closed circle. Hospital administrators, bank operations, government procurement, enterprise security buyers. Gatekept by procurement and NDAs.

### 2. Pain intensity — how much does it actually hurt?

Time and money lost must be measurable. There is a product-shaped gap between "mildly annoying" and "this costs me three days a month."

- **5** — Measurable recurring loss: missed jobs, penalties, double entry, rework, churned customers.
- **3** — Irritating but survivable; doesn't stop the business.
- **1** — "Nice to have." A vitamin, not a painkiller.

### 3. Willingness to pay — is there budget and a buying habit?

A vertical that already buys software is enormously easier: the sales conversation becomes "better than what you have" rather than "software is worth paying for."

- **5** — Already subscribed to industry software; B2B; invoices customers; per-seat spend is normal.
- **4** — Pays for adjacent tools (accounting, payments, scheduling) but not for this workflow yet.
- **2** — Could pay but has no habit; every sale requires education.
- **1** — Consumers, hobbyists, nonprofits with no budget, or an audience that expects free.

### 4. Technical fit — can this team ship it in a few months?

- **5** — CRUD plus workflow plus reporting. Standard web/mobile, no integrations required to be useful.
- **4** — One well-documented integration (payments, calendar, email, a single public API).
- **3** — Several integrations, or moderate complexity: scheduling/routing optimization, multi-tenant permissions, offline sync.
- **2** — Requires ML with training data you don't have, or heavy compliance (SOC 2 before first customer).
- **1** — Hardware, closed-data access, or illegal without a license.

### 5. Wedge availability — is there a seam a small team can enter through?

This criterion does not exist in emerging markets, and it is the one that decides outcomes here. Every US/EU vertical already has incumbents. Score the *seam*, not the emptiness.

- **5** — A clear seam: an underserved sub-vertical, an ignored adjacent workflow, a price tier nobody serves, a fresh regulatory mandate, or a platform shift incumbents haven't absorbed.
- **3** — A plausible seam that needs sharpening — incumbents are weak somewhere but not absent.
- **1** — Incumbents are mature, cheap, well-loved, and cover the workflow end to end. Nothing to enter through.

## Reading the total

- **20-25:** Strong candidate. Start Stage 2 here.
- **15-19:** Workable, but the low criterion needs a concrete offsetting advantage.
- **Under 15:** Drop it unless the team holds a specific card in this space.

**Hard override 1:** if Reachability is 1, eliminate regardless of total. Everything built without talking to users is a guess.

**Hard override 2:** if Wedge availability is 1, eliminate regardless of total. Entering a well-served market without a seam is choosing to lose on someone else's terms.

## Candidate vertical pool (US and Western Europe)

Starting points. The parenthetical is *why it's a candidate* — do not copy these into your output, verify them with current research.

**Field service and trades**
- Auto repair and independent service shops — parts ordering, status communication, technician time
- HVAC, plumbing, electrical contractors — dispatch, quoting, callbacks
- Pool, lawn, pest, cleaning services — route density, recurring scheduling, seasonal churn
- Locksmiths, garage door, appliance repair — small operators, high dispatch chaos
- Septic, well drilling, specialty trades — narrow verticals incumbents ignore

**Professional services**
- Accounting and bookkeeping firms — client document chasing (high pain, high willingness to pay)
- Law practices (small firms) — intake, matter tracking, billing reconciliation
- Insurance agencies (independent) — renewals, carrier portal juggling
- Recruiting and staffing agencies — candidate pipeline, compliance paperwork
- Architecture and engineering firms — drawing revisions, submittal tracking

**Healthcare adjacent (non-PHI)**
- Dental, optometry, veterinary practices — scheduling, recall, no-shows
- Physical therapy, chiropractic, mental health private practice — intake and insurance admin
- Medical billing companies — denial management
- *Note:* score technical fit carefully. Anything touching patient records raises the compliance burden sharply; the safe seam is the admin workflow around the record, not the record itself.

**Hospitality and food**
- Independent restaurants and cafés — inventory, scheduling, vendor ordering
- Catering and food trucks — event logistics, quoting
- Breweries, wineries, distilleries — compliance reporting, distribution tracking
- Specialty food producers and co-packers — traceability, lot tracking

**Logistics and supply**
- Small trucking fleets and owner-operators — compliance, settlement, load matching admin
- Freight brokers — carrier vetting, document collection
- Last-mile and courier operations — proof of delivery, exception handling
- Warehousing and 3PL small operators — inventory reconciliation

**Construction and property**
- Specialty subcontractors — change orders, lien waivers, progress billing
- Property management (small portfolio) — maintenance requests, turnover
- Home inspection, appraisal — report generation and delivery
- Equipment rental — asset tracking, utilization

**Education and training**
- Tutoring centers, test prep, music schools — scheduling, billing, parent communication
- Trade schools and CE providers — certification and credit tracking
- Corporate training providers — compliance training records

**Manufacturing and production**
- Job shops and machine shops — quoting, scheduling, WIP tracking
- Custom fabrication — estimating, revision control
- Print shops and signage — proofing, job routing

**Digital and creative**
- Agencies and studios — scoping, approvals, retainer reconciliation
- E-commerce sellers — multi-channel inventory, returns
- Content and creator businesses — sponsorship pipeline, rights tracking

**Compliance-driven (often the fastest to revenue)**
- Any vertical affected by a mandate in the last 12-24 months
- EU: e-invoicing mandates, accessibility requirements, sustainability/ESG reporting for SMEs, NIS2 scope expansion
- US: state-level privacy laws, DOL/OSHA recordkeeping, industry licensing renewals, beneficial ownership reporting

## Signs of life to check per vertical

One or two searches each. These four produce the rationale sentence in your table.

- **Market size** — number of businesses (US Census/BLS industry data, trade association membership, EU statistical offices). This is the denominator of every later market-size estimate.
- **Recent mandate** — anything new in the last 12-24 months creates budget that didn't exist before.
- **Incumbent pricing** — what do existing tools charge? This proves people pay and sets the price band. Also reveals the price tier gap seam.
- **Complaint volume** — search the vertical name with frustration language and see what surfaces. Silence usually means either no pain or no reachable community.
