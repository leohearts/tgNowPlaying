from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon import TelegramClient
from flask import Flask,request,redirect,Response
import asyncio
from settings import api_id, api_hash

# The first parameter is the .session file name (absolute paths allowed)
bio = ""
client = TelegramClient('leohearts', api_id, api_hash)
async def init():
    async with client:
        full = await client(GetFullUserRequest('me'))
        bio = full.full_user.about
        print(bio)

asyncio.run(init())
app = Flask(__name__)


@app.route('/<path:path>',methods=['POST'])
async def handler(path):
    if request.method=='POST':
        req = request.get_json()
        print(req)
        response = Response('{"msg": "No source"}', 500)
        if "emby" in path:
            if req["Event"] == "playback.start":
                try:
                    title = req["Title"].split("开始播放 ")[1]
                    async with client:
                        await client(UpdateProfileRequest(
                            about='▶️Playing ' + title
                        ))
                    response = Response({"msg": "Updated to %s" % title} , 200)
                except Exception as e:
                    print(e)
                    pass
            elif req["Event"] == "playback.stop":
                try:
                    async with client:
                        await client(UpdateProfileRequest(
                            about=bio
                        ))
                    response = Response({"msg": "Updated to %s" % bio } , 200)
                except Exception as e:
                    print(e)
                    pass
        return response
    else:
        response = Response('{"msg": "Method not allowed"}', 500)
        return response


if __name__ == "__main__":
    app.run()
