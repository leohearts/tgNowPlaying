from telethon.tl.functions.account import UpdateProfileRequest
from telethon import TelegramClient
from flask import Flask,request,redirect,Response

from settings import api_id, api_hash

# The first parameter is the .session file name (absolute paths allowed)
client = TelegramClient('leohearts', api_id, api_hash)

app = Flask(__name__)

@app.route('/<path:path>',methods=['POST'])
def handler(path):
    if request.method=='POST':
        req = request.get_json()
        print(req)
    else:
        response = Response('{"msg": "Method not allowed"}', 500)
    return response


if __name__ == "__main__":
    app.run()
