import itertools
from csv import DictReader
import json
from working_with_test_data.files import USERS_FILE, BOOKS_FILE

with open(USERS_FILE, 'r') as json_file, open(BOOKS_FILE, newline='') as csv_file:
    users = json.load(json_file)
    result = []
    for user in users:
        result.append(
            {
                'name': user['name'],
                'gender': user['gender'],
                'address': user['address'],
                'age': user['age'],
                'books': []
            }
        )
    iter_result = itertools.cycle(result)
    for book in DictReader(csv_file):
        person = next(iter_result)
        person['books'].append(
            {
                'title': book['Title'],
                'author': book['Author'],
                'pages': book['Pages'],
                'genre': book['Genre']
            }
        )

assert sum([len(res.get('books')) for res in result]) == 211  # 211 books in the file

with open('../files/result.json', 'w') as result_file:
    result_file.write(json.dumps(result, indent=4))
