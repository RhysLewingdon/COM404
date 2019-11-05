from Bot import bot
from SuperBot import superbot
from FlyingBot import flyingbot

bot123 = bot("bot123")
bot123super = superbot("bot123")
bot123flying = flyingbot("bot123")

print("###############################################")
bot123.display_bot()
print("###############################################")
bot123super.display_superbot()
print("###############################################")
bot123flying.display_flyingbot()
print("###############################################")