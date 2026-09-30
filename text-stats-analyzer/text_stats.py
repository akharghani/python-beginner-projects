"""Text Stats Analyzer: counts words and letters in a piece of text."""

text = "Cats and dogs are fun, but cats are definitely funnier than dogs."

def main():
    """Main function that calls all the processing steps."""

    print("INPUT_TEXT:", text)

    lowered = lower_text()
    no_punct = remove_punctuation(lowered)
    all_words = list_words(no_punct)
    get_unique_word_count(all_words)
    get_longest_word(all_words)
    get_most_common_word(all_words)
    get_letter_frequencies(lowered)

# Turns the text to lowercase.

def lower_text():
    """Converts the text to all lowercase and saves it as new_text."""

    new_text = text.lower()
    return new_text

# Gets rid of the punctuation.

def remove_punctuation(new_text):
    """Removes commas and periods from the text."""

    clean_text = ""
    for i in range(len(new_text)):
        if new_text[i] == "," or new_text[i] == ".":
            clean_text += " "
        else:
            clean_text += new_text[i]
    return clean_text

# Turns the text to words.

def list_words(clean_text):
    """Splits the punctuation-free, lowercased text into a list of words."""

    words = clean_text.split()
    return words

# Finds all the unique words.

def get_unique_word_count(words):
    """Returns the number of unique words in the list."""

    unique_words = set(words)
    print("UNIQUE_WORDS:", len(unique_words))
    return len(unique_words)

# Finds the longest word.

def get_longest_word(words):
    """Returns the longest word from the list."""

    longest = ""
    for i in words:
        if len(i) > len(longest):
            longest = i
    print("LONGEST_WORD:", longest)
    return longest

# Counts the word frequencies and finds the word with the highest count.

def get_most_common_word(words):
    """Finds and prints the most common word and its
      count using a dictionary and tuple."""

    word_counts = {}

    for i in words:
        if i in word_counts:
            word_counts[i] += 1
        else:
            word_counts[i] = 1

    most_common = ""
    highest_count = 0
    for word, count in word_counts.items():
        if count > highest_count:
            highest_count = count
            most_common = word

    result = (most_common, highest_count)

    print("MOST_COMMON_WORD:", result[0])
    print("MOST_COMMON_WORD_COUNT:", result[1])

    return result


def get_letter_frequencies(text):
    """Counts how often each letter (a-z) appears
      in the text using a dictionary."""

    all_letters = "abcdefghijklmnopqrstuvwxyz"
    letter_counts = {}
    for letter in all_letters:
        letter_counts[letter] = 0

    for char in text.lower():
        if char in all_letters:
            letter_counts[char] += 1

    print("LETTER_FREQUENCIES:")
    for letter in all_letters:
        print(f"{letter}: {letter_counts[letter]}")

    return letter_counts

# Runs the main function when the script is executed directly.
if __name__ == "__main__":
    main()
