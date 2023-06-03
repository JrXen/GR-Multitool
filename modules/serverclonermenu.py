from os import system #line:1
import psutil #line:2
import os #line:3
from pypresence import Presence #line:4
import time #line:5
import sys #line:6
import discord #line:7
import subprocess #line:8
import json #line:9
from rich .table import Table #line:10
from rich .console import Console #line:11
from rich .style import Style #line:12
from rich .panel import Panel as RichPanel #line:13
from rich .text import Text #line:14
import asyncio #line:15
import colorama #line:16
from colorama import Fore ,init ,Style #line:17
import platform #line:18
import inquirer #line:19
from cloner import Clone #line:20
version ='0.3'#line:22
clones ={'Clones_teste_feitos':0 }#line:23
versao_python =sys .version .split ()[0 ]#line:24
console =Console ()#line:26
def clearall ():#line:29
    system ('clear')#line:30
    print (f"""{Style.BRIGHT}{Fore.RED}
{' ' * 40}  /$$$$$$  /$$$$$$$ 
{' ' * 40} /$$__  $$| $$__  $$
{' ' * 40}| $$  \__/| $$  \ $$
{' ' * 40}| $$ /$$$$| $$$$$$$/
{' ' * 40}| $$|_  $$| $$__  $$
{' ' * 40}| $$  \ $$| $$  \ $$
{' ' * 40}|  $$$$$$/| $$  | $$
{' ' * 40}\______/ |__/  |__/

{' ' * 42}made by GR#1111
{Style.RESET_ALL}{Fore.MAGENTA}{Fore.RESET}""")#line:42
client =discord .Client ()#line:45
if os =="Windows":#line:46
    system ("cls")#line:47
else :#line:48
    print (chr (27 )+"[2J")#line:49
    clearall ()#line:50
while True :#line:51
    token =input (f'{Style.BRIGHT}{Fore.MAGENTA}Enter your token to proceed{Style.RESET_ALL}{Fore.RESET}\n >')#line:54
    guild_s =input (f'{Style.BRIGHT}{Fore.MAGENTA}Enter the ID of the server you wish to replicate{Style.RESET_ALL}{Fore.RESET}\n >')#line:57
    guild =input (f'{Style.BRIGHT}{Fore.MAGENTA}Enter the ID of the destination server to paste the copied server{Style.RESET_ALL}{Fore.RESET}\n>')#line:60
    clearall ()#line:61
    print (f'{Style.BRIGHT}{Fore.GREEN}The entered values are:')#line:62
    token_length =len (token )#line:63
    hidden_token ="*"*token_length #line:64
    print (f'{Style.BRIGHT}{Fore.GREEN}Your token: {Fore.YELLOW}{hidden_token}{Style.RESET_ALL}{Fore.RESET}')#line:67
    print (f'{Style.BRIGHT}{Fore.GREEN}Server ID to replicate: {Fore.YELLOW}{guild_s}{Style.RESET_ALL}{Fore.RESET}')#line:70
    print (f'{Style.BRIGHT}{Fore.GREEN}ID of the server you want to paste the copied server: {Fore.YELLOW}{guild}{Style.RESET_ALL}{Fore.RESET}')#line:73
    confirm =input (f'{Style.BRIGHT}{Fore.MAGENTA}Are the values correct? {Fore.YELLOW}(Y/N){Style.RESET_ALL}{Fore.RESET}\n >')#line:76
    if confirm .upper ()=='Y':#line:77
        if not guild_s .isnumeric ():#line:78
            clearall ()#line:79
            print (f'{Style.BRIGHT}{Fore.RED}The server ID to replicate should only contain numbers.{Style.RESET_ALL}{Fore.RESET}')#line:82
            continue #line:83
        if not guild .isnumeric ():#line:84
            clearall ()#line:85
            print (f'{Style.BRIGHT}{Fore.RED}The destination server ID should only contain numbers.{Style.RESET_ALL}{Fore.RESET}')#line:88
            continue #line:89
        if not token .strip ()or not guild_s .strip ()or not guild .strip ():#line:90
            clearall ()#line:91
            print (f'{Style.BRIGHT}{Fore.RED}One or more fields are blank.{Style.RESET_ALL}{Fore.RESET}')#line:94
            continue #line:95
        if len (token .strip ())<3 or len (guild_s .strip ())<3 or len (guild .strip ())<3 :#line:97
            clearall ()#line:98
            print (f'{Style.BRIGHT}{Fore.RED}One or more fields have less than 3 characters.{Style.RESET_ALL}{Fore.RESET}')#line:101
            continue #line:102
        break #line:103
    elif confirm .upper ()=='N':#line:105
        clearall ()#line:106
else :#line:107
    clearall ()#line:108
    print (f'{Style.BRIGHT}{Fore.RED}Invalid option. Please enter Y or N.{Style.RESET_ALL}{Fore.RESET}')#line:111
