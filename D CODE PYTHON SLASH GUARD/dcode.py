import discord
from discord.ext import commands
import os
import sqlite3
import asyncio
import re
from discord_slash import SlashCommand, SlashContext
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.
bot = commands.Bot(command_prefix="", intents=intents)
slash = SlashCommand(bot, sync_commands=True)
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

# SQLite veritabanına bağlan
conn = sqlite3.connect("koruma.db")
cursor = conn.cursor()
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

# Veritabanında rol koruma ayarları için bir tablo oluştur
cursor.execute('''CREATE TABLE IF NOT EXISTS rol_koruma (
                  server_id INTEGER PRIMARY KEY,
                  enabled BOOLEAN
               )''')
# Veritabanında kanal koruma ayarları için bir tablo oluştur
cursor.execute('''CREATE TABLE IF NOT EXISTS kanal_koruma (
                  server_id INTEGER PRIMARY KEY,
                  enabled BOOLEAN
               )''')
# Veritabanında kategori koruma ayarları için bir tablo oluştur
cursor.execute('''CREATE TABLE IF NOT EXISTS kategori_koruma (
                  server_id INTEGER PRIMARY KEY,
                  enabled BOOLEAN
               )''')
# Veritabanında yeni hesap engel ayarları için bir tablo oluştur
cursor.execute('''CREATE TABLE IF NOT EXISTS yeni_hesap_engel (
                  server_id INTEGER PRIMARY KEY,
                  enabled BOOLEAN
               )''')
# Veritabanında bot engel ayarları için bir tablo oluştur
cursor.execute('''CREATE TABLE IF NOT EXISTS bot_engel (
                  server_id INTEGER PRIMARY KEY,
                  enabled BOOLEAN
               )''')
# sürelizamanaşımı tablo
cursor.execute('''CREATE TABLE IF NOT EXISTS susturulan_kullanicilar (
                  kullanici_id INTEGER PRIMARY KEY,
                  rol_id INTEGER,
                  süre INTEGER,
                  sebep TEXT)''')
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

conn.commit()
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

bad_words = ["orosbu çocu", "orosbu çocuğu", "orospu çocuğu", "siktir git", "sq", "döl", "piç", "göt veren", "döl israfı", "göt", "mal", "gerizekalı", "andaval", "am", "amcımı yala", "yarrak", "yarramı yala", "yarak", "orospu", "orosbu", "kavanı sikem", "sik", "sikem"]
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.watching, name="D CODE TR YOUTUBE")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f'{bot.user.name} İsimli Botunuz Aktif Sorunsuz Şekilde Discorda Bağlandı - D CODE TR YOUTUBE :)')
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

@slash.slash(name="ping", description="Botun Ping Değerini ve Mesaj Gecikmesini Gösterir. | D CODE YOUTUBE © ")
async def ping(ctx):
    bot_latency = round(bot.latency * 1000)  # milisaniye cinsinden
    ##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

    if ctx.message:
        message_latency = round((ctx.created_at - ctx.message.created_at).total_seconds() * 1000)  # milisaniye cinsinden
    else:
        message_latency = None
    ##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

    response = f"Ping değeri: {bot_latency}ms"
    if message_latency is not None:
        response += f"\nMesaj gecikmesi: {message_latency}ms"
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

    await ctx.send(response)
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

@slash.slash(name="rolkoruma", description="Rol koruma açma veya kapatma. | D CODE YOUTUBE ©")
async def rol_koruma(ctx, action: str):
    if ctx.author.guild_permissions.administrator:
        if action.lower() == "aç":
            cursor.execute("INSERT OR REPLACE INTO rol_koruma (server_id, enabled) VALUES (?, ?)", (ctx.guild.id, 1))
            conn.commit()##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

            await ctx.send("Rol koruma sistemi açıldı.")
        elif action.lower() == "kapat":
            cursor.execute("INSERT OR REPLACE INTO rol_koruma (server_id, enabled) VALUES (?, ?)", (ctx.guild.id, 0))
            conn.commit()##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

            await ctx.send("Rol koruma sistemi kapatıldı.")
        else:##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

            await ctx.send("Geçersiz eylem. `/rolkoruma aç` veya `/rolkoruma kapat` kullanın.")
    else:
        await ctx.send("Bu komutu kullanma izniniz yok.")
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

