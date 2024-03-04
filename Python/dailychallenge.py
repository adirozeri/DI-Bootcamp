#user_input = input('please provide a 10 charcter string: ')
#if type(user_input) != type('word'): print('this is not a string bye bye')
user_input = '123'
if len(user_input) < 10:
        print('string not long enough')
elif len(user_input) > 10:
        print('string too long')
else: print('perfect string')

print ('first letter: ',user_input[0])
print ('last: ',user_input[-1])
for letter in user_input[::-1] :
    print(letter)


                

