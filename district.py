# Hello, thanks for buying District, you finally managed to deobfuscate the .exe file.

#MIT License
# ————————————————————
#Copyright (c) 2023 khai/kh/sanity

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
# ————————————————————

# District was heavily inspired by ethone.cc and nighty.one

# Enjoy.


# Installation and importing of requirements ————————————————————

import os
import logging
import json
import discord
import asyncio
import time
import requests
import io
import time
import subprocess
import ctypes
import openai
import string
import sys
import notifypy
import pystray
import PIL.Image
import threading
import pyPrivnote as pn
import urllib
import hashlib
import re
import random
import aiohttp

from subprocess import Popen
from subprocess import call
from pystyle import Colors, Colorate
from keyauth import api
from discord.ext import tasks
from wintoast import ToastNotifier
from datetime import datetime
from threading import Thread
from datetime import datetime
from bs4 import BeautifulSoup as bs4
from colorama import Fore
from itertools import cycle
from notifypy import Notify
from pypresence import Presence 
from discord.ext import commands

# License key authentication system ————————————————————

def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest


keyAuthApp = api(
    name = "DistrictSB",
    ownerid = "LihrBEWGYz",
    secret = "8a0a956bdb0bb77e25e2800fc04622fb54e9824d2901995f8a0948b33c7b3c58",
    version = "1.0",
    hash_to_check = getchecksum()
)


# Checking and installation of discord version that supports selfbots ————————————————————

def discordVersion():
    if(not discord.__version__ in ['1.7.0', '1.7.3']):
        logging.info('[!] Installing Discord.Py, v1.7.3')
        os.system('pip install -U discord.py==1.7.3')
    else:
        pass

# Restart function ————————————————————

def DistrictRestart():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# Toast functions ————————————————————

def DistrictNoCommand():
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Command not found."
    notification.icon = "assets/district-png.ico"
    notification.audio = "sound/error.wav"
    notification.send()
    
def DistrictConnected():
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Connected as: {district.user} | Version {district_version}"
    notification.icon = "assets/district-png.ico"
    notification.audio = "sound/connected.wav"
    notification.send()

def DistrictSniped():
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Succesfully sniped a nitro code !!"
    notification.icon = "assets/district-png.ico"
    notification.audio = "sound/sniped.wav"
    notification.send()

def DistrictError():
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Ensure the command executed was used appropriately to prevent errors."
    notification.icon = "assets/district-png.ico"
    notification.audio = "sound/error.wav"
    notification.send()



 # Importing from config.json ————————————————————

with open('core/config.json') as f:
    config = json.load(f)

Token = config.get('userToken')

stream_url = config.get('streamUrl')
guildName = config.get('guildName')
roleName = config.get('roleName')
chanName = config.get('chanName')

reason = config.get('reason')

prefix = config.get('prefix')

stat1 = config.get('stat1')
stat2 = config.get('stat2')
stat3 = config.get('stat3')

oneTimeLicense = config.get('oneTimeLicense')
oneLicenseKey = config.get('oneLicenseKey')

richPresence = config.get('richPresence')

deleteAfter = config.get('deleteAfter')

nitroSniper = config.get('nitroSniper')

# Defining the variable toaster ————————————————————

toaster = ToastNotifier()

# Basic discord stuff required for selfbot to run ————————————————————

intents = discord.Intents.all()
intents.members = True
district_version = 1.5
district = commands.Bot(command_prefix=prefix, case_insensitive=False, intents=intents, self_bot=True)
district.remove_command("help")

# Console stuff ————————————————————

ctypes.windll.kernel32.SetConsoleTitleW(f'District Selfbot | Version: {district_version} | Theme: Default')
os.system('mode 80, 20')

# Logging ————————————————————

logging.basicConfig(
    level=logging.INFO,
    format=f"» {Fore.BLUE}[{Fore.RESET} %(asctime)s {Fore.BLUE}] | {Fore.RESET}%(message)s ",
    datefmt="%H:%M:%S"
)

'''
# Sid Lock ————————————————————

hwid = keyAuthApp.user_data.hwid
token = win32security.OpenProcessToken(win32api.GetCurrentProcess(),win32security.TOKEN_QUERY)
sid = win32security.GetTokenInformation(token,win32security.TokenUser)[0]
sid_str = win32security.ConvertSidToStringSid(sid)
'''

        
# Using rich presence ————————————————————

if richPresence == "True":
    RPC = Presence('1071761243314081893')
    RPC.connect()
    RPC.update(details="Connected", large_image="logo", small_image="logo", large_text=f"District v{district_version}", small_text="discord.gg/enhancing", start=time.time(), buttons=[{"label": "Discord", "url": "https://discord.gg/enhancing"}, {"label": "Website", "url": "https://district.com"}])

else:
    pass



# Intro to be shown after login and authentication stuff ————————————————————



def intro():
    os.system('cls')
    print(Colorate.Diagonal(Colors.blue_to_cyan,
    f'''
                              ╔╦╗╦╔═╗╔╦╗╦═╗╦╔═╗╔╦╗
                               ║║║╚═╗ ║ ╠╦╝║║   ║ 
                              ═╩╝╩╚═╝ ╩ ╩╚═╩╚═╝ ╩ v{district_version}
    '''))
    print(Colorate.Vertical(Colors.blue_to_cyan,
    f'''
                           Connected: [ {district.user} ]

   ╔══════════════════════════════════════════════════════════════════════╗
   ║                        Commands: {len(district.commands)} | Guilds: {len(district.guilds)}                     ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║           HWID: {keyAuthApp.user_data.hwid}        ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║                    Developer: equi.ty aka equity                     ║
   ╚══════════════════════════════════════════════════════════════════════╝
    '''))
    logging.info(f'Running version {Fore.BLUE}[{Fore.RESET}{district_version}{Fore.BLUE}]{Fore.RESET}')
    logging.info(f'Type {Fore.BLUE},{Fore.RESET}help{Fore.BLUE}{Fore.RESET} to get started')


if oneTimeLicense == "True":
    authKey = oneLicenseKey
    os.system('cls')
    logging.info(Colorate.Diagonal(Colors.blue_to_cyan, 'Validating license key...'))
    os.system('cls')
    keyAuthApp.license(authKey)
    @district.event
    async def on_ready():
        discordVersion()
        os.system('cls')
        intro()
        DistrictConnected()


else:
    authKey = input(Colorate.Diagonal(Colors.blue_to_cyan, '[?] Enter license key: '))
    os.system('cls')
    logging.info(Colorate.Diagonal(Colors.blue_to_cyan, 'Validating license key...'))
    keyAuthApp.license(authKey)
    os.system('cls')
    intro()
    DistrictConnected()



# Command not found error handler ————————————————————

@district.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.delete()
        DistrictNoCommand()

# Commands ————————————————————

# Help commands ————————————————————

@district.command()
async def help(ctx):
    await ctx.message.delete()
    logging.info('Help Command Executed')
    await ctx.send(f'''
> ```ini
> [ District Selfbot ] | Help Command
> ```
> ```ini
> <> is required | () is optional
> ```
> ```ini
> [{prefix}moderation]    »  Shows the moderation commands
> [{prefix}utility]       »  Shows available utility commands
> [{prefix}account]       »  Shows account related commands
> [{prefix}troll]         »  Shows the available trolling commands
> [{prefix}abuse]         »  Shows all the raiding comamnds
> [{prefix}code]          »  Shows all available code commands
> [{prefix}themes]        »  Shows all available console themes and their commands
> [{prefix}status]        »  Shows all available status commands
> ```
    ''', delete_after=deleteAfter)

# Moderation commands ————————————————————

@district.command()
async def moderation(ctx):
    await ctx.message.delete()
    logging.info('Moderation Command Executed')
    await ctx.send(f'''
> ```ini
> [ District Selfbot ] | Moderation Commands
> ```
> ```ini
> <> is required | () is optional
> ```
> ```ini
> [{prefix}ban <@user>]                     » Bans the mentioned user
> [{prefix}unban <ID>]                      » Bans the mentioned user
> [{prefix}kick <@user>]                    » Kicks the mentioned user
> [{prefix}mute <@user>]                    » Mutes the mentioned user
> [{prefix}unmute <@user>]                  » Unmutes the mentioned user
> [{prefix}slowmode <seconds>]              » Sets the channel slowmode
> [{prefix}slowmodeoff]                     » Removes the channel slowmode
> [{prefix}jail <@user>]                    » Jails the mentioned user
> [{prefix}unjail <@user>]                  » Unjails the mentioned user
> [{prefix}lock <#channel> (#channel)]      » Locks the mentioned channel
> [{prefix}purge <amount>]                  » Purges an amount of messages
> [{prefix}unlock <#channel> (#channel)]    » Unlocks the mentioned channel
> [{prefix}nuke]                            » Deletes a channel and then recreates it back
> ```
    ''', delete_after=deleteAfter)

# Utility commands ————————————————————

@district.command()
async def utility(ctx):
    await ctx.message.delete()
    logging.info('Utility Command Executed')
    await ctx.send(f'''
> ```ini
> [ District Selfbot ] | Utility Commands
> ```
> ```ini
> <> is required | () is optional
> ```
> ```ini
> [{prefix}avatar <@user> (@user)]              »  Sends the mentioned users avatar
> [{prefix}userinfo <@user> (@user)]            »  Sends the userinfo of mentioned user
> [{prefix}serverinfo]                          »  Sends the serverinfo
> [{prefix}serverid]                            »  Sends the server ID
> [{prefix}servericon]                          »  Sends the servericon
> [{prefix}serverbanner]                        »  Sets the serverbanner
> [{prefix}poll <message>]                      »  Creates poll
> [{prefix}membercount]                         »  Sends the amount of members in server
> [{prefix}invites <@user> (@user)]             »  Sends the amount of invites
> [{prefix}addrole <@user> <@role>]             »  Adds role 
> [{prefix}derole <@user> <@role>]              »  Deroles the mentioned user
> [{prefix}afk <time> (time)]                   »  Sets your AFK
> [{prefix}roleinfo <@role>]                    »  Sends roleinfo on the role
> [{prefix}permissions <@user> (@user)]         »  Sends permissions for the mentioned user
> [{prefix}emojiadd <emoji>]                    »  Adds an emoji
> [{prefix}image <args>]                        »  Sends an image based on sent arg.
> [{prefix}massreact <emoji>]                   »  Mass react to 20 messages
> [{prefix}ignorefriends]                       »  Ignores all friend requests
> [{prefix}acceptfriends]                       »  Accepts all friend requests
> [{prefix}copyguild]                           »  Copies the guild 
> [{prefix}btc]                                 »  Sends bitcoin price in eur and usd
> [{prefix}clear]                               »  Clears the console
> [{prefix}8ball <question>]                    »  Runs an 8Ball on the sent question
> [{prefix}commandcount]                        »  Sends the amount of built in commands
> ```
    ''', delete_after=deleteAfter)

# Account commands ————————————————————

@district.command()
async def account(ctx):
    await ctx.message.delete()
    logging.info('Account Command Executed')
    await ctx.send(f'''
> ```ini
> [ District Selfbot ] | Account Commands
> ```
> ```ini
> <> is required | () is optional
> ```
> ```ini
> [{prefix}watching <message>]       »  Sets your watching activity
> [{prefix}playing <message>]        »  Sets your playing activity
> [{prefix}listening <message>]      »  Sets your listening activity
> [{prefix}stopactivity]             »  Stops the current activity
> [{prefix}hypesquad]                »  Sets your competing activity
> [{prefix}logout]                   »  Logs out of the account
> [{prefix}restart]                             »  Restarts District selfbot.
> [{prefix}groupleaver]              »  Leaves all available groups
> ```
    ''', delete_after=deleteAfter)

# Troll commands ————————————————————

@district.command()
async def troll(ctx):
    await ctx.message.delete()
    logging.info('Troll Command Executed')
    await ctx.send(f'''
> ```ini
> [ District Selfbot ] | Troll Commands
> ```
> ```ini
> <> is required | () is optional
> ```
> ```ini
> [{prefix}spam <message>]              »  Spams the message sent
> [{prefix}shrug]                       »  Sends a shrug
> [{prefix}lenny]                       »  Sends a lenny face
> [{prefix}tableflip]                   »  Sends a tableflip
> [{prefix}unflip]                      »  Sends an unflipped table
> [{prefix}nitro]                       »  Sends a randomly generated nitro code
> [{prefix}gay (@user)]                 »  Sends the mentioned users gay percentage
> [{prefix}tweet <username> <message>]  »  Creates a screenshot of a tweet
> [{prefix}fry <username>]              »  Fries the mentioned user
> [{prefix}virus]                       »  Runs a virus prank
> [{prefix}table]                       »  Sends a table animation in text form
> ```
    ''', delete_after=deleteAfter)

# Abuse commands ————————————————————

@district.command()
async def abuse(ctx):
    await ctx.message.delete()
    logging.info('Raid Command Executed')
    await ctx.send(f'''
> ```ini
> [ District Selfbot ] | Abuse Commands
> ```
> ```ini
> <> is required | () is optional
> ```
> ```ini
> [{prefix}destroy]                »  Destroys the server
> [{prefix}massban]                »  Bans everyone in the server
> [{prefix}dynoban]                »  Bans everyone in the server using dyno
> [{prefix}mee6ban]                »  Bans everyone in the server using dyno
> [{prefix}masskick]               »  Kicks everyone in the server
> [{prefix}massrole]               »  Mass creates roles in the server
> [{prefix}giveadmin]              »  Gives admin to message author
> [{prefix}spamchannels]           »  Mass creates channels in the server
> [{prefix}delchannels]            »  Deletes every channel in the server
> [{prefix}delroles]               »  Deletes every role in the server
> [{prefix}massunban]              »  Unbans everyone that was banned
> ```
    ''', delete_after=deleteAfter)

# Theme commands ————————————————————

@district.command()
async def themes(ctx):
    await ctx.message.delete()
    logging.info('Theme Command Executed')
    await ctx.send(f'''
> ```ini
> [ District Selfbot ] | Theme Commands
> ```
> ```ini
> <> is required | () is optional
> ```
> ```ini
> [{prefix}purble]       »  Changes the console theme to a purple ->  blue gradient
> [{prefix}pred]         »  Changes the console theme to a purple ->  red gradient
> [{prefix}breen]        »  Changes the console theme to a blue   ->  green gradient
> [{prefix}burple]       »  Changes the console theme to a blue   ->  purple gradient
> [{prefix}bite]         »  Changes the console theme to a blue   ->  white gradient
> [{prefix}reset]        »  Changes the console theme back to its original
> ```
    ''', delete_after=deleteAfter)