@slash.slash(name="kanalkoruma", description="Kanal koruma açma veya kapatma. | D CODE YOUTUBE ©")
async def kanal_koruma(ctx, action: str):
    if ctx.author.guild_permissions.administrator:
        if action.lower() == "aç":
            cursor.execute("INSERT OR REPLACE INTO kanal_koruma (server_id, enabled) VALUES (?, ?)", (ctx.guild.id, 1))
            conn.commit()##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

            await ctx.send("Kanal koruma sistemi açıldı.")
        elif action.lower() == "kapat":
            cursor.execute("INSERT OR REPLACE INTO kanal_koruma (server_id, enabled) VALUES (?, ?)", (ctx.guild.id, 0))
            conn.commit()##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

            await ctx.send("Kanal koruma sistemi kapatıldı.")
        else:##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

            await ctx.send("Geçersiz eylem. `/kanalkoruma aç` veya `/kanalkoruma kapat` kullanın.")
    else:##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

        await ctx.send("Bu komutu kullanma izniniz yok.")
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

@slash.slash(name="kategorikoruma", description="Kategori koruma açma veya kapatma. | D CODE YOUTUBE ©")
async def kategori_koruma(ctx, action: str):
    if ctx.author.guild_permissions.administrator:
        if action.lower() == "aç":
            cursor.execute("INSERT OR REPLACE INTO kategori_koruma (server_id, enabled) VALUES (?, ?)", (ctx.guild.id, 1))
            conn.commit()
            await ctx.send("Kategori koruma sistemi açıldı.")
        elif action.lower() == "kapat":
            cursor.execute("INSERT OR REPLACE INTO kategori_koruma (server_id, enabled) VALUES (?, ?)", (ctx.guild.id, 0))
            conn.commit()
            await ctx.send("Kategori koruma sistemi kapatıldı.")
        else:
            await ctx.send("Geçersiz eylem. `/kategorikoruma aç` veya `/kategorikoruma kapat` kullanın.")
    else:
        await ctx.send("Bu komutu kullanma izniniz yok.")
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

@bot.event
async def on_guild_channel_delete(channel):
    if isinstance(channel, discord.CategoryChannel):
        await asyncio.sleep(1)
        for text_channel in channel.text_channels:
            await channel.guild.create_text_channel(text_channel.name, category=channel, overwrites=text_channel.overwrites, reason="Kanal koruma")
        for voice_channel in channel.voice_channels:
            await channel.guild.create_voice_channel(voice_channel.name, category=channel, overwrites=voice_channel.overwrites, reason="Kanal koruma")
        category_overwrites = {role: overwrite for role, overwrite in channel.overwrites.items() if isinstance(role, discord.Role)}
        await channel.guild.create_category(channel.name, overwrites=category_overwrites, reason="Kategori koruma")

@bot.event
async def on_guild_channel_delete(channel):
    if isinstance(channel, discord.TextChannel) or isinstance(channel, discord.VoiceChannel):
        await asyncio.sleep(1)
        if isinstance(channel, discord.TextChannel):
            new_channel = await channel.category.create_text_channel(channel.name, overwrites=channel.overwrites, reason="Kanal koruma")
        else:
            new_channel = await channel.category.create_voice_channel(channel.name, overwrites=channel.overwrites, reason="Kanal koruma")
        await new_channel.edit(position=channel.position)
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

@slash.slash(name="ban", description="Kullanıcıyı sunucudan yasaklar. | D CODE YOUTUBE ©")
async def ban(ctx, member: discord.Member, reason: str = "Neden belirtilmedi"):
    if ctx.author.guild_permissions.ban_members:
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} sunucudan yasaklandı. Sebep: {reason}")
    else:
        await ctx.send("Bu komutu kullanma izniniz yok.")

@slash.slash(name="kick", description="Kullanıcıyı sunucudan atar. | D CODE YOUTUBE ©")
async def kick(ctx, member: discord.Member, reason: str = "Neden belirtilmedi"):
    if ctx.author.guild_permissions.kick_members:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} sunucudan atıldı. Sebep: {reason}")
    else:
        await ctx.send("Bu komutu kullanma izniniz yok.")
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

@slash.slash(name="yavasmod", description="Kanalda yavaş modu ayarlar. | D CODE YOUTUBE ©")
async def yavasmod(ctx, suresi: int):
    if ctx.author.guild_permissions.manage_channels:
        if suresi >= 0:
            await ctx.channel.edit(slowmode_delay=suresi)
            await ctx.send(f"Bu kanalda yavaş mod {suresi} saniye olarak ayarlandı.")
        else:
            await ctx.send("Yavaş mod süresi negatif olamaz.")
    else:
        await ctx.send("Bu komutu kullanma izniniz yok.")
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

