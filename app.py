import json
from aioflask import Flask, request, Response
from pyrogram import Client, filters
from pyrogram.types import Message
import os
import asyncio
from aiohttp import ClientSession
from Python_ARQ import ARQ
import telegram

app = Flask(__name__)

@app.route('/test')
def test():
 return "Running..."

@app.route('/nsfw')
async def file():
 session = ClientSession()
 arq = ARQ("https://arq.hamker.dev/", "your arq", session)
 file_id = request.args.get('file_id')
 token_ = request.args.get('token')
 bot = telegram.Bot(token=token_)
 if token_ is None :
  data = {
        'status': 'ok', 
        'resp': 'Pls Enter Token or chat with me on t.me/oooww',
        'by': '@oooww'
        }
  return json.dumps(data, ensure_ascii=False)
 if file_id is None:
  data = {
        'status': 'ok', 
        'resp': 'Pls Enter File Id or chat with me t.me/oooww',
        'by': '@oooww'
        }
  return json.dumps(data, ensure_ascii=False)
 file_info = bot.get_file(file_id)
 resp = await arq.nsfw_scan(file_info.file_path)
 data = {
        'status': 'ok', 
        'result': {
        'is_nsfw': resp.result.is_nsfw,
        'drawings' : resp.result.drawings,
        'hentai' : resp.result.hentai,
        'porn' : resp.result.porn,
        'sexy' : resp.result.sexy
        },
        'by': '@oooww'
        }
 return json.dumps(data, ensure_ascii=False)

###
@app.route('/msg')
async def nnn():
 session = ClientSession()
 arq = ARQ("https://arq.hamker.dev/", "your arq", session)
 msg_id = request.args.get('msg_id')
 chat_id = request.args.get('chat_id')
 token_ = request.args.get('token')
 bot = telegram.Bot(token=token_)
 msg_info = bot.get_messages(chat_id,msg_id)
 return msg_info
 
if __name__ == '__main__':
    app.run(host='ip', port=8080, debug=True)