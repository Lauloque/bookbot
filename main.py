import sys

from print import chars_print, row_print
from stats import (
    chars_dict_to_sorted_list,
    count_words,
    get_chars_dict,
)


def get_book_text(filepath="") -> str:
    """Returns the text of a book"""
    with open(filepath) as f:
        return f.read()


def main():
    # book_path = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Please provide a book path")
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    chars_dict = get_chars_dict(book_text)
    sorted_chars_dict = chars_dict_to_sorted_list(chars_dict)

    row_print(text="BOOKBOT")
    print(f"Analyzing book found at {book_path}...")
    row_print(text="Word Count", sign="-")
    print(f"Found {num_words} total words")
    row_print(text="Character Count", sign="-")
    chars_print(items=sorted_chars_dict)
    row_print(text="END")


if __name__ == "__main__":
    main()
