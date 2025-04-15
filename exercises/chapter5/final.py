#5-8
usernames = ['admin', 'linda', 'phil', 'daniel', 'doyle']

if usernames:
    for username in usernames:
        if username == 'admin':
            print('Hello admin')
        else:
            print(f'Hello {username}, thank you for logging in again.')
else:
    print('We dont have any users!')

#5-10
current_users = ['Melita', 'phil','daniel', 'linda', 'george']
new_users = ['melita', 'george', 'nick', 'denise', 'Irina']

current_users = [user.lower() for user in current_users]

print('\n')

for user in new_users:
    if user.lower() in current_users:
            print(f'{user} You will have to enter a new username')
    else:
            print(f'{user} Username is available')

print('\n')

#5-11 ordinal
ord_numbers = list(range(1,10))

for number in ord_numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd' )
    else:
        print(f'{number}th')
