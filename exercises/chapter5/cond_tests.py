#5-3 Alien colors

alien_color = 'yellow'
if 'green' in alien_color:
    print('You just earned 5 points!')

alien_color = 'yellow'
if 'yellow' in alien_color:
    print('You just earned 5 points!')

#5-4 

if alien_color == 'green':
    print('you just won 5 points')
else:
    print('You just won 10 points')

#5-5

if alien_color == 'green':
    print('you just won 5 points')
elif alien_color == 'yellow':
    print('You just won 10 points')
else:
    print('You just won 15 points')

#5-6

persons_age = 27

if persons_age < 2:
    print('/nThe person is a baby')

if persons_age >=2 and persons_age <4:
    print('/nThe person is a toddler')

if persons_age < 2:
    print('/nThe person is a baby')

if persons_age >=4 and persons_age <13:
    print('/nThat person is a kid')

if persons_age >=13 and persons_age <20:
    print('/nThat person is a teengager')

if persons_age >=20 and persons_age <65:
    print('\nThat person is a adult')
else:
    print('that person is an elder')

#5-7

favorite_fruits = ['apple', 'banana', 'pears']
