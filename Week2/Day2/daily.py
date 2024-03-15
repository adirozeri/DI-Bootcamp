number = int(input("Enter a number: "))
length = int(input("Enter a length: "))

multiples = [number * i for i in range(1, length + 1)]
print(multiples)

aa=['ppoeemm',"wiiiinnnnd","ttiiitllleeee","cccccaaarrrbbonnnnn"]


user_string = input("Enter a string: ")
new_string = ''
for s in user_string:
    if new_string == '' or new_string[-1] != s :
        new_string = new_string + s

print(new_string)
