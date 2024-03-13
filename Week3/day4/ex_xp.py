# ex1
from random import randint
import os
# print(os.getcwd())
def get_words_from_file():
    f = open('c:/DI_Bootcamp/Week3/day4/sowpods.txt')
    lines = f.readlines()
    f.close()
    return [line.strip() for line in lines]

word_list = get_words_from_file()

def get_random_sentence(length : int):
    return ' '.join([word_list[randint(0,len(word_list))] for k in range(length)])

k=9
# print(get_random_sentence(k))

#ex2
import json
sampleJson = '''{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}'''
# j_file = open('c:/DI_Bootcamp/Week3/day4/jsone.json', 'w')
# with open(json_file, 'w') as file_obj:
# json.dump(sampleJson, j_file, indent = 2, sort_keys=True)
# j_file.close()
# print(sampleJson)
j_dict = json.loads(sampleJson)
print(j_dict['company']['employee']['payable']['salary'])
j_dict['company']['employee']['birth_date']='01-01-2000'
print(j_dict)