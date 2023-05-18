import discord
import requests
from discord.ext import commands
from deep_translator import GoogleTranslator

class PokedexCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='poke', help='Apresenta os dados do pokemon pesquisado')
    async def poke(self, ctx, pokemon):
        try:
            # URL da API que vou consumir
            # link para ver a documentação se necessário: https://pokeapi.co/
            url = "https://pokeapi.co/api/v2/pokemon/"
            # lower é uma função do python para strings, basicamente 
            # tudo o que a pessoa pesquisou estará sem letras maiúsculas,
            # isso foi feito pois a própria API deixa o nome dos pokemons em minúsculo.
            requisicao = requests.get(url+pokemon.lower())

            pokemon = requisicao.json()

            # Apresentando o nome do pokemon por console por precausão
            # print(pokemon['name'])

            # Pegando os atributos que achei pertinente
            numero = pokemon['id']
            nome = pokemon['name']
            imagem = pokemon['sprites']['versions']['generation-v']['black-white']['animated']['front_default']
            peso = pokemon['weight']/10
            altura = pokemon['height']/10

            # Pegando a lista de elementos do pokemon pesquisado
            lista_elementos = pokemon['types']

            # Apresentando a lista de elementos
            # print(lista_elementos)
            # Contando quantos elementos tem na lista
            qtd_elementos = len(lista_elementos)
            # print(qtd_elementos)

            # Imprimindo  cada item da lista indo de i até a quantia
            i=0
            elementos = ""

            # Salvar o primeiro elemento para mudar de cor de acordo com o tipo
            p_elemento = ""

            while i < qtd_elementos:
                aux = pokemon['types'][i]['type']['name'] 
                p_elemento = pokemon['types'][0]['type']['name']

                elemento = ""
                if(aux == 'bug'):
                    elemento = "Inseto"
                    elementos+="- {}\n".format(elemento.capitalize())
                elif (aux == 'poison'):
                    elemento = "Veneno"
                    elementos+="- {}\n".format(elemento.capitalize())
                elif (aux == 'flying'):
                    elemento = "Voador"
                    elementos+="- {}\n".format(elemento.capitalize())
                elif (aux == 'dark'):
                    elemento = "Sombrio"
                    elementos+="- {}\n".format(elemento.capitalize())
                elif (aux == 'ground'):
                    elemento = "Terra"
                    elementos+="- {}\n".format(elemento.capitalize())
                else:
                    elemento = GoogleTranslator(source='auto', target='pt').translate(aux)
                    elementos+="- {}\n".format(elemento.capitalize())
        
                print(aux+" - "+elemento)
                i = i+1


            # Não são as cores corretas dos jogos, podem modificar para deixar igual se quiser
            color = 0x2ecc71
            if p_elemento == "fire":
                color = 0xe74c3c
            elif p_elemento == "grass":
                color = 0x2ecc71
            elif p_elemento == "water":
                color = 0x3498db
            elif p_elemento == "poison":
                color = 0x9b59b6
            elif p_elemento == "electric":
                color = 0xf1c40f
            elif p_elemento == "ghost":
                color = 0x99aab5
            elif p_elemento == "bug":
                color = 0x1f8b4c
            elif p_elemento == "normal":
                color = 0x1abc9c
            elif p_elemento == "psychic":
                color = 0x71368a
            elif p_elemento == "fairy":
                color = 0xe91e63

            embed = discord.Embed()

            # Capitalize() é uma função de string utilizada para deixar a 
            # primeira letra em maiúscula
            embed.title = "Informações de {}".format(nome.capitalize())

            embed.set_thumbnail(url=imagem)
            embed.description = "**Nr. {}**\nPeso: {} Kg\nAltura: {} m".format(numero,peso,altura)
            embed.add_field(name="Elementos", value="{}".format(elementos))
            embed.color = color
            await ctx.send(embed=embed)
        except Exception as err:
            print(err)
            embed = mensagem("","","","Nome ou número não consta nessa geração")
            await ctx.send(embed = embed)
            return err

async def pokedex(bot):
    await bot.add_cog(PokedexCog(bot))