# Status commands ————————————————————

@district.command()
async def status(ctx):
    await ctx.message.delete()
    logging.info('Status Command Executed')
    await ctx.send(f'''
> ```ini
> [ District Selfbot ] | Status Commands
> ```
> ```ini
> <> is required | () is optional
> ```
> ```ini
> [{prefix}customstat]       »  Creates a custom animated status
> [{prefix}stopstatus]       »  Stops the custom animated status
> ```
    ''', delete_after=deleteAfter)

# Code commands ————————————————————

@district.command()
async def code(ctx):
    await ctx.message.delete()
    logging.info('Code Command Executed')
    await ctx.send(f'''
> ```ini
> [ District Selfbot ] | Code Commands
> ```
> ```ini
> <> is required | () is optional
> ```
> ```ini
> [{prefix}asciidoc <code>]       »  Sends aciidoc codeblock inclduing code
> [{prefix}bash <code>]           »  Sends bash codeblock including code
> [{prefix}css <code>]            »  Sends css codeblock including code
> [{prefix}yaml <code>]           »  Sends yaml codeblock including code
> [{prefix}js <code>]             »  Sends js codeblock including code
> [{prefix}python <code>]         »  Sends bash codeblock including code
> [{prefix}xml <code>]            »  Sends xml codeblock including code
> [{prefix}lua <code>]            »  Sends lua codeblock including code
> [{prefix}json <code>]           »  Sends json codeblock including code
> ```
    ''', delete_after=deleteAfter)



# Console commands ————————————————————

@district.command()
async def purble(ctx):
    await ctx.message.delete()
    ctypes.windll.kernel32.SetConsoleTitleW(f'District Selfbot | Version: {district_version} | Theme: Purble')
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Succesfully set console theme to purble."
    notification.icon = "./assets/district-png.ico"
    notification.audio = "sound/success.wav"
    notification.send()

    os.system('cls')
    print(Colorate.Diagonal(Colors.purple_to_blue,
    f'''
                              ╔╦╗╦╔═╗╔╦╗╦═╗╦╔═╗╔╦╗
                               ║║║╚═╗ ║ ╠╦╝║║   ║ 
                              ═╩╝╩╚═╝ ╩ ╩╚═╩╚═╝ ╩ v{district_version}
    '''))
    print(Colorate.Vertical(Colors.purple_to_blue,
    f'''
                           Connected: [ {district.user} ]

   ╔══════════════════════════════════════════════════════════════════════╗
   ║                        Commands: {len(district.commands)} | Guilds: {len(district.guilds)}                     ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║           HWID: {keyAuthApp.user_data.hwid}        ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║                    Developer: equi.ty aka equity                     ║
   ╚══════════════════════════════════════════════════════════════════════╝
    '''))
    logging.info(f'Running version {Fore.BLUE}[{Fore.RESET}{district_version}{Fore.BLUE}]{Fore.RESET}')
    logging.info(f'Type {Fore.BLUE},{Fore.RESET}help{Fore.BLUE}{Fore.RESET} to get started')
    

@district.command()
async def reset(ctx):
    await ctx.message.delete()
    ctypes.windll.kernel32.SetConsoleTitleW(f'District Selfbot | Version: {district_version} | Theme: Default')
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Succesfully reset console theme."
    notification.icon = "./assets/district-png.ico"
    notification.audio = "sound/success.wav"
    notification.send()
    os.system('cls')
    print(Colorate.Diagonal(Colors.blue_to_cyan,
    f'''
                              ╔╦╗╦╔═╗╔╦╗╦═╗╦╔═╗╔╦╗
                               ║║║╚═╗ ║ ╠╦╝║║   ║ 
                              ═╩╝╩╚═╝ ╩ ╩╚═╩╚═╝ ╩ v{district_version}
    '''))
    print(Colorate.Vertical(Colors.blue_to_cyan,
    f'''
                           Connected: [ {district.user} ]

   ╔══════════════════════════════════════════════════════════════════════╗
   ║                        Commands: {len(district.commands)} | Guilds: {len(district.guilds)}                     ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║           HWID: {keyAuthApp.user_data.hwid}        ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║                    Developer: equi.ty aka equity                     ║
   ╚══════════════════════════════════════════════════════════════════════╝
    '''))
    logging.info(f'Running version {Fore.BLUE}[{Fore.RESET}{district_version}{Fore.BLUE}]{Fore.RESET}')
    logging.info(f'Type {Fore.BLUE},{Fore.RESET}help{Fore.BLUE}{Fore.RESET} to get started')



@district.command()
async def pred(ctx):
    await ctx.message.delete()
    ctypes.windll.kernel32.SetConsoleTitleW(f'District Selfbot | Version: {district_version} | Theme: Pred')
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Succesfully set console theme to pred."
    notification.icon = "./assets/district-png.ico"
    notification.audio = "sound/success.wav"
    notification.send()
    os.system('cls')
    print(Colorate.Diagonal(Colors.purple_to_red,
    f'''
                              ╔╦╗╦╔═╗╔╦╗╦═╗╦╔═╗╔╦╗
                               ║║║╚═╗ ║ ╠╦╝║║   ║ 
                              ═╩╝╩╚═╝ ╩ ╩╚═╩╚═╝ ╩ v{district_version}
    '''))
    print(Colorate.Vertical(Colors.purple_to_red,
    f'''
                           Connected: [ {district.user} ]

   ╔══════════════════════════════════════════════════════════════════════╗
   ║                        Commands: {len(district.commands)} | Guilds: {len(district.guilds)}                     ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║           HWID: {keyAuthApp.user_data.hwid}        ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║                    Developer: equi.ty aka equity                     ║
   ╚══════════════════════════════════════════════════════════════════════╝
    '''))
    logging.info(f'Running version {Fore.BLUE}[{Fore.RESET}{district_version}{Fore.BLUE}]{Fore.RESET}')
    logging.info(f'Type {Fore.BLUE},{Fore.RESET}help{Fore.BLUE}{Fore.RESET} to get started')



@district.command()
async def breen(ctx):
    await ctx.message.delete()
    ctypes.windll.kernel32.SetConsoleTitleW(f'District Selfbot | Version: {district_version} | Theme: Breen')
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Succesfully set console theme to breen."
    notification.icon = "./assets/district-png.ico"
    notification.audio = "sound/success.wav"
    notification.send()
    os.system('cls')
    print(Colorate.Diagonal(Colors.blue_to_green,
    f'''
                              ╔╦╗╦╔═╗╔╦╗╦═╗╦╔═╗╔╦╗
                               ║║║╚═╗ ║ ╠╦╝║║   ║ 
                              ═╩╝╩╚═╝ ╩ ╩╚═╩╚═╝ ╩ v{district_version}
    '''))
    print(Colorate.Vertical(Colors.blue_to_green,
    f'''
                           Connected: [ {district.user} ]

   ╔══════════════════════════════════════════════════════════════════════╗
   ║                        Commands: {len(district.commands)} | Guilds: {len(district.guilds)}                     ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║           HWID: {keyAuthApp.user_data.hwid}        ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║                    Developer: equi.ty aka equity                     ║
   ╚══════════════════════════════════════════════════════════════════════╝
    '''))
    logging.info(f'Running version {Fore.BLUE}[{Fore.RESET}{district_version}{Fore.BLUE}]{Fore.RESET}')
    logging.info(f'Type {Fore.BLUE},{Fore.RESET}help{Fore.BLUE}{Fore.RESET} to get started')


@district.command()
async def bred(ctx):
    await ctx.message.delete()
    ctypes.windll.kernel32.SetConsoleTitleW(f'District Selfbot | Version: {district_version} | Theme: Bred')
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Succesfully set console theme to bred."
    notification.icon = "./assets/district-png.ico"
    notification.audio = "sound/success.wav"
    notification.send()
    os.system('cls')
    print(Colorate.Diagonal(Colors.blue_to_red,
    f'''
                              ╔╦╗╦╔═╗╔╦╗╦═╗╦╔═╗╔╦╗
                               ║║║╚═╗ ║ ╠╦╝║║   ║ 
                              ═╩╝╩╚═╝ ╩ ╩╚═╩╚═╝ ╩ v{district_version}
    '''))
    print(Colorate.Vertical(Colors.blue_to_red,
    f'''
                           Connected: [ {district.user} ]

   ╔══════════════════════════════════════════════════════════════════════╗
   ║                        Commands: {len(district.commands)} | Guilds: {len(district.guilds)}                     ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║           HWID: {keyAuthApp.user_data.hwid}        ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║                    Developer: equi.ty aka equity                     ║
   ╚══════════════════════════════════════════════════════════════════════╝
    '''))
    logging.info(f'Running version {Fore.BLUE}[{Fore.RESET}{district_version}{Fore.BLUE}]{Fore.RESET}')
    logging.info(f'Type {Fore.BLUE},{Fore.RESET}help{Fore.BLUE}{Fore.RESET} to get started')



@district.command()
async def burple(ctx):
    await ctx.message.delete()
    ctypes.windll.kernel32.SetConsoleTitleW(f'District Selfbot | Version: {district_version} | Theme: Burple')
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Succesfully set console theme to burple."
    notification.icon = "./assets/district-png.ico"
    notification.audio = "sound/success.wav"
    notification.send()
    os.system('cls')
    print(Colorate.Diagonal(Colors.blue_to_purple,
    f'''
                              ╔╦╗╦╔═╗╔╦╗╦═╗╦╔═╗╔╦╗
                               ║║║╚═╗ ║ ╠╦╝║║   ║ 
                              ═╩╝╩╚═╝ ╩ ╩╚═╩╚═╝ ╩ v{district_version}
    '''))
    print(Colorate.Vertical(Colors.blue_to_purple,
    f'''
                           Connected: [ {district.user} ]

   ╔══════════════════════════════════════════════════════════════════════╗
   ║                        Commands: {len(district.commands)} | Guilds: {len(district.guilds)}                     ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║           HWID: {keyAuthApp.user_data.hwid}        ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║                    Developer: equi.ty aka equity                     ║
   ╚══════════════════════════════════════════════════════════════════════╝
    '''))
    logging.info(f'Running version {Fore.BLUE}[{Fore.RESET}{district_version}{Fore.BLUE}]{Fore.RESET}')
    logging.info(f'Type {Fore.BLUE},{Fore.RESET}help{Fore.BLUE}{Fore.RESET} to get started')


@district.command()
async def bite(ctx):
    await ctx.message.delete()
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Succesfully set console theme to bite.."
    notification.icon = "./assets/district-png.ico"
    notification.audio = "sound/success.wav"
    notification.send()
    ctypes.windll.kernel32.SetConsoleTitleW(f'District Selfbot | Version: {district_version} | Theme: Bite')
    os.system('cls')
    print(Colorate.Diagonal(Colors.blue_to_white,
    f'''
                              ╔╦╗╦╔═╗╔╦╗╦═╗╦╔═╗╔╦╗
                               ║║║╚═╗ ║ ╠╦╝║║   ║ 
                              ═╩╝╩╚═╝ ╩ ╩╚═╩╚═╝ ╩ v{district_version}
    '''))
    print(Colorate.Vertical(Colors.blue_to_white,
    f'''
                           Connected: [ {district.user} ]

   ╔══════════════════════════════════════════════════════════════════════╗
   ║                        Commands: {len(district.commands)} | Guilds: {len(district.guilds)}                     ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║           HWID: {keyAuthApp.user_data.hwid}        ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║                    Developer: equi.ty aka equity                     ║
   ╚══════════════════════════════════════════════════════════════════════╝
    '''))
    logging.info(f'Running version {Fore.BLUE}[{Fore.RESET}{district_version}{Fore.BLUE}]{Fore.RESET}')
    logging.info(f'Type {Fore.BLUE},{Fore.RESET}help{Fore.BLUE}{Fore.RESET} to get started')


@district.command()
async def clear(ctx):
    try:
        await ctx.message.delete()
        intro()
        ctypes.windll.kernel32.SetConsoleTitleW(f'District Selfbot | Version: {district_version} | Theme: Default')
        notification = Notify()
        notification.title = f"District Selfbot"
        notification.message = f"Succesfully cleared console."
        notification.icon = "./assets/district-png.ico"
        notification.audio = "sound/success.wav"
        notification.send()
    except Exception as e:
        print(e)


# Moderation commands ————————————————————

@district.command()
async def ban(ctx, member:discord.Member=None, * , reason=None):
    await ctx.message.delete()
    logging.info('Ban Command Executed')
    if member == None:
        DistrictError()
    await member.ban(reason=reason)
    await ctx.send(f'> **Succesfully Banned** `{member}`')


@district.command()
async def unban(ctx, userid):
    await ctx.message.delete()
    logging.info('Unban Command Executed')
    if userid == None:
        DistrictError()

    user = discord.Object(id=userid)
    await ctx.guild.unban(user)
    await ctx.send(f'> **Succesfully Unbanned** `{userid}`')


@district.command()
async def kick(ctx, member:discord.Member=None, *, reason=None):
    await ctx.message.delete()
    logging.info('Kick Command Executed')
    if member == None:
        DistrictError()
    await member.kick(reason=reason)
    await ctx.send(f'> **Succesfully Kicked** `{member}`')


@district.command()
async def mute(ctx, member: discord.Member=None, *, reason=None):
    await ctx.message.delete()
    logging.info('Mute Command Executed')
    guild = ctx.guild
    mutedRole = discord.utils.get(ctx.guild.roles, name="MutedDistrict")

    if member == None:
        DistrictError()

    if not mutedRole:
        mutedRole = await guild.create_role(name="MutedDistrict")

        for channel in ctx.guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f'> **Succesfully Muted** `{member}`')


@district.command()
async def unmute(ctx, member: discord.Member):
    await ctx.message.delete()
    logging.info(f'Unmute Command Executed')
    mutedRole = discord.utils.get(ctx.guild.roles, name="MutedDistrict")
    if member == None:
        DistrictError()

    await member.remove_roles(mutedRole)
    await ctx.send(f'> **Succesfully Unmuted** `{member}`')


