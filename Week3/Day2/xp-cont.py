from random import randint
# Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
from xp import Dog
# In the new python file, create a class named PetDog that inherits from Dog.
class PetDog(Dog):
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
    def __init__(self, name, age, weight):
        self.trained = False
        super().__init__(name, age, weight)
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True
    def train(self):
        print(self.bark())
        self.trained = True

# play: takes a parameter which value is a few names of other Dog instances (use *args).
# The method should print the following string: “dog_names all play together”.
    def play(self, *dog_names):
        print(f'{' '.join(dog_names)} all play together')

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.
    def do_a_trick(self):
        if not self.trained:
            return
        options = [f'{self.name} does a barrel roll',f'{self.name} stands on his back legs',f'{self.name} shakes your hand',f'{self.name} plays dead']
        return print(options[randint(0,3)])

def main():
    a = PetDog('a',1,'12')
    a.train()
    a.do_a_trick()

# main()
    
#     Exercise 4 : Family
# Instructions
# Create a class called Family and implement the following attributes:
class Family:
# members: list of dictionaries
# last_name : (string)
    def __init__(self, last_name, members = []):
        self.last_name = last_name
        self.members = members
# Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
    def born(self, **kargs):
        self.members.append(kargs)
        print('congrats')

# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
    def is_18(self, name):
        for person_dict in self.members:
            if person_dict['name'] == name:
                return person_dict['age'] > 18
        return False
# family_presentation: a method that prints the family’s last name and all the members’ details.
    def  family_presentation(self):
        print(f'familt last name is : {self.last_name}')
        for family_member_dict in self.members:
            for key, value in family_member_dict.items():
                print(f'{key} is {value}',end=', ')
            print('\n')
            # print(f'{family_member_dict['name']} age is {family_member_dict['age']}')
# Create an instance of the Family class, with the last name of your choice, and the below members. Then call all the methods you created in Point 2.
def main():
    
    members=[
        {'name':'Michael','age':35,'gender':'Male','is_child':False},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False}
    ]

    fam = Family('Cohen', members)
    # print(fam.members)
    fam.family_presentation()
# main()


# Exercise 5 : TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore the members attributes, 
# will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)
class InvalidAgeException(Exception):
    def __init__(self):
        self.message = 'not 18 yet'
        super().__init__(self.message)


class TheIncredibles(Family):
    
# Add a method called use_power, this method should print the power of a member only if they are over 18 years old. 
# If not raise an exception (look up exceptions) which stated they are not over 18 years old.



    def use_power(self, member_name):
        if super().is_18(member_name):
            for member in self.members:
                if member['name'] == member_name:
                    print(member['power'])
        else:
            raise InvalidAgeException()

# Add a method called incredible_presentation which :

# Print a sentence like “*Here is our powerful family **”
# Prints the family’s last name and all the members’ details (ie. use the super() function, to call the family_presentation method)
    def incredible_presentation(self):
        print('here is out pwerful family')
        self.family_presentation()

# Create an instance of the Incredibles class, with the “Incredibles” last name, and the below members.
def main():
    members = [
        {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
    ]

    inc = TheIncredibles('Hulk',members)
    
# Call the incredible_presentation method.

    inc.incredible_presentation()

# Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.

    inc.born(name = 'Baby', age = '0', gender = 'Male', is_child = False, power = 'Unknown Power',incredible_name = 'Baby Jack')

# Call the incredible_presentation method again.
    inc.incredible_presentation()

main()