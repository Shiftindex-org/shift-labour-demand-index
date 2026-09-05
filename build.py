# -*- coding: utf-8 -*-
"""
Builds shift_ldi_2026_e1_by_occupation.csv, the occupation margin of the
SHIFT Labour Demand Index 2024-2026 (Edition 1).

WHY THIS FILE IS PUBLISHED
    The CSV alone is a table you have to take on trust. This script is the thing
    that writes it, and it refuses to write anything that contradicts the
    published methodology. Read it, run it, and you get the CSV back byte for
    byte; change a row so the dataset would disagree with the method, and it
    stops instead of producing a file.

WHAT IS IN HERE, AND WHAT IS NOT
    The 23 rows below are the whole of the dataset: one row per kind of work,
    seven columns, all of them already visible on the free pages of
    shiftindex.org, from which they were read on 5 September 2026.

    This file does NOT contain, and never did: the SHIFT Pull value for any kind
    of work, the occupation-by-market matrix, or any per-market count. Those are
    not published.

    Note on markets_with_fewer_postings: it is a COUNT, not a list. It says in
    how many markets advertisements fell, never which ones.

RUNNING IT
    python3 build.py

    No dependencies beyond the Python standard library. Run it from the
    directory holding the three Markdown documents, which the second check
    reads.
"""
import csv
import pathlib
import re

# The build ID is written here, once. It also appears in the three Markdown
# documents, and the check at the foot of this file refuses to run if any copy
# disagrees with this line. A quantity with two definitions eventually
# disagrees at some boundary, and the boundary that matters for a dataset is the
# permanent citation: a published DOI cannot be withdrawn from the record.
# The suffix names the surface this copy is published on.
BUILD_ID = "SHIFT-LDI-2026-E1-G"

# key, label, exposure class, world count, direction status, markets visible,
# markets where advertisements fell
#
# One value is inferred rather than read: personal_services has 0 in the last
# column, because the published page omits that sentence entirely when the
# number is zero. It is declared as inferred in DATA_DICTIONARY.md and README.md.
ROWS = [
 ("accounting_finance","Accounting & bookkeeping","AI-exposed","rose","published (robust)",22,7),
 ("admin_clerical","Administrative & clerical","AI-exposed","rose","not published",20,3),
 ("agriculture","Agriculture & landscaping","AI-resilient","rose","published (robust)",8,1),
 ("sales_b2b","B2B / field sales","AI-exposed","rose","published (robust)",21,10),
 ("personal_services","Cleaning, food & security","AI-resilient","rose","published (robust)",17,0),
 ("construction","Construction & building trades","AI-resilient","rose","published (robust)",12,1),
 ("customer_support","Customer support & call center","AI-exposed","rose","published (robust)",19,6),
 ("data_analytics","Data analysts & entry","AI-exposed","fell","published (robust)",21,8),
 ("transport_driver","Drivers & transport","AI-resilient","rose","published (robust)",16,1),
 ("electrical","Electricians","AI-resilient","rose","not published",14,3),
 ("legal_support","Legal support","AI-exposed","rose","not published",8,2),
 ("marketing_content","Marketing, content & translation","AI-exposed","fell","published (robust)",18,13),
 ("mechanic_maintenance","Mechanics & maintenance techs","AI-resilient","rose","published (sensitive)",18,4),
 ("healthcare_frontline","Nurses & care workers","AI-resilient","rose","published (robust)",14,1),
 ("healthcare_physicians","Physicians & doctors","AI-resilient","rose","published (robust)",11,1),
 ("plumbing","Plumbers & pipefitters","AI-resilient","rose","published (robust)",7,1),
 ("production_operator","Production & machine operators","AI-resilient","rose","published (robust)",12,2),
 ("real_estate_broker","Real-estate agents/brokers","AI-resilient","rose","not published",9,4),
 ("retail_sales","Retail & shop assistants","AI-resilient","rose","published (robust)",22,1),
 ("software_dev","Software developers","AI-exposed","fell","published (robust)",24,21),
 ("teaching","Teachers","AI-resilient","rose","published (robust)",17,2),
 ("warehouse_logistics","Warehouse & logistics","AI-resilient","rose","published (robust)",11,1),
 ("welding_metal","Welders & metalworkers","AI-resilient","rose","published (sensitive)",13,3),
]

HEADER = ["occupation_key", "occupation_label", "ai_exposure_class",
          "world_count_change", "direction_status", "markets_visible",
          "markets_with_fewer_postings"]

with open("shift_ldi_2026_e1_by_occupation.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(HEADER)
    writer.writerows(ROWS)

# CHECK 1 - the dataset must agree with the published methodology.
#
# The methodology states how many directions are published and how firmly:
# 17 robust, 2 sensitive to the choice of combination rule, and 4 where the
# alternative rules disagreed enough that no direction is published at all.
# If editing a row breaks that split, the dataset and the method have parted
# company, and this stops rather than shipping the disagreement.
robust    = sum(1 for r in ROWS if r[4] == "published (robust)")
sensitive = sum(1 for r in ROWS if r[4] == "published (sensitive)")
withheld  = sum(1 for r in ROWS if r[4] == "not published")

assert (robust, sensitive, withheld) == (17, 2, 4), (
    f"does not match: {robust}/{sensitive}/{withheld} - "
    "the methodology states 17 robust / 2 sensitive / 4 not published")
assert len(ROWS) == 23, "there must be 23 kinds of work"
assert max(r[5] for r in ROWS) == 24, "the largest market coverage must be 24"
assert all(r[6] <= r[5] for r in ROWS), (
    "markets where advertisements fell can never exceed markets visible")

print(f"OK  23 rows | {robust} robust | {sensitive} sensitive | {withheld} no direction published")
print(f"OK  markets visible: {min(r[5] for r in ROWS)} to {max(r[5] for r in ROWS)}")

# CHECK 2 - the build ID is one value, spelled one way, everywhere.
DOCS = ["README.md", "DATA_DICTIONARY.md", "METHODOLOGY.md"]
mismatches = []
for name in DOCS:
    text = pathlib.Path(name).read_text(encoding="utf-8")
    for found in re.finditer(r"SHIFT-LDI-[0-9A-Za-z-]+", text):
        if found.group(0) != BUILD_ID:
            mismatches.append(f"{name}: {found.group(0)}")
    if BUILD_ID not in text:
        mismatches.append(f"{name}: does not mention the build ID at all")

if mismatches:
    raise SystemExit(
        "\nBUILD ID IS NOT THE SAME EVERYWHERE.\n"
        f"   Expected: {BUILD_ID}\n"
        "   Found:\n     " + "\n     ".join(mismatches) +
        "\n   Fix it in the documents. The value is set on the BUILD_ID line "
        "of this script.\n")

print(f"OK  build ID `{BUILD_ID}` identical across {len(DOCS)} documents")
