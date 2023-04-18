import revolt
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")
print(TOKEN)

class Client(revolt.Client):
    async def on_message(self, message: revolt.Message):
        message.content= message.content.lower
        if message.content == "hello":
            await message.channel.send("hi how are you")

async def main():
    async with revolt.utils.client_session() as session:
        client = Client(session, f"{TOKEN}")
        await client.start()
        print("The bot is ready")

asyncio.run(main())