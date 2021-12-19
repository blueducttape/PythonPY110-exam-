from faker import Faker
import random
import json
from conf import MODEL


def pk(start=1) -> int:
    """Создание счётчика"""
    while True:
        yield start
        start += 1


def book_name() -> str:
    """Выбирает название книги из файла books.txt"""
    with open('books.txt', 'r') as file:
        lines = file.readlines()
        return random.choice(lines)


def year() -> int:
    """Генерирует год"""
    return random.randint(1900, 2022)


def pages() -> int:
    """Генерирует кол-во страниц"""
    return random.randint(100, 1000)


def isbn() -> str:
    """Генерирует ISBN"""
    fake = Faker()
    return fake.numerify(text='%%%-%-%%%%-%%%%-%')


def rating() -> float:
    """Генерирует рейтинг книги"""
    return round(random.uniform(0, 5), 4)


def price() -> float:
    """Генерирует цену книги"""
    return round(random.uniform(100, 5000), 2)


def author() -> list:
    """Генерирует имя автора/ов"""
    list_ = []
    fake = Faker()
    for i in range(random.randint(1, 3)):
        list_.append(fake.name())
    return list_


def generate() -> dict:
    """Генератор словаря"""
    yield {
        "model": MODEL,
        "pk": next(value),
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


def main():
    books_list = []
    for x in range(100):
        books = next(generate())
        books_list.append(books)
    """создаем список"""
    with open("books.json", "w") as write_file:
        json.dump(books_list, write_file, indent=4, ensure_ascii=False)
    """запись в файл"""


if __name__ == '__main__':
    value = pk()
    main()


