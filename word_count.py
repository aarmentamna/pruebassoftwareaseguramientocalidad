"""
word_count.py - A script to count the frequency of words in a file.
"""

import time
import sys

def read_file(file_path):
    """
    Reads the content of the specified file and returns a list of words.

    Parameters:
    - file_path (str): The path to the file.

    Returns:
    - words (list): List of words read from the file.
    - num_words (int): Number of words.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.read().split()
        return words, len(words)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

def count_words(words):
    """
    Counts the frequency of each word in the given list.

    Parameters:
    - words (list): List of words.

    Returns:
    - word_count (dict): Dictionary containing word frequencies.
    """
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def main():
    """
    Main function to execute the word counting process.
    """
    if len(sys.argv) != 2:
        print("Usage: python word_count.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()

    try:
        words, _ = read_file(file_path)

        word_frequency = count_words(words)

        end_time = time.time()

        with open("WordCountResults.txt", 'w', encoding='utf-8') as result_file:
            for word, count in word_frequency.items():
                result_file.write(f"{word}: {count}\n")

            result_file.write(f"Time Elapsed: {end_time - start_time} seconds\n")

        print("Word count completed successfully. "
              "Results saved to WordCountResults.txt.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
