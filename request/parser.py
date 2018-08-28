import requests
import json

settings = {
    'id': '6675659',
    'api_base_url': 'https://api.vk.com/method/',
    #'base_dir': os.path.dirname(os.path.abspath(__file__)),
    #'update_period': 86400,
    'token': "ddb7c180ddb7c180ddb7c180f7ddd21d4bdddb7ddb7c18086324492b39512a71e6ea76d"
}


# ----------------action--------------------
def make_request(method, params=None):
    url = 'https://api.vk.com/method/{}?&v=5.80'.format(method, params)
    r = requests.post(url)
    return r
    """
    if r.status_code != 200:
        print(r.status_code)
        return None, None
    else:
        result = json.loads(r.content.decode('utf-8'))
        return result
    """
params = {
    'user_ids': settings["id"],
    'fields': 'bdate',
    'access_token': settings["token"],
}
print(requests.post('https://api.vk.com/method/users.get?user_ids={}&fields=bdate&access_token={}&v=5.80'.format(settings["id"], settings["token"])))

print(make_request("users.get"))