from faker import Faker
import random
import json
from conf import MODEL


def generator(pk):
    fake = Faker()
    with open('books.txt', 'r') as file:
        lines = file.readlines()
        book = random.choice(lines)
    title = book
    year = random.randint(1900, 2022)
    pages = random.randint(100, 1000)
    isbn13 = (fake.numerify(text='%%%-%-%%%%-%%%%-%'))
    rating = random.uniform(0, 5)
    price = random.uniform(100, 1000)
    author = fake.name()
    dict_ = {
        "model": MODEL,
        "pk": 1,
        "fields": {
            "title": title,
            "year": year,
            "pages": pages,
            "isbn13": isbn13,
            "rating": rating,
            "price": price,
            "author": author
        }
    }
    pk += 1
    yield dict_


if __name__ == '__main__':
    books_list = []
    for pk in range(1, 101, 1):
        books = generator(pk)
        books_list.append(books)
    print(books_list)
with open("books.json", "w") as write_file:
    json.dump(books_list, write_file)
