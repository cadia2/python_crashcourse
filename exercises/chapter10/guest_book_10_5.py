from pathlib import Path

guest_messages = ""
prompt =  "\nHi, what's your name? "
prompt += "\nEnter 'q' if you're the last guest. "

while True:
    message = input(prompt)

    if message == 'q':
        break

    guest_messages +=f'{message}\n'

path = Path('guest_book.txt')
path.write_text(guest_messages)






