from collections import defaultdict
def get_num_words(book):
    split_book = book.split()
    return len(split_book)

def letter_count(book):
    dictionary_of_letters = defaultdict(int)
    for letters in book.lower():
        dictionary_of_letters[letters] +=1
    return dictionary_of_letters
def chars_dict_to_sorted_list(dictionArg):
    char_list = []
    for ch in dictionArg:
        char_list.append({"char": ch, "num": dictionArg[ch]})
    # newlist = sorted(dictionArg, key=lambda d: d['name'])
    char_list.sort(reverse=True,key = sort_on)
    return char_list

def sort_on(d):
    return d["num"]