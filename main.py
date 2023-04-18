import revolt
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

class Client(revolt.Client):
    async def on_message(self, message: revolt.Message):
       try:
            message.content= message.content.lower()
            if message.content == "hello":
                await message.channel.send("hi how are you")
            elif message.content == "hi":
                await message.channel.send("Hey there")
            elif message.content == "oye":
                await message.channel.send("Han Oye?")
       except Exception as e:
           print(e)
    async def on_member_join(self, member: revolt.Member):
        try:
            embed = revolt.Embed(
            title="Title of the embedded message",
            description="Description of the embedded message",
            color=0xff0000  # Color of the left vertical stripe, in hex
            )
            message.channel.send(embed=embed)
        except Exception as e:
            print(e)
async def main():
    async with revolt.utils.client_session() as session:
        client = Client(session, f"{TOKEN}")#? Your token goes here
        await client.start()
        print("The bot is ready")

asyncio.run(main())