# נ Exercise 1: Cats
# Instructions
# Using this class

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: ג€The oldest cat is <cat_name>, and is <cat_age> years old.ג€. Use the function previously created.
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# 1
cat1 = Cat('cat1',1)
cat2 = Cat('cat2',2)
cat3 = Cat('cat3',3)
# 2
print(sorted([cat1,cat2,cat3],key=lambda x:x.age )[-1].name)
# 3
oldes_cat = sorted([cat1,cat2,cat3],key=lambda x:x.age )[-1]
print(f'The oldest cat is {oldes_cat.name}, and is {oldes_cat.age} years old.')

# נ Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string ג€<dog_name> goes woof!ג€.

# Create a method called jump that prints the following string ג€<dog_name> jumps <x> cm high!ג€. x is the height*2.

# Outside of the class, create an object called davids_dog. His dogג€™s name is ג€Rexג€ and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dogג€™s name is ג€Teacupג€ and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

class Dog:
    def __init__(self,name,height):
        self.name = name
        self.height = height

    def bark(self):
        print(f'{self.name} goes woof!')
    
    def jump(self):
        print(f'{self.name} jumps {self.height*2} cm high!')
    
davids_dog = Dog('Rex',50)
print(davids_dog.name)
print(davids_dog.height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog('LALA',20)
print(sarahs_dog.name)
print(sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height < sarahs_dog.height:
    print(sarahs_dog.name)
else:
    print(davids_dog.name)



# נ Exercise 3 : Whoג€™s The Song Producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:

# stairway= Song(["Thereג€™s a lady who's sure","all that glitters is gold", "and sheג€™s buying a stairway to heaven"])


# Then, call the sing_me_a_song method. The output should be:

# Thereג€™s a lady who's sure
# all that glitters is gold
# and sheג€™s buying a stairway to heaven


class Song:
    def __init__(self,lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
        
stairway= Song(["Thereג€™s a lady who's sure","all that glitters is gold", "and sheג€™s buying a stairway to heaven"])

stairway.sing_me_a_song()

# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isnג€™t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.


# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }


# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)

class Zoo:
    def __init__(self,zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals = self.animals + [new_animal]
            # print(self.animals)
    
    def get_animals(self):
        return self.animals
    
    def sell_animal(self, animal_sold):
        return self.animals != self.animals.remove(animal_sold)

    def create_group(self):
        self.animals_dict = {}
        sorted_animals=sorted(self.animals, key=lambda x:x.lower())
        j=1   
        first_letter = sorted_animals[0][0]
        current_animal_group=[sorted_animals[0]]
        for animal in sorted_animals[1:]:
            if animal[0] == first_letter:
                current_animal_group = current_animal_group + [animal]
                # print(f'i={i} j={j}  first_letter = {first_letter} current_animal_group = {current_animal_group}')
            else:
                self.animals_dict.update({j : current_animal_group})
                j=j+1
                first_letter = animal[0]
                current_animal_group=[animal]
                self.animals_dict.update({j : current_animal_group})
                
        return self.animals_dict

    def get_groups(self):
        return self.create_group()
		
ramat_gan_safari = Zoo('ZooZoo')
alist = ['kkk','jjj','iii','ahhh','ggg','fff','eee','ddd','ccc','aab','aaa']
for a in alist: 
    ramat_gan_safari.add_animal(a)

print(f'get_animals = {ramat_gan_safari.get_animals()}')
print(f'sortgrupss = {ramat_gan_safari.create_group()}')
print(f'sort_animals = {ramat_gan_safari.get_groups()}')
# print(f'sell_animal = {ramat_gan_safari.sell_animal('bbb')}')
print(f'get_animals = {ramat_gan_safari.get_animals()}')

print(f'get_groups = {ramat_gan_safari.get_groups()}')





da={}           
for animal in ramat_gan_safari.animals:
    firstletter=animal[0]
    da[firstletter]=[animal] daappend(animal)

print(f'da is {da}')