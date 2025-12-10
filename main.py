import os
import sys
from stats import get_num_words
from stats import letter_count
from stats import sort_on
from stats import chars_dict_to_sorted_list
dirname = os.path.dirname(__file__)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



def main():
    #Had to use absolute pathing, TODO: figure out relative pathing so I can redo this project elsewhere
    print("Usage: python3 main.py <path_to_book>")
    if len(sys.argv)!=2:
        sys.exit(1)
    relative_path = sys.argv[1]
    print(f"check the path {relative_path}")
    weGotBook = get_book_text(relative_path)
    # print(weGotBook)
    num_words = get_num_words(weGotBook)
    print(f"Found {num_words} total words")
    dynamic_counting = letter_count(weGotBook)
    # print(dynamic_counting)

    sorted_Thang = chars_dict_to_sorted_list(dynamic_counting)
    print(f"""============ BOOKBOT ============
Analyzing book found at {relative_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for letter_pair in sorted_Thang:
        ch = letter_pair["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {letter_pair['num']}")

    print("============= END ===============")
main()