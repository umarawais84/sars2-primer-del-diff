 SARS-CoV-2 Primer–Deletion Nearest Coordinate Finder

**Description:**  
Matches SARS-CoV-2 deletion coordinates to the nearest primer start or end from a BED file. Reports distance (positive if after, negative if before) and whether the match is to a primer start or end. Runs with no external Python dependencies.

---

## How to Run

```bash
python primer_del_match.py <primer_file.bed> <deletions.csv> <output.csv>
Arguments:

primer_file.bed — ARTIC primer BED; column 2 = start, column 3 = end.

deletions.csv — CSV with deletion start/end coordinates.

output.csv — path to write results CSV.

Example:

bash
Copy
Edit
python primer_del_match.py SARS-CoV-2.primer-artic_4.1.bed all_del_var_9.csv results.csv
Input Formats
Primer BED (tab-separated):

nginx
Copy
Edit
chr1   15400   15424   nCoV-2019_501_LEFT
chr1   15580   15602   nCoV-2019_501_RIGHT
Deletions CSV (comma-separated):

sql
Copy
Edit
ID,Start,End
del_001,15412,15435
del_002,15590,15600
Output (CSV)
The script finds the nearest primer coordinate for each deletion Start and End, checking both primer starts (BED col 2) and ends (BED col 3).

Columns:

del_start, del_end — input coordinates

nearest_start_coord, diff_start, side_start — nearest to deletion Start

nearest_end_coord, diff_end, side_end — nearest to deletion End

Conventions:

side_* ∈ {start,end} → came from BED column 2 (start) or 3 (end)

diff_* = nearest_coord − deletion_coord

Positive → primer coordinate is after

Negative → primer coordinate is before

Features
No third-party imports (pure Python 3)

Linear scan for easy review and modification

Well-commented for clarity

Quick Test
bash
Copy
Edit
python primer_del_match.py SARS-CoV-2.primer-artic_4.1.bed all_del_var_9.csv results.csv
Open results.csv to view nearest coordinates, differences, and sides.

Author & Citation
Author: Umar Awais

Suggested citation:

scss
Copy
Edit
Awais, U. (2025). SARS-CoV-2 Primer–Deletion Nearest Coordinate Finder (Version X.Y). GitHub repository: <repo URL>
License
MIT License © 2025 Umar Awais

pgsql
Copy
Edit

Do you want me to also make the **MIT LICENSE file** so your authorship is legall
