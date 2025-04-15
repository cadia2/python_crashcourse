prompt = '\nHello, what toppings would you like for your pizza?'
prompt += '\n(1. Enter "my pizza" to check your toppings)' 
prompt += '\n(2. Enter "quit" when you are finished) ' 

my_pizza = []

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    elif topping == 'my pizza':
        if not  my_pizza:
            print('Add some toppings first!')
        else:
             print('\nYour pizza consists of:')
             for t in my_pizza:
                 print(f'\t{t}')
    else:
        if topping in my_pizza:
            print(f'You already added {topping}!')
        else:
            my_pizza.append(topping)
            print(f'\nI will add {topping} to your pizza.')
