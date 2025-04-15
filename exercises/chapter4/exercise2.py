for i in range(1, 11):
    print(i)


million = list(range(1, 1_000_001))
print(million)
print(min(million))
print(max(million))
print(sum(million))

odd_numbers = list(range(1, 21 , 2))
for numbers in odd_numbers:
    print(numbers)
print('\n')

#4-7 Threes
multhree_numbers = list(range(3, 31, 3))
for threes in multhree_numbers:
    print(threes)
print('\n')

#4-8 Cubes
cube_list = []
for i in range(1, 11):
    cube_list.append(i**3)
print(cube_list)
print('\n')

#4-9 list comprehesion
cubes = [ value ** 3 for value in range(1, 11) ]
print(cubes)

#4-10
print(f'the fiest three items in the list are:{cubes[0:3]}')
