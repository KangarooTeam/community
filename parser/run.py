import requests
import json

from settings import settings
from mainFunctions import make_request
from params import params_users_get


users_get = make_request("users.get", settings, params_users_get)


print(users_get)