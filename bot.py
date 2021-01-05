import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound, MissingPermissions, MissingRole, MissingRequiredArgument

import asyncio
import logging
from config import *
import os

# # LOGGING
# logging.basicConfig(level=logging.INFO)

with open('token.txt', 'r') as f:
    token = f.read()

print('Bot is connecting...')

class bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix=kwargs.pop('command_prefix', ('T.', 't.')),
                         case_insensitive=True,
                         **kwargs)

    # EVENTS
    async def on_ready(self):
        """Prints 'Bot is live!' to the console when the bot is ready"""
        await self.change_presence(status=discord.Status.online,
                                   activity=discord.Activity(type=discord.ActivityType.playing, name='use prefix "v."'))

        # loads all cogs in the cogs folder
        for cog in os.listdir('./cogs'):
            if cog.endswith('.py'):
                self.load_extension(f"cogs.{cog[:-3]}")

        print(f"Bot is live!")

    async def process_commands(self, message):
        if message.author.bot:
            return

        ctx = await self.get_context(message=message)

        await self.invoke(ctx)
 
rver!")

    async def on_command_error(self, ctx, error):
        """When someone tries to access a unknown command"""
        if isinstance(error, CommandNotFound):
            return await ctx.send("Command Not Found!")
        elif isinstance(error, MissingPermissions):
            return await ctx.send("You can't use that command. Reason: Missing Perms")
        elif isinstance(error, MissingRole):
            return await ctx.send("You can't use that command. Reason: Missing Role")
        elif isinstance(error, MissingRequiredArgument):
            return await ctx.send("Missing Required Parameter")
        else:
            raise error

    async def setup(self, **kwargs):
        try:
            await self.start(token, **kwargs)
        except KeyboardInterrupt:
            await self.close()


bot = bot()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.setup())
