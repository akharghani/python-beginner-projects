# Text Stats Analyzer

A beginner Python program from an intro course (Fall 2025). It takes a sentence and prints some basic stats about it.

It practises string handling, loops, lists, sets, dictionaries, and tuples, and each step is its own small function.

## What it does

1. Lowercases the text
2. Removes commas and periods
3. Splits the text into words
4. Prints:
   - the number of unique words
   - the longest word
   - the most common word and how many times it appears
   - how often each letter a–z appears

## How to run

```
python text_stats.py
```

To try your own text, change the `text = "..."` line at the top of the file.

## Example output

```
INPUT_TEXT: Cats and dogs are fun, but cats are definitely funnier than dogs.
UNIQUE_WORDS: 9
LONGEST_WORD: definitely
MOST_COMMON_WORD: cats
MOST_COMMON_WORD_COUNT: 2
LETTER_FREQUENCIES:
a: 6
b: 1
...
```

## Known limitations

- Only commas and periods are removed, so other punctuation like `!` or `?` stays attached to words.
- If several words tie for most common, only the first one found is shown.
