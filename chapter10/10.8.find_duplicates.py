def find_duplicates_in_ranges(file_path, range_size, max_value):
    duplicates = set()

    for range_start in range(1, max_value + 1, range_size):
        range_end = min(range_start + range_size - 1, max_value)
        range_duplicates = find_duplicates_in_range(file_path, range_start, range_end)
        duplicates.update(range_duplicates)

    return list(duplicates)


def find_duplicates_in_range(file_path, range_start, range_end):
    seen = set()
    duplicates = set()

    with open(file_path, 'r') as file:
        for line in file:
            num = int(line.strip())
            if range_start <= num <= range_end:
                if num in seen:
                    duplicates.add(num)
                else:
                    seen.add(num)

    return duplicates


# Example usage
file_path = "large_file.txt"
range_size = 1000000  # Adjust based on memory capacity and data distribution
max_value = 100000000  # The maximum value that could be in the file
duplicates = find_duplicates_in_ranges(file_path, range_size, max_value)
print(duplicates)
