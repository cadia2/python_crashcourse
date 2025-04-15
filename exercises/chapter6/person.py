person =  {
    'first_name':'Melita',
    'last_name': 'Senikidi',
    'age': 14,
    'city': 'Loutda',
}

print(person)
print('\n')

#6-2 Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

fav_numbers = {
    'Melita': 3,
    'Irina': 7,
    'Gewrgia': 5,
    'Jason': 1,
    'Diwnh': 88,
}

for number in fav_numbers:
    print(f'{number}, your fav number is {fav_numbers[number]}')
