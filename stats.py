def num_words(count_words):
    split_words = count_words.split()
    word_count = 0
    for i in split_words:
        word_count += 1   
    return word_count

def book_string(book_contents):
    
    lower_case_chars = book_contents.lower()
    count_dict = {}
    for i in lower_case_chars:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1

    return count_dict

def sort_chars(char_count):
    unsorted_list = []
    for k, v in char_count.items():
        unsorted_list.append({"char":k,"num":v})

    unsorted_list.sort(key=lambda item: item["num"], reverse=True)
    return unsorted_list




    