from stats import num_words
from stats import book_string

def get_book_text(filepath):
    #takes a filepath as input and returns the contents of the file as a string.
  
    with open(filepath) as f:
        #open the file to read the contents
        file_contents = f.read()
    return file_contents



def main():
    book_contents = get_book_text("books/frankenstein.txt")
    print(book_contents)
    count_words_text = num_words(book_contents)
    print(f"{count_words_text} words found in the document")
    print(book_string)
    converted_to_strings = book_string(book_contents)
    print(converted_to_strings)
main()


