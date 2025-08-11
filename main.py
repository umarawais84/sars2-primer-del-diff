"""
SARS-CoV-2 Deletion to Primer Coordinate Mapper

This program finds the nearest primer coordinates to deletion start and end positions.
It reads deletion coordinates from 'all_del_var_9.csv' and primer coordinates from 
'SARS-CoV-2.primer-artic_4.1.bed', then outputs results to a CSV file.

Usage:
    python main.py

Input files:
    - all_del_var_9.csv: Contains deletion data (Size, Start, End)
    - SARS-CoV-2.primer-artic_4.1.bed: Contains primer coordinates (tab-separated)
    - headers.csv: Contains output column headers

Output:
    - results.csv: Contains nearest primer coordinates for each deletion
"""

def read_csv_file(filename):
    """
    Read a CSV file and return data as list of lists.
    
    Args:
        filename (str): Path to the CSV file
        
    Returns:
        list: List of rows, where each row is a list of values
    """
    data = []
    with open(filename, 'r') as file:
        for line in file:
            # remove newline and split by comma
            row = line.strip().split(',')
            data.append(row)
    return data

def read_bed_file(filename):
    """
    Read a BED file and extract primer coordinates.
    
    Args:
        filename (str): Path to the BED file
        
    Returns:
        list: List of primer coordinates [start, end]
    """
    coordinates = []
    with open(filename, 'r') as file:
        for line in file:
            # remove newline and split by tab
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                start = int(parts[1]) # Column 2 (0-indexed as 1)
                end = int(parts[2]) # Column 3 (0-indexed as 2)
                coordinates.extend([start, end])
    
    # remove duplicates and sort
    coordinates = sorted(list(set(coordinates)))
    return coordinates

def find_nearest_coordinate(target, coordinates):
    """
    Find the nearest coordinate to a target position.
    
    Args:
        target (int): Target position
        coordinates (list): Sorted list of coordinates
        
    Returns:
        tuple: (nearest_coordinate, difference, side)
               side is 'start' if from column 2, 'end' if from column 3
    """
    if not coordinates:
        return None, 0, 'unknown'
    
    # find the closest coordinate
    min_diff = float('inf')
    nearest_coord = coordinates[0]
    
    for coord in coordinates:
        diff = abs(coord - target)
        if diff < min_diff:
            min_diff = diff
            nearest_coord = coord
    
    # calculate signed difference (positive if coord is after target, negative if before)
    signed_diff = nearest_coord - target
    
    return nearest_coord, signed_diff, 'unknown'

def find_coordinate_side(coord, bed_filename):
    """
    Determine if a coordinate comes from start (column 2) or end (column 3).
    
    Args:
        coord (int): The coordinate to check
        bed_filename (str): Path to the BED file
        
    Returns:
        str: 'start' if from column 2, 'end' if from column 3, 'both' if in both
    """
    in_start = False
    in_end = False
    
    with open(bed_filename, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                start = int(parts[1])
                end = int(parts[2])
                
                if start == coord:
                    in_start = True
                if end == coord:
                    in_end = True
    
    if in_start and in_end:
        return 'both'
    elif in_start:
        return 'start'
    elif in_end:
        return 'end'
    else:
        return 'unknown'

def write_csv_file(filename, data):
    """
    Write data to a CSV file.
    
    Args:
        filename (str): Output filename
        data (list): List of rows to write
    """
    with open(filename, 'w') as file:
        for row in data:
            file.write(','.join(map(str, row)) + '\n')

def main():
    """
    Main function to process deletions and find nearest primer coordinates.
    """
    print("SARS-CoV-2 Deletion to Primer Coordinate Mapper")
    print("=" * 50)
    
    # read input files
    print("Reading deletion data...")
    deletion_data = read_csv_file('all_del_var_9.csv')
    
    print("Reading primer coordinates...")
    primer_coordinates = read_bed_file('SARS-CoV-2.primer-artic_4.1.bed')
    
    print("Reading headers...")
    headers = read_csv_file('headers.csv')
    
    print(f"Found {len(deletion_data)-1} deletions and {len(primer_coordinates)} unique primer coordinates")
    
    # prepare results
    results = []
    
    # add headers
    if headers:
        results.append(headers[0])
    else:
        results.append(['Size', 'Start', 'diff', 'side', 'End', 'diff', 'side'])
    
    # process each deletion (skip header row)
    print("Processing deletions...")
    for i, row in enumerate(deletion_data[1:], 1):
        if len(row) >= 3:
            try:
                size = int(row[0])
                start = int(row[1])
                end = int(row[2])
                
                # find nearest coordinates for start position
                start_coord, start_diff, _ = find_nearest_coordinate(start, primer_coordinates)
                start_side = find_coordinate_side(start_coord, 'SARS-CoV-2.primer-artic_4.1.bed')
                
                # find nearest coordinates for end position
                end_coord, end_diff, _ = find_nearest_coordinate(end, primer_coordinates)
                end_side = find_coordinate_side(end_coord, 'SARS-CoV-2.primer-artic_4.1.bed')
                
                # create result row
                result_row = [size, start, start_diff, start_side, end, end_diff, end_side]
                results.append(result_row)
                
                if i % 10 == 0: # progress indicator
                    print(f"Processed {i} deletions...")
                    
            except ValueError as e:
                print(f"Warning: Skipping row {i+1} due to invalid data: {row}")
                continue
    
    print("Writing results to 'results.csv'...")
    write_csv_file('results.csv', results)
    
    print(f"Complete! Processed {len(results)-1} deletions.")
    print("Results saved to 'results.csv'")
    
    print("\nSample results:")
    print("Size,Start,diff,side,End,diff,side")
    for i, row in enumerate(results[1:6]): # show first 5 data rows for brevity
        print(','.join(map(str, row)))
    if len(results) > 6:
        print("...")

if __name__ == "__main__":
    main()