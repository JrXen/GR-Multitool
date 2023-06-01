import asyncio #line:1
import random #line:2
import httpx #line:3
async def spam (OOO0OOOOOO00OOO0O ,O0OO00OOOOOO00000 ,OO00000000O0OOOOO ,OOO0OO0OO00O0O0O0 ,O00O0O0OOOOOO00O0 ,OO0OO0O0O0O00O000 ):#line:5
    async with OOO0OOOOOO00OOO0O :#line:6
        for _OO0000OOOO000O0OO in range (O00O0O0OOOOOO00O0 ):#line:7
            OOO00O0O00OO0OO0O =' '.join ([f'<@{OOOOOOOO00OOO000O}>'for OOOOOOOO00OOO000O in OO0OO0O0O0O00O000 ])#line:8
            OOOO0OOOO0OOOOOOO ={"content":f"{OOO00O0O00OO0OO0O} {OOO0OO0OO00O0O0O0}"}#line:9
            O0O000000OOOOOO00 =await OOO0OOOOOO00OOO0O .post (f"https://discord.com/api/v9/channels/{O0OO00OOOOOO00000}/messages",headers =OO00000000O0OOOOO ,json =OOOO0OOOO0OOOOOOO )#line:10
            if O0O000000OOOOOO00 .status_code ==200 :#line:11
                try :#line:12
                    _OO0000OOOO000O0OO =O0O000000OOOOOO00 .json ()#line:13
                except ValueError :#line:14
                    pass #line:15
            await asyncio .sleep (0.00001 )#line:16
async def main ():#line:18
    O00000O00O0O0OOOO ="config/tokens.txt"#line:19
    OO0OO0OOOOOO0OO00 ="config/proxy.txt"#line:20
    OOOOOOOO00000OO0O ="config/ids.txt"#line:21
    with open (O00000O00O0O0OOOO ,"r")as OOO00OO0O0OOO0OOO ,open (OO0OO0OOOOOO0OO00 ,"r")as O0O00O0OO0000000O ,open (OOOOOOOO00000OO0O ,"r")as O0O00O0000OO0OO00 :#line:23
        OOO00O00O0O00000O =OOO00OO0O0OOO0OOO .read ().splitlines ()#line:24
        OO0000O00000OOOO0 =O0O00O0OO0000000O .read ().splitlines ()#line:25
        O0OOO0O00O00O0000 =O0O00O0000OO0OO00 .read ().splitlines ()#line:26
    O00O00O0O00000OOO =input ("Enter the channel ID to spam: ")#line:28
    O0O0OOO0OOO00O0OO =input ("Enter the message to spam: ")#line:29
    OOOO0OOOO0OO0000O =int (input ("Enter the number of times to send the message: "))#line:30
    O0O00OOOO00O0OO00 =[]#line:32
    for O0OOO00OOOOO00OOO ,O0O00O0OO0000000O in zip (OOO00O00O0O00000O ,OO0000O00000OOOO0 ):#line:33
        O0OOOOOOO0OOOO0O0 ={"Authorization":O0OOO00OOOOO00OOO }#line:34
        OO00OO0OOO0O0000O =httpx .AsyncClient (proxies ={"http://":O0O00O0OO0000000O ,"https://":O0O00O0OO0000000O })#line:35
        O000O0OOOOO00O000 =asyncio .create_task (spam (OO00OO0OOO0O0000O ,O00O00O0O00000OOO ,O0OOOOOOO0OOOO0O0 ,O0O0OOO0OOO00O0OO ,OOOO0OOOO0OO0000O ,O0OOO0O00O00O0000 ))#line:36
        O0O00OOOO00O0OO00 .append (O000O0OOOOO00O000 )#line:37
    await asyncio .gather (*O0O00OOOO00O0OO00 )#line:39
if __name__ =="__main__":#line:41
    asyncio .run (main ())#line:42
