SARS-CoV-2 Primer–Deletion Nearest Coordinate Finder
Description (≤350 chars):
Matches SARS-CoV-2 deletion coordinates to the nearest primer start or end from a BED file. Reports distance (positive if after, negative if before) and whether the match is to a primer start or end. Runs with no external Python dependencies.

How to Run
bash
Copy
Edit
python primer_del_match.py <primer_file.bed> <deletions.csv> <output.csv>
Arguments

primer_file.bed — ARTIC primer BED; column 2 = start, column 3 = end.

deletions.csv — CSV with deletion start/end coordinates.

output.csv — path to write results CSV.

Example

bash
Copy
Edit
python primer_del_match.py SARS-CoV-2.primer-artic_4.1.bed all_del_var_9.csv results.csv
Input Formats
Primer BED (tab-separated)
Standard BED with primer intervals. Only columns 2 and 3 are used.

nginx
Copy
Edit
chr1   15400   15424   nCoV-2019_501_LEFT
chr1   15580   15602   nCoV-2019_501_RIGHT
Deletions CSV (comma-separated)
Must contain deletion start and end coordinates (header names are flexible, e.g. Start,End):

sql
Copy
Edit
ID,Start,End
del_001,15412,15435
del_002,15590,15600
Output (CSV)
For each deletion, the nearest primer coordinate is computed separately for the deletion Start and End against both primer starts (col 2) and ends (col 3).

Columns:

del_start, del_end — input coordinates.

nearest_start_coord, diff_start, side_start — nearest to deletion Start.

nearest_end_coord, diff_end, side_end — nearest to deletion End.

Conventions:

side_* ∈ {start,end} indicating whether the match came from BED column 2 (start) or column 3 (end).

diff_* = nearest_coord − deletion_coord

Positive → primer coordinate is after the deletion coordinate

Negative → primer coordinate is before the deletion coordinate

(If two primer coordinates are equally close, the script uses a deterministic tie-break—see code comments.)

Features
No third-party imports; works with stock Python 3.

Linear scan with simple arithmetic; easy to audit and port.

Clear in-code documentation and comments.

Quick Test
bash
Copy
Edit
# Replace with your actual file names
python primer_del_match.py SARS-CoV-2.primer-artic_4.1.bed all_del_var_9.csv results.csv
# Open results.csv to review nearest coordinates, diffs, and sides
Reproducibility Notes
Coordinates are treated as 1-based integers (match your input).

Only numeric positions are used; chromosome names in BED are ignored.

Whitespace and empty lines are safely skipped.

Author & Citation
Author: Umar Awais
Suggested citation (if used in a publication):
Awais, U. (2025). SARS-CoV-2 Primer–Deletion Nearest Coordinate Finder (Version X.Y). GitHub repository: <repo URL>

License
MIT License © 2025 Umar Awais
(Include a LICENSE file in the repo; MIT is recommended for academic reuse with attribution.)

Contact
For questions or feature requests, please open a GitHub issue or email me.
