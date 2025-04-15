top_guests = ['Sokrates','Plato','Great Alexander']
print(f'Dear {top_guests[0]}!, you are invited for dinner at 19:00')
print(f'Dear {top_guests[1]}!, you are invited for dinner at 19:00')
print(f'Dear {top_guests[2]}!, you are invited for dinner at 19:00')
print(f"\nUnfortunately {top_guests[2]} has an urgent war to attend, therefore he won't be able to make it today.")

#replacing guest
top_guests[2] = 'Musk'
print(f'Dear {top_guests[0]}!, you are invited for dinner at 19:00')
print(f'Dear {top_guests[1]}!, you are invited for dinner at 19:00')
print(f'Dear {top_guests[2]}!, you are invited for dinner at 19:00')

#Adding 3 more quests

print('We found a bigger table, 3 more guests will be invited')

top_guests.insert(0, 'Poutin')
top_guests.insert(2,'Kim Yong')
top_guests.append('Kardasian')

print(f'\nDear {top_guests[0]}!, you are invited for dinner at 19:00')
print(f'Dear {top_guests[1]}!, you are invited for dinner at 19:00')
print(f'Dear {top_guests[2]}!, you are invited for dinner at 19:00')
print(f'Dear {top_guests[3]}!, you are invited for dinner at 19:00')
print(f'Dear {top_guests[4]}!, you are invited for dinner at 19:00')
print(f'Dear {top_guests[5]}!, you are invited for dinner at 19:00')

#Unfortunately we can only add 2 guests

print(f'\nDear {top_guests.pop()},you are uninvited')
print(f'Dear {top_guests.pop()},you are uninvited')
print(f'Dear {top_guests.pop()},you are uninvited')
print(f'Dear {top_guests.pop()},you are uninvited')

#Let the 2 remaining guests that they  are invited

print(f'\nDear {top_guests[0]} and {top_guests[1]} you are the lucky 2 guests!')

print(f'The number of guests is {len(top_guests)}')

top_guests.remove('Poutin')
top_guests.remove('Sokrates')
print(top_guests)


