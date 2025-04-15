from random import choice

raffle_list = ["1","2","3","4","5","6","7","8","9","10","a","b","c","d","f"]
winning_list = []
counter = 0
my_raffle = []

    
while len(winning_list) < 4:
    raffle = choice(raffle_list)

    if raffle not in winning_list:
        winning_list.append(raffle)

print(f'The winning_list is {winning_list}')

while my_raffle != winning_list:
    my_raffle = []

    while len(my_raffle) < 4:

        raffle = choice(raffle_list)

        if raffle not in my_raffle:
            my_raffle.append(raffle)

        if winning_list != my_raffle and len(my_raffle) == 4:
            counter += 1
        elif winning_list == my_raffle:
            print(f'You won and it took you {counter} times.')


