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
    
    bad_words = ['bad', "stop", "unfriendly"]
    for word in bad_words:
        if message.content.count(word) > 0:
            print("Bad word deleted")
            await message.channel.purge(limit=1)

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == 'general':
            await channel.send_message(f"""Welcometo the server{member.mention}""")
        


client.run(TOKEN)
