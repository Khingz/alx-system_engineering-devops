#!/usr/bin/python3
"""Makes a get request to json placeholder"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    """main api method"""
    filename = "{}.csv".format(argv[1])
    url = 'https://jsonplaceholder.typicode.com/'
    res = requests.get(url + "users/{}".format(argv[1]))
    res_t = requests.get(url + "todos", params={"userId": argv[1]})
    emp = res.json()
    todo = res_t.json()
    c = [item for item in todo if item.get("completed") is True]
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for item in todo:
            u = emp.get("username")
            s = item.get("completed")
            t = item.get("title")
            writer.writerow([argv[1], u, s, t])