@slash.slash(name="temizle", description="Belirli bir kanaldan mesajları siler. | D CODE YOUTUBE ©")
async def temizle(ctx, miktar: int):
    if ctx.author.guild_permissions.manage_messages:
        if miktar > 0:
            await ctx.channel.purge(limit=miktar + 1)
            response = await ctx.send(f"{miktar} mesaj silindi.")
            await ctx.channel.send("Başarı ile mesaj silindi.")
            await asyncio.sleep(5)
            await response.delete()
        else:##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

            await ctx.send("Silinecek mesaj miktarı pozitif olmalıdır.", hidden=True)
    else:
        await ctx.send("Bu komutu kullanma izniniz yok.", hidden=True)
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

@bot.event
async def on_ready():
    ses_kanal_id = 1144627426631098449
    ses_kanalı = bot.get_channel(ses_kanal_id)

    if ses_kanalı and ses_kanalı.type == discord.ChannelType.voice:
        voice_client = await ses_kanalı.connect()
        print(f"{ses_kanalı.name} kanalına katıldım! | D CODE YOUTUBE ©")
    else:
        print("Geçerli bir ses kanalı bulunamadı. | D CODE YOUTUBE © ")
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

@slash.slash(name="yenihesapengel", description="Yeni hesap engellemeyi açma veya kapatma. | D CODE YOUTUBE © ")
async def yeni_hesap_engel(ctx, action: str):
    if ctx.author.guild_permissions.administrator:
        if action.lower() == "aç":
            cursor.execute("INSERT OR REPLACE INTO yeni_hesap_engel (server_id, enabled) VALUES (?, ?)", (ctx.guild.id, 1))
            conn.commit()
            await ctx.send("Yeni hesap engelleme sistemi açıldı. 14 günden önce açılmış hesaplar yasaklanacak.")
        elif action.lower() == "kapat":
            cursor.execute("INSERT OR REPLACE INTO yeni_hesap_engel (server_id, enabled) VALUES (?, ?)", (ctx.guild.id, 0))
            conn.commit()
            await ctx.send("Yeni hesap engelleme sistemi kapatıldı.")
        else:
            await ctx.send("Geçersiz eylem. `/yenihesapengel aç` veya `/yenihesapengel kapat` kullanın.")
    else:
        await ctx.send("Bu komutu kullanma izniniz yok.")

@bot.event##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

async def on_member_join(member):
    yeni_hesap_engel = cursor.execute("SELECT enabled FROM yeni_hesap_engel WHERE server_id=?", (member.guild.id,)).fetchone()
    
    if yeni_hesap_engel and yeni_hesap_engel[0] == 1:
        if (member.created_at - member.created_at).days < 14:
            await member.ban(reason="Yeni hesap engel koruması")
            await member.send("Sunucuya katılmak için 14 günden önce açılmış bir hesaba ihtiyacınız var.")
            return

@slash.slash(name="botengel", description="Bot ekleme engellemeyi açma veya kapatma. | D CODE YOUTUBE ©")
async def bot_engel(ctx, action: str):
    if ctx.author.guild_permissions.administrator:
        if action.lower() == "aç":
            cursor.execute("INSERT OR REPLACE INTO bot_engel (server_id, enabled) VALUES (?, ?)", (ctx.guild.id, 1))
            conn.commit()##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

            await ctx.send("Bot ekleme engelleme sistemi açık. Artık botlar sunucuya eklenemeyecek.")
        elif action.lower() == "kapat":
            cursor.execute("INSERT OR REPLACE INTO bot_engel (server_id, enabled) VALUES (?, ?)", (ctx.guild.id, 0))
            conn.commit()
            await ctx.send("Bot ekleme engelleme sistemi kapatıldı.")##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

        else:
            await ctx.send("Geçersiz eylem. `/botengel aç` veya `/botengel kapat` kullanın.")
    else:
        await ctx.send("Bu komutu kullanma izniniz yok.")

@bot.event##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

async def on_member_join(member):
    bot_engel = cursor.execute("SELECT enabled FROM bot_engel WHERE server_id=?", (member.guild.id,)).fetchone()
    
    if bot_engel and bot_engel[0] == 1 and member.bot:
        await member.ban(reason="Bot ekleme engel koruması")

# Küfür engeli açık mı?
kufur_engel_acik = False

