import time
import sys

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = [float(line.strip()) for line in file]
        return data, len(data)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except ValueError:
        print(f"Error: Invalid data found in '{file_path}'. "
              f"Please ensure all entries are valid numbers.")
        sys.exit(1)

def convert_to_binary_hex(data):
    binary_results = [bin(int(num)) for num in data]
    hex_results = [hex(int(num)) for num in data]
    return binary_results, hex_results

def main():
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()

    try:
        data, num_records = read_file(file_path)

        binary_results, hex_results = convert_to_binary_hex(data)

        end_time = time.time()

        with open("ConversionResults.txt", 'w') as result_file:
            for i in range(num_records):
                result_file.write(f"Original: {data[i]}, Binary: {binary_results[i]},"
                                  f"Hex: {hex_results[i]}\n")

            result_file.write(f"Time Elapsed: {end_time - start_time} seconds\n")

        print("Conversion completed successfully. Results saved to ConversionResults.txt.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
