my_fav_numbers = set([1,2,3,4,4])
my_fav_numbers.add(5)
my_fav_numbers.add(6)
my_fav_numbers.remove(6)
friend_fav_numbers  = set([7,8,9,9])
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("My favorite numbers:", my_fav_numbers)
print("My friend's favorite numbers:", friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)


#e2
# no. the touple is set to be 2 values. cannot change it . immutable

#e3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apples_count = basket.count("Apples")
print("Number of Apples in the basket:", apples_count)
basket.clear()
print(basket)

#e4
print('a float is a Real number.')
my_list = [x/2 for x in range(3,11)]
print(my_list)
#another what
k=1.5
new_way=[]
for i in range(0,8):
    new_way.append(k)
    k = k+ 0.5
print(new_way)

#5
for a in range(1,21):
    print(a)

for a in range(1,21):
    if a%2 == 0: print(a)

#6
name = ''
while name != 'adir':
    name = input('what is you name: ')

#7
favorite_fruits_input = input("Enter your favorite fruit(s), separated by a single space: ")
favorite_fruits = favorite_fruits_input.split()

user_fruit = input("Enter the name of any fruit: ")

if user_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")
