import yaml
import hikari

with open('config.yaml', 'r') as file:
    dict = yaml.safe_load(file)
    lst = yaml.dump(dict)
    tkInit = lst.split(":")
    tkEdit = tkInit[2]
    tkFinal = tkEdit[1:73]

bot = hikari.GatewayBot(token=tkFinal)

@bot.listen()
async def ping(event: hikari.GuildMessageCreateEvent) -> None:
    if event.is_bot or not event.content:
        return
    if event.content.startswith("rb.ping"):
        await event.message.respond("Pong!")

bot.run()
