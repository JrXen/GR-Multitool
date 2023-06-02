import requests #line:1
def check_token (OOO0OOOOOOO0OO00O ):#line:3
    OO00O00OOOO0O00O0 ='https://discord.com/api/v9/users/@me'#line:4
    O0O0OO0OO000000OO ={'Authorization':OOO0OOOOOOO0OO00O }#line:7
    OOOO0OO0OOO000OO0 =requests .get (OO00O00OOOO0O00O0 ,headers =O0O0OO0OO000000OO )#line:8
    O0OOOOO00OO00O0OO =OOOO0OO0OOO000OO0 .status_code ==200 #line:9
    return O0OOOOO00OO00O0OO #line:10
def main ():#line:12
    O00O0O0OO00OO0OOO ='config/tokens.txt'#line:13
    with open (O00O0O0OO00OO0OOO ,'r')as O0OOO000O000000O0 :#line:15
        OO0O00OOOO0OOOOO0 =O0OOO000O000000O0 .read ().splitlines ()#line:16
    for O0O0OO0OOO0OOOOOO in OO0O00OOOO0OOOOO0 :#line:18
        O00OO0O00OO00OOOO =check_token (O0O0OO0OOO0OOOOOO )#line:19
        if O00OO0O00OO00OOOO :#line:20
            print (f'Token {O0O0OO0OOO0OOOOOO} is valid.')#line:21
        else :#line:22
            print (f'Token {O0O0OO0OOO0OOOOOO} is invalid.')#line:23

    input("Press any key to quit.")

if __name__ =="__main__":#line:25
    main ()#line:26