@district.command()
async def purge(ctx, amount=0):
    await ctx.message.delete()
    logging.info('Purge Command Executed')
    if amount == 0:
        DistrictError()
    else:
        await ctx.channel.purge(limit=amount)
        prgmsg = await ctx.send(f'> **Succesfully Purged** `{amount}` **messages**')
        await asyncio.sleep(5)
        await prgmsg.delete()

@district.command()
async def nuke(ctx):
    await ctx.message.delete()
    logging.info('Nuke Command Executed')
    channel_info = [ctx.channel.category, ctx.channel.position]
    await ctx.channel.clone()
    await ctx.channel.delete()
    new_channel = channel_info[0].text_channels[-1]
    await new_channel.edit(position=channel_info[1])
    await new_channel.send(f'> **Succesfully Nuked** `{ctx.channel.name}`')

@district.command()
async def offslowmode(ctx):
    await ctx.message.delete()
    logging.info('OffSlowmode Command Executed')
    await ctx.channel.edit(slowmode_delay=0)
    await ctx.send(f'> **Succesfully Turned Off Slowmode**')


@district.command()
async def slowmode(ctx, seconds: int):
    await ctx.message.delete()
    logging.info('Slowmode Command Executed')
    if seconds == None:
        DistrictError()

    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f'> **Succesfully Set Slowmode To** `{seconds}s`')


@district.command()
async def jail(ctx, member: discord.Member):
    await ctx.message.delete()
    logging.info('Jail Command Executed')
    guild = ctx.guild
    jailedRole = discord.utils.get(ctx.guild.roles, name='PrisonerDistrict')
    if member == None:
        DistrictError()

    if not jailedRole:
        jailedRole = await guild.create_role(name="PrisonerDistrict")
        for channel in ctx.guild.channels:
            await channel.set_permissions(jailedRole, speak=False, send_messages=False, read_message_history=False, read_messages=False)

    await member.add_roles(jailedRole)
    await ctx.send(f'> **Succesfully Jailed** `{member}`')



@district.command()
async def unjail(ctx, member: discord.Member):
    await ctx.message.delete()
    logging.info(f'Unjail Command Executed')
    jailedRole = discord.utils.get(ctx.guild.roles, name='PrisonerDistrict')
    if member == None:
        DistrictError()

    await member.remove_roles(jailedRole)
    await ctx.send(f'> **Succesfully Unjailed** `{member}`')


@district.command()
async def lock(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    logging.info('Lock Command Executed')
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f'> **Succesfully Locked** `{channel}`')
    

@district.command()
async def unlock(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    logging.info('Unlock Command Executed')
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f'> **Succesfully Unlocked** `{channel}`')

# Utility commands ————————————————————

@district.command(aliases=['cc'])
async def commandcount(ctx):
    await ctx.message.delete()
    logging.info('Commandcount Command Executed')
    await ctx.send(f'> **Commands:** `{len(district.commands)}`')


@district.command(aliases=['av'])
async def avatar(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    logging.info('Avatar Command Executed')
    if user is None:
        user = ctx.message.author
    embed=discord.Embed(color=0x2f3136, title=f"{user.name}'s avatar", url=user.display_avatar.url)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
    embed.set_image(url=user.display_avatar.url)
    await ctx.reply(embed=embed)


@district.command(aliases=['rpc'])
async def richpresence(ctx, toggle: str):
    await ctx.message.delete()
    logging.info('Richpresence Command Executed')
    if toggle == "on" and richPresence == "False":
            richPresence = "True"
            notification = Notify()
            notification.title = f"District Selfbot"
            notification.message = f"Succesfully enabled rpc."
            notification.icon = "./assets/district-png.ico"
            notification.audio = "sound/success.wav"
            notification.send()

    if toggle == "off" and richPresence == "True":
            richPresence = "False"
            notification = Notify()
            notification.title = f"District Selfbot"
            notification.message = f"Succesfully disabled rpc."
            notification.icon = "./assets/district-png.ico"
            notification.audio = "sound/success.wav"
            notification.send()

    elif toggle == "on" and richPresence == "True":
            notification = Notify()
            notification.title = f"District Selfbot"
            notification.message = f"RPC is already enabled."
            notification.icon = "./assets/district-png.ico"
            notification.audio = "sound/error.wav"
            notification.send()

    elif toggle == "off" and richPresence == "False":
            notification = Notify()
            notification.title = f"District Selfbot"
            notification.message = f"RPC is already disabled."
            notification.icon = "./assets/district-png.ico"
            notification.audio = "sound/error.wav"
            notification.send()

    else:
        logging.info('Invalid toggle method.')

@district.command()
async def serverid(ctx):
    await ctx.message.delete()
    logging.info('Guild ID Command Executed')
    await ctx.send(f"> **Guild ID**: `{ctx.guild.id}`")


@district.command(aliases=["memberid"])
async def userid(ctx, member:discord.Member=None):
    await ctx.message.delete()
    logging.info('User ID Command Executed')
    member = ctx.author if not member else member
    await ctx.send(f"> **{member.name}'s ID:** `{member.id}`")



@district.command(aliases=['sicon'])
async def servericon(ctx):
    await ctx.message.delete()
    logging.info('Servericon Command Executed')
    guild = ctx.message.guild
    embed = discord.Embed(title=f'{ctx.guild.name}\'s icon', color=0x2f3136)
    embed.set_image(url=ctx.guild.icon)
    await ctx.reply(embed=embed) 


@district.command()
async def serverbanner(ctx):
    await ctx.message.delete()
    logging.info(f'Serverbanner Command Executed')
    if ctx.guild.banner == None:
        DistrictError()
    else:
        embed = discord.Embed(title=f'{ctx.guild.name}\'s banner', color=0x2f3136)
        embed.set_image(url=ctx.guild.banner.url)
        await ctx.send(embed=embed) 


@district.command()
async def serverinfo(ctx):
    await ctx.message.delete()
    logging.info('Serverinfo Command Executed')
    guild = ctx.message.guild
    total_bots = len([member for member in guild.members if member.bot == True])
    text_channels = len(ctx.guild.text_channels)
    voice_channel = len(ctx.guild.voice_channels)
    await ctx.send(f'''
    > __**{guild.name}** **Server Info**__
    > ```
    > Owner          »  {str(guild.owner)}
    > Boost Count    »  {guild.premium_subscription_count}
    > Role Count     »  {len(guild.roles)}
    > Members        »  {len(guild.members)}
    > Bot Count      »  {total_bots}
    > Channels       »  {text_channels}
    > Voice Channels »  {voice_channel}
    > ```
    ''', delete_after=deleteAfter)

@district.command()
async def userinfo(ctx, user: str=None):
    await ctx.message.delete()
    logging.info(f'Userinfo Command Executed')
    if user is None:
        member = ctx.author
    embed = discord.Embed(color=0x2f3136)
    embed.add_field(name='Created Account', value=f"`{member.created_at.strftime('%d %B %Y')}`")
    embed.add_field(name='Joined', value=f"`{member.joined_at.strftime('%d %B %Y')}`")
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in member.guild_permissions if p[1]])
    embed.add_field(name="Guild permissions", value=f'```{perm_string}```', inline=False)
    embed.set_thumbnail(url=member.display_avatar)
    embed.set_author(name=f'{member.name}', icon_url=member.display_avatar)
    await ctx.send(embed=embed)

@district.command()
async def poll(ctx, *, message):
    await ctx.message.delete()
    logging.info(f'Poll Command Executed')
    message = await ctx.send(f"```{message} | {ctx.message.author}```")
    await message.add_reaction('👍')
    await message.add_reaction('👎')

@district.command()
async def membercount(ctx):
    await ctx.message.delete()
    logging.info(f'Membercount Command Executed')
    await ctx.send(f"``{ctx.guild.name}` **has** `{ctx.guild.member_count}` **members**")


@district.command()
async def invites(ctx, member: discord.Member = None):
    await ctx.message.delete()
    logging.info(f'Invites Command Executed')
    totalInvites = 0
    if member == None:
        member = ctx.author
    for i in await ctx.guild.invites():
        if i.inviter == member:
            totalInvites += i.uses
    if member == ctx.author:
            await ctx.send("> **you've invited** `%s` **member(s) to the server**" % (totalInvites))
    else:
        await ctx.send(">  `%s` **has invited** `%s` **member(s) to the server**" % (member.name, totalInvites))


@district.command()
async def addrole(ctx, member: discord.Member, role: discord.Role):
    await ctx.message.delete()
    logging.info(f'Addrole Command Executed')
    await member.add_roles(role)
    await ctx.send(f"> **Succesfully Added** `{role.name}` **To** `{member.name}`")

@district.command()
async def derole(ctx, member: discord.Member, role: discord.Role):
    await ctx.message.delete()
    logging.info(f'Derole Command Executed')
    await member.remove_roles(role)
    await ctx.send(f"> **Succesfully Removed** `{role.name}` **From** `{member.name}`")

@district.command()
async def emojiadd(ctx, emote):
    await ctx.message.delete()
    logging.info(f'Emojiadd Command Executed')
    try:
        if emote[0] == '<':
            name = emote.split(':')[1]
            emoji_name = emote.split(':')[2][:-1]
            anim = emote.split(':')[0]
            if anim == '<a':
                url = f'https://cdn.discordapp.com/emojis/{emoji_name}.gif'
            else:
                url = f'https://cdn.discordapp.com/emojis/{emoji_name}.png'
            try:
                response = requests.get(url) 
                img = response.content
                emote = await ctx.guild.create_custom_emoji(name=name, image=img) 
                return await ctx.send("> **Succesfully Added** %s" % (emote))
            except Exception:
                DistrictError()
        else:
            DistrictError()
    except Exception:
        DistrictError()



@district.command()
async def afk(ctx, mins, reason=None):
    await ctx.message.delete()
    logging.info(f'AFK Command Executed')
    current_nick = ctx.author.nick
    await ctx.send("{0.author.mention} **has gone afk for** `{1}` **minutes(s)**.".format(ctx, mins))
    await ctx.author.edit(nick=f"[AFK] {ctx.author.name}")

    counter = 0
    while counter <= int(mins):
        counter += 1
        await asyncio.sleep(60)

        if counter == int(mins):
            await ctx.author.edit(nick=current_nick)
            await ctx.send(f"{ctx.author.mention} **is no longer AFK*")
            break

@district.command(aliases=['bitcoin'])
async def btc(ctx):
    await ctx.message.delete()
    logging.info(f'Bitcoin Command Executed')
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    await ctx.send(f'> **USD** `${str(usd)}`\n> **EUR** `${str(eur)}`')

@district.command() 
async def roleinfo(ctx, *, role: discord.Role=None):
    await ctx.message.delete()
    logging.info(f'Roleinfo Command Executed')
    if role == None:
        DistrictError()
    perms = role.permissions
    members = len([x for x in ctx.guild.members if role in x.roles])
    if perms.value == 0: 
        msg = f"{role.name} **has no permissions**"
    else:
        msg = " ".join([x[0].replace("_", " ").title() for x in filter(lambda p: p[1] == True, perms)])
    if role.hoist:
        hoist = "yes"
    else:
        hoist = "no"
    if role.mentionable:
        mention = "yes"
    else:
        mention = "no"
    await ctx.send(
    f'''
    > __**{role.name} Role Info**__
    > ```  
    > mentionable     »   {mention}
    > role count      »   {role.colour}
    > user count      »   {members}
    > hoisted         »   {hoist}
    > role id         »   {role.id}
    > role perms 
    > ```
    > ```{msg}```
    ''', delete_after=deleteAfter)


@district.command()
async def permissions(ctx, *, user: discord.Member=None):
    await ctx.message.delete()
    logging.info(f'Permissions Command Executed')
    author = ctx.message.author
    if not user:
        user = author
    perms = "\n".join([x[0].replace("_", " ").title() for x in filter(lambda p: p[1] == True, user.guild_permissions)])
    await ctx.send(f'''
> __**{user.name}'s Permissions**__
> ```{perms}```
    ''', delete_after=deleteAfter)

# Abuse commands ————————————————————

@district.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    logging.info(f'Spam Command Executed')
    for _i in range(amount):
        await ctx.send(message)



@district.command(aliases=["rekt", "smoke"])
async def destroy(ctx):
    await ctx.message.delete()
    logging.info( f'Destroy Command Executed')
    for user in list(ctx.guild.members):
        try:
            await user.ban()
            logging.info( f'Succesfully Banned {user.name}')
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            logging.info( f'Succesfully Deleted {channel.name}')
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            logging.info( f'Succesfully Deleted {role.name}')
        except:
            pass
    try:
        await ctx.guild.edit(
            name=guildName,
            description="district was here",
            reason=reason,
            icon=None,
            banner=None
        )
        logging.info( f'Succesfully Edited Guild')
    except:
        pass
    for _i in range(150):
        await ctx.guild.create_text_channel(name=chanName)
        logging.info( f'Succesfully Created {channel.name}')
    for _i in range(150):
        await ctx.guild.create_role(name=roleName)
        logging.info( f'Succesfully Created {role.name}')



@district.command(aliases=["banwave", "banall", "pack"])
async def massban(ctx):
    await ctx.message.delete()
    logging.info( f'Massban Command Executed')
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason=reason)
            logging.info( f'Succesfully Banned {user.name}')
        except:
            pass

@district.command()
async def mee6(ctx):
    await ctx.message.delete()
    logging.info( f'MEE6ban Command Executed')
    for member in list(ctx.guild.members):
        message = await ctx.send("!ban " + member.mention)
        await message.delete()
        await asyncio.sleep(1.5)
        logging.info( f'Succesfully MEE6banned {member.name}')

@district.command()
async def dynoban(ctx):
    await ctx.message.delete()
    logging.info( f'Dynoban Command Executed')
    for member in list(ctx.guild.members):
        message = await ctx.send("?ban " + member.mention)
        await message.delete()
        await asyncio.sleep(1.5)
        logging.info( f'Succesfully Dynobanned {member.name}')


@district.command(aliases=["kickall", "kickwave"])
async def masskick(ctx):
    await ctx.message.delete()
    logging.info( f'Masskick Command Executed')
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason=reason)
            logging.info( f'Succesfully Kicked {user.name}')
        except:
            pass


