#!/usr/bin/python3i
"""Makes a get request to json placeholder"""
import requests
from sys import argv


def main():
    """main api method"""
    url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    response = requests.get(url)
    if response.status_code == 200:
        emp = (response.json())
        response_2 = requests.get(f'{url}/todos')
        if response_2.status_code == 200:
            todo = response_2.json()
            c = [item for item in todo if item['completed']]
            print(f'Employee {emp["name"]} is \
                    done with tasks({len(c)}/{len(todo)}):')
            for item in c:
                print(f'\t {item["title"]}')


if __name__ == "__main__":
    main()
