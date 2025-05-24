from pathlib import Path

path = Path('learning_python_10_1.txt')
contents = path.read_text()

lines = contents.splitlines()

for line in range(len(lines)):
    lines[line] = lines[line].replace('Python', 'C')
    print(lines[line])


