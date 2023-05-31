import asyncio #line:1
import random #line:2
import httpx #line:3
async def spam_webhook (O00O0OOO0OO00OOOO ,O0OOO00OOOOO0O0OO ,O0OO00OO0OO0O00OO ,OOO000O0OOOO00OOO ):#line:6
    async with O00O0OOO0OO00OOOO :#line:7
        for _OO0OO0O0000OOO00O in range (OOO000O0OOOO00OOO ):#line:8
            OO0OO0000OO00O0O0 =await O00O0OOO0OO00OOOO .post (O0OOO00OOOOO0O0OO ,json =O0OO00OO0OO0O00OO )#line:9
            if OO0OO0000OO00O0O0 .status_code ==200 :#line:10
                try :#line:11
                    O0OO00O00000OOOO0 =OO0OO0000OO00O0O0 .json ()#line:12
                except ValueError :#line:14
                    pass #line:15
            await asyncio .sleep (0.00001 )#line:18
async def main ():#line:21
    OOOO000O000000O00 =input ("Enter the webhook URL: ")#line:22
    O0000O0OOOOO00OOO =input ("Enter the message to send: ")#line:23
    O00O000O0OOO0OO00 =int (input ("Enter the number of times to send the message: "))#line:24
    OO0O00O00O0OO00OO =int (input ("Enter the timeout duration (in seconds): "))#line:25
    O000O0OOO0OO0O0O0 ="config/tokens.txt"#line:27
    OOO0000O000O0O000 ="config/proxy.txt"#line:28
    with open (O000O0OOO0OO0O0O0 ,"r")as O000O0OOO0OO0O0O0 ,open (OOO0000O000O0O000 ,"r")as OOO0000O000O0O000 :#line:29
        O0O000O00OOO0000O =O000O0OOO0OO0O0O0 .read ().splitlines ()#line:30
        OO0O00OOOO0O0O0OO =OOO0000O000O0O000 .read ().splitlines ()#line:31
    O0OO0O00OO0OO0OO0 =[]#line:33
    for OOOO00O0OOOO0OOOO ,OO000O00O0O000O00 in enumerate (O0O000O00OOO0000O ):#line:34
        O000O00O0O0OOO00O =random .choice (OO0O00OOOO0O0O0OO )#line:35
        O0O0O0000OOOOO00O =httpx .AsyncClient (proxies ={"http://":O000O00O0O0OOO00O ,"https://":O000O00O0O0OOO00O },timeout =httpx .Timeout (timeout =None ))#line:39
        OOO0OO0OO0O0O0000 ={"content":O0000O0OOOOO00OOO }#line:42
        O0OO000O00OOOOO00 =asyncio .create_task (spam_webhook (O0O0O0000OOOOO00O ,OOOO000O000000O00 ,OOO0OO0OO0O0O0000 ,O00O000O0OOO0OO00 ))#line:43
        O0OO0O00OO0OO0OO0 .append (O0OO000O00OOOOO00 )#line:44
    await asyncio .gather (*O0OO0O00OO0OO0OO0 )#line:46
if __name__ =="__main__":#line:48
    asyncio .run (main ())#line:49
