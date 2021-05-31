prefix = "angelo!" 
token = ""

import discord
from discord.ext import commands

print("Conectando...")

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("\n\nConectado!") 

@bot.command()
async def clear(ctx, limit: int=None):
    passed = 0
    failed = 0
    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == bot.user.id:
            try:
                await msg.delete()
                passed += 1
            except:
                failed += 1
    print(f"Foram deletadas {passed} mensagens com {failed} falhas.")

bot.run(token, bot=False)
