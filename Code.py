import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

items = {'пластик': 450, 'стекло': "бесконечно", 'полиэтилен': 20, 'алюминий': 318, 'подгузник': 500}

@bot.command()
async def howlong(ctx, item):
    if item in items.keys():
        await ctx.send(f'Вещь {item} разлагается {items[item]} лет')
    else:
        await ctx.send('такой вещи нет в базе данных')

bot.run("Token")
