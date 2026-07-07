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
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Uma vez que chamamos o comando duck, o programa chama a função get_duck_image_url '''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
bot.run("token")
