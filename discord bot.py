import discord, random
import requests
from bs4 import BeautifulSoup
from discord.ext import commands

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    print("message-->", message.author, message.content)
    if message.author == client.user:
        return

    user = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    if message.content.lower().startswith('!ping'):
        await message.channel.send('pong!')

    if message.content.lower().startswith('!hi'):
        await message.channel.send('Hello!')

    if message.content.startswith('!audio'):
        await message.channel.send(file=discord.File('myRecording00 (1).wav'))

    if message.content.startswith('!random'):
        await message.channel.send(random.randint(1, 10))

    if message.content.lower().startswith('!даня'):
        await message.channel.send('лох!')

    if message.content.lower().startswith('!тімур'):
        await message.channel.send('красава')

    if "+" in message.content and message.content.lower().startswith('!'):
        culc_list = message.content[1:].split("+")
        await message.channel.send(int(culc_list[0]) + int(culc_list[1]))

    if "-" in message.content and message.content.lower().startswith('!'):
        culc_list = message.content[1:].split("-")
        await message.channel.send(int(culc_list[0]) - int(culc_list[1]))

    if "*" in message.content and message.content.lower().startswith('!'):
        culc_list = message.content[1:].split("*")
        await message.channel.send(int(culc_list[0]) * int(culc_list[1]))

    if "/" in message.content and message.content.lower().startswith('!'):
        culc_list = message.content[1:].split("/")
        await message.channel.send(int(culc_list[0]) / int(culc_list[1]))

    url = 'https://minfin.com.ua/currency/nbu/'

    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text)
    tr = soup.findAll('p', {'class': 'sc-1x32wa2-9 glerpA'})
    e = []
    for i in tr:
        e.append(i.text)

    if message.content.lower().startswith('!доллар') or message.content.lower().startswith('!долар'):
        await message.channel.send(e[0])

    if message.content.lower().startswith('!євро') or message.content.lower().startswith('!евро'):
        await message.channel.send(e[1])

    if message.content.lower().startswith('!злоті'):
        await message.channel.send(e[2])

    if message.content.lower().startswith('!втрати'):
        url = 'https://zaxid.net/vtrati_rosiyan_u_viyni_proti_ukrayini_n1537635'
        source = requests.get(url)
        main_text = source.text
        soup = BeautifulSoup(main_text)
        tr = soup.findAll('div', {'newsSummary1537635'})
        for i in tr:
            await message.channel.send(i.text)

    if message.content.lower().startswith('!clear'):
        if int(message.content.split()[1]) <= 10:
            await message.channel.purge(limit=int(message.content.split()[1]))
        else:
            await message.channel.send("Можна видаляти тільки 10 повідомлень за раз максимум")

    if message.content.lower().startswith('!buttoms'):
        @discord.ui.button(label="Button", style=discord.ButtonStyle.gray)
        async def gray_button(self, button: discord.ui.Button, interaction: discord.Interaction):
            await message.channel.send(content=f"This is an edited button response!")


client.run('MTA1MjE1NDIyNTE3OTc3NTAzNg.GAK-HM.qTw5ZuBSGZfWiA_m-6C2FG4F1S3j_OQQgd8on4')
