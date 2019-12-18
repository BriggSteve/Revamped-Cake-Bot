import discord
import asyncio
import datetime

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    await cakeday(message)
    await version(message)
    if message.content.startswith('.start'):
        await message.channel.send("Started bot. Date time: " + datetime.datetime.today().strftime("%d-%m-%Y"))
        x = message.guild.members
        while True:
            today = todaydate()
            for member in x:
                j = member.joined_at
                j = j.strftime("%m %d")
                if j == today:
                    await announcement(member.name, member.id)
            await asyncio.sleep(86400) #24 hours


def todaydate():
    today = datetime.datetime.now()
    today = today.strftime("%m %d")
    return today


@client.event
async def announcement(name, ID):
    channel = client.get_channel()
    await channel.send(name + " is celebrating their cake day!!! <@" + str(ID) + "> " + "@everyone")


@client.event
async def cakeday(message):
    if message.author == client.user:
        return

    if message.content.startswith('.cakeday'):
        j = message.author.joined_at
        j = (monthconvert(j.strftime("%m")) + (dayconvert(j.strftime("%d"))) + j.strftime("%Y"))
        await message.channel.send("Your cake day is " + j + "!!")


def monthconvert(month): #01 - 12
    if month == "01":
        return "January "
    if month == "02":
        return "February "
    if month == "03":
        return "March "
    if month == "04":
        return "April "
    if month == "05":
        return "May "
    if month == "06":
        return "June "
    if month == "07":
        return "July "
    if month == "08":
        return "August "
    if month == "09":
        return "September "
    if month == "10":
        return "October "
    if month == "11":
        return "November "
    if month == "12":
        return "December "


def dayconvert(day): #0x - xx
    if day == "01":
        return "1st "
    elif day == "02":
        return "2nd "
    elif day == "03":
        return "3rd "
    else:
        return day + "th "


@client.event
async def version(message):
    if message.author == client.user:
        return

    if message.content.startswith('.version'):
        await message.channel.send("Version: 1.0 ")

client.run("")
