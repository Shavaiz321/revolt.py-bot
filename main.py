import os
import asyncio
import aiohttp
import revolt
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")
class Client(revolt.Client):
    async def on_message(self, message: revolt.Message):
            message.content= message.content.lower() #? So every message is lower case
            if message.content == "hello":
                await message.channel.send("What do you want?")
            elif message.content == "hi":
                await message.channel.send("Hey there")
            elif message.content == "oye":
                await message.channel.send("Han Oye?")
            else:
                return
            
#?This is a simple chat bot, to add more responses you can add on to the existing code

async def main():
    async with aiohttp.ClientSession() as session:
        client = Client(session, f"{TOKEN}") #! Input your own token here, I just did this to hide my own token.
        print("The bot has started")
        await client.start()
asyncio.run(main())