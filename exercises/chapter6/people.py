#6-7
person =  {
    'first_name':'Melita',
    'last_name': 'Senikidi',
    'age': 14,
    'city': 'Loutda',
}

person1 = {
    'first_name':'Jason',
    'last_name':'Andreopoulos',
    'age': 4,
    'hobby': 'kicking cat',
}

person2 = {
    'first_name': 'Irina',
    'last_name': 'Lugovskaya',
    'age' : 42,
    'hobby': 'farming',
}

people = [person, person1, person2]

for i in people:
    print(f'\n{i}')

#6-8 Pets
dict1 = {
    'animal': 'cat',
    'owners name': 'Yolo Bong',
}

dict2 = {
    'animal': 'Dog',
    'owners name': 'Van Dame',
}

dict3 = {
    'animal': 'bird',
    'owners name': 'Rocky Balboa',
}

pets = [dict1, dict2, dict3]
for pet in pets:
    print('\nHeres what I know:')
    for key, value in pet.items():
        print(f'\t{key}: {value}')

#6-9 Favorite places
favorite_places = {
    'Melita': ['Russia','Japan','London'],
    'Chris': ['Italy', 'Turkey', 'Crimea'],
    'Irina': ['Siberia','China', 'Austria'],
    }

for person,places in favorite_places.items():
    print(f"\n {person.title()}'s favorite places are:")
    for place in places:
        print(f'\t{place.title()}')

#6-10 Favorite Numbers

fav_numbers = {
    'Melita': [3,4,5],
    'Jason': [5,6,2,3], 
    'Diwnh': [33,22,56,66,77], 
}

for person,numbers in fav_numbers.items():
    print(f"\n{person.title()}'s favorite numbers are:")
    for number in numbers:
       print(f'\t{number}') 

#6-11 Cities
cities = {
    'Athens': {
        'country': 'Greece',
        'population': 3_000_000,
        'fact': """Athens is one of the oldest continuously inhabited cities in
        the world, with recorded history dating back over 3,400 years, and
        human presence going back at least 7,000 years. It’s often referred to
        as the cradle of Western civilization and the birthplace of
        democracy!"""
    },
    'Constantinople': {
        'country': 'Turkey',
        'population': 16_000_000,
        'fact':""" Constantinople was the largest and wealthiest city in Europe during much of the Middle Ages, thanks to its strategic position between Europe and Asia and its control over key trade routes like the Silk Road. """  
    },
    'Tokio': {
        'country': 'Japan',
        'population': 37_000_000,
        'fact':"""Tokyo is the most populous metropolitan area in the world when including the greater metro region, with over 37 million people!  """   },
}

for city,information in cities.items():
    print(f'\n{city.title()} has the following information:')
    for info,values in information.items():
      print(f'\t{info.title()}: {values}') 
       


