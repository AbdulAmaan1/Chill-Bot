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

    # if a user replies to chill bot, chill bot will reply with "Fug off"
    if message.reference and message.author.id != 898570354904154162:
        for mention in message.mentions:
            if mention.id == 898570354904154162:
                await message.channel.send(
                    content="Fug off",
                    reference=message
                )
     
    #to reply to some specific messages sent by users
    if message.content.lower() == "hello there" :
        await message.channel.send("General Kenobi!")
    elif message.content.lower() == "understandable" :
        await message.channel.send("Have a nice day!")
    elif message.content.lower() == "dhruv" :
        await message.channel.send("You mean Supreme Leader Signor Fuhrer Thalapathy Dhruv Sama")
    elif message.content.lower() == "naruto" :
        await message.channel.send("SASUKE!")
    elif message.content.lower() == "69" :
        await message.channel.send("nice ( ͡° ͜ʖ ͡°)")

    await client.process_commands(message)


# ping pong
@client.command()
async def ping(ctx):
    await ctx.send("pong!")

#8ball
@client.command(aliases=['8ball'])
async def eightball (x):

    response=[
    "it's worth it",
    "it's bad",
    "you could have done it better",
    "you are the worst testing me ",
    "it is all well",
    "it is good ",
    'As I see it',
    ' yes Ask again later',
    'Better not tell you now',
    'Cannot predict now',
    'Concentrate and ask again',
    'Don’t count on it',
    'Don’t count on it',
    'It is certain',
    'It is decidedly so',
    'Most likely',
    'My reply is no',
    'My sources say no',
    'Outlook good',
    'Outlook not so good',
    'Signs point to yes',
    'Very doubtful',
    'Without a doubt',
    ' Yes',
    ' definitely',
    'You may rely on it ' 
     ]

    await x.send(choice(response))

# running the bot

client.run("ODk3Mzk4NTYzODA0NDQ2ODAx.YWVFig.V0cNd_RvlUuTPtwvWPoDA-InNHc")