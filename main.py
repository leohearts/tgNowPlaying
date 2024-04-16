from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon import TelegramClient
from flask import Flask,request,redirect,Response
import asyncio
from settings import api_id, api_hash

bio = ""

app = Flask(__name__)


@app.route('/<path:path>',methods=['POST'])
async def handler(path):
    client = TelegramClient('leohearts', api_id, api_hash)
    global bio
    if bio == "":
        async with client:
            full = await client(GetFullUserRequest('me'))
            _bio = full.full_user.about
            print(_bio)
            if "▶️Playing" not in _bio:
                bio = _bio
    if request.method=='POST':
        req = request.get_json()
        print(req)
        response = Response('{"msg": "No source"}', 500)
        if "emby" in path:
            if req["Event"] == "playback.start":
                try:
                    async with client:
                        full = await client(GetFullUserRequest('me'))
                        _bio = full.full_user.about
                        print(_bio)
                        if "▶️Playing" not in _bio:
                            bio = _bio

                    title = req["Title"]
                    async with client:
                        await client(UpdateProfileRequest(
                            about='▶️Playing ' + title
                        ))
                    response = Response(str({"msg": "Updated to %s" % title}) , 200)
                except Exception as e:
                    print(e)
                    pass
            elif req["Event"] == "playback.stop":
                try:
                    async with client:
                        await client(UpdateProfileRequest(
                            about=bio
                        ))
                    response = Response(str({"msg": "Updated to %s" % bio }) , 200)
                except Exception as e:
                    print(e)
                    pass
        return response
    else:
        response = Response('{"msg": "Method not allowed"}', 500)
        return response


if __name__ == "__main__":
    app.run()
