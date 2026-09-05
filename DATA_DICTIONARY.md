# Data dictionary — SHIFT Labour Demand Index 2024–2026 (Edition 1)

Build ID: `SHIFT-LDI-2026-E1-G`

## `shift_ldi_2026_e1_by_occupation.csv` — 23 rows, one per kind of work

| column | type | values | meaning |
|---|---|---|---|
| `occupation_key` | string | 23 fixed keys | Stable identifier. Does not change between editions. |
| `occupation_label` | string | — | The published name of the kind of work. |
| `ai_exposure_class` | enum | `AI-exposed`, `AI-resilient` | **A lens, not a finding.** It is how the 23 kinds of work were chosen — to place high- and low-exposure work side by side. It is not a claim about cause. |
| `world_count_change` | enum | `rose`, `fell` | Whether the raw number of advertisements for this work was higher or lower in the second window than the first, worldwide. **This is not the index reading.** |
| `direction_status` | enum | `published (robust)`, `published (sensitive)`, `not published` | Whether the index publishes a direction for this work, and how firmly. See below. |
| `markets_visible` | integer | 7–24 | How many of the 24 markets held enough advertisements for this work to be reported. |
| `markets_with_fewer_postings` | integer | 0–21 | Of those markets, how many had **fewer** advertisements in the second window than the first. Fewer jobs, not a smaller share. |

## `direction_status` — what the three values mean

The index reading is the **SHIFT Pull**: an occupation's growth relative to its own
market's whole basket, combined across markets with weights fixed in advance. Above 1
means the work pulled ahead of the market it sits in; below 1 means it fell behind.

Every figure is then recomputed under **five other ways of combining markets**, all fixed
before the results were seen.

- `published (robust)` — all five alternatives put the work on the same side. **17 of 23.**
- `published (sensitive)` — one alternative disagrees. The direction is published and the
  page says so. **2 of 23.**
- `not published` — two or more disagree, so **no direction is published at all**, only the
  figure. **4 of 23.**

⚠️ **`world_count_change` and `direction_status` are independent.** A kind of work can have
`rose` in the raw worldwide count and still have no published direction — because the count
rising says nothing about whether it rose *faster or slower than the market around it*.
Four rows in this file are exactly that case. Reading `rose` as "this work is doing well"
is the single easiest way to misuse this file.

## What is deliberately NOT in this dataset

- **The SHIFT Pull value itself.** How much a kind of work moved is not published free.
- **The occupation × market matrix** — 552 cells. Which markets a kind of work grew or
  shrank in, named, is the paid product.
- **Per-market advertisement counts.**

This file is the occupation margin of that matrix, and only the margin.

## Provenance

Every value was read from the published pages of `shiftindex.org` on 5 September 2026, not
from an internal export. One value is inferred: `personal_services` has
`markets_with_fewer_postings = 0` because its page omits the sentence that names that count
— the site states the number only when it is at least one.
