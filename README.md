# SARS-CoV-2 Primer–Deletion Nearest Coordinate Finder

**Description:**  
Matches SARS-CoV-2 deletion coordinates to the nearest primer start or end from a BED file. Reports distance (positive if after, negative if before) and whether the match is to a primer start or end. Runs with no external Python dependencies.

---

## How to Run

```bash
python primer_del_match.py <primer_file.bed> <deletions.csv> <output.csv>
