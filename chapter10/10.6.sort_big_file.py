import heapq
import os


def sort_large_file(input_file, output_file, chunk_size):
    # Split the input file into sorted chunks
    chunk_files = []
    with open(input_file, 'r') as f:
        lines = []
        for line in f:
            lines.append(line.strip())
            if len(lines) >= chunk_size:
                lines.sort()
                temp_file = write_chunk_to_temp_file(lines)
                chunk_files.append(temp_file)
                lines = []
        if lines:
            lines.sort()
            temp_file = write_chunk_to_temp_file(lines)
            chunk_files.append(temp_file)

    # Merge sorted chunks into the output file
    merge_sorted_chunks(chunk_files, output_file)

    # Clean up temporary files
    for temp_file in chunk_files:
        os.remove(temp_file)


def write_chunk_to_temp_file(lines):
    temp_file_name = f"chunk_{os.urandom(8).hex()}.txt"
    with open(temp_file_name, 'w') as f:
        for line in lines:
            f.write(line + '\n')
    return temp_file_name


def merge_sorted_chunks(chunk_files, output_file):
    min_heap = []
    file_handlers = []

    # Open all chunk files and initialize the heap
    for i, file_name in enumerate(chunk_files):
        f = open(file_name, 'r')
        file_handlers.append(f)
        line = f.readline().strip()
        if line:
            heapq.heappush(min_heap, (line, i))

    with open(output_file, 'w') as out_f:
        while min_heap:
            smallest_line, file_index = heapq.heappop(min_heap)
            out_f.write(smallest_line + '\n')
            next_line = file_handlers[file_index].readline().strip()
            if next_line:
                heapq.heappush(min_heap, (next_line, file_index))

    # Close all file handlers
    for f in file_handlers:
        f.close()
