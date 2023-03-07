import discord
from discord.ext import commands
from discord.utils import get
from PIL import Image, ImageFilter
from urllib.request import Request, urlopen
from discord.utils import get
import requests
from bs4 import BeautifulSoup
import tracemalloc

tracemalloc.start()
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)


# exchange rates
# url = 'https://minfin.com.ua/currency/nbu/'
#
# source = requests.get(url)
# main_text = source.text
# soup = BeautifulSoup(main_text)
# tr = soup.findAll('p', {'class': 'sc-1x32wa2-9 glerpA'})
# currency_list = []
# for i in tr:
#     currency_list.append(i.text)


@bot.event
async def on_ready():
    print("bot is connected")

    await bot.change_presence(status=discord.Status.online, activity=discord.Game("топ"))


# greetings
@bot.command(pass_context=True)
async def hello(ctx):
    author = ctx.message.author
    message = discord.Embed(color=0x45E356, description=f'здаров {author.mention}')
    await ctx.send(embed=message)


# ping pong
@bot.command(pass_context=True)
async def ping(ctx):
    message = discord.Embed(color=0x45E356, description="pong")
    await ctx.send(embed=message)


# clear
@bot.command(pass_context=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)


# kick
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)

    await member.kick(reason=None)


# ban
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await member.ban(reason=None)


# avatar
@bot.command(pass_context=True)
async def avatar(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    message = discord.Embed(color=0x22ff00, title=f"ава - {member.name}",
                            description=f"download link: \n [png ]({member.avatar})")
    message.set_image(url=member.avatar)
    await ctx.send(embed=message)


# курс, доллара, евро, злоті
# @bot.command(pass_context=True)
# async def currency(ctx):
#     await ctx.send(
#         f'курс доллара - {currency_list[0]} \nкурс евро - {currency_list[1]} \nкурс злотих - {currency_list[2]} ')


# voice
# @bot.command(pass_context=True)
# async def join(ctx, arg1):
#     global voice
#     channel = ctx.message.author.voice.channel
#     voice = get(bot.voice_clients, guild=ctx.guild)
#     if voice and voice.is_connected():
#         await voice.move_to(channel)
#     else:
#         voice = await channel.connect(reconnect=True, timeout=None)

#
# @bot.command(pass_context=True)
# async def join(ctx, arg1):
#     voice_ch = ctx.guild.fetch_channel(ctx.message.author.voice.channel)
#     voice_ch.id = (arg1)
#     voice_ch.connect()
# channel = ctx.author.voice.channel
# await channel.connect()
# await member.edit(mute=True)


token = "MTA1MjE1NDIyNTE3OTc3NTAzNg.GdHNBo.bH9BU8QmZSW_z9P0xFcg1rHm5uFOr-E876gEfw"

bot.run(token)


