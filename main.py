import sys
from stats import num_returned , count_characters ,report_characters
def get_book_text(filepath):
    with open(filepath) as f:
         file = f.read()
         return file
    



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    # print(text)
    number_of_words = num_returned(text)
    
    count = count_characters(text)
    sorted_list =report_characters(count)
    print(f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {number_of_words} total words
--------- Character Count -------
    """)
    for item in sorted_list :
        if item["char"].isalpha() :
            print(f"{item["char"]}: {item["num"]}")
main()