input_guild_id =guild_s #line:112
output_guild_id =guild #line:113
token =token #line:114
clearall ()#line:115
@client .event #line:118
async def on_ready ():#line:119
    try :#line:120
        OOO00O00OOOOO0O00 =time .time ()#line:121
        global clones #line:122
        O0O0OOO00000000O0 =Table (title ="Versions",style ="bold magenta")#line:123
        O0O0OOO00000000O0 .add_column ("Component")#line:124
        O0O0OOO00000000O0 .add_column ("Version")#line:125
        O0O0OOO00000000O0 .add_row ("Cloner",str (version ),style ="cyan")#line:126
        O0O0OOO00000000O0 .add_row ("Discord.py",str (discord .__version__ ),style ="cyan")#line:127
        O0O0OOO00000000O0 .add_row ("Python",str (versao_python ),style ="cyan")#line:128
        console .print (RichPanel (O0O0OOO00000000O0 ))#line:129
        console .print (RichPanel (f" Successful authentication",style ="bold green",width =47 ))#line:133
        console .print (RichPanel (f" Hello, {client.user.name}! Cloning will start momentarily...",style ="bold blue",width =47 ))#line:138
        print (f"\n")#line:139
        OOOOO0O0000O0OOO0 =[inquirer .List ('clone_emojis',message ="\033[35mDo you want to clone emojis?\033[0m",choices =['\033[32mYes\033[0m','\033[31mNo\033[0m'],),]#line:146
        OO0OOO00O0000000O =inquirer .prompt (OOOOO0O0000O0OOO0 )#line:147
        OO000O0O000O000OO =client .get_guild (int (input_guild_id ))#line:148
        O0OOO000O0OO000OO =client .get_guild (int (output_guild_id ))#line:149
        await Clone .guild_edit (O0OOO000O0OO000OO ,OO000O0O000O000OO )#line:150
        await Clone .channels_delete (O0OOO000O0OO000OO )#line:151
        await Clone .roles_create (O0OOO000O0OO000OO ,OO000O0O000O000OO )#line:152
        await Clone .categories_create (O0OOO000O0OO000OO ,OO000O0O000O000OO )#line:153
        await Clone .channels_create (O0OOO000O0OO000OO ,OO000O0O000O000OO )#line:154
        O000O0OO0O0OO0O0O =time .time ()#line:155
        O0O000OO0O0OO0OOO =O000O0OO0O0OO0O0O -OOO00O00OOOOO0O00 #line:156
        OO00OO0000000OO00 =time .strftime ("%M:%S",time .gmtime (O0O000OO0O0OO0OOO ))#line:157
        if OO0OOO00O0000000O ['clone_emojis']=='\033[32mYes\033[0m':#line:158
            print (f"{Style.BRIGHT}{Fore.YELLOW}Cloning emojis in progress. This may take a few moments.")#line:161
            await asyncio .sleep (20 )#line:162
            await Clone .emojis_create (O0OOO000O0OO000OO ,OO000O0O000O000OO )#line:163
            print (f"{Style.BRIGHT}{Fore.BLUE}The server was successfully cloned in {Fore.YELLOW}{OO00OO0000000OO00}{Style.RESET_ALL}")#line:166
            print (f"{Style.BRIGHT}{Fore.BLUE}Visit our Discord server: {Fore.YELLOW}https://discord.gg/Qvf5NUtqMg{Style.RESET_ALL}")#line:169
            clones ['Clones_teste_feitos']+=1 #line:170
            with open ('saves.json','w')as OOO0O00000OOO0O0O :#line:171
                json .dump (clones ,OOO0O00000OOO0O0O )#line:172
            print (f"{Style.BRIGHT}{Fore.BLUE}Finalizing process and ending session on account {Fore.YELLOW}{client.user}")#line:175
            await client .close ()#line:176
    except discord .LoginFailure :#line:177
        print ("Could not authenticate to the account. Check if the token is correct.")#line:180
    except discord .Forbidden :#line:181
        print ("Could not clone due to insufficient permissions.")#line:182
    except discord .HTTPException :#line:183
        print ("An error occurred communicating with the Discord API.")#line:184
    except discord .NotFound :#line:185
        print ("Could not find one of the copy elements (channels, categories, etc.).")#line:188
    except Exception as OOO000OOOO0000OO0 :#line:189
        print (Fore .RED +"An error occurred:",OOO000OOOO0000OO0 )#line:190
try :#line:193
    client .run (token ,bot =False )#line:194
except discord .LoginFailure :#line:195
    print (Fore .RED +"The inserted token is invalid")#line:196
    print (Fore .YELLOW +"\n\nThe code will be restarted in 10 seconds. If you don't want to wait, refresh the page and start again.")#line:200
    print (Style .RESET_ALL )#line:201
    time .sleep (10 )#line:202
    subprocess .Popen (["python",__file__ ])#line:203
    print (Fore .RED +"Restarting...")#line:204
