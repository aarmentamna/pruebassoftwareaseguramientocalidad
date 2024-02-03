import time
import sys

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
        return words, len(words)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

def count_words(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()

    try:
        words, num_words = read_file(file_path)

        word_frequency = count_words(words)

        end_time = time.time()

        with open("WordCountResults.txt", 'w') as result_file:
            for word, count in word_frequency.items():
                result_file.write(f"{word}: {count}\n")

            result_file.write(f"Time Elapsed: {end_time - start_time} seconds\n")

        print("Word count completed successfully. Results saved to WordCountResults.txt.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
