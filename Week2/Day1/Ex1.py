import os
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco            laboris nisi ut aliquip ex ea commodo consequat.            Duis aute irure dolor in reprehenderit in voluptate velit            esse cillum dolore eu fugiat nulla pariatur.            Excepteur sint occaecat cupidatat non proident,            sunt in culpa qui officia deserunt mollit anim id est laborum."
text=my_text.split()
total_length=0
for a in text:
    total_length += len(a)
print('total length is: ',total_length)
print('wrong total length(with spaces) is: ',len(my_text))

input('enter to coninue!')
os.system('cls')
my_text =''
longest = 0
while my_text != 'exit':
    if longest < len(my_text):
        longest = len(my_text)
        print('congratulations! - new hight score')
    my_text = input('input the longest sentence they can without the character “A”: ')
