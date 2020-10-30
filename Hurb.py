import discord
from discord.ext import commands
import json

intents = discord.Intents.default()
intents.members = True


def getprefix(_bot, message):
    with open('/Users/sethraphael/PycharmProject/Hurb/Bots/prefixes.json', 'r') as f:
        prefixes = json.load(f)
        if message.guild is None:
            return "%"
        else:
            return commands.when_mentioned_or(prefixes[str(message.guild.id)])(_bot, message)


bot = commands.Bot(command_prefix=getprefix, help_command=None, intents=intents)


@bot.event
async def on_command_error(ctx, error):
    pass


bot.run("NzM2MjgzOTg4NjI4NjAyOTYw.Xxsj5g.ra2OkTKgLoSf_SYRxUFtw4fX0pQ", bot=True, reconnect=True)
