def num_words(count_words):
    split_words = count_words.split()
    word_count = 0
    for i in split_words:
        word_count += 1   
    return word_count

def book_string(book_contents):
    print("Import file working")
    lower_case_chars = book_contents.lower()
    count_dict = {}
    for i in lower_case_chars:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1

    return count_dict


    