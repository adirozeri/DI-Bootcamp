class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Create another cat breed named Siamese which inherits from the Cat class.
class Siamese(Cat):
    pass
        
def main():

# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
    all_cats = [Bengal('ben',1),Chartreux('charly',2),Siamese('sia',3)]
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, 
#and pass the variable all_cats to the new instance.
    sara_pets = Pets(all_cats)
# Take all the cats for a walk, use the walk method.
    sara_pets.walk()



# #e2
# Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. ---
# This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return self.weight/self.age*10
    
    def power(self):
        return self.run_speed() * self.weight
    
    def fight(self,other_dog):
        if other_dog.power() > self.power():
            return f'{other_dog.name} is the winner'
        return f'{self.name} is the winner'

# a = Dog('a',1,111)
# b = Dog('b',2,222)
# c = Dog('c',3,333)
# print(a.power())
# print(b.power())
# print(c.power())
# print(a.fight(b))
# print(b.fight(a))
# print(a.fight(c))
# print(c.fight(a))
# print(b.fight(c))
# print(c.fight(b))
# print(a.fight(a))






