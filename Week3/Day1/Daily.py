class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = dict()

    def add_animal(self,name : str ,count=2):
        self.animals[name] = count
    
    def get_animal_types(self):
        return sorted(list(self.animals.keys()))

    def get_short_info(self):
        animals_plural = []
        for animal in self.get_animal_types():
            if self.animals[animal] > 1:
                animals_plural.append(animal + 's')
            else:
                animals_plural.append(animal)
                
        animals_string = ', '.join(animals_plural[:-2]) + f', {animals_plural[-2]} and {animals_plural[-1]}'

        return f'McDonald\'s farm has {animals_string}.'
    
    def get_info(self):
        farm_name_string = f'{self.name}\'s farm'
        animal_list_string = ''
        for item in self.animals.items():
            animal_list_string = animal_list_string + f'{item[0]} : {item[1]}\n'
        eieio_string = '    E-I-E-I-0!'
        total_string = f'''{farm_name_string}


{animal_list_string}
{eieio_string}'''
        return total_string

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('lala',1)
macdonald.add_animal('lalda',2)
macdonald.add_animal('la3la',1)
macdonald.add_animal('lafla',1)
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())



    (1 , 'Greg' , 'Jones'),
    (2 , 'Sandra' , 'Jones'),
    (3 , 'Scott' , 'Scott'),
    (4 , 'Trevor' , 'Green'),
    (5 , 'Melanie' , 'Johnson')