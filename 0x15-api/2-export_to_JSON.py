#!/usr/bin/python3
"""Makes a get request to json placeholder"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """main api method"""
    filename = "{}.json".format(argv[1])
    url = 'https://jsonplaceholder.typicode.com/'
    res = requests.get(url + "users/{}".format(argv[1]))
    res_t = requests.get(url + "todos", params={"userId": argv[1]})
    emp = res.json()
    todo = res_t.json()
    with open(filename, "w") as f:
        datas = []
        for item in todo:
            u = emp.get("username")
            s = item.get("completed")
            t = item.get("title")
            data = {"task": t, "completed": s, "username": u}
            datas.append(data)
        ent = {argv[1]: datas}
        json.dump(ent, f)
