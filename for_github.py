import discord
from discord.ext import commands
import webbrowser
import ctypes
import os
import pyautogui
import time
from plyer import notification
import asyncio
from mss import mss


client = discord.Client()
#my_id = <your_id>

@client.event
async def on_ready():
    print("Ready")

@client.event
async def on_message(message):
    if message.content.startswith('message'):
        to_say = message.content.replace("message", "")
        notification.notify(
            title = message.content,
            message = to_say,
            timeout  = 10
        )
        await message.channel.send(f'Sent : {to_say} by {message.author}')
    elif message.content.startswith('open'):
        url = message.content.replace("open", "")
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
        webbrowser.get(chrome_path).open_new(url)
        await message.channel.send(f'Opened : {url} by {message.author}')
    elif message.content.startswith('lock') and message.author.id == my_id :
        ctypes.windll.user32.LockWorkStation()
    elif message.content == 'screenshot':
        if os.path.isfile('screenshot.png'):  # Check if a screenshot.png exists, if yes, delete it so it can be replaced
            os.remove('screenshot.png')
        await message.channel.send("Taking a screenshot.")
        with mss() as sct:
            filename = sct.shot(mon=-1, output='screenshot.png')
        await message.channel.send(file=discord.File('screenshot.png'))
    else:
        print(message.content)    

    
client.run("<bot_token>")