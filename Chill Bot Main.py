# importing necessary libraries
import discord
from discord.ext import commands
from random import choice

# initializing bot prefix
client = commands.Bot(command_prefix = "-")


# checking if bot is online
@client.event
async def on_ready():
    print("I am ready")


# checking messages
@client.event
async def on_message(message):

    await client.process_commands(message)


# ping pong
@client.command()
async def ping(ctx):
    await ctx.send("pong!")
#8ball
@client.command(aliases=['8ball','ball','8b'])
async def eightball (x):

    response=["it's woth it","it's bad","you could have don it better","you are the worst testing me ","it is all well","it is good "]

    await x.send(choice(response))

# running the bot
client.run("ODk3Mzk4NTYzODA0NDQ2ODAx.YWVFig.rJaBgmx930aDqKkm9aE1nGyFZ3c")
