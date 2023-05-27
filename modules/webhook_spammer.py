import httpx #line:1
import asyncio #line:2
ANSI_PURPLE ="\u001b[35m"#line:5
ANSI_RESET ="\u001b[0m"#line:7
async def spam_webhook (O00OO000O00OOOOO0 ,O00O0OO00OO00OO00 ,OO00000OOOO0O00O0 ):#line:9
    try :#line:10
        async with httpx .AsyncClient (proxies ={"https://":O00O0OO00OO00OO00 })as O0O00O0O00OOOO00O :#line:11
            O00OO00O00OO0OO0O =False #line:12
            while True :#line:13
                OO0OOOOO000OO0000 =await O0O00O0O00OOOO00O .post (O00OO000O00OOOOO0 ,json ={"content":OO00000OOOO0O00O0 })#line:14
                if OO0OOOOO000OO0000 .status_code ==204 and not O00OO00O00OO0OO0O :#line:15
                    O00OO00O00OO0OO0O =True #line:16
                await asyncio .sleep (0.5 )#line:17
    except httpx .HTTPError :#line:18
        pass #line:19
async def main ():#line:21
    O00O0000OOO00000O =input ("Enter the webhook URL: ")#line:22
    O0OOO00O00O0OO0OO ="config/proxy.txt"#line:23
    O0OOO000OOOOOO0OO =input ("Enter the message you want to send: ")#line:24
    with open (O0OOO00O00O0OO0OO ,"r")as OOOOO00O0000OO00O :#line:28
        OOOOOO0OO0O0O0O0O =OOOOO00O0000OO00O .read ().splitlines ()#line:29
    if not OOOOOO0OO0O0O0O0O :#line:32
        print ("No proxies found. Using current IP address without a proxy.")#line:33
        await spam_webhook (O00O0000OOO00000O ,"",O0OOO000OOOOOO0OO )#line:34
    else :#line:35
        O00O0OO00OO00O00O =[]#line:36
        for O0000O0OOO0OO000O in OOOOOO0OO0O0O0O0O :#line:37
            OO0O0O0O0OO00OO0O ="http://"+O0000O0OOO0OO000O #line:38
            O00O0OO00OO00O00O .append (spam_webhook (O00O0000OOO00000O ,OO0O0O0O0OO00OO0O ,O0OOO000OOOOOO0OO ))#line:39
        print (f"Using {len(OOOOOO0OO0O0O0O0O)} proxy(s) for the request.")#line:41
        print (f"{ANSI_PURPLE}SPAMMING!{ANSI_RESET}")#line:42
        await asyncio .gather (*O00O0OO00OO00O00O )#line:43
if __name__ =="__main__":#line:46
    asyncio .run (main ())#line:47
