import hikari.guilds
import hikari.messages
import hikari.events
from Ribbit import mainBot

# https://www.hikari-py.dev/hikari/embeds.html

@mainBot.bot.listen()
async def on_event(event: hikari.MemberCreateEvent) -> None:
    # await something something message send event
    # RTFM !!!!!!!