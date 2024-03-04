import random
import os

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 

### YOUR CODE STARTS FROM HERE ###

head =' O'
body = ' |'
left_arm = '/|'
right_arm = '/|\\'
left_leg = '/'
right_leg = '/ \\'
hangman = [head ,body ,left_arm,right_arm ,left_leg ,right_leg ]





def hangmanState(hangman_progress):
    if (hangman_progress == 0):
        os.system('cls')
        print('  __'    )
        print(' |  |'   )
        print(' |  '   )
        print(' | ' )
        print(' | ' )
        print('_|_'     )
    if (hangman_progress == 1):
        os.system('cls')
        print('  __'    )
        print(' |  |'   )
        print(' |  O'   )
        print(' | ' )
        print(' | ' )
        print('_|_'     )
    if (hangman_progress == 2):
        os.system('cls')
        print('  __'    )
        print(' |  |'   )
        print(' |  O'   )
        print(' |  |' )
        print(' | ' )
        print('_|_'     )
    if (hangman_progress == 3):
        os.system('cls')
        print('  __'    )
        print(' |  |'   )
        print(' |  O'   )
        print(' | /|' )
        print(' | ' )
        print('_|_'     )
    if (hangman_progress == 4):
        os.system('cls')
        print('  __'    )
        print(' |  |'   )
        print(' |  O'   )
        print(' | /|\\' )
        print(' | ' )
        print('_|_'     )
    if (hangman_progress == 5):
        os.system('cls')
        print('  __'    )
        print(' |  |'   )
        print(' |  O'   )
        print(' | /|\\' )
        print(' | /' )
        print('_|_'     )
    if (hangman_progress == 6):
        os.system('cls')
        print('  __'    )
        print(' |  |'   )
        print(' |  O'   )
        print(' | /|\\' )
        print(' | / \\' )
        print('_|_'     )

# hangmanState(3)
# word = 's'

i=0
word_mask='*'*len(word)
letter_guess = ''
letters_used = set()

hangmanState(0)
print('Word to gurss: {}'.format(word_mask))
while i<6 and word != word_mask:
    if len(letters_used) == 0:
        print('used letters: {}')
    else: 
        print('used letters: {}'.format(letters_used))

    letter_guess = input('guess a letter: ')
    if letter_guess in letters_used: 
        hangmanState(i)
        print('\'{}\' has been guessed before.'.format(letter_guess))
    elif (letter_guess not in 'abcdefghijklmnopqrstuvwxyz') or letter_guess == '' :
        hangmanState(i)
        print('\'{}\' is an illeagle letter'.format(letter_guess))
    else:#if not guessed before
        letters_used.add(letter_guess)
        if letter_guess in word:
            hangmanState(i)
            print('\'{}\' is IN the word!!'.format(letter_guess))
            word_mask = ''.join(['*' if letter not in letters_used else letter for letter in word])
        else:
            i += 1
            hangmanState(i)
            print('\'{}\' is not in the word - try again.'.format(letter_guess))
            
    
    print('Word to gurss: {}'.format(word_mask))
os.system('cls')
hangmanState(i)
print('used letters: {}'.format(letters_used))
if i==6 :
    print(f'game finish.NO LUCK. actual word is \'{word}\' you guesed word is: {word_mask}')
else: print(f'WINNNNNNN!!!!!!!!!!!!!!!!!!!!!!!!!!!!.\n word is \'{word}\'')




