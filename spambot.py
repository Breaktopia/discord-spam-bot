import discord
from discord.ext.commands import *
from discord.ext import commands
import random
import asyncio
import time
import json
from itertools import cycle
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get

 
##PREFIX##

bot = commands.Bot(command_prefix='§')
TOKEN = 'token'
client = commands.Bot(command_prefix='§')

##OTHER##
bot.remove_command('help')

@bot.command(pass_context=True)
async def spam(ctx): #run "!spam" to run the command
    await ctx.message.delete()
    while True:
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n") 
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")
        await ctx.send("You Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\nYou Have Been Spammed!@everyone\n")



##BOT IS READY##
@bot.event
async def on_ready():
#BOT STATUS#
    print("Bot Is Online! Getting Ready To Spam.")
    print(f"Bot Status: Online!...")