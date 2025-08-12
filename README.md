```markdown
# 🧬 SARS-CoV-2 Primer–Deletion Nearest Coordinate Finder

```

---

/ ****|                    (*)           | |
\| (***  \_ \_\_   \_\_\_ \_ \_\_ \_\_\_  \_ \_ \_\_   \_\_ *| |* \_\_\_
\_\_\_ | '\_ \ / \_ \ '\_ ` _ \| | '_ \ / _` | **/ \_&#x20;
****) | |*) |  \_\_/ | | | | | | | | | (*| | ||  **/
|****\_/| .**/ \_**|*| |*| |*|*|*| |*|\_*,*|\_\_\_**|
\| |
|\_|
Nearest Primer–Deletion Coordinate Finder

````

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
````

**With custom headers:**

```bash
python primer_del_match.py SARS-CoV-2.primer-artic_4.1.bed all_del_var_9.csv results.csv --headers headers.csv
```

---

## What the Script Does

1. Reads primer start/end positions from the BED file.
2. Reads each deletion's start and end coordinates from the CSV.
3. Finds which primer coordinate is closest to each deletion coordinate.
4. Figures out if that primer is before or after (positive = after, negative = before).
5. Writes everything into a results CSV you can open in Excel.

---

## Output CSV Columns

* **del\_start** → deletion start coordinate
* **nearest\_start** → closest primer to deletion start
* **side\_start** → “start” or “end” depending on whether it matched to col 2 or col 3 from BED
* **diff\_start** → signed distance from deletion start to primer

(same thing for deletion end: **del\_end**, **nearest\_end**, **side\_end**, **diff\_end**)

---

## Example

If deletion start = 150 and nearest primer start = 160 → `diff = 10` (primer after deletion start)
If deletion end = 600 and nearest primer end = 590 → `diff = -10` (primer before deletion end)

---

## Tips / Notes

* Make sure both files use the same coordinate system (BED is usually 0-based, CSV might be 1-based).
* If the script gives weird values, check if you need to adjust for that.
* It’s written to be easy to follow, so you can change the logic if you need to.

---

## Why I Made It

This was for a project where we might need it for a publication. I wanted it to be super easy to run and understand, even if you’ve never used Python much before.

---

## Contact

If you have questions or want me to change something, just let me know.

```

Do you want me to also make a **shorter, one-line GitHub repo description** that matches this student vibe for when people see your repo on the search page?
```
