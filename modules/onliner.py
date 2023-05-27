import discord #line:1
intents =discord .Intents .default ()#line:3
intents .presences =True #line:4
intents .typing =False #line:5
tokens_file ='config/tokens.txt'#line:7
def set_activity (OOO000O0OOO0OO0O0 ):#line:9
    OOOO0OO000OOO000O =discord .Client (intents =intents )#line:10
    @OOOO0OO000OOO000O .event #line:12
    async def OOO0OOO00O00000OO ():#line:13
        OO00O0000000O0000 =discord .Status .dnd #line:14
        O0O0OOOO0OOO0OOO0 =discord .Activity (name ="GR IS BEST",type =discord .ActivityType .playing ,url ="https://discord.gg/EA6JcYfXfa")#line:19
        await OOOO0OO000OOO000O .change_presence (status =OO00O0000000O0000 ,activity =O0O0OOOO0OOO0OOO0 )#line:20
        print (f"Successfully set custom status for token: {OOO000O0OOO0OO0O0}")#line:21
    @OOOO0OO000OOO000O .event #line:23
    async def OO0OO00OO00000O00 ():#line:24
        print (f"Connected using token: {OOO000O0OOO0OO0O0}")#line:25
    OOOO0OO000OOO000O .run (OOO000O0OOO0OO0O0 ,bot =False )#line:27
while True :#line:29
    with open (tokens_file ,'r')as file :#line:30
        tokens =file .read ().splitlines ()#line:31
    for token in tokens :#line:33
        set_activity (token )#line:34
