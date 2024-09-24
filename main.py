from keep_alive import keep_alive
import discord
from discord import app_commands
import asyncio
import os

from discord import message


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print('Ready')
    new_activity = f"こうきゅうバナナ" 
    await client.change_presence(activity=discord.Game(new_activity)) 
    await tree.sync()
    
@client.event
async def on_message(message: discord.Message):
    # メッセージの送信者がbotだった場合は無視する
    if message.author.bot:
        return

@tree.command(name='banana_twitter', description='公式𝕏を表示') 
async def test_command(interaction: discord.Interaction):
    await interaction.response.send_message('https://x.com/denpaningen', ephemeral=True)
    
@tree.command(name='banana_event', description='曜日イベントを表示') 
async def test_command(interaction: discord.Interaction):
    await interaction.response.send_message('https://media.discordapp.net/attachments/1269059651584921681/1269059823165509733/Getstage_240729001.png?ex=66aeaf8f&is=66ad5e0f&hm=c6862355266d4fd56c474dd1392bf1d98d7dded277846df50b75223b3998954d&=&format=webp&quality=lossless&width=550&height=238', ephemeral=True)

@tree.command(name='banana_status', description='複数の体格表を表示') 
async def test_command(interaction: discord.Interaction): 
    await interaction.response.send_message(content="https://x.com/takka0407/status/1818476455535493576\nhttps://x.com/Mazime/status/1833791101737545801\nhttps://x.com/nmyon_denpa/status/1834236595949711786?s=46&t=Sd2kqUdES1yw3BY7BCW8XQ\nhttps://x.com/tatawas1_denpa/status/1835603378224931086?s=46&t=Sd2kqUdES1yw3BY7BCW8XQ\nhttps://x.com/denpalagoon/status/1835565332079243272?s=46&t=Sd2kqUdES1yw3BY7BCW8XQ", ephemeral=True)

@tree.command(name='banana_head', description='頭の形の表を表示/作成:月詠めあ')
async def test_command(interaction: discord.Interaction): 
    await interaction.response.send_message('https://media.discordapp.net/attachments/1269059651584921681/1269074381594689596/188_20240803082820.png?ex=66c47dde&is=66c32c5e&hm=c0cb0c7f6d3b8d8d65daeba8fe00a6f03a07947ce87813f100a4ee8b276f8aca&=&format=webp&quality=lossless&width=687&height=222', ephemeral=True)


#コピー用
#@tree.command(name='denpa_', description='')
#async def test(interaction: discord.Interaction): 
#  await interaction.response.send_message('')

keep_alive()
TOKEN = os.getenv("DISCORD_TOKEN")
try:
    client.run(TOKEN)
except:
    os.system("kill 1")
