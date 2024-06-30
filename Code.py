import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

items = {'пластик': 450, 'стекло': "бесконечно", 'полиэтилен': 20, 'алюминий': 318, 'подгузник': 500}
facts = [
    "Каждый год в океаны попадает около 8 миллионов тонн пластика.",
    "Леса покрывают около 30% поверхности земли и являются домом для 80% наземных видов животных и растений.",
    "Более миллиарда людей живут без доступа к чистой питьевой воде.",
    "Один рециклированный стеклянный бутыль экономит достаточно энергии, чтобы запитать лампу на 4 часа.",
    "Каждое сохраненное дерево может поглотить около 21 кг углекислого газа в год."
]
Throw = {'стекло': "стекло лучше выбрасывать в зелёную мусорку", "пластик": "пластик лучше выбрасывать в жёлтую мусорку", "бумага": "лучше выбрасывать в синию мусорку", "метал": "метал лучше выбрасывать в красную мусорку"}

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command()
async def howlong(ctx, item):
    if item in items.keys():
        await ctx.send(f'Вещь {item} разлагается {items[item]} лет')
    else:
        await ctx.send('такой вещи нет в базе данных')

@bot.command()
async def throw(ctx, item):
    if item in Throw.keys():
        if item == "стекло":
            with open('images/green.png', 'rb') as f:
                picture = discord.File(f)
                await ctx.send(file=picture)
        
        if item == "пластик":
            with open('images/yellow.png', 'rb') as f:
                picture = discord.File(f)
                await ctx.send(file=picture)
        
        if item == "бумага":
            with open('images/blue.png', 'rb') as f:
                picture = discord.File(f)
                await ctx.send(file=picture)
        
        if item == "метал":
            with open('images/red.png', 'rb') as f:
                picture = discord.File(f)
                await ctx.send(file=picture)

        await ctx.send(f'{Throw[item]}')
    else:
        await ctx.send('не знаю')

@bot.command()
async def eco(ctx):
    await ctx.send(f'Рандомный факт: {random.choice(facts)}')

bot.run("Token")
