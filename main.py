import revolt
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")
class Client(revolt.Client):
    async def get_prefix(self,message: revolt.Message):
        return "!"
    async def on_message(self, message: revolt.Message):
        message.content= message.content.lower
        if message.content == "hello":
            await message.channel.send("hi how are you")
        elif message.content == "hi":
            await message.channel.send("Hey there")
        elif message.content == "oye":
            await message.reply(f"Han Oye?",True)
async def main():
    async with revolt.utils.client_session() as session:
        client = Client(session, f"{TOKEN}")#? Your token goes here
        await client.start()
        print("The bot is ready")

asyncio.run(main())