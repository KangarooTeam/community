import requests, json

def make_request(method, settings, params=None):
    url = '{}{}?{}&v=5.73'.format(settings['api_base_url'], method, params)
    r = requests.post(url, params)

    if r.status_code != 200:
        print(r.status_code)
        return None, None
    else:
        result = json.loads(r.content.decode('utf-8'))
        return result