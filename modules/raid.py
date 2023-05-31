import asyncio #line:1
import random #line:2
import httpx #line:3
async def spam (O000OO00O0O00000O ,O000OOOOO0O0OOOOO ,O0O0O00O0OO00OO0O ,OO0OOOOO0OO0O00OO ,OOO0O00OOOOO0OO00 ):#line:6
    async with O000OO00O0O00000O :#line:7
        for _OOOO0O0OO000O0000 in range (OOO0O00OOOOO0OO00 ):#line:8
            O0000O00OO0OO00O0 ={"content":OO0OOOOO0OO0O00OO }#line:11
            OO000OOOO0OO00OOO =await O000OO00O0O00000O .post (f"https://discord.com/api/v9/channels/{O000OOOOO0O0OOOOO}/messages",headers =O0O0O00O0OO00OO0O ,json =O0000O00OO0OO00O0 )#line:12
            if OO000OOOO0OO00OOO .status_code ==200 :#line:13
                try :#line:14
                    OO00O000O0O00O0O0 =OO000OOOO0OO00OOO .json ()#line:15
                except ValueError :#line:17
                    pass #line:18
            await asyncio .sleep (0.00001 )#line:21
async def main ():#line:24
    O000OOOOO00OO00OO ="config/tokens.txt"#line:25
    OO00OOOOO0O000O00 ="config/proxy.txt"#line:26
    with open (O000OOOOO00OO00OO ,"r")as O000OOOOO00OO00OO ,open (OO00OOOOO0O000O00 ,"r")as OO00OOOOO0O000O00 :#line:27
        O0O0OOO0O00O0000O =O000OOOOO00OO00OO .read ().splitlines ()#line:28
        OOOOOO0O00O0OO00O =OO00OOOOO0O000O00 .read ().splitlines ()#line:29
    OO0OOOOO000OOO00O =input ("Enter the channel ID to spam: ")#line:31
    OO0OO00000OO000O0 =input ("Enter the message to spam: ")#line:32
    OOOO000OO0OO00000 =int (input ("Enter the number of times to send the message: "))#line:33
    O000O00O00OO0OO00 =[]#line:35
    for O0O00O000OO0OO000 ,O0OO00OO0O0OOO000 in enumerate (O0O0OOO0O00O0000O ):#line:36
        OO0OO0000O0OO0O00 =random .choice (OOOOOO0O00O0OO00O )#line:37
        O000O000OO00OO0O0 =httpx .AsyncClient (proxies ={"http://":OO0OO0000O0OO0O00 ,"https://":OO0OO0000O0OO0O00 })#line:38
        O0OO0O0OOOOO0OO00 ={"Authorization":O0OO00OO0O0OOO000 ,}#line:41
        OOOOOOOO0OOO00O00 =asyncio .create_task (spam (O000O000OO00OO0O0 ,OO0OOOOO000OOO00O ,O0OO0O0OOOOO0OO00 ,OO0OO00000OO000O0 ,OOOO000OO0OO00000 ))#line:42
        O000O00O00OO0OO00 .append (OOOOOOOO0OOO00O00 )#line:43
    await asyncio .gather (*O000O00O00OO0OO00 )#line:45
if __name__ =="__main__":#line:47
    asyncio .run (main ())#line:48
