from pathlib import Path

books = ['moby_dick.txt', 'romeo_and_juliete.txt']

count = 0

for book in books:
    path = Path(book)
    contents = path.read_text()
    count += contents.lower().count('the ')

print(count)
