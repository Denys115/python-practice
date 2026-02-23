import sys
from stats import get_num_words , get_chars_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import get_num_words, get_chars_dict, sort_chars # Adaugă noua funcție aici

def main():
    path = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars_list = sort_chars(chars_dict) # Sortăm datele
    
    # Începem să printăm exact ca în cerință
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars_list:
        # Verificăm dacă e literă (să nu printăm cifre sau spații)
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
