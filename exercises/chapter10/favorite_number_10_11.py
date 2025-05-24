from pathlib import Path
import json

path = Path('number.json')
number = json.dumps(input('What is your favorite number?'))
path.write_text(number)
