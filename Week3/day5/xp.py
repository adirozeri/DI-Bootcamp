from anagram_checker import AnagramChecker

def user_selection():
    a=True
    while a:
        try:
            is_continue = int(input('select 0 to enter a word or any number to exit'))
            a=False
        except:
            print('enter only 0 or 1')
    return is_continue




while user_selection() == 0:
    word = input('please enter a word: ').strip()
    if word.isalpha(): #no numbers and symbols imcliding space so this is a single word
        check = AnagramChecker()
        print(f'YOUR WORD :"{word.upper()}"')
        if check.is_valid_word(word):
            print(f'this is a valid English word.\nAnagrams for your word: ',end='')
            anagrams = check.get_anagrams(word)
            anagrams.remove(word.upper())
            if anagrams:
                for k ,anagram in enumerate(anagrams):
                    if k < len(anagrams)-1:
                        print(anagram, end =', ')
                    else:
                        print(anagram,end='.\n')
            else:
                print('sorry no anagrams')
    else:
        is_continue = print('entered wrong word (multiple words or nun numeric)')

print('bye bye')
                

