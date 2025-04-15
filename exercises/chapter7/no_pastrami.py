sandwich_orders = ['ham ', 'mushroom', 'special', ' vegie', 'pastrami',
                   'pastrami', 'pastrami']
finished_sandwiches = []

print('The deli has run out of pastrami\n')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    prepared_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(prepared_sandwich)

    print(f'I made your {prepared_sandwich} sandwich')

else:
    print('\nThe sandwiches that are prepared are:')
    for sandwich in finished_sandwiches:
            print(f'\t{sandwich}')
