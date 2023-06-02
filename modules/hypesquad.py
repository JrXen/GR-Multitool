import requests #line:1
houses =["Bravery","Brilliance","Balance"]#line:3
def check_token (OOOOOOOOO0O00OOOO ):#line:5
    OO00OO0OO0O0O0O00 ='https://discord.com/api/v9/users/@me'#line:6
    OOO0OO00OOOO00O00 ={'Authorization':OOOOOOOOO0O00OOOO }#line:9
    O00O0000OO0OO0OO0 =requests .get (OO00OO0OO0O0O0O00 ,headers =OOO0OO00OOOO00O00 )#line:10
    OO0O00000OO0000OO =O00O0000OO0OO0OO0 .status_code ==200 #line:11
    return OO0O00000OO0000OO #line:12
def change_hypesquad (OOOOO00O000OOOOO0 ,OO0OO0O000000OOO0 ):#line:14
    if not check_token (OOOOO00O000OOOOO0 ):#line:15
        raise ValueError ("Invalid token, please check your token.")#line:16
    OO00OO000O00OOO0O ='https://discord.com/api/v9/hypesquad/online'#line:18
    OO0O0O0OOOOOO00O0 ={'Authorization':OOOOO00O000OOOOO0 }#line:21
    O0OOO0O0O00O0OOOO ={"house_id":OO0OO0O000000OOO0 }#line:24
    OOOOOO00OO00O0OOO =requests .post (OO00OO000O00OOO0O ,headers =OO0O0O0OOOOOO00O0 ,json =O0OOO0O0O00O0OOOO )#line:25
    O0OOOOO00O0O0OOO0 =OOOOOO00OO00O0OOO .status_code ==204 #line:26
    return O0OOOOO00O0O0OOO0 #line:27
def main ():#line:29
    O00OOOOOO0O00000O =input ("Enter your Discord token: ")#line:30
    O0O000OO0OO0OOOO0 =None #line:33
    while O0O000OO0OO0OOOO0 is None :#line:34
        print (f"\n[🏠] Choose your hypesquad house:")#line:35
        for OO0O000O00000O0OO ,OO0OO0O0000OOOO00 in enumerate (houses ):#line:36
            print (f"    {OO0O000O00000O0OO+1}. {OO0OO0O0000OOOO00}")#line:37
        try :#line:38
            O0O000OO0OO0OOOO0 =int (input ("House: "))#line:39
            if O0O000OO0OO0OOOO0 <1 or O0O000OO0OO0OOOO0 >len (houses ):#line:40
                O0O000OO0OO0OOOO0 =None #line:41
                print ("Please provide a valid number!")#line:42
        except ValueError :#line:43
            O0O000OO0OO0OOOO0 =None #line:44
            print ("Please provide a valid number!")#line:45
    print (f"\n[?] Changing to {houses[O0O000OO0OO0OOOO0-1]}...")#line:48
    OO00O00OOO00O0O0O =change_hypesquad (O00OOOOOO0O00000O ,O0O000OO0OO0OOOO0 )#line:49
    if OO00O00OOO00O0O0O :#line:51
        print (f"[✅] Successfully changed to {houses[O0O000OO0OO0OOOO0-1]}!")#line:52
    else :#line:53
        print (f"[-] Failed to change to {houses[O0O000OO0OO0OOOO0-1]}, please try again later!")#line:54
    input("Press any key to quit.")        
if __name__ =="__main__":#line:56
    main ()#line:57
