# Methodology — SHIFT Labour Demand Index 2024–2026 (Edition 1)

Build ID: `SHIFT-LDI-2026-E1-G` · Version 1.0 · Frozen 5 September 2026

This file restates, for the open dataset, the method published in full at
<https://shiftindex.org/methodology/>. Where the two differ, the website governs.

## Scope

SHIFT counts **online job advertisements**. It does not count people, hires, vacancies
across the whole economy, or salaries, and it does not by itself establish *why* demand
changed. It is aggregated market evidence — **not advice, and not a forecast**.

## Windows

Edition 1 counts two complete twelve-month windows:

| window | advertisements |
|---|---|
| 12 months to **June 2024** (base) | **4,241,295** |
| 12 months to **June 2026** (current) | **9,323,023** |

Both windows are counted on the same sources, which removes the largest way a market could
move for reasons of measurement rather than hiring.

## The reading

For occupation *o* in market *m*:

    R(o,m) = [ Postings(o,m,now) / Postings(o,m,base) ] / [ Basket(m,now) / Basket(m,base) ]

where *Basket(m,year)* is every advertisement counted in that market that year, across every
kind of work. Markets are combined with weights fixed in advance from the base window:

    w(m) = Basket(m,base) / all base-window postings
    Pull(o) = Σ w(m)·R(o,m) / Σ w(m)

That combined figure is the **SHIFT Pull**. Above 1: the work pulled ahead of the market it
sits in. Below 1: it fell behind. It is not a count, not a forecast, and not a statement
about cause.

The weights are deliberately **not** each occupation's own geography — weighting an
occupation by where it happens to be advertised would let the shape of its coverage decide
its answer. 5 cells in 552 have no base-window count and are excluded, with weights
renormalised over the rest.

## Robustness

Each figure is recomputed under five other combination rules, settled on 20 August 2026 in
advance: the median of R(o,m); the unweighted mean; the geometric mean; the weighted rule
restricted to markets clearing the floor; and a pooled ratio summing postings before
dividing.

- all five agree → direction published
- one disagrees → direction published, and said so
- two or more disagree → **figure published, no direction at all**

Edition 1: **17 robust · 2 sensitive · 4 with no published direction.**

## Coverage and taxonomy

23 kinds of work · 24 markets · 9 languages · **744 search terms** and **39 exclusions**,
all fixed before counting began, including terms tested and rejected · 7 groups derived
from ISCO-08 · 552 occupation × market cells.

Coverage is deliberately uneven: the number of markets in which a kind of work is visible
ranges from **7 to 24**.

## Three restrictions

1. **A floor, fixed in advance.** A market is shown for a kind of work only once it clears
   **500 advertisements** in the base window. Sub-floor cells are *not* deleted from the
   basket — they keep their weight, so every occupation is measured against the same
   geography. Median sub-floor share of an occupation's numerator: 0.82%; maximum 9.3%;
   largest single sub-floor cell 496 advertisements.
2. **We never compare one market against another.** Advertisement density and how much
   hiring happens online differ too much between countries for raw counts to mean the same
   thing. Only direction and pace of change *within* each market are comparable.
3. **A large source was removed from the count** because it entered the index halfway
   through the period. A source arriving mid-series makes growth in our sight of the market
   look like growth in the market. Throwing that data away is what protects the comparison,
   and it is why the source list is narrower than it could be.

## What we can and cannot see

- **97.0%** of what is counted comes from a single site. Two markets add a second.
- In **4 of the 24** published markets, at least a quarter of the base-window count sits in
  cells too small to publish alone. Read those as a direction, not a measurement.
- **Two further markets were collected and are not published**: under this edition's source
  recipe the provider returns no advertisements for them at all — not few, none.
- **One kind of work sits below our own admission rule.** It requires clearing the floor in
  at least eight markets; plumbers & pipefitters clears it in seven. The rule forbids
  changing a closed occupation list because of what the numbers say, so the pre-committed
  list is kept and the shortfall is disclosed instead. Removing it would change the reported
  basket trend by 0.08 percentage points.
- Independent work on AI and hiring points in more than one direction, and some of it
  complicates this reading.

## The AI lens, honestly

AI exposure is the lens used to choose which kinds of work to place side by side. It is
**not a finding about cause**. Changes in advertised demand may reflect the economic cycle,
hiring practices, platform coverage, occupational reclassification, automation, or other
factors.

## Freezing rule and changelog

Once frozen, this methodology does not change without a changelog entry and a version bump.
A source or fact that contradicts an existing classification is marked as an exception and
stops the line for review — never resolved silently.

- **v1.0** — 5 September 2026. Edition 1, first open release.

*Note: Edition 1 was recalculated before commercial launch following independent statistical
review. The earlier rule summed postings across markets before dividing, which let a
market's change in coverage enter the numerator of every kind of work present in it. The
rule above removes that by construction rather than testing for it afterwards.*
