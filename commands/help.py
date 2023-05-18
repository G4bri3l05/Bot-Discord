import discord
from discord.ext import commands

class AjudaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ajudinha', help='Apresenta os comandos do seu bot')
    async def help(self, ctx):
        if ctx.author.guild_permissions.administrator:
            description = '$ajudinha - Apresenta os comandos do seu bot\n'
            description += '$criador - Mostra informações do bot e do criador dele\n'
            description += '$apresentar - Apresenta dados do servidor\n'
            description += '$infobot - Apresenta informações sobre o bot e os servidores que ele está\n'
            description += '$poke <nome do pokemon ou número> - Pesquisar pokemon\n'
            description += '$embed <titulo> <descrição> - Envia uma mensagem personalizada no chat\n'
            description += '$usuario <@usuario> - Mostra informações sobre um usuário\n'
        else:
            description = '$ajudinha - Apresenta os comandos do seu bot\n'
            description += '$criador - Mostra informações do bot e do criador dele\n'
            description += '$infobot - Apresenta informações sobre o bot e os servidores que ele está\n'
            description += '$poke <nome do pokemon ou número> - Pesquisar pokemon\n'

        embed = discord.Embed()
        embed.title = "Lista de Comandos:"
        embed.description = description
        embed.color = 0x3498db
        await ctx.send(embed=embed)

    # Comando para enviar uma embed personalizada
    @commands.command(name='embed', help='Cria um embed personalizado')
    @commands.has_permissions(administrator=True)
    async def embed(self, ctx, title, description):
        embed = discord.Embed(title=title, description=description, color=discord.Color.blue())
        await ctx.send(embed=embed)

    # função que mostra as cores disponíveis para a embed personalizada
    def mensagem(title,url1,url2,description):

        default = 0
        teal = 0x1abc9c
        dark_teal = 0x11806a
        green = 0x2ecc71
        dark_green = 0x1f8b4c
        blue = 0x3498db
        dark_blue = 0x206694
        purple = 0x9b59b6
        dark_purple = 0x71368a
        magenta = 0xe91e63
        dark_magenta = 0xad1457
        gold = 0xf1c40f
        dark_gold = 0xc27c0e
        orange = 0xe67e22
        dark_orange = 0xa84300
        red = 0xe74c3c
        dark_red = 0x992d22
        lighter_grey = 0x95a5a6
        dark_grey = 0x607d8b
        light_grey = 0x979c9f
        darker_grey = 0x546e7a
        blurple = 0x7289da
        greyple = 0x99aab5

        embed = discord.Embed()
        embed.color = magenta
        embed.title = title
        embed.set_thumbnail(url=url1)
        embed.set_image(url=url2)
        embed.description = description
        return embed

async def helpcog(bot):
    await bot.add_cog(AjudaCog(bot))
