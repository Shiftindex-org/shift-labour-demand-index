# SHIFT Labour Demand Index 2024–2026 (Edition 1)

**Build ID:** `SHIFT-LDI-2026-E1-G`

An open measurement of **what happened to advertised demand for 23 kinds of work across 24
markets**, between the twelve months to June 2024 and the twelve months to June 2026.

It is a **count of what employers already advertised for** — not a forecast, not a survey,
and not a statement about cause.

## Headline

| | |
|---|---|
| Advertisements counted, base window (12 months to June 2024) | **4,241,295** |
| Advertisements counted, current window (12 months to June 2026) | **9,323,023** |
| Kinds of work | **23** |
| Markets | **24** |
| Languages | **9** |
| Search terms · exclusions | **744** · **39** |
| Occupation × market cells | **552** |
| Directions published | **17 robust · 2 sensitive · 4 not published** |

**Three kinds of work fell** in the world taken as a whole: software developers, data
analysts & entry, and marketing, content & translation.

**Software developers is the sharpest case in Edition 1**: visible in all 24 markets, and in
**21 of them employers advertised fewer of these jobs** in the latest twelve months than two
years earlier. Fewer jobs — not a smaller share.

## Files

| file | rows | what it is |
|---|---|---|
| `shift_ldi_2026_e1_by_occupation.csv` | 23 | One row per kind of work: exposure class, whether the worldwide count rose or fell, whether a direction is published and how firmly, how many markets it is visible in, and in how many of those advertisements fell. |
| `DATA_DICTIONARY.md` | — | Every column, its values, and the one trap in reading them. |
| `METHODOLOGY.md` | — | Windows, the SHIFT Pull formula, the five robustness tests, the floor, and what the index cannot see. |

## Method, in one paragraph

For each kind of work in each market, advertisements matching a list of job titles **fixed
before counting** are counted in both windows. What is reported is not the count: it is how
that count moved **against the whole basket of work in the same market over the same two
years**. That ratio — the **SHIFT Pull** — is then combined across markets with weights
fixed in advance, and recomputed under five alternative combination rules. Where two or more
alternatives disagree, **no direction is published at all**. Full method in
`METHODOLOGY.md`.

## What this dataset does not contain

This is the **occupation margin** of the index. It does not contain:

- the SHIFT Pull value for any kind of work,
- the occupation × market matrix — **which markets** a kind of work grew or shrank in,
- per-market advertisement counts.

**Buy the full occupation × market detail:** each kind of work is published as a document
naming every market it is visible in and what happened there — <https://shiftindex.org>

## Explore the interactive version

<https://shiftindex.org> — all 23 kinds of work are listed free, with the searches behind
each one.

## Cite this dataset

> Covas, J. (2026). *SHIFT Labour Demand Index 2024–2026 (Edition 1)* [Data set].
> SHIFT Research. https://doi.org/10.5281/zenodo.22346056

DOI: `10.5281/zenodo.22346056`

## Version

Edition 1 · v1.0 · frozen 5 September 2026 · build `SHIFT-LDI-2026-E1-G`

## Author and licence

**Author:** José Covas
**Rights holder:** José Covas Education Academy, Lda
**Licence:** **CC BY 4.0** — you may copy, redistribute and build on this material, including
commercially, provided you credit the source as set out above.

## Provenance

Every value in the CSV was read from the published pages of `shiftindex.org` on
5 September 2026 and checked against the counts the methodology page states
(17 robust / 2 sensitive / 4 not published). One value is inferred and marked as such in
the data dictionary.
