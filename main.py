import os
import asyncio
import aiohttp
import revolt
from dotenv import load_dotenv
from revolt.ext import commands
load_dotenv()

TOKEN = os.getenv("TOKEN")
class Client(commands.CommandsClient):
    async def get_prefix(self, message: revolt.Message):
        return "!"

    @commands.command()
    async def ping(self, ctx: commands.Context):
        try:
            await ctx.send("pong")
            return
        except Exception as e:
            print(f"{e} = exception, and the error was caught in the ping block")
    async def on_message(self, message: revolt.Message):
        message.content= message.content.lower()
        await self.process_commands(message)
        if message.content == "hello":
            await message.channel.send("hi how are you")
        elif message.content == "hi":
            await message.channel.send("Hey there")
        elif message.content == "oye":
            await message.channel.send("Han Oye?")
        else:
             return
async def main():
    async with aiohttp.ClientSession() as session:
        client = Client(session, f"{TOKEN}")
        print("The bot has started")
        await client.start()
asyncio.run(main())

