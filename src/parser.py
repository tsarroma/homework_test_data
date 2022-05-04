import json
import csv

users_list = []
books_list = []

with open("../data/users.json", "r") as file:
    users = json.load(file)

    for user in users:
        filtered_user = dict(sorted(filter(lambda item: item[0] in ('gender', 'name', 'address', 'age'), user.items())))
        filtered_user['books'] = []
        users_list.append(filtered_user)

with open('../data/books.csv', newline='') as file:
    books = csv.DictReader(file)
    header = next(books)

    for book in books:
        filtered_book = dict(filter(lambda item: item[0] in ('Title', 'Author', 'Pages', 'Genre'), book.items()))
        filtered_book['title'] = filtered_book.pop('Title')
        filtered_book['author'] = filtered_book.pop('Author')
        filtered_book['pages'] = filtered_book.pop('Pages')
        filtered_book['genre'] = filtered_book.pop('Genre')
        books_list.append(filtered_book)

books_count = len(books_list)

data = users_list

i = 0

for i in range(books_count):
    for user in users_list:
        if books_list:
            user['books'].append(books_list.pop())


with open("../src/reference.json", "w") as file:
    result = json.dumps(data, indent=4)
    file.write(result)
