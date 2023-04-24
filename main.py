import discord
import colorama

from discord import app_commands
from discord.ext import commands    
from discord.ext.commands import Bot 
from os import system 
from os import name
from colorama import *
import random, datetime

id_do_servidor = #ID HERE      #1096086002747064432 / 1060333174493823136

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False #Nós usamos isso para o bot não sincronizar os comandos mais de uma vez

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #Checar se os comandos slash foram sincronizados 
            await tree.sync(guild = discord.Object(id=id_do_servidor)) # Você também pode deixar o id do servidor em branco para aplicar em todos servidores, mas isso fará com que demore de 1~24 horas para funcionar.
            self.synced = True
        print(f"Entramos como {self.user}.")

async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'Bem-vindo ao servidor, {member.mention}!')


aclient = client()
tree = app_commands.CommandTree(aclient)


@tree.command(guild = discord.Object(id=id_do_servidor), name='rolar', description='Rola um dado com o número de lados especificado.')
async def slash3(interaction: discord.Interaction, lados: int):
    resultado = random.randint(1, lados)
    await interaction.response.send_message(f"O resultado do dado de {lados} lados é: {resultado}", ephemeral = False)

@tree.command(guild = discord.Object(id=id_do_servidor), name='termos', description='Confira nossos termos de uso')
async def slash4(interaction: discord.Interaction):
    await interaction.response.send_message(f"```diff\n+        Confira nossos termos de uso em:       +\n``` https://github.com/Cel0xSec/DoSCria-BOT/blob/main/terms-of-service ", ephemeral = False)

@tree.command(guild = discord.Object(id=id_do_servidor), name='privacidade', description='Confira nossa política de privacidade') 
async def slash5(interaction: discord.Interaction):
    await interaction.response.send_message(f"```diff\n+    Confira nossa política de privacidade em:    +``` https://github.com/Cel0xSec/DoSCria-BOT/blob/main/privacy-policy \n```diff\n- Atente-se à política de dados.```  ", ephemeral = False)


@tree.command(guild=discord.Object(id=id_do_servidor), name='ping', description='Verifica o ping do servidor')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong! Latência: {round(aclient.latency * 1000)}ms', ephemeral=False)


@tree.command(guild = discord.Object(id=id_do_servidor), name='kick', description='Expulsa um membro do servidor')
async def kick_member(interaction: discord.Interaction, member: discord.Member):
    await member.kick()
    await interaction.response.send_message(f"O membro {member.mention} foi expulso.", ephemeral=False)

@tree.command(guild = discord.Object(id=id_do_servidor), name='ban', description='Bane um membro do servidor')
async def ban_member(interaction: discord.Interaction, member: discord.Member):
    await member.ban()
    await interaction.response.send_message(f"O membro {member.mention} foi banido.", ephemeral=False)

@bot.command(guild = discord.Object(id=id_do_servidor), name='help', description='exibe ajuda dos cria')
async def helpx(interaction: discord.Interaction):
    embed = discord.Embed(title="Cosm0x Network | Doscria", description=f"Doscria Bot ", color=await random_color())
    embed.set_footer(text=f"© 2023 Copyright Cel0x Security.")
    await interaction.response.send_message(embed=embed, ephemeral=False)

@tree.command(guild = discord.Object(id=id_do_servidor), name='limpar', description='Limpa mensagens em um canal')
async def clear_messages(interaction: discord.Interaction, amount: int):
    channel = interaction.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
        messages.append(message)
    #await interaction.response.send_message(f"{amount} mensagens foram limpas", ephemeral=False)
    await channel.delete_messages(messages)
    
@tree.command(guild=discord.Object(id=id_do_servidor), name='mute', description='Muta um membro do servidor por um tempo específico')
async def mute_member(interaction: discord.Interaction, member: discord.Member, duration: int):
    role = discord.utils.get(member.guild.roles, name='Muted')
    if not role:
        role = await member.guild.create_role(name='Muted', permissions=discord.Permissions(send_messages=False))
        for channel in member.guild.text_channels:
            await channel.set_permissions(role, send_messages=False)
    await member.add_roles(role)
    await interaction.response.send_message(f"O membro {member.mention} foi mutado por {duration} segundos.", ephemeral=False)
    await asyncio.sleep(duration)
    await member.remove_roles(role)
    await interaction.followup.send(f"O membro {member.mention} foi desmutado.", ephemeral=False)




aclient.run('TOKEN')
