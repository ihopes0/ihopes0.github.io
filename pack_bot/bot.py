import disnake
from disnake.ext import commands
from config import config

bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all())


@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready to work!")

bot.run(config.settings["bot"]["TOKEN"])