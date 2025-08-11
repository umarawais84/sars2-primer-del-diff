SARS-CoV-2 Primer–Deletion Nearest Coordinate Finder
📌 Description
This program matches SARS-CoV-2 deletion coordinates to the nearest primer start or end positions from a primer BED file.
It outputs the distance between each deletion start/end and the closest primer coordinate, reporting whether the primer is located before (negative difference) or after (positive difference) the deletion coordinate.

The script was written to use no external Python imports for minimal dependencies and portability. It is fully documented for ease of use and modification.

📂 Input Files
Primer File (SARS-CoV-2.primer-artic_4.1.bed)

Column 2 = Primer start coordinate

Column 3 = Primer end coordinate

Deletion File (all_del_var_9.csv)

Contains deletion start and end coordinates

Headers File (Optional)

Defines column names for output CSV

📊 Output
The program generates a CSV file containing:

Nearest primer to each deletion start and end

Distance (diff) between primer and deletion coordinate

Positive = primer is after the deletion coordinate

Negative = primer is before the deletion coordinate

Side (start or end) indicating whether the nearest coordinate came from BED column 2 or 3

⚙️ Usage
bash
Copy
Edit
python primer_del_match.py primer_file.bed deletions.csv output.csv
Example:

bash
Copy
Edit
python primer_del_match.py SARS-CoV-2.primer-artic_4.1.bed all_del_var_9.csv results.csv
🧾 Notes
No external libraries are required (runs with standard Python 3)

The program uses simple loops and comparisons for maximum compatibility

Written for clarity and easy adaptation to new datasets

👤 Author
Developed by Umar Awais based on specifications from Jim.