@district.command(aliases=["spamroles", "massroles", "addroles"])
async def massrole(ctx):
    await ctx.message.delete()
    logging.info( f'Massrole Command Executed')
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=random.choice(roleName))
            logging.info( f'Succesfully Created Role {roleName}')
        except:
            try:
                await ctx.guild.create_role(name=random.choice(roleName))
                logging.info( f'Succesfully Created Role {roleName}')
            except:
                return


@district.command(aliases=["givemeadmin", "giveadminrole", "giveadminroles"])
async def giveadmin(ctx):
    await ctx.message.delete()
    logging.info( f'Giveadmin Command Executed')
    for role in ctx.guild.roles:
        try:
            if role.permissions.administrator:
                await ctx.author.add_roles(role)
                logging.info( f'Succesfully Gave Admin To {ctx.author.name}')
        except:
            pass


@district.command(aliases=["masschannels", "masschannel", "ctc"])
async def spamchannels(ctx):
    await ctx.message.delete()
    logging.info( f'Spamchannels Command Executed')
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name=random.choice(chanName))
            logging.info( f'Succesfully Created Channel {chanName}')
        except:
            return


@district.command(aliases=["delchannel"])
async def delchannels(ctx):
    await ctx.message.delete()
    logging.info( f'Deletechannels Command Executed')
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            logging.info( f'Succesfully Deleted Channel {channel.name}')
        except:
            return


@district.command(aliases=["deleteroles"])
async def delroles(ctx):
    await ctx.message.delete()
    logging.info( f'Deleteroles Command Executed')
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            logging.info( f'Succesfully Deleted Role {role.name}')
        except:
            pass


@district.command(aliases=["purgebans", "unbanall"])
async def massunban(ctx):
    await ctx.message.delete()
    logging.info( f'Massunban Command Executed')
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
            logging.info( f'Succesfully Unbanned {users.name}')
            await ctx.send(f'> **Succesfully Unbanned All Users**')
        except:
            pass

@district.command()
async def massping(ctx,):
    await ctx.message.delete()
    logging.info('Massping Command Executed')
    for member in list(ctx.guild.members):
        message = await ctx.send(member.mention)
        await message.delete()
        await asyncio.sleep(0.5)

# Account commands ————————————————————

@district.command()
async def restart(ctx):
    await ctx.message.delete()
    logging.info('Restart Command Executed')
    cmd = "mode 80,20"
    os.system(cmd)
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Restarting..."
    notification.icon = "./assets/district-png.ico"
    notification.audio = "sound/success.wav"
    notification.send()
    DistrictRestart()

@district.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house):
    await ctx.message.delete()
    logging.info(f'Hypesquad Command Executed')
    request = requests.Session()
    headers = {
        'Authorization': Token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if house == "bravery":
        payload = {'house_id': 1}
    elif house == "brilliance":
        payload = {'house_id': 2}
    elif house == "balance":
        payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v8/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(e)

@district.command()
async def logout(ctx):
    await ctx.message.delete()
    logging.info( f'Logout Command Executed')
    await district.logout()

@district.command(name='group-leaver', aliases=['leaveallgroups', 'leavegroup', 'leavegroups', "groupleave", "groupleaver"])
async def _group_leaver(ctx):
    await ctx.message.delete()
    logging.info('Group Leaver Command Executed')
    for channel in district.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()
            logging.info(f'Succesfully Left {channel.name}')




# Troll commands ————————————————————


@district.command(name='8ball')
async def _ball(ctx, *, question):
    await ctx.message.delete()
    logging.info( f'8Ball Command Executed')
    responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'That is a definite yes!',
        'Maybe',
        'There is a good chance'
    ]
    answer = random.choice(responses)
    await ctx.send(f'> **Question** {question}\n> **Answer** {answer}')

@district.command()
async def virus(ctx):
    await ctx.message.delete()
    logging.info( f'Virus Command Executed')
    message = await ctx.send(f'''
``[▓▓▓                    ] / -virus.exe Packing files.``        
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓                ] — -virus.exe Packing files..``         
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ -virus.exe Packing files..``        
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | -virus.exe Packing files..``         
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / -virus.exe Packing files..``      
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] — -virus.exe Packing files..``    
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ -virus.exe Packing files..``   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``New file with name change, New file : district.exe``   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``Injecting virus.   |``
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``Injecting virus..  /``
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``Injecting virus... —``
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        > **Successfully Injected district.exe**
        ''')

@district.command()
async def table(ctx):
    await ctx.message.delete()
    logging.info( f'Table Command Executed')
    message = await ctx.send(f'''
`(\°-°)\  ┬─┬`       
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°□°)\  ┬─┬`       
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(-°□°)-  ┬─┬`      
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯    ]`       
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯     ┻━┻`   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯       [`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯          ┬─┬`   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯                 ]`   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯                  ┻━┻`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯                         [`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°-°)\                               ┬─┬`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°-°)\                                     ]`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°-°)\                                       ┻━┻`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°-°)\                                               [`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°-°)\                                              ┬─┬`
''')

@district.command()
async def shrug(ctx):
    await ctx.message.delete()
    logging.info(f'Shrug Command Executed')
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)


@district.command()
async def lenny(ctx):
    await ctx.message.delete()
    logging.info(f'Lenny Command Executed')
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)


@district.command(aliases=["fliptable"])
async def tableflip(ctx):
    await ctx.message.delete()
    logging.info(f'Tableflip Command Executed')
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)


@district.command()
async def unflip(ctx):
    await ctx.message.delete()
    logging.info(f'Unflip Command Executed')
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

@district.command()
async def nitro(ctx):
    await ctx.message.delete()
    logging.info(f'Nitro Command Executed')
    await ctx.send(Nitro())

@district.command()
async def gay(ctx, user: discord.User):
    await ctx.message.delete()
    logging.info(f'Gay Command Executed')
    percentage_numbers = ["0%", "1%", "5%", "10%", "15%", "20%", "25%", "30%", "35%", "40%", "45%", "50%", "55%", "60%", "65%", "70%", "75%", "80%", "85%", "90%", "95%", "100%", "∞"]
    percentage = random.choice(percentage_numbers)
    await ctx.send(f'''
        > **How gay are you or are you gay ?**
        > ```
        > {user.name} is {percentage} gay !!
        > ```
        >
        ''')



@district.command()
async def tweet(ctx, username: str = None, *, message: str = None):
    await ctx.message.delete()
    if username is None or message is None:
        DistrictError()
        logging.info(f'Tweet Command Executed')
        return
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(str(res['message'])) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, f"districttweeted.png"))
            except:
                await ctx.send(res['message'])


@district.command(aliases=["deepfry"])
async def fry(ctx, user: discord.Member = None):
    logging.info(f'Fry Command Executed')
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"districtfried.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"districtfried.png"))
        except:
            await ctx.send(res['message'])


@district.command(aliases=["img", "searchimg", "searchimage", "imagesearch", "imgsearch"])
async def image(ctx, *, args):
    logging.info(f'Image Command Executed')
    await ctx.message.delete()
    url = 'https://unsplash.com/search/photos/' + args.replace(" ", "%20")
    page = requests.get(url)
    soup = bs4(page.text, 'html.parser')
    image_tags = soup.findAll('img')
    if str(image_tags[2]['src']).find("https://trkn.us/pixel/imp/c="):
        link = image_tags[2]['src']
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(link) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(f"> **Search result for:** `{args}`", file=discord.File(file, f"districtimg.png"))
        except:
            await ctx.send(f'' + link + f"\n> **Search result for:** `{args}`")
    else:
        await ctx.send(f"> **Nothing found for** `{args}`")



@district.command()
async def copyguild(ctx):
    logging.info(f'Copyguild Command Executed')
    await ctx.message.delete()
    await district.create_guild(f'backup - {ctx.guild.name}')
    await asyncio.sleep(4)
    for g in district.guilds:
        if f'backup - {ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                        await asyncio.sleep(0.5)
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
                        await asyncio.sleep(0.5)

    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

@district.command()
async def acceptfriends(ctx):
    await ctx.message.delete()
    logging.info(f'Acceptfriends Command Executed')
    for relationship in district.user.relationships:
        if relationship == discord.RelationshipType.incoming_request:
            await relationship.accept()


@district.command()
async def ignorefriends(ctx):
    await ctx.message.delete()
    logging.info(f'Ignorefriends Command Executed')
    for relationship in district.user.relationships:
        if relationship is discord.RelationshipType.incoming_request:
            relationship.delete()


@district.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    logging.info(f'Massreact Command Executed')
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)

@district.event
async def on_message(message):
    if 'discord.gift/' in message.content:
        if nitroSniper == "True":
            code = re.search("discord.gift/(.*)", message.content).group(1)
            Token = config.get('userToken')

            headers = {'Authorization': Token}

            r = requests.post(
                f'https://discordapp.com/api/v9/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text


            if 'This gift has been redeemed already.' in r:
                logging.info(f"Nitro Code {Fore.BLUE}[{Fore.RESET} {code} {Fore.BLUE}]{Fore.RESET} was already redeemed" + Fore.RESET)
                print(f"""
                » Channel: {Fore.BLUE}[{Fore.RESET} {message.channel} {Fore.BLUE}]{Fore.RESET}
                » Server:  {Fore.BLUE}[{Fore.RESET} {message.guild} {Fore.BLUE}]{Fore.RESET}
                » Sender:  {Fore.BLUE}[{Fore.RESET} {message.author} {Fore.BLUE}]{Fore.RESET}
                » Code:    {Fore.BLUE}[{Fore.RESET} {code} {Fore.BLUE}]{Fore.RESET}
                """)

            elif 'subscription_plan' in r:
                logging.info(f"Nitro Code {Fore.BLUE}[{Fore.RESET} {code} {Fore.BLUE}]{Fore.RESET} was succesfully redeemed !" + Fore.RESET)
                print(f"""
                » Channel: {Fore.BLUE}[{Fore.RESET} {message.channel} {Fore.BLUE}]{Fore.RESET}
                » Server:  {Fore.BLUE}[{Fore.RESET} {message.guild} {Fore.BLUE}]{Fore.RESET}
                » Sender:  {Fore.BLUE}[{Fore.RESET} {message.author} {Fore.BLUE}]{Fore.RESET}
                » Code:    {Fore.BLUE}[{Fore.RESET} {code} {Fore.BLUE}]{Fore.RESET}
                """)
                DistrictSniped()

            elif 'Unknown Gift Code' in r:
                logging.info(f"Nitro Code {Fore.BLUE}[{Fore.RESET} {code} {Fore.BLUE}]{Fore.RESET} is unknown" + Fore.RESET)
                print(f"""
                » Channel: {Fore.BLUE}[{Fore.RESET} {message.channel} {Fore.BLUE}]{Fore.RESET}
                » Server:  {Fore.BLUE}[{Fore.RESET} {message.guild} {Fore.BLUE}]{Fore.RESET}
                » Sender:  {Fore.BLUE}[{Fore.RESET} {message.author} {Fore.BLUE}]{Fore.RESET}
                » Code:    {Fore.BLUE}[{Fore.RESET} {code} {Fore.BLUE}]{Fore.RESET}
                """)
        else:
            return
    await district.process_commands(message)

# Status commands ————————————————————

@district.command()
async def customstat(ctx):
    await ctx.message.delete()
    logging.info( f'Customstatus Command Executed')
    customstatus.start()

@tasks.loop(seconds=1)
async def customstatus():
    await district.change_presence(activity=discord.Game(name=stat1))
    await asyncio.sleep(1)
    await district.change_presence(activity=discord.Game(name=stat2))
    await asyncio.sleep(1)
    await district.change_presence(activity=discord.Game(name=stat3))
    await asyncio.sleep(1)

@district.command()
async def stopstatus(ctx):
    await ctx.message.delete()
    logging.info( f'Stopstatus Command Executed')
    await district.change_presence(activity=None, status=discord.Status.offline)

@district.command(aliases=["stream"])
async def watching(ctx, *, message):
    await ctx.message.delete()
    logging.info(f'Stream Command Executed')
    stream = discord.Streaming(
        name=message,
        url=stream_url,
    )
    await district.change_presence(activity=stream, status=discord.Status.dnd)


@district.command(alises=["game"])
async def playing(ctx, *, message):
    await ctx.message.delete()
    logging.info(f'Playing Command Executed')
    game = discord.Game(
        name=message
    )
    await district.change_presence(activity=game, status=discord.Status.dnd)


@district.command(aliases=["listen"])
async def listening(ctx, *, message):
    await ctx.message.delete()
    logging.info(f'Listening Command Executed')
    await district.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))

