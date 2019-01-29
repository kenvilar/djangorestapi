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


# print(get_list())
get_list()
