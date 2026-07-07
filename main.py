import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá eu sou um bot {bot.user}!')
@bot.command()
async def dado(ctx):
    import random
    await ctx.send(f"🎲 Você tirou {random.randint(1,6)}")
@bot.command()
async def hehe(ctx):
    import random
    risadas = ["KKKKKKKKKKKK",
               "MUAHAHAHAHAHA",
               "HA HA HA HA HA",
               "RS RS RS RS",
               "HUE HUE HUE HUE"
        ]
    await ctx.send(random.choice(risadas))
@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def meme(ctx):
    with open('images/mem1.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("token")
