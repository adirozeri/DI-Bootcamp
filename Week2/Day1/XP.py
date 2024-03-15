for i in range(0,5):
    print('Hello World!')

#2
print(99*99*99*8)

#3
# >>> 5 < 3 False
# >>> 3 == 3 True
# >>> 3 == "3" False
# >>> "3" > 3 exception cannot compare str to int
# >>> "Hello" == "hello" False

#4
computer_brand = 'hp'
print(f'I have a {computer_brand} computer')

#5
name = 'adir ozeri'
age = 38
shoe_size = 42
info = f'hi my name is {name} i am {age} years old and my shoe size is {shoe_size}'
print(info)

#6
a=1
b=2
if a > b: print('Hello world')
#7

var = int(input('enter an int number to determin if odd or even'))
if var % 2 == 0:
    print('even')
else:
    print('odd')

#8
youname = str(input('please enter your name'))
if youname == 'adir':
    print('a funny message based on the outcome. ')
else:
    print('we do not have the same name')

#9
    
height = int(input('please privide you height in cm: '))
if height > 145:
    print('you are tall enough to ride')
else:
    print('not tall enough')