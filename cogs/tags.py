from discord.ext import commands
import discord
import asyncio

from datetime import datetime

import sqlite3

conn = sqlite3.connect('tags.db')
c = conn.cursor()


def setup(bot):
    bot.add_cog(TagCommands(bot=bot))


class TagCommands(commands.Cog, name="Tags"):
    def __init__(self, bot):
        self.bot = bot

    def cog_check(self, ctx):
        if ctx.guild is None:
            return False
        return True

    @commands.group(invoke_without_command=True)
    async def tag(self, ctx, *, name: lambda inp: inp.lower()):
        """Main tag group."""

        #c.execute(f'UPDATE tags SET uses = uses + 1 WHERE name = "{name}" ')

        #conn.commit()
        

        c.execute(f'SELECT content FROM tags WHERE (guildID = {ctx.message.guild.id} AND name = "{name.strip()}" ) ')
        await ctx.send(f"{c.fetchone()[0]}")
        

    @tag.command()
    async def info(self, ctx, *, name: lambda inp: inp.lower()):
        """Get information regarding the specified tag."""
        #c.execute('SELECT authorID  FROM tags WHERE ')
        #conn.commit()
        
        

    @tag.command()
    async def create(self, ctx, *,inp: lambda inp: inp.lower(),):
        """Create a new tag."""

        name = inp.split(',,')[0].strip()
        text = inp.split(',,')[1].strip()
        

        c.execute('SELECT * FROM tags')

        i = 0

        for record in c.fetchall():
            if name == record[1]:
                i += 1

        if i:
            await ctx.send('Tag with that name already exists!')

        else:
            c.execute('INSERT INTO tags (guildID, name, content, creator, created_at) VALUES (?, ?, ?, ?, ?)', (ctx.message.guild.id, name, text, f'{ctx.author}', datetime.now()))
            conn.commit()
            

            await ctx.send(f'Tag succesfully created by: {ctx.message.author}')
        



    @tag.command()
    async def list(self, ctx, member: commands.MemberConverter = None):
        """List your existing tags."""

        


        

    @tag.command()
    async def edit(self, ctx, name: lambda inp: inp.lower(), *, text: str):
        """Edit a tag"""
        c.execute('')
        conn.commit()
       

    @tag.command()
    async def delete(self, ctx, *, name: lambda inp: inp.lower()):
        """Delete a tag."""
        c.execute(f'DELETE FROM tags WHERE (guildID = {ctx.message.guild.id} AND name = "{name.strip()}" )')
        conn.commit()
        await ctx.send(f'Tag succesfully deleted by: {ctx.message.author}')
        

    @tag.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def search(self, ctx, *, term: str):
        """Search for a tag given a search term. PostgreSQL syntax must be used for the search."""
        c.execute('')
        conn.commit()
       

    @tag.command()
    async def rename(self, ctx, name: lambda inp: inp.lower(), *, new_name: lambda inp: inp.lower()):
        """Rename a tag."""
        c.execute('')
        conn.commit()

        

    @tag.command()
    async def append(self, ctx, name: lambda inp: inp.lower(), *, text: str):
        """Append some content to the end of a tag"""
        c.execute('')
        conn.commit()
        

