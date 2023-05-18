import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingPermissions, MissingRequiredArgument, BadArgument, CommandNotFound
import asyncio

class ErrosCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener(name='on_command_error')
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            message = await ctx.send('Você não tem permissão para usar esse comando!')
            await asyncio.sleep(5)
            await message.delete()

        elif isinstance(error, MissingRequiredArgument):
            message = await ctx.send('Você não passou todos os argumentos necessários!')
            await asyncio.sleep(5)
            await message.delete()

        elif isinstance(error, BadArgument):
            message = await ctx.send('Você passou algum argumento errado!')
            await asyncio.sleep(5)
            await message.delete()

        elif isinstance(error, CommandNotFound):
            message = await ctx.send('Esse comando não existe!')
            await asyncio.sleep(5)
            await message.delete()

        else:
            message = await ctx.send('Ocorreu um erro inesperado!')
            await asyncio.sleep(5)
            await message.delete()

async def erros(bot):
    await bot.add_cog(ErrosCog(bot))