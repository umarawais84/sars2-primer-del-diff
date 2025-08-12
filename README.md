# SARS-CoV-2 Primer–Deletion Nearest Coordinate Finder

**Description:**  
Matches SARS-CoV-2 deletion coordinates to the nearest primer start or end from a BED file. Reports distance (positive if after, negative if before) and whether the match is to a primer start or end. Runs with no external Python dependencies.

---

## How to Run

```bash
python primer_del_match.py <primer_file.bed> <deletions.csv> <output.csv>

Arguments:

1. primer_file.bed — ARTIC primer BED; column 2 = start, column 3 = end.

deletions.csv — CSV with deletion start/end coordinates.

output.csv — path to write results CSV.
