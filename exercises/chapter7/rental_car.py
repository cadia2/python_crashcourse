#7-1
car =  input('What kind of car would you like? ')
print(f'Let me see if I can find you a {car}')

#7-2
people =int(input('How many people are in your dinner group? '))
if people > 8:
    print('''Sorry but all the big tables are full, we are asking for your
          parience''')
else:
    print('Your table is ready!')

#7-3
number =int(input('Give me a number: '))
if number % 10 == 0:
    print(f'{number} is a multiple of 10')
else:
    print(f'{number} is not a multiple of 10')

