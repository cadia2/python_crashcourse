sandwich_orders = ['ham ', 'mushroom', 'special', ' vegie']
finished_sandwiches = []

while sandwich_orders:
    prepared_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(prepared_sandwich)

    print(f'I made your {prepared_sandwich} sandwich')

else:
    print('\nThe sandwiches that are prepared are:')
    for sandwich in finished_sandwiches:
            print(f'\t{sandwich}')
