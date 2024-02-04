"""
convert_numbers.py - A script to convert numbers from a file to binary and hex.
"""

import time
import sys

def read_file(file_path):
    """
    Reads the data from the specified file and returns it.

    Parameters:
    - file_path (str): The path to the file.

    Returns:
    - data (list): List of numbers read from the file.
    - num_records (int): Number of records read.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = []
            for line in file:
                try:
                    num = float(line.strip())
                    data.append(num)
                except ValueError:
                    print(f"Warning: Invalid data found in '{file_path}'. "
                          f"Skipping entry: {line.strip()}")
            num_records = len(data)
        return data, num_records
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

def convert_to_binary_hex(data):
    """
    Converts a list of numbers to binary and hex formats.

    Parameters:
    - data (list): List of numbers.

    Returns:
    - binary_results (list): List of binary representations.
    - hex_results (list): List of hex representations.
    """
    binary_results = [bin(int(num)) for num in data]
    hex_results = [hex(int(num)) for num in data]
    return binary_results, hex_results

def main():
    """
    Main function to execute the conversion process.
    """
    if len(sys.argv) != 2:
        print("Usage: python convert_numbers.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()

    try:
        data, num_records = read_file(file_path)

        binary_results, hex_results = convert_to_binary_hex(data)

        end_time = time.time()

        with open("ConversionResults.txt", 'w', encoding='utf-8') as result_file:
            for i in range(num_records):
                result_file.write(f"Original: {data[i]}, Binary: {binary_results[i]},"
                                  f" Hex: {hex_results[i]}\n")

            result_file.write(f"Time Elapsed: {end_time - start_time} seconds\n")

        print("Conversion completed successfully. "
              "Results saved to ConversionResults.txt.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