@district.command(aliases=["stopstreaming", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.message.delete()
    logging.info(f'StopActivity Command Executed')
    await district.change_presence(activity=None, status=discord.Status.dnd)

# Code commands ————————————————————

@district.command()
async def asciidoc(ctx, code: str):
    await ctx.message.delete()
    logging.info('Asciidoc Command Executed')
    await ctx.send(f'''
```asciidoc
{code}```
    ''')

@district.command()
async def bash(ctx, code: str):
    await ctx.message.delete()
    logging.info('Bash Command Executed')
    await ctx.send(f'''
```bash
{code}```
    ''')

@district.command()
async def css(ctx, code: str):
    await ctx.message.delete()
    logging.info('Css Command Executed')
    await ctx.send(f'''
```css
{code}```
    ''')

@district.command()
async def yaml(ctx, code: str):
    await ctx.message.delete()
    logging.info('YAML Command Executed')
    await ctx.send(f'''
```yaml
{code}```
    ''')

@district.command()
async def lua(ctx, code: str):
    await ctx.message.delete()
    logging.info('Lua Command Executed')
    await ctx.send(f'''
```lua
{code}```
    ''')

@district.command()
async def js(ctx, code: str):
    await ctx.message.delete()
    logging.info('JS Command Executed')
    await ctx.send(f'''
```js
{code}```
    ''')

@district.command()
async def python(ctx, code: str):
    await ctx.message.delete()
    logging.info('Python Command Executed')
    await ctx.send(f'''
```
py
{code}```
    ''')

@district.command()
async def xml(ctx, code: str):
    await ctx.message.delete()
    logging.info('XML Command Executed')
    await ctx.send(f'''
```xml
{code}```
    ''')

@district.command()
async def json(ctx, code: str):
    await ctx.message.delete()
    logging.info('JSON Command Executed')
    await ctx.send(f'''
```asciidoc
{code}```
    ''')

district.run(Token, bot=False, reconnect=True)
# Hello, thanks for buying District, you finally managed to deobfuscate the .exe file.

#MIT License
# ————————————————————
#Copyright (c) 2023 khai/kh/sanity

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
# ————————————————————

# District was heavily inspired by ethone.cc and nighty.one

# Enjoy.


# Installation and importing of requirements ————————————————————

import os
import logging
import json
import discord
import asyncio
import time
import requests
import io
import time
import subprocess
import ctypes
import openai
import string
import sys
import notifypy
import pystray
import PIL.Image
import threading
import pyPrivnote as pn
import urllib
import hashlib
import re
import random
import aiohttp

from subprocess import Popen
from subprocess import call
from pystyle import Colors, Colorate
from keyauth import api
from discord.ext import tasks
from wintoast import ToastNotifier
from datetime import datetime
from threading import Thread
from datetime import datetime
from bs4 import BeautifulSoup as bs4
from colorama import Fore
from itertools import cycle
from notifypy import Notify
from pypresence import Presence 
from discord.ext import commands

# License key authentication system ————————————————————

def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest


keyAuthApp = api(
    name = "DistrictSB",
    ownerid = "LihrBEWGYz",
    secret = "8a0a956bdb0bb77e25e2800fc04622fb54e9824d2901995f8a0948b33c7b3c58",
    version = "1.0",
    hash_to_check = getchecksum()
)


# Checking and installation of discord version that supports selfbots ————————————————————

def discordVersion():
    if(not discord.__version__ in ['1.7.0', '1.7.3']):
        logging.info('[!] Installing Discord.Py, v1.7.3')
        os.system('pip install -U discord.py==1.7.3')
    else:
        pass

# Restart function ————————————————————

def DistrictRestart():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# Toast functions ————————————————————

def DistrictNoCommand():
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Command not found."
    notification.icon = "assets/district-png.ico"
    notification.audio = "sound/error.wav"
    notification.send()
    
def DistrictConnected():
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Connected as: {district.user} | Version {district_version}"
    notification.icon = "assets/district-png.ico"
    notification.audio = "sound/connected.wav"
    notification.send()

def DistrictSniped():
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Succesfully sniped a nitro code !!"
    notification.icon = "assets/district-png.ico"
    notification.audio = "sound/sniped.wav"
    notification.send()

def DistrictError():
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Ensure the command executed was used appropriately to prevent errors."
    notification.icon = "assets/district-png.ico"
    notification.audio = "sound/error.wav"
    notification.send()



 # Importing from config.json ————————————————————

with open('core/config.json') as f:
    config = json.load(f)

Token = config.get('userToken')

stream_url = config.get('streamUrl')
guildName = config.get('guildName')
roleName = config.get('roleName')
chanName = config.get('chanName')

reason = config.get('reason')

prefix = config.get('prefix')

stat1 = config.get('stat1')
stat2 = config.get('stat2')
stat3 = config.get('stat3')

oneTimeLicense = config.get('oneTimeLicense')
oneLicenseKey = config.get('oneLicenseKey')

richPresence = config.get('richPresence')

deleteAfter = config.get('deleteAfter')

nitroSniper = config.get('nitroSniper')

# Defining the variable toaster ————————————————————

toaster = ToastNotifier()

# Basic discord stuff required for selfbot to run ————————————————————

intents = discord.Intents.all()
intents.members = True
district_version = 1.5
district = commands.Bot(command_prefix=prefix, case_insensitive=False, intents=intents, self_bot=True)
district.remove_command("help")

# Console stuff ————————————————————

ctypes.windll.kernel32.SetConsoleTitleW(f'District Selfbot | Version: {district_version} | Theme: Default')
os.system('mode 80, 20')

# Logging ————————————————————

logging.basicConfig(
    level=logging.INFO,
    format=f"» {Fore.BLUE}[{Fore.RESET} %(asctime)s {Fore.BLUE}] | {Fore.RESET}%(message)s ",
    datefmt="%H:%M:%S"
)

'''
# Sid Lock ————————————————————

hwid = keyAuthApp.user_data.hwid
token = win32security.OpenProcessToken(win32api.GetCurrentProcess(),win32security.TOKEN_QUERY)
sid = win32security.GetTokenInformation(token,win32security.TokenUser)[0]
sid_str = win32security.ConvertSidToStringSid(sid)
'''

        
# Using rich presence ————————————————————

if richPresence == "True":
    RPC = Presence('1071761243314081893')
    RPC.connect()
    RPC.update(details="Connected", large_image="logo", small_image="logo", large_text=f"District v{district_version}", small_text="discord.gg/enhancing", start=time.time(), buttons=[{"label": "Discord", "url": "https://discord.gg/enhancing"}, {"label": "Website", "url": "https://district.com"}])

else:
    pass



# Intro to be shown after login and authentication stuff ————————————————————



def intro():
    os.system('cls')
    print(Colorate.Diagonal(Colors.blue_to_cyan,
    f'''
                              ╔╦╗╦╔═╗╔╦╗╦═╗╦╔═╗╔╦╗
                               ║║║╚═╗ ║ ╠╦╝║║   ║ 
                              ═╩╝╩╚═╝ ╩ ╩╚═╩╚═╝ ╩ v{district_version}
    '''))
    print(Colorate.Vertical(Colors.blue_to_cyan,
    f'''
                           Connected: [ {district.user} ]

   ╔══════════════════════════════════════════════════════════════════════╗
   ║                        Commands: {len(district.commands)} | Guilds: {len(district.guilds)}                     ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║           HWID: {keyAuthApp.user_data.hwid}        ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║                    Developer: equi.ty aka equity                     ║
   ╚══════════════════════════════════════════════════════════════════════╝
    '''))
    logging.info(f'Running version {Fore.BLUE}[{Fore.RESET}{district_version}{Fore.BLUE}]{Fore.RESET}')
    logging.info(f'Type {Fore.BLUE},{Fore.RESET}help{Fore.BLUE}{Fore.RESET} to get started')


if oneTimeLicense == "True":
    authKey = oneLicenseKey
    os.system('cls')
    logging.info(Colorate.Diagonal(Colors.blue_to_cyan, 'Validating license key...'))
    os.system('cls')
    keyAuthApp.license(authKey)
    @district.event
    async def on_ready():
        discordVersion()
        os.system('cls')
        intro()
        DistrictConnected()


else:
    authKey = input(Colorate.Diagonal(Colors.blue_to_cyan, '[?] Enter license key: '))
    os.system('cls')
    logging.info(Colorate.Diagonal(Colors.blue_to_cyan, 'Validating license key...'))
    keyAuthApp.license(authKey)
    os.system('cls')
    intro()
    DistrictConnected()



# Command not found error handler ————————————————————

@district.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.delete()
        DistrictNoCommand()

# Commands ————————————————————

# Help commands ————————————————————

@district.command()
async def help(ctx):
    await ctx.message.delete()
    logging.info('Help Command Executed')
    await ctx.send(f'''
> ```ini
> [ District Selfbot ] | Help Command
> ```
> ```ini
> <> is required | () is optional
> ```
> ```ini
> [{prefix}moderation]    »  Shows the moderation commands
> [{prefix}utility]       »  Shows available utility commands
> [{prefix}account]       »  Shows account related commands
> [{prefix}troll]         »  Shows the available trolling commands
> [{prefix}abuse]         »  Shows all the raiding comamnds
> [{prefix}code]          »  Shows all available code commands
> [{prefix}themes]        »  Shows all available console themes and their commands
> [{prefix}status]        »  Shows all available status commands
> ```
    ''', delete_after=deleteAfter)

# Moderation commands ————————————————————

@district.command()
async def moderation(ctx):
    await ctx.message.delete()
    logging.info('Moderation Command Executed')
    await ctx.send(f'''
> ```ini
> [ District Selfbot ] | Moderation Commands
> ```
> ```ini
> <> is required | () is optional
> ```
> ```ini
> [{prefix}ban <@user>]                     » Bans the mentioned user
> [{prefix}unban <ID>]                      » Bans the mentioned user
> [{prefix}kick <@user>]                    » Kicks the mentioned user
> [{prefix}mute <@user>]                    » Mutes the mentioned user
> [{prefix}unmute <@user>]                  » Unmutes the mentioned user
> [{prefix}slowmode <seconds>]              » Sets the channel slowmode
> [{prefix}slowmodeoff]                     » Removes the channel slowmode
> [{prefix}jail <@user>]                    » Jails the mentioned user
> [{prefix}unjail <@user>]                  » Unjails the mentioned user
> [{prefix}lock <#channel> (#channel)]      » Locks the mentioned channel
> [{prefix}purge <amount>]                  » Purges an amount of messages
> [{prefix}unlock <#channel> (#channel)]    » Unlocks the mentioned channel
> [{prefix}nuke]                            » Deletes a channel and then recreates it back
> ```
    ''', delete_after=deleteAfter)

# Utility commands ————————————————————

@district.command()
async def utility(ctx):
    await ctx.message.delete()
    logging.info('Utility Command Executed')
    await ctx.send(f'''
> ```ini
> [ District Selfbot ] | Utility Commands
> ```
> ```ini
> <> is required | () is optional
> ```
> ```ini
> [{prefix}avatar <@user> (@user)]              »  Sends the mentioned users avatar
> [{prefix}userinfo <@user> (@user)]            »  Sends the userinfo of mentioned user
> [{prefix}serverinfo]                          »  Sends the serverinfo
> [{prefix}serverid]                            »  Sends the server ID
> [{prefix}servericon]                          »  Sends the servericon
> [{prefix}serverbanner]                        »  Sets the serverbanner
> [{prefix}poll <message>]                      »  Creates poll
> [{prefix}membercount]                         »  Sends the amount of members in server
> [{prefix}invites <@user> (@user)]             »  Sends the amount of invites
> [{prefix}addrole <@user> <@role>]             »  Adds role 
> [{prefix}derole <@user> <@role>]              »  Deroles the mentioned user
> [{prefix}afk <time> (time)]                   »  Sets your AFK
> [{prefix}roleinfo <@role>]                    »  Sends roleinfo on the role
> [{prefix}permissions <@user> (@user)]         »  Sends permissions for the mentioned user
> [{prefix}emojiadd <emoji>]                    »  Adds an emoji
> [{prefix}image <args>]                        »  Sends an image based on sent arg.
> [{prefix}massreact <emoji>]                   »  Mass react to 20 messages
> [{prefix}ignorefriends]                       »  Ignores all friend requests
> [{prefix}acceptfriends]                       »  Accepts all friend requests
> [{prefix}copyguild]                           »  Copies the guild 
> [{prefix}btc]                                 »  Sends bitcoin price in eur and usd
> [{prefix}clear]                               »  Clears the console
> [{prefix}8ball <question>]                    »  Runs an 8Ball on the sent question
> [{prefix}commandcount]                        »  Sends the amount of built in commands
> ```
    ''', delete_after=deleteAfter)

# Account commands ————————————————————

@district.command()
async def account(ctx):
    await ctx.message.delete()
    logging.info('Account Command Executed')
    await ctx.send(f'''
> ```ini
> [ District Selfbot ] | Account Commands
> ```
> ```ini
> <> is required | () is optional
> ```
> ```ini
> [{prefix}watching <message>]       »  Sets your watching activity
> [{prefix}playing <message>]        »  Sets your playing activity
> [{prefix}listening <message>]      »  Sets your listening activity
> [{prefix}stopactivity]             »  Stops the current activity
> [{prefix}hypesquad]                »  Sets your competing activity
> [{prefix}logout]                   »  Logs out of the account
> [{prefix}restart]                             »  Restarts District selfbot.
> [{prefix}groupleaver]              »  Leaves all available groups
> ```
    ''', delete_after=deleteAfter)

# Troll commands ————————————————————

@district.command()
async def troll(ctx):
    await ctx.message.delete()
    logging.info('Troll Command Executed')
    await ctx.send(f'''
> ```ini
> [ District Selfbot ] | Troll Commands
> ```
> ```ini
> <> is required | () is optional
> ```
> ```ini
> [{prefix}spam <message>]              »  Spams the message sent
> [{prefix}shrug]                       »  Sends a shrug
> [{prefix}lenny]                       »  Sends a lenny face
> [{prefix}tableflip]                   »  Sends a tableflip
> [{prefix}unflip]                      »  Sends an unflipped table
> [{prefix}nitro]                       »  Sends a randomly generated nitro code
> [{prefix}gay (@user)]                 »  Sends the mentioned users gay percentage
> [{prefix}tweet <username> <message>]  »  Creates a screenshot of a tweet
> [{prefix}fry <username>]              »  Fries the mentioned user
> [{prefix}virus]                       »  Runs a virus prank
> [{prefix}table]                       »  Sends a table animation in text form
> ```
    ''', delete_after=deleteAfter)

# Abuse commands ————————————————————

@district.command()
async def abuse(ctx):
    await ctx.message.delete()
    logging.info('Raid Command Executed')
    await ctx.send(f'''
> ```ini
> [ District Selfbot ] | Abuse Commands
> ```
> ```ini
> <> is required | () is optional
> ```
> ```ini
> [{prefix}destroy]                »  Destroys the server
> [{prefix}massban]                »  Bans everyone in the server
> [{prefix}dynoban]                »  Bans everyone in the server using dyno
> [{prefix}mee6ban]                »  Bans everyone in the server using dyno
> [{prefix}masskick]               »  Kicks everyone in the server
> [{prefix}massrole]               »  Mass creates roles in the server
> [{prefix}giveadmin]              »  Gives admin to message author
> [{prefix}spamchannels]           »  Mass creates channels in the server
> [{prefix}delchannels]            »  Deletes every channel in the server
> [{prefix}delroles]               »  Deletes every role in the server
> [{prefix}massunban]              »  Unbans everyone that was banned
> ```
    ''', delete_after=deleteAfter)

# Theme commands ————————————————————

@district.command()
async def themes(ctx):
    await ctx.message.delete()
    logging.info('Theme Command Executed')
    await ctx.send(f'''
> ```ini
> [ District Selfbot ] | Theme Commands
> ```
> ```ini
> <> is required | () is optional
> ```
> ```ini
> [{prefix}purble]       »  Changes the console theme to a purple ->  blue gradient
> [{prefix}pred]         »  Changes the console theme to a purple ->  red gradient
> [{prefix}breen]        »  Changes the console theme to a blue   ->  green gradient
> [{prefix}burple]       »  Changes the console theme to a blue   ->  purple gradient
> [{prefix}bite]         »  Changes the console theme to a blue   ->  white gradient
> [{prefix}reset]        »  Changes the console theme back to its original
> ```
    ''', delete_after=deleteAfter)

# Status commands ————————————————————

@district.command()
async def status(ctx):
    await ctx.message.delete()
    logging.info('Status Command Executed')
    await ctx.send(f'''
> ```ini
> [ District Selfbot ] | Status Commands
> ```
> ```ini
> <> is required | () is optional
> ```
> ```ini
> [{prefix}customstat]       »  Creates a custom animated status
> [{prefix}stopstatus]       »  Stops the custom animated status
> ```
    ''', delete_after=deleteAfter)

# Code commands ————————————————————

@district.command()
async def code(ctx):
    await ctx.message.delete()
    logging.info('Code Command Executed')
    await ctx.send(f'''
> ```ini
> [ District Selfbot ] | Code Commands
> ```
> ```ini
> <> is required | () is optional
> ```
> ```ini
> [{prefix}asciidoc <code>]       »  Sends aciidoc codeblock inclduing code
> [{prefix}bash <code>]           »  Sends bash codeblock including code
> [{prefix}css <code>]            »  Sends css codeblock including code
> [{prefix}yaml <code>]           »  Sends yaml codeblock including code
> [{prefix}js <code>]             »  Sends js codeblock including code
> [{prefix}python <code>]         »  Sends bash codeblock including code
> [{prefix}xml <code>]            »  Sends xml codeblock including code
> [{prefix}lua <code>]            »  Sends lua codeblock including code
> [{prefix}json <code>]           »  Sends json codeblock including code
> ```
    ''', delete_after=deleteAfter)



# Console commands ————————————————————

@district.command()
async def purble(ctx):
    await ctx.message.delete()
    ctypes.windll.kernel32.SetConsoleTitleW(f'District Selfbot | Version: {district_version} | Theme: Purble')
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Succesfully set console theme to purble."
    notification.icon = "./assets/district-png.ico"
    notification.audio = "sound/success.wav"
    notification.send()

    os.system('cls')
    print(Colorate.Diagonal(Colors.purple_to_blue,
    f'''
                              ╔╦╗╦╔═╗╔╦╗╦═╗╦╔═╗╔╦╗
                               ║║║╚═╗ ║ ╠╦╝║║   ║ 
                              ═╩╝╩╚═╝ ╩ ╩╚═╩╚═╝ ╩ v{district_version}
    '''))
    print(Colorate.Vertical(Colors.purple_to_blue,
    f'''
                           Connected: [ {district.user} ]

   ╔══════════════════════════════════════════════════════════════════════╗
   ║                        Commands: {len(district.commands)} | Guilds: {len(district.guilds)}                     ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║           HWID: {keyAuthApp.user_data.hwid}        ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║                    Developer: equi.ty aka equity                     ║
   ╚══════════════════════════════════════════════════════════════════════╝
    '''))
    logging.info(f'Running version {Fore.BLUE}[{Fore.RESET}{district_version}{Fore.BLUE}]{Fore.RESET}')
    logging.info(f'Type {Fore.BLUE},{Fore.RESET}help{Fore.BLUE}{Fore.RESET} to get started')
    

@district.command()
async def reset(ctx):
    await ctx.message.delete()
    ctypes.windll.kernel32.SetConsoleTitleW(f'District Selfbot | Version: {district_version} | Theme: Default')
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Succesfully reset console theme."
    notification.icon = "./assets/district-png.ico"
    notification.audio = "sound/success.wav"
    notification.send()
    os.system('cls')
    print(Colorate.Diagonal(Colors.blue_to_cyan,
    f'''
                              ╔╦╗╦╔═╗╔╦╗╦═╗╦╔═╗╔╦╗
                               ║║║╚═╗ ║ ╠╦╝║║   ║ 
                              ═╩╝╩╚═╝ ╩ ╩╚═╩╚═╝ ╩ v{district_version}
    '''))
    print(Colorate.Vertical(Colors.blue_to_cyan,
    f'''
                           Connected: [ {district.user} ]

   ╔══════════════════════════════════════════════════════════════════════╗
   ║                        Commands: {len(district.commands)} | Guilds: {len(district.guilds)}                     ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║           HWID: {keyAuthApp.user_data.hwid}        ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║                    Developer: equi.ty aka equity                     ║
   ╚══════════════════════════════════════════════════════════════════════╝
    '''))
    logging.info(f'Running version {Fore.BLUE}[{Fore.RESET}{district_version}{Fore.BLUE}]{Fore.RESET}')
    logging.info(f'Type {Fore.BLUE},{Fore.RESET}help{Fore.BLUE}{Fore.RESET} to get started')



@district.command()
async def pred(ctx):
    await ctx.message.delete()
    ctypes.windll.kernel32.SetConsoleTitleW(f'District Selfbot | Version: {district_version} | Theme: Pred')
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Succesfully set console theme to pred."
    notification.icon = "./assets/district-png.ico"
    notification.audio = "sound/success.wav"
    notification.send()
    os.system('cls')
    print(Colorate.Diagonal(Colors.purple_to_red,
    f'''
                              ╔╦╗╦╔═╗╔╦╗╦═╗╦╔═╗╔╦╗
                               ║║║╚═╗ ║ ╠╦╝║║   ║ 
                              ═╩╝╩╚═╝ ╩ ╩╚═╩╚═╝ ╩ v{district_version}
    '''))
    print(Colorate.Vertical(Colors.purple_to_red,
    f'''
                           Connected: [ {district.user} ]

   ╔══════════════════════════════════════════════════════════════════════╗
   ║                        Commands: {len(district.commands)} | Guilds: {len(district.guilds)}                     ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║           HWID: {keyAuthApp.user_data.hwid}        ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║                    Developer: equi.ty aka equity                     ║
   ╚══════════════════════════════════════════════════════════════════════╝
    '''))
    logging.info(f'Running version {Fore.BLUE}[{Fore.RESET}{district_version}{Fore.BLUE}]{Fore.RESET}')
    logging.info(f'Type {Fore.BLUE},{Fore.RESET}help{Fore.BLUE}{Fore.RESET} to get started')



@district.command()
async def breen(ctx):
    await ctx.message.delete()
    ctypes.windll.kernel32.SetConsoleTitleW(f'District Selfbot | Version: {district_version} | Theme: Breen')
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Succesfully set console theme to breen."
    notification.icon = "./assets/district-png.ico"
    notification.audio = "sound/success.wav"
    notification.send()
    os.system('cls')
    print(Colorate.Diagonal(Colors.blue_to_green,
    f'''
                              ╔╦╗╦╔═╗╔╦╗╦═╗╦╔═╗╔╦╗
                               ║║║╚═╗ ║ ╠╦╝║║   ║ 
                              ═╩╝╩╚═╝ ╩ ╩╚═╩╚═╝ ╩ v{district_version}
    '''))
    print(Colorate.Vertical(Colors.blue_to_green,
    f'''
                           Connected: [ {district.user} ]

   ╔══════════════════════════════════════════════════════════════════════╗
   ║                        Commands: {len(district.commands)} | Guilds: {len(district.guilds)}                     ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║           HWID: {keyAuthApp.user_data.hwid}        ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║                    Developer: equi.ty aka equity                     ║
   ╚══════════════════════════════════════════════════════════════════════╝
    '''))
    logging.info(f'Running version {Fore.BLUE}[{Fore.RESET}{district_version}{Fore.BLUE}]{Fore.RESET}')
    logging.info(f'Type {Fore.BLUE},{Fore.RESET}help{Fore.BLUE}{Fore.RESET} to get started')


@district.command()
async def bred(ctx):
    await ctx.message.delete()
    ctypes.windll.kernel32.SetConsoleTitleW(f'District Selfbot | Version: {district_version} | Theme: Bred')
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Succesfully set console theme to bred."
    notification.icon = "./assets/district-png.ico"
    notification.audio = "sound/success.wav"
    notification.send()
    os.system('cls')
    print(Colorate.Diagonal(Colors.blue_to_red,
    f'''
                              ╔╦╗╦╔═╗╔╦╗╦═╗╦╔═╗╔╦╗
                               ║║║╚═╗ ║ ╠╦╝║║   ║ 
                              ═╩╝╩╚═╝ ╩ ╩╚═╩╚═╝ ╩ v{district_version}
    '''))
    print(Colorate.Vertical(Colors.blue_to_red,
    f'''
                           Connected: [ {district.user} ]

   ╔══════════════════════════════════════════════════════════════════════╗
   ║                        Commands: {len(district.commands)} | Guilds: {len(district.guilds)}                     ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║           HWID: {keyAuthApp.user_data.hwid}        ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║                    Developer: equi.ty aka equity                     ║
   ╚══════════════════════════════════════════════════════════════════════╝
    '''))
    logging.info(f'Running version {Fore.BLUE}[{Fore.RESET}{district_version}{Fore.BLUE}]{Fore.RESET}')
    logging.info(f'Type {Fore.BLUE},{Fore.RESET}help{Fore.BLUE}{Fore.RESET} to get started')



@district.command()
async def burple(ctx):
    await ctx.message.delete()
    ctypes.windll.kernel32.SetConsoleTitleW(f'District Selfbot | Version: {district_version} | Theme: Burple')
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Succesfully set console theme to burple."
    notification.icon = "./assets/district-png.ico"
    notification.audio = "sound/success.wav"
    notification.send()
    os.system('cls')
    print(Colorate.Diagonal(Colors.blue_to_purple,
    f'''
                              ╔╦╗╦╔═╗╔╦╗╦═╗╦╔═╗╔╦╗
                               ║║║╚═╗ ║ ╠╦╝║║   ║ 
                              ═╩╝╩╚═╝ ╩ ╩╚═╩╚═╝ ╩ v{district_version}
    '''))
    print(Colorate.Vertical(Colors.blue_to_purple,
    f'''
                           Connected: [ {district.user} ]

   ╔══════════════════════════════════════════════════════════════════════╗
   ║                        Commands: {len(district.commands)} | Guilds: {len(district.guilds)}                     ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║           HWID: {keyAuthApp.user_data.hwid}        ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║                    Developer: equi.ty aka equity                     ║
   ╚══════════════════════════════════════════════════════════════════════╝
    '''))
    logging.info(f'Running version {Fore.BLUE}[{Fore.RESET}{district_version}{Fore.BLUE}]{Fore.RESET}')
    logging.info(f'Type {Fore.BLUE},{Fore.RESET}help{Fore.BLUE}{Fore.RESET} to get started')


@district.command()
async def bite(ctx):
    await ctx.message.delete()
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Succesfully set console theme to bite.."
    notification.icon = "./assets/district-png.ico"
    notification.audio = "sound/success.wav"
    notification.send()
    ctypes.windll.kernel32.SetConsoleTitleW(f'District Selfbot | Version: {district_version} | Theme: Bite')
    os.system('cls')
    print(Colorate.Diagonal(Colors.blue_to_white,
    f'''
                              ╔╦╗╦╔═╗╔╦╗╦═╗╦╔═╗╔╦╗
                               ║║║╚═╗ ║ ╠╦╝║║   ║ 
                              ═╩╝╩╚═╝ ╩ ╩╚═╩╚═╝ ╩ v{district_version}
    '''))
    print(Colorate.Vertical(Colors.blue_to_white,
    f'''
                           Connected: [ {district.user} ]

   ╔══════════════════════════════════════════════════════════════════════╗
   ║                        Commands: {len(district.commands)} | Guilds: {len(district.guilds)}                     ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║           HWID: {keyAuthApp.user_data.hwid}        ║
   ║       ═══════════════════════════════════════════════════════════    ║
   ║                    Developer: equi.ty aka equity                     ║
   ╚══════════════════════════════════════════════════════════════════════╝
    '''))
    logging.info(f'Running version {Fore.BLUE}[{Fore.RESET}{district_version}{Fore.BLUE}]{Fore.RESET}')
    logging.info(f'Type {Fore.BLUE},{Fore.RESET}help{Fore.BLUE}{Fore.RESET} to get started')


@district.command()
async def clear(ctx):
    try:
        await ctx.message.delete()
        intro()
        ctypes.windll.kernel32.SetConsoleTitleW(f'District Selfbot | Version: {district_version} | Theme: Default')
        notification = Notify()
        notification.title = f"District Selfbot"
        notification.message = f"Succesfully cleared console."
        notification.icon = "./assets/district-png.ico"
        notification.audio = "sound/success.wav"
        notification.send()
    except Exception as e:
        print(e)


# Moderation commands ————————————————————

@district.command()
async def ban(ctx, member:discord.Member=None, * , reason=None):
    await ctx.message.delete()
    logging.info('Ban Command Executed')
    if member == None:
        DistrictError()
    await member.ban(reason=reason)
    await ctx.send(f'> **Succesfully Banned** `{member}`')


@district.command()
async def unban(ctx, userid):
    await ctx.message.delete()
    logging.info('Unban Command Executed')
    if userid == None:
        DistrictError()

    user = discord.Object(id=userid)
    await ctx.guild.unban(user)
    await ctx.send(f'> **Succesfully Unbanned** `{userid}`')


@district.command()
async def kick(ctx, member:discord.Member=None, *, reason=None):
    await ctx.message.delete()
    logging.info('Kick Command Executed')
    if member == None:
        DistrictError()
    await member.kick(reason=reason)
    await ctx.send(f'> **Succesfully Kicked** `{member}`')


@district.command()
async def mute(ctx, member: discord.Member=None, *, reason=None):
    await ctx.message.delete()
    logging.info('Mute Command Executed')
    guild = ctx.guild
    mutedRole = discord.utils.get(ctx.guild.roles, name="MutedDistrict")

    if member == None:
        DistrictError()

    if not mutedRole:
        mutedRole = await guild.create_role(name="MutedDistrict")

        for channel in ctx.guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f'> **Succesfully Muted** `{member}`')


@district.command()
async def unmute(ctx, member: discord.Member):
    await ctx.message.delete()
    logging.info(f'Unmute Command Executed')
    mutedRole = discord.utils.get(ctx.guild.roles, name="MutedDistrict")
    if member == None:
        DistrictError()

    await member.remove_roles(mutedRole)
    await ctx.send(f'> **Succesfully Unmuted** `{member}`')


@district.command()
async def purge(ctx, amount=0):
    await ctx.message.delete()
    logging.info('Purge Command Executed')
    if amount == 0:
        DistrictError()
    else:
        await ctx.channel.purge(limit=amount)
        prgmsg = await ctx.send(f'> **Succesfully Purged** `{amount}` **messages**')
        await asyncio.sleep(5)
        await prgmsg.delete()

@district.command()
async def nuke(ctx):
    await ctx.message.delete()
    logging.info('Nuke Command Executed')
    channel_info = [ctx.channel.category, ctx.channel.position]
    await ctx.channel.clone()
    await ctx.channel.delete()
    new_channel = channel_info[0].text_channels[-1]
    await new_channel.edit(position=channel_info[1])
    await new_channel.send(f'> **Succesfully Nuked** `{ctx.channel.name}`')

@district.command()
async def offslowmode(ctx):
    await ctx.message.delete()
    logging.info('OffSlowmode Command Executed')
    await ctx.channel.edit(slowmode_delay=0)
    await ctx.send(f'> **Succesfully Turned Off Slowmode**')


@district.command()
async def slowmode(ctx, seconds: int):
    await ctx.message.delete()
    logging.info('Slowmode Command Executed')
    if seconds == None:
        DistrictError()

    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f'> **Succesfully Set Slowmode To** `{seconds}s`')


