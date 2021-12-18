from faker import Faker
import random
import json
from conf import MODEL


def book_name():
    with open('books.txt', 'r') as file:
        lines = file.readlines()
        book = random.choice(lines)



def year():
    random.randint(1900, 2022)


def pages():
    random.randint(100, 1000)


def isbn():
    fake = Faker()
    (fake.numerify(text='%%%-%-%%%%-%%%%-%'))

def rating():
    random.uniform(0, 5)


def price():
     random.uniform(100, 1000)


def author():
    fake = Faker()
    fake.name()


def generator():
    dict_ = {
        "model": MODEL,
        "pk": 1,
        "fields": {
            "title": book_name(),
            "year": year(),
            "pages": pages(),
            "isbn13": isbn(),
            "rating": rating(),
            "price": price(),
            "author": author()
        }
    }
    yield dict_



if __name__ == '__main__':
    books_list = []
    for pk in range(1, 101, 1):
        books = generator()
        books_list.append(books)
with open("books.json", "w") as write_file:
    json.dump(books_list, write_file)
