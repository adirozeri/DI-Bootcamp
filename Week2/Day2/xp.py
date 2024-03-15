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

#8
toppings = []
price_per_topping = 2.5

while True:
    topping = input("Enter a pizza topping (type 'quit' to finish): ")
    if topping == 'quit':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

total_price = 10 + (len(toppings) * price_per_topping)
print(f"All toppings on the pizza: {', '.join(toppings)}")
print(f"The total price of the pizza is: ${total_price}")

#e9


family_members = int(input("How many people are in your family? "))
total_cost = 0

for a in range(0,family_members):
    age = int(input("Enter the age of the family member: "))
    if age < 3:
        continue
    elif age <= 12:
        total_cost += 10
    else:
        total_cost += 15

print(f"The total cost of all tickets is: ${total_cost}")

teenagers = ['a', 'b', 'c', 'd', 'e']
teenagers_c =teenagers.copy()
for teen in teenagers:
    age = int(input(f"Enter {teen}'s age: "))
    if not(16 <= age <= 21):
        teenagers_c.remove(teen)

print("Teens allowed to watch the movie:", teenagers_c)

# e10
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []

while sandwich_orders != []:
    finished_sandwiches.append(sandwich_orders.pop(0))  # Remove the first sandwich from the list

for sandwich in finished_sandwiches:
    print(f"I made your {sandwich.lower()}")