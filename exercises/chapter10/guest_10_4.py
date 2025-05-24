from pathlib import Path

guest = Path('guest.txt')
name = input('What is your name?')
guest.write_text(name)

