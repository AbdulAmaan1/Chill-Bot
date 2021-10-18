# importing necessary libraries
import discord
import discord.colour
import math,sys
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


# user defined function for calculator feature    
def extract(t,q,i):
    global comma_detector
    comma_detector=False
    for q in range(len(t)):
        res,base,count='','',0
        while True:
            if count<len(t[q]):
                if t[q][count]==',' or comma_detector==True:
                    base+=t[q][count]
                    comma_detector=True
                    count+=1
                elif t[q][count]!=')' and comma_detector==False:
                    res+=t[q][count]
                    count+=1
                else:
                    res+=t[q][count]
                    break
            else:
                break
    if comma_detector==False:
        string_to_replace=i+res
    else:
        string_to_replace=i+res+base
    if comma_detector==False:
        return string_to_replace,[res]
    else:
        return string_to_replace,[res,base]

#calculates stuff
@client.command()
async def cal(ctx):
    heading,con,embed='','',''
    try:# to handle errors like a boss
        j=ctx.message.content #getting the expression
        j=j[4:].lower() #remove the -cal part form it
        j=j.replace(' ','') #removing unwanted spaces
        trig_flags=['sin','tan','cosec','cos','sec','cot']
        other_mathflags=['^','log','ln','^b']
        flag1=False
        flag2=False
        for i in trig_flags:#checks if trig functions are there or not
            if i in j:
                flag1=True
                break
        for i in other_mathflags:#checks if other math functions are there or not
            if i in j:
                flag2=True
                break
        if flag1:
            for i in trig_flags:# checks which trig functions are there and then evauluates them
                r=j.find(i)
                if r!=-1:
                    t=j.split(i)[1:]# removes and seperates all trig functions from string and seperates their values 
                    string_to_replace,res=extract(t,0,i)#extracts values
                    res=res[0]
                    num=res.lstrip('(').rstrip(')')#edits it so that it can be accepted by the float method
                    cosec_check=False#checks if its a cosec function, had to do this on top of the if condition to prevent error
                    if 'rad' in num:#checks if the value inside trig functions is in radians else converts them to radians
                        u=num.find('rad')
                        num=float(num[:u])
                    else:
                        num=math.radians(float(num))
                    if i=='sin':
                        answer=math.sin(num)
                    elif i=='cos':
                        answer=math.cos(num)
                    elif i=='tan':
                        answer=math.tan(num)
                    elif i=='sec':
                        answer=math.cos(num)
                        answer=1/answer
                    elif i=='cot':
                        answer=math.tan(num)
                        answer=1/answer
                    elif i=='cosec':
                        answer=math.sin(num)
                        answer=1/answer
                        answer='('+str(answer)+')'
                        j=j.replace(string_to_replace,answer)#replacing the trig function in the expression string with the value of the function, so that the eval function can evaulate it at the end
                        cosec_check=True
                    if cosec_check==False:
                        answer='('+str(answer)+')'
                        j=j.replace(string_to_replace,answer)#same thing as the above comment
        if flag2:# checks which math functions are there and then evauluates them
            for i in other_mathflags:
                r=j.find(i)
                if r!=-1:
                    t=j.split(i)[1:]
                    if i=='^':
                        j=j.replace('^','**')#replaces ^ symbol for ** as in python we represent power with '**' symbol and '^' is binary or 
                    if i=='^b':
                        j=j.replace('^b','^')#replaces ^b with ^ symbol so that the eval function can evaluate it as binary or
                    if i=='ln':
                        s,res=extract(t,0,'ln')
                        res=res[0]
                        num=float(res.lstrip('(').rstrip(')'))
                        answer=str(math.log(num))
                        j=j.replace(s,answer)#same replacing thing
                    if i=='log':#here it also takes input in form log(value,base) so thats why the if else with the comma detector
                        base=10
                        s,y=extract(t,0,'log')
                        if comma_detector==True:
                            res=y[0]
                            base=y[1]
                        else:
                            res=y[0]
                        num=float(res.lstrip('(').rstrip(')'))
                        if comma_detector==True:
                            base=float(base.lstrip(',').rstrip(')'))
                        answer=str(math.log(num,base))
                        j=j.replace(s,answer)

        p=eval(j)
        con=str(round(p,3))
        heading='Answer'
        embed=discord.Embed(title=heading,content=con,colour=discord.Colour.random())
        embed.add_field(value='____',name=con)
        await ctx.send(embed=embed)
    except Exception as err:
        er=sys.exc_info()[0]
        if str(er)=="<class 'ZeroDivisionError'>":
            del embed# so that it dosent give me that shitty send() found unexpected embed error
            em=discord.Embed(title="I can't divde by 0 macha",colour=discord.Colour.random())
            em.set_image(url="https://media3.giphy.com/media/LRVnPYqM8DLag/giphy.gif?cid=ecf05e47h41g7209ip3gibmhjecuubrj5hnb4mq9de3zf5x2&rid=giphy.gif&ct=g")
            await ctx.send(embed=em)
        elif str(er)=="<class 'NameError'>":
            del embed
            em=discord.Embed(title="ERROR",colour=discord.Colour.red())
            em.set_image(url="https://media2.giphy.com/media/9Ai5dIk8xvBm0/giphy.gif?cid=ecf05e47qer7xbat2ydqrsqh3igdndn9vcevqok1j51avevm&rid=giphy.gif&ct=g")
            em.add_field(name='Please put proper expression variables are not allowed in expressions only values and function names',value='You can read my **documentation** to make proper expressions or try again :)')
            await ctx.send(embed=em)
        else:
            del embed
            em=discord.Embed(title="ERROR",colour=discord.Colour.red())
            em.set_image(url="https://media2.giphy.com/media/1VT3UNeWdijUSMpRL4/giphy.gif?cid=ecf05e47hbie1f18p093176buoo01qsi36eqapkfwx5c93jf&rid=giphy.gif&ct=g")
            em.add_field(name='Something is wrong',value=str(err))
            await ctx.send(embed=em)

            
@client.command()
async def hehe(ctx):#hehe boi
    em=discord.Embed(title="HEHE BOI",colour=discord.Colour.random())
    em.set_image(url="https://media3.giphy.com/media/dPEJxh06y4OTC/giphy.gif?cid=ecf05e47vcr0ix4bhnyopjql1fcwcgj22hdn51h935aey0gr&rid=giphy.gif&ct=g")
    await ctx.send(embed=em)
    
    
@client.command()
async def noob(ctx):#LOL NOOB
    em=discord.Embed(title='Noob',colour=discord.Colour.random())
    em.set_image(url="https://media0.giphy.com/media/To7eFJmTrvS9y/giphy.gif?cid=ecf05e47kwlq4f6oaaqs9wzbzo9hfl6xxtkub76bqo0su76d&rid=giphy.gif&ct=g")
    await ctx.send(embed=em)    
    
    
# running the bot
client.run("ODk3Mzk4NTYzODA0NDQ2ODAx.YWVFig.V0cNd_RvlUuTPtwvWPoDA-InNHc")