@district.command()
async def jail(ctx, member: discord.Member):
    await ctx.message.delete()
    logging.info('Jail Command Executed')
    guild = ctx.guild
    jailedRole = discord.utils.get(ctx.guild.roles, name='PrisonerDistrict')
    if member == None:
        DistrictError()

    if not jailedRole:
        jailedRole = await guild.create_role(name="PrisonerDistrict")
        for channel in ctx.guild.channels:
            await channel.set_permissions(jailedRole, speak=False, send_messages=False, read_message_history=False, read_messages=False)

    await member.add_roles(jailedRole)
    await ctx.send(f'> **Succesfully Jailed** `{member}`')



@district.command()
async def unjail(ctx, member: discord.Member):
    await ctx.message.delete()
    logging.info(f'Unjail Command Executed')
    jailedRole = discord.utils.get(ctx.guild.roles, name='PrisonerDistrict')
    if member == None:
        DistrictError()

    await member.remove_roles(jailedRole)
    await ctx.send(f'> **Succesfully Unjailed** `{member}`')


@district.command()
async def lock(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    logging.info('Lock Command Executed')
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f'> **Succesfully Locked** `{channel}`')
    

@district.command()
async def unlock(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    logging.info('Unlock Command Executed')
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f'> **Succesfully Unlocked** `{channel}`')

