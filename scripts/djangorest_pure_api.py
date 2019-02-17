import json

import requests  # http requests

BASE_URL = "http://localhost:8000/"
ENDPOINT = "api/updates/"


def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    print(r.status_code)
    status_code = r.status_code
    if status_code != 200:
        print("not good sign!!!")
    data = r.json()
    print(type(data))
    # print(type(json.dumps(data)))
    for obj in data:
        # print(obj['id'])
        if obj['id'] == 1:
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            # print(dir(r2))
            print(r2.json())
    return data


def create_update():
    _new_data = {
        'user': 1,
        'content': 'Another cool content',
    }
    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(_new_data))
    # r = requests.delete(BASE_URL + ENDPOINT, data=_new_data)
    print(r.status_code)
    print(requests.codes.ok)
    print(r.headers)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text


def do_obj_update():
    _new_data = {
        "id": 4,
        'content': 'Some new awesome content.',
    }
    # r = requests.put(BASE_URL + ENDPOINT + "1/", data=json.dumps(_new_data)) #for detail
    r = requests.put(BASE_URL + ENDPOINT, data=json.dumps(_new_data)) #for list
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text


def do_obj_delete():
    _new_data = {
        "id": 7,
        # 'content': 'Delete obj data',
    }
    r = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(_new_data))
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


# print(do_obj_update())
# print(get_list())
# get_list()
# print(create_update())
print(do_obj_delete())
