responses = []
#polling flag
polling_active = True

while polling_active:
    #prompt fav place
    response = input('''If you could visit one place in the world, where would  you go? ''')
    
    #Store the response in the list.
    responses.append(response)
   
   # Find out if anyone else will take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
       polling_active = False

#Polling is complete. Show the results
print("\n--- Poll results ---")
for response in responses:
    print(f'\t{response}')