@slash.slash(name="küfürengel", description="Küfür engellemeyi aç veya kapat. | D CODE YOUTUBE ©")
async def kufur_engel(ctx: SlashContext, action: str):
    global kufur_engel_acik
    if ctx.author.guild_permissions.administrator:
        if action.lower() == "aç":##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

            kufur_engel_acik = True
            await ctx.send("Küfür engelleme sistemi açıldı.")
        elif action.lower() == "kapat":
            kufur_engel_acik = False
            await ctx.send("Küfür engelleme sistemi kapatıldı.")
        else:
            await ctx.send("Geçersiz eylem. `/küfürengel aç` veya `/küfürengel kapat` kullanın.")
    else:
        await ctx.send("Bu komutu kullanma izniniz yok.")
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    if kufur_engel_acik:##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

        content = message.content.lower()
        for word in bad_words:
            if word in content:
                await message.delete()
                await message.channel.send(f"{message.author.mention}, küfür içerdiğinden dolayı mesajın silindi.")
                ##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

                mute_role = discord.utils.get(message.guild.roles, name="Muted")
                if mute_role:
                    await message.author.add_roles(mute_role)
                    await asyncio.sleep(300)
                    await message.author.remove_roles(mute_role)
                ##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

                break
    
    await bot.process_commands(message)
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

@slash.slash(name="hesap", description="Etiketlenen kullanıcının hesap bilgilerini gösterir. | D CODE YOUTUBE ©")
async def hesap(ctx: SlashContext, member: discord.Member = None):
    if member is None:
        member = ctx.author
    ##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

    # Kullanıcının Discord'a katılım tarihi
    joined_discord_at = member.created_at.strftime("%Y-%m-%d %H:%M:%S")
    
    # Kullanıcının sunucuya katılım tarihi
    joined_server_at = member.joined_at.strftime("%Y-%m-%d %H:%M:%S")
    
    # Kullanıcının rozetleri
    badges = [f"{badge.name} ({badge.value})" for badge in member.public_flags.all()]
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

    if not badges:
        badges = ["Rozet yok."]
    ##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

    # Hesap bilgilerini gönder
    embed = discord.Embed(title=f"{member.display_name} Hesap Bilgileri", color=discord.Color.blurple())
    embed.add_field(name="Discord'a Katılım Tarihi", value=joined_discord_at, inline=False)
    embed.add_field(name="Sunucuya Katılım Tarihi", value=joined_server_at, inline=False)
    embed.add_field(name="Rozetler", value="\n".join(badges), inline=False)
    ##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

    await ctx.send(embed=embed)
# Uyarıların saklandığı bir sözlük oluştur
uyarilar = {}
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

@slash.slash(name="uyarıekle", description="Kullanıcıya uyarı ekle | D CODE YOUTUBE ©")
async def uyarı_ekle(ctx: SlashContext, member: discord.Member, *, uyarı_mesajı: str):
    # Kullanıcının "MESAJLARI_YÖNET" yetkisine sahip olup olmadığını kontrol et
    if ctx.author.guild_permissions.manage_messages:
        # Etiketlenen kullanıcının ID'sini kullanarak uyarı mesajını sakla
        uyarilar[member.id] = uyarı_mesajı
        # Kullanıcıya DM olarak uyarı mesajını gönder
        try:
            await member.send(f"Şu yetkili tarafından uyarıldınız: {ctx.author.display_name}\n\nNeden: {uyarı_mesajı}")
            await ctx.send(f"{member.mention} kullanıcısına başarıyla uyarı gönderildi.")
        except discord.Forbidden:
            await ctx.send("Kullanıcıya DM gönderilemedi. Kullanıcının DM'lerini engellemiş olabilir.")
    else:##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

        await ctx.send("Bu komutu kullanma izniniz yok.")
# Otomatik selamlaşma durumu
selam_acik = False

@slash.slash(name="saas", description="Otomatik selamlaşmayı aç veya kapat. | D CODE YOUTUBE ©")
async def saas(ctx: SlashContext, durum: str):
    global selam_acik
    if ctx.author.guild_permissions.manage_messages:
        if durum.lower() == "aç":
            selam_acik = True
            await ctx.send("Otomatik selamlaşma açıldı.")
        elif durum.lower() == "kapat":
            selam_acik = False
            await ctx.send("Otomatik selamlaşma kapatıldı.")
        else:
            await ctx.send("Geçersiz durum. `/saas aç` veya `/saas kapat` kullanın.")
    else:
        await ctx.send("Bu komutu kullanma izniniz yok.")

@bot.event
async def on_message(message):
    if message.author.bot:##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

        return
    
    if selam_acik:
        selam_mesaji = message.content.lower()
        if selam_mesaji in ["sa", "sea", "SA", "selamın aleyküm"]:
            await message.channel.send(f"Aleyküm Selam, {message.author.mention}! Hoş geldin.")
    
    await bot.process_commands(message)
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

