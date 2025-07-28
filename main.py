from stats import num_words
from stats import book_string
from stats import sort_chars

def get_book_text(filepath):
    #takes a filepath as input and returns the contents of the file as a string.
  
    with open(filepath) as f:
        #open the file to read the contents
        file_contents = f.read()
    return file_contents



def main():
    book_contents = get_book_text("books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    count_words_text = num_words(book_contents)
    print("----------- Word Count ----------")
    print(f"Found {count_words_text} total words")
    print("--------- Character Count -------")
    converted_to_strings = book_string(book_contents)
    sorted_chars = sort_chars(converted_to_strings)
    print(sorted_chars)
    


main()


