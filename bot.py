import discord

client = discord.Client()
TOKEN = 'OTU5MDk0NDMxMzkzNDExMTIz.YkW4Sw.Vfq2LoBOVr3_3AKcXw2JRdP3Dh8'

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

@client.event
async def on_voice_state_update(member, before, after):
 
    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
    if before.channel != after.channel:
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        botRoom = client.get_channel(959388535276843038)
 
        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        announceChannelIds = [844637321449570378, 959388917252124722]
 
        # 退室通知
        if before.channel is not None and before.channel.id in announceChannelIds:
            await botRoom.send("**" + before.channel.name + "** から、__" + member.name + "__  が抜けました！")
        # 入室通知
        if after.channel is not None and after.channel.id in announceChannelIds:
            await botRoom.send("**" + after.channel.name + "** に、__" + member.name + "__  が参加しました！")
 

client.run(TOKEN)
