"""
Script to compute descriptive statistics from a file containing numbers.
"""

import time
import sys
import math

def read_file(file_path):
    """
    Read data from the given file.

    Parameters:
    - file_path (str): Path to the file containing numbers.

    Returns:
    - data (list): List of numbers read from the file.
    - num_records (int): Number of records found in the file.
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

def calculate_mean(data):
    """
    Calculate the mean of a list of numbers.

    Parameters:
    - data (list): List of numbers.

    Returns:
    - mean (float): Mean of the numbers.
    """
    return sum(data) / len(data)

def calculate_median(data):
    """
    Calculate the median of a list of numbers.

    Parameters:
    - data (list): List of numbers.

    Returns:
    - median (float): Median of the numbers.
    """
    sorted_data = sorted(data)
    n = len(data)
    if n % 2 == 0:
        middle1 = sorted_data[n // 2 - 1]
        middle2 = sorted_data[n // 2]
        return (middle1 + middle2) / 2
    return sorted_data[n // 2]

def calculate_mode(data):
    """
    Calculate the mode of a list of numbers.

    Parameters:
    - data (list): List of numbers.

    Returns:
    - mode_list (list): List of modes.
    """
    count_dict = {}
    for num in data:
        count_dict[num] = count_dict.get(num, 0) + 1

    max_count = max(count_dict.values())
    mode_list = [k for k, v in count_dict.items() if v == max_count]
    return mode_list

def calculate_variance(data, mean):
    """
    Calculate the variance of a list of numbers.

    Parameters:
    - data (list): List of numbers.
    - mean (float): Mean of the numbers.

    Returns:
    - variance (float): Variance of the numbers.
    """
    return sum((x - mean) ** 2 for x in data) / len(data)

def calculate_standard_deviation(variance):
    """
    Calculate the standard deviation.

    Parameters:
    - variance (float): Variance.

    Returns:
    - std_deviation (float): Standard deviation.
    """
    return math.sqrt(variance)

def main():
    """
    Main function to calculate and display descriptive statistics.
    """
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()

    try:
        data, num_records = read_file(file_path)

        mean = calculate_mean(data)
        median = calculate_median(data)
        mode = calculate_mode(data)
        variance = calculate_variance(data, mean)
        std_deviation = calculate_standard_deviation(variance)

        end_time = time.time()

        with open("StatisticsResults.txt", 'w', encoding='utf-8') as result_file:
            result_file.write(f"Count: {num_records}\n")
            result_file.write(f"Mean: {mean}\n")
            result_file.write(f"Median: {median}\n")
            result_file.write(f"Mode: {mode}\n")
            result_file.write(f"Variance: {variance}\n")
            result_file.write(f"Standard Deviation: {std_deviation}\n")
            result_file.write(f"Time Elapsed: {end_time - start_time} seconds\n")

        print("Descriptive statistics calculated successfully."
                "Results saved to StatisticsResults.txt.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
