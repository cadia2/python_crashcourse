from pathlib import Path
import json

path = Path('number.json')
if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}")

else:
    number = json.dumps(input('What is your favorite number?'))
    path.write_text(number)

