from stats import count_words, count_characters, make_report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    try:
        book = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        print("----------- Word Count ----------")
        count = count_words(get_book_text(book))
        print(f"Found {count} total words")
        print("--------- Character Count -------")
        #chars = count_characters(get_book_text("books/frankenstein.txt"))
        #print(chars)
        report = make_report(count_characters(get_book_text(book)))
        for dici in report:
            letter = dici.get("char")
            amount = dici.get("num")
            if letter.isalpha():
                print(f"{letter}: {amount}")
        print("============= END ===============")
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()