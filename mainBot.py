import hikari

bot = hikari.GatewayBot(token="")

@bot.listen()
async def ping(event: hikari.GuildMessageCreateEvent) -> None:
    if event.is_bot or not event.content:
        return
    if event.content.startswith("rb.ping"):
        await event.message.respond("Pong!")

bot.run()