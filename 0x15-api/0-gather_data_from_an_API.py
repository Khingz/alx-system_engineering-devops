#!/usr/bin/python3i
"""Makes a get request to json placeholder"""
import requests
from sys import argv


def main():
    """main api method"""
    url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    response = requests.get(url)
    response_t = response_2 = requests.get(f'{url}/todos')
    emp = (response.json())
    todo = response_2.json()
    c = [item for item in todo if item.get('completed')]
    print("Employee {} is done with tasks({}/{}):".format(
        emp.get("name"), len(c), len(todo)))
    for item in c:
        print('\t {}'.format(item.get("title")))


if __name__ == "__main__":
    main()
