import discord
import os
import requests

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("wakeup")

@client.event
async def on_message(message):
    if message.content.startswith("!getItem"):

            # 最初のリクエストで取得したURLを使って次のリクエストを送信
            response = requests.get("http://djangoapitest-web-1:8000/storage/api/Item/")

            data = response.json()

            for item in data:
                await message.channel.send(f"{item['name']}")

            # dataがリストであることを確認
            # if isinstance(data, list):
            #     for item in data:
            #         if isinstance(item, dict) and 'name' in item:
            #             await message.channel.send(f"{item['name']}")
            #         else:
            #             await message.channel.send("Error: Unexpected item format")


client.run(TOKEN)


# import discord
# import os
# import requests
#
# TOKEN = os.getenv('TOKEN')
#
# intents = discord.Intents.all()
#
# client = discord.Client(intents=intents)
#
# @client.event
# async def on_ready():
#     print("wakeup")
#
# async def on_message(message):
#     if message.content.startswith("!getItem"):
#
#             response = requests.get("http://djangoapitest-web-1:8000/storage/api/Item/")
#             response.raise_for_status()  # HTTPエラーチェック
#             data = response.json()
#             print(data)
#
#             # for item in data:
#             #     print(item)
#             #     await message.channel.send(f"{item['name']}")  # 'await'を追加
#
#             if isinstance(data, list):
#                 for item in data:
#                     if isinstance(item, dict) and 'name' in item:
#                         await message.channel.send(f"{item['name']}")
#
#
#
#
# client.run(TOKEN)