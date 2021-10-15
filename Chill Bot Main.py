# importing necessary libraries
import discord
from discord.ext import commands


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
    j=ctx.message.content
    j=j[10:].lower()
    print(type(j))
    trig_flags=['sin','tan','cos','cosec','sec','cot']
    other_mathflags=['^','']
    if j in trig_flags:
        flags=[]
        for i in trig_flags:
            r=j.find(i)
            if r==-1:
                flags.append(i)
        

    p=eval(str(j))
    print(p)
    await ctx.send(p)


# running the bot
client.run("ODk4NTcwMzU0OTA0MTU0MTYy.YWmI2w.NZtpa5f83RJrJouULNytn9bynEU")
