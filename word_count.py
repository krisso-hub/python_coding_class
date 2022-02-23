'''A program that count words from a file and dislay the number
   of occurence of each word
   author: Ndubuisi  Date: 02/14/2022
'''
# Analysis of words from a file
def main():
    text_file = open('./texts/cleantext.txt', 'r')
    text = text_file.read()
    text_file.close()
    print(f'The lenght of the string is {len(text)}')
    list_words = text.split(' ')
    print(f'1) The lenght of the "list_word" is {len(list_words)}')
    for word in list_words:
        if not (word.isalpha()):
            list_words.remove(word)
    print(f'2) The lenght of the "list_word" is {len(list_words)}')
    list_words.sort()
    ist_word = list_words[0]
    counter = 1
    for i in range(1, len(list_words), ):
        
        if (ist_word == list_words[i]):
            counter +=1
        else:
            print(f'Word {ist_word:15} occurs {counter:5} times')
            ist_word = list_words[i]
            counter = 1
    print(f'word {ist_word} occurs {counter} times')
    print('----end Program----')
main()