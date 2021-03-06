from base64 import b64encode, b64decode
import requests
import json
from settings import *

flip = {
    "1":"0",
    "0":"1"
}

info = requests.get(url).json()

sha = info["sha"]
content = flip[b64decode(info["content"])]

headers = {
    'Authorization': 'token {0}'.format(token)
}

pl = {
    "message": "This is why I have commitment issues",
    "content": b64encode(content),
    "sha": sha
}

r = requests.put(url, headers=headers, data = json.dumps(pl))
