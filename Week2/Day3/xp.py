# e1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print(dict(zip(keys,values)))

#2
family = {'rick': 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f'{name} has to pay: ${price}')
    total_cost += price

print(f'total cost: ${total_cost}')
#e3

brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': ['pink', 'green']
    }
}

brand['number_stores'] = 2

print('men, women, children')

brand['country_creation'] = 'Spain'

if 'international_competitors' in brand.keys():
    brand['international_competitors'].append('Desigual')

del brand['creation_date']

print(brand['international_competitors'][-1])

print('major clothes colors in the US:', brand['major_color']['US'])

print('key-value pairs amount:', len(brand))

print('keys:', list(brand.keys()))

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

brand.update(more_on_zara)

print(brand['number_stores'])

#e4
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

disney_users_A = {user: index for index, user in enumerate(users)}

disney_users_B = {index: user for index, user in enumerate(users)}

disney_users_C = {user: index for index, user in enumerate(sorted(users))}

print(disney_users_A)
print(disney_users_B)
print(disney_users_C)

disney_users_A_i = {user: index for index, user in enumerate(users) if "i" in user}

disney_users_A_mp = {user: index for index, user in enumerate(users) if user[0].lower() in ["m", "p"]}

print(disney_users_A_i)
print(disney_users_A_mp)

