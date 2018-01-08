import discord
import lxml.html
import requests
import cssselect
import json






client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):

    if message.content.startswith("!rate"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            target_url = 'https://www.cryptopia.co.nz/api/GetMarket/PAC_DOGE'
            target_html = requests.get(target_url)
            # jsonのデータがテキストなのでjsonでロードしなおす
            x = json_dict = json.loads(target_html.text)
            # データを取って辞書型で表示する
            m="銘柄:{} ".format(x['Data']['Label']),"現在価格: {}".format(x['Data']['LastPrice']),"24時間値動き :{}".format(x['Data']['Change'])
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await client.send_message(message.channel, m)

client.run("Mzk5NTUwMTUzNjkxNzU4NTky.DTO1bw.6EHvl_CpjIxJakeS_blmoEtHUFI")