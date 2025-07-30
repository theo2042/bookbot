from stats import num_words
from stats import book_string
from stats import sort_chars
import sys



def get_book_text(filepath):
    #takes a filepath as input and returns the contents of the file as a string.
  
    with open(filepath) as f:
        #open the file to read the contents
        file_contents = f.read()
    return file_contents



def main():

    
    if len(sys.argv) != 2:       
           
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    else:
        book_location = sys.argv[1]       
        book_contents = get_book_text(sys.argv[1])
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        count_words_text = num_words(book_contents)
        print("----------- Word Count ----------")
        print(f"Found {count_words_text} total words")
        print("--------- Character Count -------")
        converted_to_strings = book_string(book_contents)
    
        sorted_chars = sort_chars(converted_to_strings)
        sorted_alpha = []
        for item in sorted_chars:
            if item["char"].isalpha():
                print(f"{item['char']}: {item['num']}")
        print("============= END ===============")


main()


