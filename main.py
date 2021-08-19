# RoAuth, developed by github.com/n0vuh

# Configuration
BOT_TOKEN = "ODc3ODA5MzcxNjkyODAyMDk4.YR4Brw.6V3Lc3K9r_6JE-S78OneYBGY0Hs"
BOT_PREFIX = "f!"
WORD_FILE = "words.txt"
KEY_COUNT = 5
CHECKS = 10
COOLDOWN = 2

# Imports/Dependencies
import discord

from discord.ext import commands
from asyncio import sleep
from backend import check, words

# Setup client
word_list = words.get_words(WORD_FILE)
roauth = commands.Bot(BOT_PREFIX, help_command=None, description="A simple bot to authenticate ownership of Roblox accounts.")
intents = discord.Intents.all()
intents.members = True

# Commands
@roauth.event
async def on_ready():
    print(f"RoAuth is online.\nLogged into: {roauth.user}")
    
@roauth.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"{ctx.message.author.mention}, please try again in {error.retry_after} second(s).")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send(f"{ctx.message.author.mention}, command doesn't exist.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"{ctx.message.author.mention}, you are missing an argument.")

@commands.cooldown(1, COOLDOWN, commands.cooldowns.BucketType.member)
@roauth.command(aliases=["auth"])
async def authenticate(ctx, userId: int):
    u = check.user(userId)
    skey = words.generate_key(word_list, KEY_COUNT)
    if u.exists() == True:
        await ctx.send(f"{ctx.author.mention}, please add `{skey}` to your description in roblox.")
        for _ in range(CHECKS):
            if u.compare(skey) == True:
                await ctx.send(f"{ctx.author.mention}, your account has been validated.")
                # do something after validated
                try:
                    await ctx.author.edit(nick=u.username())
                except: 
                    pass
                break
            else:
                await sleep(5)
    else:
        await ctx.send(f"{ctx.author.mention}, that user id is invalid.")


roauth.run(BOT_TOKEN)
