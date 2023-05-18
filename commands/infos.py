import discord
from discord.ext import commands

class InformacaoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='criador', help='Mostra informações do criador do bot')
    async def criador(self, ctx):
        embed = discord.Embed()

        # Cor azul do cartão
        embed.color = 0x3498db

        embed.title = "Criador"
        embed.description = "Criador por Gabriel B. Araujo (15/05/2023)"
        embed.add_field(name="Sobre mim", value="Fui criado como forma de treino na semana da computação e também sou o mascote da turma de BCC de 2023 do IFSP de Pres. Epitácio, e continuarei sendo desenvolvido para que eu possa ser um bot mais completo e útil para todos.")
        embed.add_field(name="Perfil do Criador", value="[D4rk#8248](https://discord.com/users/477956505380061184)")
        await ctx.send(embed=embed)

    # Comando para apresentar dados do servidor
    @commands.command(name='apresentar', help='Apresenta dados do servidor')
    @commands.has_permissions(administrator=True)
    async def apresentar(self, ctx):
        url = "https://raw.githubusercontent.com/G4bri3l05/Images/main/"
        url_thumbnail = url + "capy2.gif"
        url_imagem = url + "capy1.gif"

        nome_server = ctx.guild.name
        criador = ctx.guild.owner
        qtd_membros = ctx.guild.member_count
        qtd_membros_real = len([m for m in ctx.guild.members if not m.bot])
        qtd_bots = qtd_membros - qtd_membros_real

        embed = discord.Embed()
        embed.color = 0x3498db
        embed.title = "Dados sobre o servidor:"
        embed.description = "Servidor: {}\nCriado por: {}\nQuantia de membros: {}\nQuantia de bots: {}\n".format(
            nome_server, criador, qtd_membros_real, qtd_bots)
        embed.set_thumbnail(url=url_thumbnail)
        embed.set_image(url=url_imagem)

        message = await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        qtd_membros_real = len([m for m in guild.members if not m.bot])
        qtd_bots = guild.member_count - qtd_membros_real
        await self.atualizar_embed(guild, qtd_membros_real, qtd_bots)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = member.guild
        qtd_membros_real = len([m for m in guild.members if not m.bot])
        qtd_bots = guild.member_count - qtd_membros_real
        await self.atualizar_embed(guild, qtd_membros_real, qtd_bots)

    async def atualizar_embed(self, guild, qtd_membros_real, qtd_bots):
        url = "https://raw.githubusercontent.com/G4bri3l05/Images/main/"
        url_thumbnail = url + "capy2.gif"
        url_imagem = url + "capy1.gif"

        nome_server = guild.name
        criador = guild.owner

        embed = discord.Embed()
        embed.color = 0x3498db
        embed.title = "Dados sobre o servidor:"
        embed.description = "Servidor: {}\nCriado por: {}\nQuantia de membros: {}\nQuantia de bots: {}\n".format(
            nome_server, criador, qtd_membros_real, qtd_bots)
        embed.set_thumbnail(url=url_thumbnail)
        embed.set_image(url=url_imagem)

        channel = guild.system_channel
        message = await channel.fetch_message(self.message_id)
        await message.edit(embed=embed)

    # Comando para mostrar informações de um usuário
    @commands.command(name='usuario', help='Mostra informações sobre um usuário')
    @commands.has_permissions(administrator=True)
    async def usuario(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        username = member.name
        discriminator = member.discriminator
        avatar_url = member.avatar.url
        joined_at = member.joined_at.strftime("%d/%m/%Y %H:%M:%S")
        created_at = member.created_at.strftime("%d/%m/%Y %H:%M:%S")
        roles = [role.name for role in member.roles[1:]]

        embed = discord.Embed()
        embed.title = f"Informações do usuário: {username}"
        embed.set_thumbnail(url=avatar_url)
        embed.add_field(name="Nome", value=f"{username}#{discriminator}", inline=False)
        embed.add_field(name="Entrou no servidor em", value=joined_at, inline=False)
        embed.add_field(name="Conta criada em", value=created_at, inline=False)
        embed.add_field(name="Cargos", value=', '.join(roles) if roles else "Nenhum cargo", inline=False)

        await ctx.send(embed=embed)

    @commands.command(name='infobot', help='Apresenta informações sobre o bot')
    async def infobot(self, ctx):
        # Quantia de servidores que o bot está
        aux = 0
        var_nome_servers = ""
        for guild in self.bot.guilds:
            var_nome_servers += "-" + guild.name + "\n"
            aux += 1

        embed = discord.Embed()
        embed.color = 0x3498db
        embed.title = "Dados sobre o Bot:"
        embed.description = "Quantia de servidores que o bot está: {}".format(aux)
        embed.add_field(name="Servidores em que está:", value=var_nome_servers)
        await ctx.send(embed=embed)

async def infoscog(bot):
    await bot.add_cog(InformacaoCog(bot))
