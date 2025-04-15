from random import choice

raffle_list = ["1","2","3","4","5","6","7","8","9","10","a","b","c","d","f"]
winning_list = []

while len(winning_list) < 4:
    raffle = choice(raffle_list)

    if raffle not in winning_list:
        winning_list.append(raffle)

print(f'The winning ticket is: {winning_list}')


