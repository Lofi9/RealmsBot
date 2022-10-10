import yaml
import hikari

with open('config.yaml', 'r') as file:
    dict = yaml.safe_load(file)
    lst = yaml.dump(dict)
    tkInit = lst.split(":")
    tkEdit = tkInit[2]
    tkFinal = tkEdit[1:73]

bot = hikari.GatewayBot(token=tkFinal)

bot.run()