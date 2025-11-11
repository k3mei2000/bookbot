import sys
from stats import get_word_count, get_character_count, get_sorted_character_counts

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path=sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = get_word_count(book_text)
    char_counts = get_character_count(book_text)
    sorted_char_counts = get_sorted_character_counts(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in sorted_char_counts:
        char = d["char"]
        if str.isalpha(char):
            print(f"{char}: {d["num"]}")
    print("============= END ===============")

main()