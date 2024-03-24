def main():
    #print (get_book_text())
    print (get_word_count())
    print (get_lettercount_dict())

def get_book_text():
    with open('books/frankenstein.txt') as text:
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
        if letter not in letter_count:
            letter_count[letter] = 0
        letter_count[letter] += 1
    return letter_count
    
if __name__ == '__main__':
    main()
  
