from decouple import config, Csv

import discord


client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Que hay perro {} ✌️'.format(message.author.mention)
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(client.user.default_avatar_url)
    print('------')

client.run(config('TOKEN'))