# Utility commands ————————————————————

@district.command(aliases=['cc'])
async def commandcount(ctx):
    await ctx.message.delete()
    logging.info('Commandcount Command Executed')
    await ctx.send(f'> **Commands:** `{len(district.commands)}`')


@district.command(aliases=['av'])
async def avatar(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    logging.info('Avatar Command Executed')
    if user is None:
        user = ctx.message.author
    embed=discord.Embed(color=0x2f3136, title=f"{user.name}'s avatar", url=user.display_avatar.url)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
    embed.set_image(url=user.display_avatar.url)
    await ctx.reply(embed=embed)


@district.command(aliases=['rpc'])
async def richpresence(ctx, toggle: str):
    await ctx.message.delete()
    logging.info('Richpresence Command Executed')
    if toggle == "on" and richPresence == "False":
            richPresence = "True"
            notification = Notify()
            notification.title = f"District Selfbot"
            notification.message = f"Succesfully enabled rpc."
            notification.icon = "./assets/district-png.ico"
            notification.audio = "sound/success.wav"
            notification.send()

    if toggle == "off" and richPresence == "True":
            richPresence = "False"
            notification = Notify()
            notification.title = f"District Selfbot"
            notification.message = f"Succesfully disabled rpc."
            notification.icon = "./assets/district-png.ico"
            notification.audio = "sound/success.wav"
            notification.send()

    elif toggle == "on" and richPresence == "True":
            notification = Notify()
            notification.title = f"District Selfbot"
            notification.message = f"RPC is already enabled."
            notification.icon = "./assets/district-png.ico"
            notification.audio = "sound/error.wav"
            notification.send()

    elif toggle == "off" and richPresence == "False":
            notification = Notify()
            notification.title = f"District Selfbot"
            notification.message = f"RPC is already disabled."
            notification.icon = "./assets/district-png.ico"
            notification.audio = "sound/error.wav"
            notification.send()

    else:
        logging.info('Invalid toggle method.')

@district.command()
async def serverid(ctx):
    await ctx.message.delete()
    logging.info('Guild ID Command Executed')
    await ctx.send(f"> **Guild ID**: `{ctx.guild.id}`")


@district.command(aliases=["memberid"])
async def userid(ctx, member:discord.Member=None):
    await ctx.message.delete()
    logging.info('User ID Command Executed')
    member = ctx.author if not member else member
    await ctx.send(f"> **{member.name}'s ID:** `{member.id}`")



@district.command(aliases=['sicon'])
async def servericon(ctx):
    await ctx.message.delete()
    logging.info('Servericon Command Executed')
    guild = ctx.message.guild
    embed = discord.Embed(title=f'{ctx.guild.name}\'s icon', color=0x2f3136)
    embed.set_image(url=ctx.guild.icon)
    await ctx.reply(embed=embed) 


@district.command()
async def serverbanner(ctx):
    await ctx.message.delete()
    logging.info(f'Serverbanner Command Executed')
    if ctx.guild.banner == None:
        DistrictError()
    else:
        embed = discord.Embed(title=f'{ctx.guild.name}\'s banner', color=0x2f3136)
        embed.set_image(url=ctx.guild.banner.url)
        await ctx.send(embed=embed) 


@district.command()
async def serverinfo(ctx):
    await ctx.message.delete()
    logging.info('Serverinfo Command Executed')
    guild = ctx.message.guild
    total_bots = len([member for member in guild.members if member.bot == True])
    text_channels = len(ctx.guild.text_channels)
    voice_channel = len(ctx.guild.voice_channels)
    await ctx.send(f'''
    > __**{guild.name}** **Server Info**__
    > ```
    > Owner          »  {str(guild.owner)}
    > Boost Count    »  {guild.premium_subscription_count}
    > Role Count     »  {len(guild.roles)}
    > Members        »  {len(guild.members)}
    > Bot Count      »  {total_bots}
    > Channels       »  {text_channels}
    > Voice Channels »  {voice_channel}
    > ```
    ''', delete_after=deleteAfter)

@district.command()
async def userinfo(ctx, user: str=None):
    await ctx.message.delete()
    logging.info(f'Userinfo Command Executed')
    if user is None:
        member = ctx.author
    embed = discord.Embed(color=0x2f3136)
    embed.add_field(name='Created Account', value=f"`{member.created_at.strftime('%d %B %Y')}`")
    embed.add_field(name='Joined', value=f"`{member.joined_at.strftime('%d %B %Y')}`")
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in member.guild_permissions if p[1]])
    embed.add_field(name="Guild permissions", value=f'```{perm_string}```', inline=False)
    embed.set_thumbnail(url=member.display_avatar)
    embed.set_author(name=f'{member.name}', icon_url=member.display_avatar)
    await ctx.send(embed=embed)

@district.command()
async def poll(ctx, *, message):
    await ctx.message.delete()
    logging.info(f'Poll Command Executed')
    message = await ctx.send(f"```{message} | {ctx.message.author}```")
    await message.add_reaction('👍')
    await message.add_reaction('👎')

@district.command()
async def membercount(ctx):
    await ctx.message.delete()
    logging.info(f'Membercount Command Executed')
    await ctx.send(f"``{ctx.guild.name}` **has** `{ctx.guild.member_count}` **members**")


@district.command()
async def invites(ctx, member: discord.Member = None):
    await ctx.message.delete()
    logging.info(f'Invites Command Executed')
    totalInvites = 0
    if member == None:
        member = ctx.author
    for i in await ctx.guild.invites():
        if i.inviter == member:
            totalInvites += i.uses
    if member == ctx.author:
            await ctx.send("> **you've invited** `%s` **member(s) to the server**" % (totalInvites))
    else:
        await ctx.send(">  `%s` **has invited** `%s` **member(s) to the server**" % (member.name, totalInvites))


@district.command()
async def addrole(ctx, member: discord.Member, role: discord.Role):
    await ctx.message.delete()
    logging.info(f'Addrole Command Executed')
    await member.add_roles(role)
    await ctx.send(f"> **Succesfully Added** `{role.name}` **To** `{member.name}`")

@district.command()
async def derole(ctx, member: discord.Member, role: discord.Role):
    await ctx.message.delete()
    logging.info(f'Derole Command Executed')
    await member.remove_roles(role)
    await ctx.send(f"> **Succesfully Removed** `{role.name}` **From** `{member.name}`")

@district.command()
async def emojiadd(ctx, emote):
    await ctx.message.delete()
    logging.info(f'Emojiadd Command Executed')
    try:
        if emote[0] == '<':
            name = emote.split(':')[1]
            emoji_name = emote.split(':')[2][:-1]
            anim = emote.split(':')[0]
            if anim == '<a':
                url = f'https://cdn.discordapp.com/emojis/{emoji_name}.gif'
            else:
                url = f'https://cdn.discordapp.com/emojis/{emoji_name}.png'
            try:
                response = requests.get(url) 
                img = response.content
                emote = await ctx.guild.create_custom_emoji(name=name, image=img) 
                return await ctx.send("> **Succesfully Added** %s" % (emote))
            except Exception:
                DistrictError()
        else:
            DistrictError()
    except Exception:
        DistrictError()



@district.command()
async def afk(ctx, mins, reason=None):
    await ctx.message.delete()
    logging.info(f'AFK Command Executed')
    current_nick = ctx.author.nick
    await ctx.send("{0.author.mention} **has gone afk for** `{1}` **minutes(s)**.".format(ctx, mins))
    await ctx.author.edit(nick=f"[AFK] {ctx.author.name}")

    counter = 0
    while counter <= int(mins):
        counter += 1
        await asyncio.sleep(60)

        if counter == int(mins):
            await ctx.author.edit(nick=current_nick)
            await ctx.send(f"{ctx.author.mention} **is no longer AFK*")
            break

@district.command(aliases=['bitcoin'])
async def btc(ctx):
    await ctx.message.delete()
    logging.info(f'Bitcoin Command Executed')
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    await ctx.send(f'> **USD** `${str(usd)}`\n> **EUR** `${str(eur)}`')

@district.command() 
async def roleinfo(ctx, *, role: discord.Role=None):
    await ctx.message.delete()
    logging.info(f'Roleinfo Command Executed')
    if role == None:
        DistrictError()
    perms = role.permissions
    members = len([x for x in ctx.guild.members if role in x.roles])
    if perms.value == 0: 
        msg = f"{role.name} **has no permissions**"
    else:
        msg = " ".join([x[0].replace("_", " ").title() for x in filter(lambda p: p[1] == True, perms)])
    if role.hoist:
        hoist = "yes"
    else:
        hoist = "no"
    if role.mentionable:
        mention = "yes"
    else:
        mention = "no"
    await ctx.send(
    f'''
    > __**{role.name} Role Info**__
    > ```  
    > mentionable     »   {mention}
    > role count      »   {role.colour}
    > user count      »   {members}
    > hoisted         »   {hoist}
    > role id         »   {role.id}
    > role perms 
    > ```
    > ```{msg}```
    ''', delete_after=deleteAfter)


@district.command()
async def permissions(ctx, *, user: discord.Member=None):
    await ctx.message.delete()
    logging.info(f'Permissions Command Executed')
    author = ctx.message.author
    if not user:
        user = author
    perms = "\n".join([x[0].replace("_", " ").title() for x in filter(lambda p: p[1] == True, user.guild_permissions)])
    await ctx.send(f'''
> __**{user.name}'s Permissions**__
> ```{perms}```
    ''', delete_after=deleteAfter)

# Abuse commands ————————————————————

@district.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    logging.info(f'Spam Command Executed')
    for _i in range(amount):
        await ctx.send(message)



@district.command(aliases=["rekt", "smoke"])
async def destroy(ctx):
    await ctx.message.delete()
    logging.info( f'Destroy Command Executed')
    for user in list(ctx.guild.members):
        try:
            await user.ban()
            logging.info( f'Succesfully Banned {user.name}')
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            logging.info( f'Succesfully Deleted {channel.name}')
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            logging.info( f'Succesfully Deleted {role.name}')
        except:
            pass
    try:
        await ctx.guild.edit(
            name=guildName,
            description="district was here",
            reason=reason,
            icon=None,
            banner=None
        )
        logging.info( f'Succesfully Edited Guild')
    except:
        pass
    for _i in range(150):
        await ctx.guild.create_text_channel(name=chanName)
        logging.info( f'Succesfully Created {channel.name}')
    for _i in range(150):
        await ctx.guild.create_role(name=roleName)
        logging.info( f'Succesfully Created {role.name}')



@district.command(aliases=["banwave", "banall", "pack"])
async def massban(ctx):
    await ctx.message.delete()
    logging.info( f'Massban Command Executed')
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason=reason)
            logging.info( f'Succesfully Banned {user.name}')
        except:
            pass

@district.command()
async def mee6(ctx):
    await ctx.message.delete()
    logging.info( f'MEE6ban Command Executed')
    for member in list(ctx.guild.members):
        message = await ctx.send("!ban " + member.mention)
        await message.delete()
        await asyncio.sleep(1.5)
        logging.info( f'Succesfully MEE6banned {member.name}')

@district.command()
async def dynoban(ctx):
    await ctx.message.delete()
    logging.info( f'Dynoban Command Executed')
    for member in list(ctx.guild.members):
        message = await ctx.send("?ban " + member.mention)
        await message.delete()
        await asyncio.sleep(1.5)
        logging.info( f'Succesfully Dynobanned {member.name}')


@district.command(aliases=["kickall", "kickwave"])
async def masskick(ctx):
    await ctx.message.delete()
    logging.info( f'Masskick Command Executed')
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason=reason)
            logging.info( f'Succesfully Kicked {user.name}')
        except:
            pass


