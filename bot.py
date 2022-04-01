import discord

client = discord.Client()
TOKEN = 'OTU5MDk0NDMxMzkzNDExMTIz.YkW4Sw.NKOkKizl78igyumQEus0D7hYg5Y'

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.channel.id != 959096526020427816:
        print('chigau')
        return

    print('あってる!')

    if message.author == client.user:
        return

    if message.channel.name == 'bot-working-check':
        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')
        


client.run(TOKEN)
