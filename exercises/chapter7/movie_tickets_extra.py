#7-5
prompt = '\nWhat is your age? '
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age =input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print(f'You are {age} years old, you have a free ticket!')
    elif age < 13: 
        print(f'You are {age} years old, your ticket costs 10$!')
    else: 
        print(f'You are {age} years old, your ticket costs 15$!')


#2nd way
prompt = '\nWhat is your age? '
prompt += "\nEnter 'quit' when you are finished. "

active = True
while active:
    age =input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)

        if age < 3:
            print(f'You are {age} years old, you have a free ticket!')
        elif age < 13: 
            print(f'You are {age} years old, your ticket costs 10$!')
        else: 
            print(f'You are {age} years old, your ticket costs 15$!')

#3d way
prompt = '\nWhat is your age? '
prompt += "\nEnter 'quit' when you are finished. "

age = ''
while age != 'quit':
    age =input(prompt)
    if age == 'quit':
        print('End of program')
    else:    
        age = int(age)

        if age < 3:
            print(f'You are {age} years old, you have a free ticket!')
        elif age < 13: 
            print(f'You are {age} years old, your ticket costs 10$!')
        else: 
            print(f'You are {age} years old, your ticket costs 15$!')