@district.command(aliases=["spamroles", "massroles", "addroles"])
async def massrole(ctx):
    await ctx.message.delete()
    logging.info( f'Massrole Command Executed')
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=random.choice(roleName))
            logging.info( f'Succesfully Created Role {roleName}')
        except:
            try:
                await ctx.guild.create_role(name=random.choice(roleName))
                logging.info( f'Succesfully Created Role {roleName}')
            except:
                return


@district.command(aliases=["givemeadmin", "giveadminrole", "giveadminroles"])
async def giveadmin(ctx):
    await ctx.message.delete()
    logging.info( f'Giveadmin Command Executed')
    for role in ctx.guild.roles:
        try:
            if role.permissions.administrator:
                await ctx.author.add_roles(role)
                logging.info( f'Succesfully Gave Admin To {ctx.author.name}')
        except:
            pass


@district.command(aliases=["masschannels", "masschannel", "ctc"])
async def spamchannels(ctx):
    await ctx.message.delete()
    logging.info( f'Spamchannels Command Executed')
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name=random.choice(chanName))
            logging.info( f'Succesfully Created Channel {chanName}')
        except:
            return


@district.command(aliases=["delchannel"])
async def delchannels(ctx):
    await ctx.message.delete()
    logging.info( f'Deletechannels Command Executed')
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            logging.info( f'Succesfully Deleted Channel {channel.name}')
        except:
            return


@district.command(aliases=["deleteroles"])
async def delroles(ctx):
    await ctx.message.delete()
    logging.info( f'Deleteroles Command Executed')
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            logging.info( f'Succesfully Deleted Role {role.name}')
        except:
            pass


@district.command(aliases=["purgebans", "unbanall"])
async def massunban(ctx):
    await ctx.message.delete()
    logging.info( f'Massunban Command Executed')
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
            logging.info( f'Succesfully Unbanned {users.name}')
            await ctx.send(f'> **Succesfully Unbanned All Users**')
        except:
            pass

@district.command()
async def massping(ctx,):
    await ctx.message.delete()
    logging.info('Massping Command Executed')
    for member in list(ctx.guild.members):
        message = await ctx.send(member.mention)
        await message.delete()
        await asyncio.sleep(0.5)

# Account commands ————————————————————

@district.command()
async def restart(ctx):
    await ctx.message.delete()
    logging.info('Restart Command Executed')
    cmd = "mode 80,20"
    os.system(cmd)
    notification = Notify()
    notification.title = f"District Selfbot"
    notification.message = f"Restarting..."
    notification.icon = "./assets/district-png.ico"
    notification.audio = "sound/success.wav"
    notification.send()
    DistrictRestart()

@district.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house):
    await ctx.message.delete()
    logging.info(f'Hypesquad Command Executed')
    request = requests.Session()
    headers = {
        'Authorization': Token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if house == "bravery":
        payload = {'house_id': 1}
    elif house == "brilliance":
        payload = {'house_id': 2}
    elif house == "balance":
        payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v8/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(e)

@district.command()
async def logout(ctx):
    await ctx.message.delete()
    logging.info( f'Logout Command Executed')
    await district.logout()

@district.command(name='group-leaver', aliases=['leaveallgroups', 'leavegroup', 'leavegroups', "groupleave", "groupleaver"])
async def _group_leaver(ctx):
    await ctx.message.delete()
    logging.info('Group Leaver Command Executed')
    for channel in district.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()
            logging.info(f'Succesfully Left {channel.name}')




# Troll commands ————————————————————


@district.command(name='8ball')
async def _ball(ctx, *, question):
    await ctx.message.delete()
    logging.info( f'8Ball Command Executed')
    responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'That is a definite yes!',
        'Maybe',
        'There is a good chance'
    ]
    answer = random.choice(responses)
    await ctx.send(f'> **Question** {question}\n> **Answer** {answer}')

@district.command()
async def virus(ctx):
    await ctx.message.delete()
    logging.info( f'Virus Command Executed')
    message = await ctx.send(f'''
``[▓▓▓                    ] / -virus.exe Packing files.``        
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓                ] — -virus.exe Packing files..``         
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ -virus.exe Packing files..``        
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | -virus.exe Packing files..``         
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / -virus.exe Packing files..``      
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] — -virus.exe Packing files..``    
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ -virus.exe Packing files..``   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``New file with name change, New file : district.exe``   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``Injecting virus.   |``
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``Injecting virus..  /``
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``Injecting virus... —``
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        > **Successfully Injected district.exe**
        ''')

@district.command()
async def table(ctx):
    await ctx.message.delete()
    logging.info( f'Table Command Executed')
    message = await ctx.send(f'''
`(\°-°)\  ┬─┬`       
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°□°)\  ┬─┬`       
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(-°□°)-  ┬─┬`      
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯    ]`       
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯     ┻━┻`   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯       [`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯          ┬─┬`   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯                 ]`   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯                  ┻━┻`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯                         [`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°-°)\                               ┬─┬`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°-°)\                                     ]`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°-°)\                                       ┻━┻`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°-°)\                                               [`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°-°)\                                              ┬─┬`
''')

@district.command()
async def shrug(ctx):
    await ctx.message.delete()
    logging.info(f'Shrug Command Executed')
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)


@district.command()
async def lenny(ctx):
    await ctx.message.delete()
    logging.info(f'Lenny Command Executed')
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)


@district.command(aliases=["fliptable"])
async def tableflip(ctx):
    await ctx.message.delete()
    logging.info(f'Tableflip Command Executed')
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)


@district.command()
async def unflip(ctx):
    await ctx.message.delete()
    logging.info(f'Unflip Command Executed')
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

@district.command()
async def nitro(ctx):
    await ctx.message.delete()
    logging.info(f'Nitro Command Executed')
    await ctx.send(Nitro())

@district.command()
async def gay(ctx, user: discord.User):
    await ctx.message.delete()
    logging.info(f'Gay Command Executed')
    percentage_numbers = ["0%", "1%", "5%", "10%", "15%", "20%", "25%", "30%", "35%", "40%", "45%", "50%", "55%", "60%", "65%", "70%", "75%", "80%", "85%", "90%", "95%", "100%", "∞"]
    percentage = random.choice(percentage_numbers)
    await ctx.send(f'''
        > **How gay are you or are you gay ?**
        > ```
        > {user.name} is {percentage} gay !!
        > ```
        >
        ''')



@district.command()
async def tweet(ctx, username: str = None, *, message: str = None):
    await ctx.message.delete()
    if username is None or message is None:
        DistrictError()
        logging.info(f'Tweet Command Executed')
        return
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(str(res['message'])) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, f"districttweeted.png"))
            except:
                await ctx.send(res['message'])


@district.command(aliases=["deepfry"])
async def fry(ctx, user: discord.Member = None):
    logging.info(f'Fry Command Executed')
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"districtfried.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"districtfried.png"))
        except:
            await ctx.send(res['message'])


@district.command(aliases=["img", "searchimg", "searchimage", "imagesearch", "imgsearch"])
async def image(ctx, *, args):
    logging.info(f'Image Command Executed')
    await ctx.message.delete()
    url = 'https://unsplash.com/search/photos/' + args.replace(" ", "%20")
    page = requests.get(url)
    soup = bs4(page.text, 'html.parser')
    image_tags = soup.findAll('img')
    if str(image_tags[2]['src']).find("https://trkn.us/pixel/imp/c="):
        link = image_tags[2]['src']
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(link) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(f"> **Search result for:** `{args}`", file=discord.File(file, f"districtimg.png"))
        except:
            await ctx.send(f'' + link + f"\n> **Search result for:** `{args}`")
    else:
        await ctx.send(f"> **Nothing found for** `{args}`")



@district.command()
async def copyguild(ctx):
    logging.info(f'Copyguild Command Executed')
    await ctx.message.delete()
    await district.create_guild(f'backup - {ctx.guild.name}')
    await asyncio.sleep(4)
    for g in district.guilds:
        if f'backup - {ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                        await asyncio.sleep(0.5)
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
                        await asyncio.sleep(0.5)

    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

@district.command()
async def acceptfriends(ctx):
    await ctx.message.delete()
    logging.info(f'Acceptfriends Command Executed')
    for relationship in district.user.relationships:
        if relationship == discord.RelationshipType.incoming_request:
            await relationship.accept()


@district.command()
async def ignorefriends(ctx):
    await ctx.message.delete()
    logging.info(f'Ignorefriends Command Executed')
    for relationship in district.user.relationships:
        if relationship is discord.RelationshipType.incoming_request:
            relationship.delete()


@district.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    logging.info(f'Massreact Command Executed')
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)

@district.event
async def on_message(message):
    if 'discord.gift/' in message.content:
        if nitroSniper == "True":
            code = re.search("discord.gift/(.*)", message.content).group(1)
            Token = config.get('userToken')

            headers = {'Authorization': Token}

            r = requests.post(
                f'https://discordapp.com/api/v9/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text


            if 'This gift has been redeemed already.' in r:
                logging.info(f"Nitro Code {Fore.BLUE}[{Fore.RESET} {code} {Fore.BLUE}]{Fore.RESET} was already redeemed" + Fore.RESET)
                print(f"""
                » Channel: {Fore.BLUE}[{Fore.RESET} {message.channel} {Fore.BLUE}]{Fore.RESET}
                » Server:  {Fore.BLUE}[{Fore.RESET} {message.guild} {Fore.BLUE}]{Fore.RESET}
                » Sender:  {Fore.BLUE}[{Fore.RESET} {message.author} {Fore.BLUE}]{Fore.RESET}
                » Code:    {Fore.BLUE}[{Fore.RESET} {code} {Fore.BLUE}]{Fore.RESET}
                """)

            elif 'subscription_plan' in r:
                logging.info(f"Nitro Code {Fore.BLUE}[{Fore.RESET} {code} {Fore.BLUE}]{Fore.RESET} was succesfully redeemed !" + Fore.RESET)
                print(f"""
                » Channel: {Fore.BLUE}[{Fore.RESET} {message.channel} {Fore.BLUE}]{Fore.RESET}
                » Server:  {Fore.BLUE}[{Fore.RESET} {message.guild} {Fore.BLUE}]{Fore.RESET}
                » Sender:  {Fore.BLUE}[{Fore.RESET} {message.author} {Fore.BLUE}]{Fore.RESET}
                » Code:    {Fore.BLUE}[{Fore.RESET} {code} {Fore.BLUE}]{Fore.RESET}
                """)
                DistrictSniped()

            elif 'Unknown Gift Code' in r:
                logging.info(f"Nitro Code {Fore.BLUE}[{Fore.RESET} {code} {Fore.BLUE}]{Fore.RESET} is unknown" + Fore.RESET)
                print(f"""
                » Channel: {Fore.BLUE}[{Fore.RESET} {message.channel} {Fore.BLUE}]{Fore.RESET}
                » Server:  {Fore.BLUE}[{Fore.RESET} {message.guild} {Fore.BLUE}]{Fore.RESET}
                » Sender:  {Fore.BLUE}[{Fore.RESET} {message.author} {Fore.BLUE}]{Fore.RESET}
                » Code:    {Fore.BLUE}[{Fore.RESET} {code} {Fore.BLUE}]{Fore.RESET}
                """)
        else:
            return
    await district.process_commands(message)

# Status commands ————————————————————

@district.command()
async def customstat(ctx):
    await ctx.message.delete()
    logging.info( f'Customstatus Command Executed')
    customstatus.start()

@tasks.loop(seconds=1)
async def customstatus():
    await district.change_presence(activity=discord.Game(name=stat1))
    await asyncio.sleep(1)
    await district.change_presence(activity=discord.Game(name=stat2))
    await asyncio.sleep(1)
    await district.change_presence(activity=discord.Game(name=stat3))
    await asyncio.sleep(1)

@district.command()
async def stopstatus(ctx):
    await ctx.message.delete()
    logging.info( f'Stopstatus Command Executed')
    await district.change_presence(activity=None, status=discord.Status.offline)

@district.command(aliases=["stream"])
async def watching(ctx, *, message):
    await ctx.message.delete()
    logging.info(f'Stream Command Executed')
    stream = discord.Streaming(
        name=message,
        url=stream_url,
    )
    await district.change_presence(activity=stream, status=discord.Status.dnd)


@district.command(alises=["game"])
async def playing(ctx, *, message):
    await ctx.message.delete()
    logging.info(f'Playing Command Executed')
    game = discord.Game(
        name=message
    )
    await district.change_presence(activity=game, status=discord.Status.dnd)


@district.command(aliases=["listen"])
async def listening(ctx, *, message):
    await ctx.message.delete()
    logging.info(f'Listening Command Executed')
    await district.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))

@district.command(aliases=["stopstreaming", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.message.delete()
    logging.info(f'StopActivity Command Executed')
    await district.change_presence(activity=None, status=discord.Status.dnd)

# Code commands ————————————————————

@district.command()
async def asciidoc(ctx, code: str):
    await ctx.message.delete()
    logging.info('Asciidoc Command Executed')
    await ctx.send(f'''
```asciidoc
{code}```
    ''')

@district.command()
async def bash(ctx, code: str):
    await ctx.message.delete()
    logging.info('Bash Command Executed')
    await ctx.send(f'''
```bash
{code}```
    ''')

@district.command()
async def css(ctx, code: str):
    await ctx.message.delete()
    logging.info('Css Command Executed')
    await ctx.send(f'''
```css
{code}```
    ''')

@district.command()
async def yaml(ctx, code: str):
    await ctx.message.delete()
    logging.info('YAML Command Executed')
    await ctx.send(f'''
```yaml
{code}```
    ''')

@district.command()
async def lua(ctx, code: str):
    await ctx.message.delete()
    logging.info('Lua Command Executed')
    await ctx.send(f'''
```lua
{code}```
    ''')

@district.command()
async def js(ctx, code: str):
    await ctx.message.delete()
    logging.info('JS Command Executed')
    await ctx.send(f'''
```js
{code}```
    ''')

@district.command()
async def python(ctx, code: str):
    await ctx.message.delete()
    logging.info('Python Command Executed')
    await ctx.send(f'''
```
py
{code}```
    ''')

@district.command()
async def xml(ctx, code: str):
    await ctx.message.delete()
    logging.info('XML Command Executed')
    await ctx.send(f'''
```xml
{code}```
    ''')

@district.command()
async def json(ctx, code: str):
    await ctx.message.delete()
    logging.info('JSON Command Executed')
    await ctx.send(f'''
```asciidoc
{code}```
    ''')

district.run(Token, bot=False, reconnect=True)
