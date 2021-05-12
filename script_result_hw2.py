import json
import csv
from json import loads

# Сохранение CSV файла с книгами в список из dict
with open('resources/books-39204-271043.csv') as books:
    book_list = []
    csv_reader = csv.DictReader(books)
    for row in csv_reader:
        book_list.append(
            {'title': row['Title'], 'author': row['Author'], 'height': row['Height']})

# Сохранение полученного списка из dict-ов в словарь json
with open('books_dictionary.json', 'w') as books_json:
    json.dump(book_list, books_json, sort_keys=True, indent=4)

# Форматируем json файл с пользаками в объекты Python
with open('resources/users-39204-8e2f95.json', "r") as users:
    u = users.read()
    user_dict = loads(u)

result_data = []

# Цикл, проходящий по парам счетчик-элемент.
for index, book in enumerate(book_list):
    try:
        user = user_dict[index]
        result_data.append(
            {'name': user["name"], 'gender': user["gender"], 'address': user['address'], 'books': book})
    except IndexError:
        book = []

with open('resources/result.json', 'w') as f:
    json.dump(result_data, f, indent=4)
