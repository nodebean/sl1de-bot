#!/usr/bin/env python3

import discord
from discord.ext import commands
import os
import random
import re
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

BOT_TOKEN = os.environ['BOT_TOKEN']

bot = commands.Bot(command_prefix='!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def windmills(ctx):
    await ctx.send("Also, I get it you think dank memes are all that exist but don't understand the concept of acceptable versus unacceptable actions. Swastikas with a direct connection to Israeli flag is not funny. The insinuation that a joke you were a part of going to far and having to be mediated doesn't justify your or anyone else's actions now. So please graduate high school before you discuss what is or is not a funny joke. Also beyond that yall pussy asses wouldn't do that shit in front of me so don't do it anywhere period.")

@bot.command()
async def anime(ctx):
    await ctx.send("see, I'll jerk off to some drawn, pubescent girls with giant cans, covered in gallons of goop all day too... my problem with weebs is that they don't just jerk off to the nasty shit like us normal perverts. They post and share their weeb shit in NON-porn communities, and actually think it's cute, funny, and I honestly suspect... cool. Like... they're not even ashamed. BE ASHAMED GOD DAMNIT, you're disgusting.\n\nLike... it hasn't happened yet, but I know someday it will. Someday I'll jerk off to a My Little Pony character with a human ass drawn onto it and a giant pink phallus stretching open it's purple vaj... but you can be damn sure I won't be dying my hair rainbow and going to any fucking conferences about it. I'll be ashamed of it like a normal grown man. Get it together weebos. Learn some shame.")

@bot.command()
async def brain(ctx):
    await ctx.send("https://imgur.com/AdORsX0")

@bot.command()
async def iran(ctx):
    await ctx.send("NEVER, EVER THREATEN THE UNITED STATES AGAIN OR YOU WILL SUFFER CONSEQUENCES THE LIKES OF WHICH FEW HAVE EVER SUFFERED BEFORE. WE ARE NO LONGER A COUNTRY THAT WILL STAND FOR YOUR DEMENTED WORDS OF VIOLENCE & DEATH. BE CAUTIOUS!")

@bot.command()
async def source(ctx):
    await ctx.send('https://github.com/terrancotta/sl1de-bot')

@bot.command()
async def parrot(ctx):
    await ctx.send('http://cultofthepartyparrot.com/assets/sirocco.gif')

@bot.command()
async def turtle(ctx):
    t = "<:ocean:483791904064929805><:turtle:483791987003228162><:turtle:483791987003228162> A turtle made it to the water!"
    c = "<:crab:483792084172800009><:turtle:483791987003228162><:crab:483792084172800009> The cycle of life can be cruel..."
    await ctx.send(random.choice([t, c]))

@bot.command()
async def driver(ctx):
    quote = [
        "OH NO! I CANT COME TO WORK TODAY! I HAVE HEAT STROKE!!!",
        "Can I get a Pay Advance?",
        "What do you mean I smoke in car? I NEVER smoke in car!!!",
        "YOU'RE FIRED YOU UGLY STAIN",
        "Holy fuck\nDriver fell asleep\nAt an arrival\n17 calls later\nI'm going to kill someone",
        "yes hello can I gave job on thanks",
        "I don't know what to do, the toilet paper just isn't there",
        "Employee who pissed everywhere is now upset\nThat he was caught pissing in front of the hotel directors window\nAnd blaming me\nFor not defending him\nIn front of hotel management\nFucking unbelievable\nEnd me now lord\nFor I have given my last fuck\nAnd have no more fucks left to give",
        "bank froze corporate account\nturns out they froze the wrong one",
        "OK\nwho is the king nigta\nwho can rap\nte slim shady verse\nthis guy\npeace hmies"
    ]
    await ctx.send(random.choice(quote))

@bot.command()
async def how(ctx):
    query = ctx.message.content.split(' ')[1:]
    query_string = ' '.join(str(q) for q in query)
    banned = ['`', 'here', 'everyone']
    if any(s in query_string for s in banned):
        await ctx.channel.send("{} <:lod:308700110521368576>".format(ctx.author.mention))
        await ctx.message.delete()
        return 
    if query_string.lower() == 'mad is rusrog' or query_string.lower() == 'mad is rusrog?':
        await ctx.send("RUSROG IS 10000% REALLY FUCKING MAD")
        return
    if query_string.lower() == 'thot is danktor' or query_string.lower() == 'thot is danktor?':
        await ctx.send("Danktor is 100% THOT")
        return
    is_many = False
    if query[0] == "many":
        is_many = True
        query = query[1:]
        query_string = ' '.join(str(q) for q in query)
    query_array = re.split(' is | are ', query_string)
    x = query_array[0]
    y = query_array[1]
    if y[-1] == "?": y = y[:-1]
    amt = random.randint(1, 105)
    nltk_y = nltk.word_tokenize(query_string)
    nltk_result = nltk.pos_tag(nltk_y)
    nltk_result = [i[1] for i in nltk_result if i[0].lower() in y]
    preps = ['in', 'on', 'at', 'over']
    if is_many:
        desc = ""
        joiner = " "
        if 'IN' in nltk_result or (len(nltk_result) == 1 and any(p in nltk_result for p in ['JJ', 'RB'])):
            desc = "There is" if " is " in query_string else "There are"
        else:
            joiner = " is " if " is " in query_string else " are "

        if any(p in y for p in preps):
            msgdata = "{} {} {}{}{}".format(desc, amt, x, joiner, y)
        else:
            if 'RB' in nltk_result:
                y = ""
            msgdata = "{} {} {}{}{}".format(desc, amt, y, joiner, x)
    else:
        msgdata = "{} is {}% {}".format(y, amt, x)
    await ctx.send(msgdata)

if __name__ == "__main__":
    bot.run(BOT_TOKEN)
