import crescent
import os
from dotenv import load_dotenv

load_dotenv()
bot = crescent.Bot(os.getenv('TOKEN'))
bot.run()