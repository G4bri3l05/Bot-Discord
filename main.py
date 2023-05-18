import discord
import os
import asyncio
import random
from dotenv import load_dotenv
from discord.ext import commands

# Importa as classes que criei para o bot funcionar
from commands.pokedex import pokedex
from commands.help import helpcog
from commands.infos import infoscog
from tasks.erros import erros

load_dotenv()

DISCORD_TOKEN = os.getenv('TOKEN')

intents = discord.Intents().all()
client = discord.Client(intents=intents)
intents.voice_states = True
bot = commands.Bot(command_prefix='$',intents=intents)

# Remove o comando de ajuda padrão, eu decidi criar o meu próprio
bot.remove_command('help')

# Imprime no console quando o bot estiver pronto e chama as funções que eu criei
@bot.event
async def on_ready():
	print("Bot pronto para uso.")
	await pokedex(bot)
	await erros(bot)
	await helpcog(bot)
	await infoscog(bot)

# Evento para deletar mensagens que começam com o prefixo do bot
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$'):  # Verifica se a mensagem começa com o prefixo '$'
        await asyncio.sleep(1)  # Aguarda 1 segundo
        await message.delete()  # Deleta a mensagem do usuário

    await bot.process_commands(message)  # Processa os comandos do bot

if __name__ == "__main__" :
    bot.run(DISCORD_TOKEN)