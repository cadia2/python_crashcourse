pizza = ['margarita', 'special', 'peperoni']
for pizza_names in pizza:
    print(f'I like {pizza_names}')
print(f'I really like eating {pizza[0]}pizza' )
print(f'I really like eating {pizza[1]}pizza' )
print(f'I really like eating {pizza[2]}pizza' )
print('I really love pizza!')

#4-11
friend_pizza = pizza[:]
print(f'\n{friend_pizza}')
pizza.append('meat lovers')
friend_pizza.append('pineapple')

print(f'My favorite pizzas are: {pizza}')
for i in pizza:
    print(i)


print(f'My friends  favorite pizzas are: {friend_pizza}')
