import disnake
from disnake.ext import commands
from config import config

bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all())


@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready to work!")


@bot.event
async def on_member_join(member):
    role = disnake.utils.get(member.guild.roles, id=825725400520458260)
    channel = bot.get_channel(720741595254620323)

    embed = disnake.Embed(
        title="Новый член стаи!",
        description=f"{member.name}",
        color=0xffffff
    )

    await member.add_roles(role)
    await channel.send(embed=embed)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        

@bot.command(name="hello")
async def hello(context):
    await context.send("hello")

bot.run(config.settings["bot"]["TOKEN"])