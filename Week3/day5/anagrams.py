from anagram_checker import AnagramChecker
a=True
while a:
    try:
        is_continue = int(input('select 0 to enter a word or any number to exit'))
        a=False
    except:
        print('enter only 0 or 1')

while is_continue == 0:
    word = input('please enter a word: ').strip()
    if word.isalpha():
        is_continue = 1
        check = AnagramChecker()
        print(f'YOUR WORD :"{word.upper()}"')
        if check.is_valid_word(word)

this is a valid English word.
# Anagrams for your word: ''',end='')
        anagrams = check.get_anagrams(word)
        anagrams.remove(word.upper())
        for k ,anagram in enumerate(anagrams):
            if k < len(anagrams)-1:
                print(anagram, end =', ')
            else:
                print(anagram,end='.\n')
    else:
        is_continue = int(input('entered wrong word (multiple words or nun numeric). select 0 to enter a word or any number to exit'))
    
        

