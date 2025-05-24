from pathlib import Path
import json

username = input("What is your name? ")
age = input("What is your age?")
location = input("What is your location?")

user_dict = {username: [age,location]}

path = Path('dict_user.json')
user_dict = json.dumps(user_dict)
path.write_text(user_dict)

contents = path.read_text()
user_info = json.loads(contents)

print(user_info)
