prompt1 ="Hello enter the first number\n"
prompt1 += '(Press q to quit the program) '

prompt2 = 'Enter the second number\n'
prompt2 += '(Press q to quit the program) '

while True:
    input1 = input(prompt1)
    if input1 == 'q':
        break
    try:
        number1 = int(input1)
    except ValueError:
        print('Sorry, you must provide a valid integer number. \n')
        continue

    input2 = input(prompt2)
    if input2 == 'q':
        break
    try:
        number2 = int(input2)
    except ValueError:
        print('Sorry, you must provide a valid integer number. \n')
        continue

    result = number1 + number2
    print(f'The addition result is: {result}')
    break



