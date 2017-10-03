import discord
import asyncio
import threading
from random import randint
from time import gmtime, strftime

client = discord.Client()

@client.event
async def on_ready():
    print(' ')
    print('\033[35m' + '|' + '\033[36m' + ' Logging messages.'+ '\033[39m')
    print('\033[35m' + '|' + '\033[33m' + ' Logged in as:',client.user.name)
    print('\033[35m' + '|' + '\033[33m' + ' UID:',client.user.id)
    print(' ')

messages1 = []

@client.event
async def on_message(message):
	string = message.channel
	print("\033[1;31mMessage \033[0;32m'" + message.content + "' \033[1;31msent by \033[0;32m" + message.author.name + " \033[1;31min server \033[0;32m" + message.server.name + ' \033[1;31mat \033[0;32m' + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
	if message.author == client.user:
		messages1.append(message.content)
		# MAKES A LIST WITH THE COMMAND ATRIBUTES
		commands = []
		z = 0
		for index, a in enumerate(message.content):
			if a == " ":
				commands.append(message.content[z:index])
				z = index+1
		commands.append(message.content[z:])

client.run("token",bot=False)