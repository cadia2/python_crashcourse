from pathlib import Path

path = Path('cats.txt')
path2 = Path('dogs.txt')
try:
    cats = path.read_text()
    dogs = path.read_text()

except FileNotFoundError:
    pass
else:
    print(cats)
    print(dogs)
