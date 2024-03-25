def main():
    #print (get_book_text())
    #print (get_word_count())
    #print (get_lettercount_dict())
    sorted_chars = seperate_into_list(get_lettercount_dict())
    sort(sorted_chars)
    get_readable(sorted_chars)

def get_input():
    return 'books/frankenstein.txt'

def get_book_text():
    with open(get_input()) as text:
        file_contents = text.read()
        #print (file_contents)
        return (file_contents)
    
def get_word_count():
    text = get_book_text()
    if type(text) == str:
        words = text.split()
        word_count = len(words)
        return word_count
    
def get_lettercount_dict():
    text = get_book_text()
    lowered_text = text.lower()
    letter_count = {}
    for letter in lowered_text:
        if letter.isalpha():
            if letter not in letter_count:
                letter_count[letter] = 0
            letter_count[letter] += 1
    return letter_count

def seperate_into_list(og_dict):
    char_list = []
    for char, freq in og_dict.items():
        char_list.append({"char":char, "freq":freq})
    return(char_list)

def get_freq(dict):
    return dict["freq"]

def sort(item):
    item.sort(key=get_freq, reverse=True)
    return item

def get_readable(meepmorp):
    print (f"--- Begin report of {get_input()} ---")
    print (f"{get_word_count()} words found in the document\n")
    for item in meepmorp:
        print (f"The '{item['char']}' character was found '{item['freq']}' times")
    print ("--- End report ---")


if __name__ == '__main__':
    main()

