# SARS-CoV-2 Primer–Deletion Nearest Coordinate Finder

**Description:** Matches SARS-CoV-2 deletion coordinates to the nearest primer *start* or *end* from a BED file. Outputs signed distances (positive = primer after deletion coord; negative = primer before). Pure Python (no external deps). Suitable for analysis and publication pipelines.

---

## Contents
- `primer_del_match.py` – main script (no external imports)
- `SARS-CoV-2.primer-artic_4.1.bed` – primer BED (cols: chrom, **start**, **end**, …)
- `all_del_var_9.csv` – deletions table (includes **Start**, **End**)
- `headers.csv` (optional) – output header names
- `README.md` – this file

---

## Quick Start

### Requirements
- Python 3.8+ (standard library only)

### Run
```bash
python primer_del_match.py SARS-CoV-2.primer-artic_4.1.bed all_del_var_9.csv results.csv
# With custom headers:
python primer_del_match.py SARS-CoV-2.primer-artic_4.1.bed all_del_var_9.csv results.csv --headers headers.csv
