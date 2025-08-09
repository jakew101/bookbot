import sys
from stats import word_count, char_count, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    text = get_book_text(path)
    print(f"Analyzing book found at {path}...")
    num_words = word_count(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_chars = char_count(text)
    sort_chars = sort_dict(num_chars)
    for char in sort_chars:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")
main()