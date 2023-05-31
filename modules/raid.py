import asyncio #line:1
import random #line:2
import httpx #line:3
async def spam (O00O00O000OO000OO ,O0OOOOOOOO00O0OO0 ,O000O00000000OOO0 ,OO00OO0O00O0O000O ,O0OOO00O00O0OO0OO ):#line:6
    async with O00O00O000OO000OO :#line:7
        for _OOO0O000O0O0OOOOO in range (O0OOO00O00O0OO0OO ):#line:8
            OO0O0OOO00OOO00O0 ={"content":OO00OO0O00O0O000O }#line:11
            O0O00OO00O0OO00OO =await O00O00O000OO000OO .post (f"https://discord.com/api/v9/channels/{O0OOOOOOOO00O0OO0}/messages",headers =O000O00000000OOO0 ,json =OO0O0OOO00OOO00O0 )#line:12
            if O0O00OO00O0OO00OO .status_code ==200 :#line:13
                try :#line:14
                    O0O0000000O00O00O =O0O00OO00O0OO00OO .json ()#line:15
                except ValueError :#line:17
                    pass #line:18
            await asyncio .sleep (0.00001 )#line:21
async def main ():#line:24
    O00O000O000O0OOO0 ="config/tokens.txt"#line:25
    O00O00OO0OO00OOOO ="config/proxy.txt"#line:26
    with open (O00O000O000O0OOO0 ,"r")as O00O000O000O0OOO0 ,open (O00O00OO0OO00OOOO ,"r")as O00O00OO0OO00OOOO :#line:27
        O00OOOO0O0OO00O00 =O00O000O000O0OOO0 .read ().splitlines ()#line:28
        O0OOO0O00O000O0OO =O00O00OO0OO00OOOO .read ().splitlines ()#line:29
    OO0OOO0OO00OOO000 =input ("Enter the channel ID to spam: ")#line:31
    OOO0O00OO0OO00OO0 =input ("Enter the message to spam: ")#line:32
    OOO00OOO0OO00OO0O =int (input ("Enter the number of times to send the message: "))#line:33
    O0O0OO0O00OOO0OO0 =[]#line:35
    for O0OOO0O00OO0O000O ,O00OOOO0O00OOO00O in enumerate (O00OOOO0O0OO00O00 ):#line:36
        O00OO0O000000O000 =random .choice (O0OOO0O00O000O0OO )#line:37
        O0OOOO0OOO0O0OO0O =httpx .AsyncClient (proxies ={"http://":O00OO0O000000O000 ,"https://":O00OO0O000000O000 })#line:38
        O0O0OO000OOO00OO0 ={"Authorization":O00OOOO0O00OOO00O ,}#line:41
        O0O0O0OOOO0OOOO0O =asyncio .create_task (spam (O0OOOO0OOO0O0OO0O ,OO0OOO0OO00OOO000 ,O0O0OO000OOO00OO0 ,OOO0O00OO0OO00OO0 ,OOO00OOO0OO00OO0O ))#line:42
        O0O0OO0O00OOO0OO0 .append (O0O0O0OOOO0OOOO0O )#line:43
    await asyncio .gather (*O0O0OO0O00OOO0OO0 )#line:45
if __name__ =="__main__":#line:47
    asyncio .run (main ())#line:48
