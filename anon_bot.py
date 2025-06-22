import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Бот запущен как {bot.user}")

@bot.event
async def on_message(message):
    if message.guild is None and not message.author.bot:
        channel = bot.get_channel(int(os.getenv("CHANNEL_ID")))
        if channel:
            embed = discord.Embed(title="📩 Анонимное сообщение", description=message.content, color=0x00ffcc)
            await channel.send(embed=embed)
    await bot.process_commands(message)

@bot.command()
async def report(ctx, *, message):
    channel = bot.get_channel(int(os.getenv("CHANNEL_ID")))
    if channel:
        embed = discord.Embed(title="📢 Анонимная жалоба", description=message, color=0xff5555)
        embed.set_footer(text="Отправлено через команду !report")
        await channel.send(embed=embed)
        await ctx.send("✅ Жалоба отправлена модераторам.")
    else:
        await ctx.send("⚠️ Не удалось найти канал для отправки.")

keep_alive()
bot.run(os.getenv("DISCORD_TOKEN"))
