import hikari
import os
from dotenv import load_dotenv

load_dotenv()

bot = hikari.GatewayBot(os.getenv('TOKEN'))
bot.run()