import requests
import json

from settings import settings
from mainFunctions import make_request

params = {
    "access_token": settings["token"]
}

user_search = make_request("users.get", settings, params)


print(user_search)