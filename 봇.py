import discord
import os
client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("테스트봇")
    await client.change_presence("status=discord.Status.online,activity=game")



@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요")
 if message.content.startswith("!반가워"):
        await message.channel.send("반갑습니다")
 if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요")
 if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요")
        if message.content.startswith("!안녕"):
            await message.channel.send("안녕하세요")
            if message.content.startswith("!안녕"):
                await message.channel.send("안녕하세요")









access_tokken = os.environ["BOT_TOKEN"]
client.run('acces_token')

