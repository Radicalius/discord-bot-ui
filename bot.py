import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='/')

@bot.command("status")
async def status(ctx):
    servers = {"Google": "UP", "Yahoo": "DOWN", "Bing": "UP"}
    message = await ctx.send(embed=discord.Embed(
          title="Server Status - Google",
          description="""
```diff
+ Server is UP
```
"""
    ))
    await message.add_reaction('\u25c0')
    #await message.add_reaction('\u25b8')
    await message.add_reaction('\u25b6')

    i = 0
    while True:
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60.0)
        except TimeoutError:
            break

        if str(user) != "shopkeeper#4781":
            if reaction.emoji == "\u25c0":
                i += 1
            #if reaction.emoji == "\u25c1":
            #    pass
            if reaction.emoji == "\u25b6":
                i -= 1
            i %= 3

            server = list(servers.keys())[i]
            await message.edit(embed=discord.Embed(
                 title="Server Status - {0}".format(server),
                 description="""
            ```diff
 {0} Server is {1}
            ```
            """.format("+" if servers[server] == "UP" else "-", servers[server])
            ))

        await message.remove_reaction(reaction.emoji, user)
    await message.clear_reactions()

bot.run(os.environ["BOT_CODE"])
