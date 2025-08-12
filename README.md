# SARS-CoV-2 Primer–Deletion Nearest Coordinate Finder

## About
This is a Python script I wrote to help match SARS-CoV-2 deletion coordinates with the closest primer positions from an ARTIC primer BED file.  
It tells you if the closest primer is before or after the deletion, and by how many bases. No extra Python packages are needed—just run it with regular Python.

---

## Files in this repo
- `primer_del_match.py` → the main script
- `SARS-CoV-2.primer-artic_4.1.bed` → primer coordinates (col 2 = start, col 3 = end)
- `all_del_var_9.csv` → deletions list (has Start and End columns)
- `headers.csv` (optional) → lets you rename output columns
- `README.md` → this file

---

## How to Run It

**Requirements:**
- Python 3 (I used 3.9, but any 3.8+ should work)
- No installs needed

**Basic command:**
```bash
python primer_del_match.py SARS-CoV-2.primer-artic_4.1.bed all_del_var_9.csv results.csv
