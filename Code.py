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

@bot.command()

async def eco(ctx):
    facts = [
        "Каждый год в океаны попадает около 8 миллионов тонн пластика.",
        "Леса покрывают около 30% поверхности земли и являются домом для 80% наземных видов животных и растений.",
        "Более миллиарда людей живут без доступа к чистой питьевой воде.",
        "Один рециклированный стеклянный бутыль экономит достаточно энергии, чтобы запитать лампу на 4 часа.",
        "Каждое сохраненное дерево может поглотить около 21 кг углекислого газа в год."
    ]
    
    await ctx.send(f'Рандомный факт: {random.choice(facts)}')

bot.run("Token")
