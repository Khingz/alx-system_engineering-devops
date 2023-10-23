#!/usr/bin/python3i
"""Makes a get request to json placeholder"""
import requests
from sys import argv


def main():
    """main api method"""
    url = 'https://jsonplaceholder.typicode.com/'
    res = requests.get(url + "users/{}".format(argv[1]))
    res_t = requests.get(url + "todos", params={"userId": argv[1]})
    emp = (res.json())
    todo = res_t.json()
    c = [item for item in todo if item.get('completed')]
    print("Employee {} is done with tasks({}/{}):".format(
        emp.get("name"), len(c), len(todo)))
    for item in c:
        print('\t {}'.format(item.get("title")))


if __name__ == "__main__":
    main()