# /rolal komutu##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

@slash.slash(name="rolal", description="Kullanıcıdan rol al | D CODE YOUTUBE ©", options=[
    {"name": "kullanici", "description": "Rolü alınacak kullanıcı", "type": 6, "required": True},##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

    {"name": "rol", "description": "Alınacak rol", "type": 8, "required": True}
])##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

async def rolal(ctx: SlashContext, kullanici: discord.Member, rol: discord.Role):
    await kullanici.remove_roles(rol)##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

    await ctx.send(f'{kullanici.mention} kullanıcısından {rol.name} rolü alındı. | D CODE YOUTUBE ©')

# /rolver komutu
@slash.slash(name="rolver", description="Kullanıcıya rol ver | D CODE YOUTUBE © ", options=[
    {"name": "kullanici", "description": "Role verilecek kullanıcı", "type": 6, "required": True},
    {"name": "rol", "description": "Verilecek rol", "type": 8, "required": True}
])##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

async def rolver(ctx: SlashContext, kullanici: discord.Member, rol: discord.Role):
    await kullanici.add_roles(rol)
    await ctx.send(f'{kullanici.mention} kullanıcısına {rol.name} rolü verildi. | D CODE YOUTUBE ©')
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

# Hata işleme
@rolal.error
@rolver.error##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Bu komutu kullanma izniniz yok. | D CODE YOUTUBE ©")
    elif isinstance(error, commands.BadArgument):##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

        await ctx.send("Geçersiz argümanlar. Kullanım: /rolal @etiket @rol veya /rolver @etiket @rol | D CODE YOUTUBE ©")
    else:##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

        print(error)

##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.
# /sürelizamanaşımı komutu
@slash.slash(name="sürelizamanaşımı", description="Kullanıcıyı süreli olarak sustur ve izinleri kaldır | D CODE YOUTUBE © ", options=[
    {"name": "kullanici", "description": "Susturulacak kullanıcı", "type": 6, "required": True},
    {"name": "sebep", "description": "Susturma sebebi", "type": 3, "required": True},##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.
    {"name": "süre", "description": "Susturma süresi (dakika cinsinden)", "type": 4, "required": True}
])##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

async def sürelizamanaşımı(ctx: SlashContext, kullanici: discord.Member, sebep: str, süre: int):
    try:
        # Kullanıcının mevcut rollerini kaydet
        mevcut_roll = kullanici.roles##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

        # Veritabanına kaydet
        cursor.execute("INSERT INTO susturulan_kullanicilar (kullanici_id, rol_id, süre, sebep) VALUES (?, ?, ?, ?)",
                       (kullanici.id, mute_rol.id, süre, sebep))##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

        conn.commit()

        # Mute rolünü al veya oluştur
        mute_rol = discord.utils.get(ctx.guild.roles, name="mute")
        if mute_rol is None:##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

            mute_rol = await ctx.guild.create_role(name="mute", reason="Süreli susturma için otomatik rol oluşturuldu | D CODE YOUTUBE ©")
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

        # Kullanıcıyı mute rolü ile sustur
        await kullanici.add_roles(mute_rol)
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

        # Kullanıcının izinlerini kaldır
        await kullanici.send(f"Siz {sebep} nedeniyle {süre} dakika boyunca susturuldunuz.  | D CODE YOUTUBE ©")
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

        # Süre sonunda kullanıcının susturmasını kaldır
        await asyncio.sleep(süre * 60)  # Süre dakika cinsinden olduğu için saniyeye çeviriyoruz
        await kullanici.remove_roles(mute_rol)
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

        # Kullanıcının önceki rollerini geri ver
        await kullanici.edit(roles=mevcut_roll)
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

        await ctx.send(f"{kullanici.mention}, zaman aşımı işlemi başarıyla gerçekleştirildi. | D CODE YOUTUBE ©")
    except discord.errors.Forbidden:
        pass##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.

    except Exception as e:
        print(f"Hata oluştu: {e}")
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.



bot.run('')
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.
##BU ALTYAPI https://www.youtube.com/c/DCodetr YOUTUBE KANALINA AİTTİR DİSCORD HESABI OLARAK deathh8113 KİŞİSİNE AİTTİR discord.gg/yZ46S4vJ7P DİSCORD SUNUCUMUZ  22.08.2023 TARİHİNDE YAPIMA BAŞLANMIŞTIR.
