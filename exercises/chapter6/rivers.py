#6-5 Rivers

rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Danube': 'Germany',
}

for river,country in rivers.items():
    print(f'The {river} runs through {country}.')

for river in rivers.keys():
    print(f'\nThe {river}') 

for country in rivers.values():
    print(f'\nThe {country}') 

#6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
poll_candidates = [
     'Melita',
    'Georgia',
     'Nodas',
     'edward',
     'phil',
 ]

for people in poll_candidates:
    if people in favorite_languages.keys():
        print(f'{people} thank you for taking the poll')
    else:
        print(f'{people} would you like to take the poll?')
