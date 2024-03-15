# e1
def display_message():
    print('I am learning Python programming in this course.')

display_message()
# e2
def favorite_book(title):
    print(f'One of my favorite books is {title}.')

favorite_book('Alice in Wonderland')
# e3
def describe_city(city, country):
    print(f'{city} is in {country}.')

describe_city('Madrid', 'Spain')
# e4
import random

def compare_numbers(user_number):
    random_number = random.randint(1, 100)
    if user_number == random_number:
        print('Success')
    else:
        print(f'Fail. Your number {user_number}  random number  {random_number}')

user_number = int(input('number between 1 and 100:'))
compare_numbers(user_number)

# e5
def make_shirt(size='large', text='I love Python'):
    print(f' shirt size s {size}  text  {text}')

make_shirt()
make_shirt(size='medium')
make_shirt(size='small', text='lalalalal')

# e6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    return [magician + ' the Great' for magician in magicians]

magician_names = make_great(magician_names)
show_magicians(magician_names)

# e7
import random

def get_random_temp(season):
    if season == 'winter':
        return random.uniform(-10, 16)
    elif season == 'spring':
        return random.uniform(10, 25)
    elif season == 'summer':
        return random.uniform(20, 40)
    elif season == 'autumn':
        return random.uniform(10, 20)

def main():
    season = input('Enter the season: ')
    temp = get_random_temp(season)
    print(f'temperature  is {temp}')

main()

# e8
qs = [
    {'question': 'What is Baby Yoda\'s real name?', 'answer': 'Grogu'},
    {'question': 'Where did Obi-Wan take Luke after his birth?', 'answer': 'Tatooine'},
    # Add the rest of your questions here
]

def star_wars_quiz(qs):
    correct_answers = 0
    wrong_answers = []
    
    for item in qs:
        user_answer = input(item['question'] + ' ')
        if user_answer.lower() == item['answer'].lower():
            correct_answers += 1
        else:
            wrong_answers.append((item['question'], user_answer, item['answer']))
            
    print(f'correct_answers: {correct_answers},wrong answers: {len(wrong_answers)}')
    
    if len(wrong_answers) > 0:
        for question, user_answer, correct_answer in wrong_answers:
            print(f'Question: {question}')
            print(f'Your answer: {user_answer}')
            print(f'Correct answer: {correct_answer}')
    
    if len(wrong_answers) > 3:
        print('more than 3 wrong answers try again')
        star_wars_quiz(qs)

star_wars_quiz(qs)
