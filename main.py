import os
import asyncio
import aiohttp
import revolt
import random
from dotenv import load_dotenv
from revolt.ext import commands
import json
load_dotenv()

TOKEN = os.getenv("TOKEN")
class Client(commands.CommandsClient):
    async def get_prefix(self, message: revolt.Message):
        return "!"

    @commands.command()
    async def bing(self, ctx: commands.Context):
        await ctx.send("bong")
                
    @commands.command()
    async def joke(self, ctx: commands.Context):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://official-joke-api.appspot.com/random_joke') as resp:
                data = await resp.json()
                await ctx.send(f"{data['setup']}\n\n{data['punchline']}")
    
    @commands.command()
    async def roll(self, ctx: commands.Context, number: int):
        roll = random.randint(1, number)
        await ctx.send(f"You rolled a {roll}!")
    
    @commands.command()
    async def dadjoke(self, ctx: commands.Context):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://icanhazdadjoke.com", headers={"Accept": "application/json"}) as resp:
                data = await resp.json()
                await ctx.send(data["joke"])

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
        print(f"The bot has started")
        await client.start()
asyncio.run(main())

