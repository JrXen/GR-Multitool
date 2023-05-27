import requests #line:1
import ctypes #line:2
def tokenInfo (O0OO000OO000OOOO0 ):#line:4
    ctypes .windll .kernel32 .SetConsoleTitleW ("Gr | Token Info")#line:5
    OOO0OO000OO0OOOO0 ={'Authorization':O0OO000OO000OOOO0 ,'Content-Type':'application/json'}#line:6
    OOOO000000O0O0OOO =requests .get ('https://discord.com/api/v6/users/@me',headers =OOO0OO000OO0OOOO0 )#line:7
    if OOOO000000O0O0OOO .status_code ==200 :#line:8
        O000OO000OOO0OO0O =OOOO000000O0O0OOO .json ()['username']+'#'+OOOO000000O0O0OOO .json ()['discriminator']#line:9
        O0O0O00O0OO0O0O0O =OOOO000000O0O0OOO .json ()['id']#line:10
        OOO00OOOOO0O00OO0 =OOOO000000O0O0OOO .json ().get ('phone')#line:11
        OO00OO0O0OOOO0O00 =OOOO000000O0O0OOO .json ().get ('email')#line:12
        O0000OO00OOOOO000 =OOOO000000O0O0OOO .json ()['mfa_enabled']#line:13
        print (f'''
        [User ID]         {O0O0O00O0OO0O0O0O}
        [User Name]       {O000OO000OOO0OO0O}
        [2 Factor]        {O0000OO00OOOOO000}
        [Email]           {OO00OO0O0OOOO0O00 if OO00OO0O0OOOO0O00 else "None"}
        [Phone number]    {OOO00OOOOO0O00OO0 if OOO00OOOOO0O00OO0 else "None"}
        [Token]           {O0OO000OO000OOOO0}
        ''')#line:21
        input ('Press any key to continue...')#line:22
token =input ("Enter your Discord token: ")#line:24
tokenInfo (token )#line:25
