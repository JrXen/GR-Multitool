import discord #line:1
from discord .ext import commands #line:2
import asyncio #line:3
intents =discord .Intents .default ()#line:5
intents .typing =False #line:6
intents .presences =False #line:7
bot =commands .Bot (command_prefix ="!",intents =intents )#line:9
@bot .event #line:11
async def on_ready ():#line:12
    print (f"Bot connected as {bot.user}")#line:13
@bot .command (name ='start')#line:15
async def start (OOO0O0O0000O0OO00 ):#line:16
    global stop_flag #line:17
    await OOO0O0O0000O0OO00 .send ("Please enter the base name for the new channels.")#line:19
    def OO0O000O000O0O00O (O00000000OOOO0OOO ):#line:21
        return O00000000OOOO0OOO .author ==OOO0O0O0000O0OO00 .author and O00000000OOOO0OOO .channel ==OOO0O0O0000O0OO00 .channel #line:22
    try :#line:24
        O0O000000000OOOO0 =await bot .wait_for ('message',timeout =60.0 ,check =OO0O000O000O0O00O )#line:25
        O000OOO0O0OOO0OOO =O0O000000000OOOO0 .content #line:26
        await OOO0O0O0000O0OO00 .send ("How many channels would you like to create?")#line:28
        try :#line:30
            O0O000000000OOOO0 =await bot .wait_for ('message',timeout =60.0 ,check =OO0O000O000O0O00O )#line:31
            O0000000OOOOO00O0 =int (O0O000000000OOOO0 .content )#line:32
            OO0O00OO000000OOO =OOO0O0O0000O0OO00 .guild #line:34
            O0000OO0O0O00O0O0 =OO0O00OO000000OOO .text_channels #line:37
            O0O00OOOOO000OOOO =[O0O0OO000O00O0O00 for O0O0OO000O00O0O00 in O0000OO0O0O00O0O0 if O0O0OO000O00O0O00 !=OOO0O0O0000O0OO00 .channel and O0O0OO000O00O0O00 .name .startswith (O000OOO0O0OOO0OOO )]#line:40
            await asyncio .gather (*[O0OO0OO0OO00OO000 .delete ()for O0OO0OO0OO00OO000 in O0O00OOOOO000OOOO ])#line:41
            await OOO0O0O0000O0OO00 .send ("Please enter the messages you want to send (separated by new lines).")#line:43
            O0O000000000OOOO0 =await bot .wait_for ('message',timeout =60.0 ,check =OO0O000O000O0O00O )#line:44
            O00O0O0O000O00OOO =O0O000000000OOOO0 .content .split ('\n')#line:45
            stop_flag =False #line:47
            await send_messages_to_channels (OO0O00OO000000OOO ,O000OOO0O0OOO0OOO ,O0000000OOOOO00O0 ,O00O0O0O000O00OOO )#line:48
            await OOO0O0O0000O0OO00 .send (f"{O0000000OOOOO00O0} new channels have been created and messages are being sent!")#line:50
        except ValueError :#line:51
            await OOO0O0O0000O0OO00 .send ("Invalid input for the number of channels. Operation cancelled.")#line:52
    except asyncio .TimeoutError :#line:53
        await OOO0O0O0000O0OO00 .send ("No base name provided. Operation cancelled.")#line:54
async def send_messages_to_channels (OO00OOOO0O0O0O0O0 ,O0O0O00O00O0O0OOO ,O00O0O000O0OO0000 ,O00O0000OO0OOO00O ):#line:56
    global stop_flag ,running_tasks #line:57
    O00O0O000O00O0O00 =[]#line:59
    for O000000OO0OOO0O0O in range (1 ,O00O0O000O0OO0000 +1 ):#line:61
        if stop_flag :#line:62
            break #line:63
        OO0OOOOO0OO0OO000 =f"{O0O0O00O00O0O0OOO}-{O000000OO0OOO0O0O}"#line:65
        OO0OOO00O0O00OO0O =await OO00OOOO0O0O0O0O0 .create_text_channel (OO0OOOOO0OO0OO000 )#line:66
        OO0OO0O0O00OOO00O =asyncio .create_task (send_messages_to_channel (OO0OOO00O0O00OO0O ,O00O0000OO0OOO00O ))#line:67
        O00O0O000O00O0O00 .append (OO0OO0O0O00OOO00O )#line:68
    running_tasks .extend (O00O0O000O00O0O00 )#line:70
    await asyncio .gather (*O00O0O000O00O0O00 )#line:71
async def send_messages_to_channel (O0OOO0O0O000O0OOO ,O0O00OOOOOO000OOO ):#line:73
    global stop_flag #line:74
    while not stop_flag :#line:76
        for OOOOOO0O0O00OO0O0 in O0O00OOOOOO000OOO :#line:77
            await asyncio .sleep (0 )#line:78
            await O0OOO0O0O000O0OOO .send (OOOOOO0O0O00OO0O0 )#line:79
@bot .command (name ='dc')#line:82
async def delete_channels (OO0O000OOO000OOO0 ):#line:83
    O0OOO0OO0000O0OOO =OO0O000OOO000OOO0 .guild #line:84
    O0O000O0O0000OO00 =O0OOO0OO0000O0OOO .text_channels #line:85
    O0OO0O0O0O0OOOOO0 =[O00OO00O00OOOO0OO for O00OO00O00OOOO0OO in O0O000O0O0000OO00 if O00OO00O00OOOO0OO !=OO0O000OOO000OOO0 .channel ]#line:88
    await asyncio .gather (*[O0O0OOO0O00O000O0 .delete ()for O0O0OOO0O00O000O0 in O0OO0O0O0O0OOOOO0 ])#line:91
    await OO0O000OOO000OOO0 .send ("All existing channels, except the command invocation channel, have been deleted.")#line:93
bot_token =input ("Enter your bot token: ")#line:95
bot .run (bot_token )#line:96
