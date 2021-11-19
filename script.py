import os

import requests


def fetch_books(books_count: int, dir_name: str) -> None:
    url = 'https://tululu.org/txt.php'

    for id in range(1, (books_count + 1)):
        options = {
            'id': id
        }
        resp = requests.get(url, params=options)
        resp.raise_for_status()

        with open(f'{dir_name}/{id}.txt', 'wb') as f:
            f.writelines(resp)


def main() -> None:
    dir_name = 'books'
    os.makedirs(dir_name, exist_ok=True)
    fetch_books(10, dir_name)


if __name__ == '__main__':
    main()
