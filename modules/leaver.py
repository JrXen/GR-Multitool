import requests #line:1
import time #line:2
token =input ("Enter your Discord token: ")#line:4
exceptions =open ("exceptions.txt").read ().splitlines ()#line:5
proxies =open ("config/proxy.txt").read ().splitlines ()#line:6
proxy_index =0 #line:7
def get_proxy ():#line:9
    global proxy_index #line:10
    O0OO00OOO0000000O =proxies [proxy_index ]#line:11
    proxy_index =(proxy_index +1 )%len (proxies )#line:12
    return {'http':O0OO00OOO0000000O ,'https':O0OO00OOO0000000O }#line:13
try :#line:15
    print (f"\n[+] Using proxy: {proxies[proxy_index]}")#line:16
    print (f"\n[+] Leave all available guilds")#line:18
    guildsIds =requests .get ("https://discord.com/api/v9/users/@me/guilds",headers ={'Authorization':token },proxies =get_proxy ()).json ()#line:19
    for guild in guildsIds :#line:20
        if guild ["id"]not in exceptions :#line:21
            try :#line:22
                response =requests .delete (f'https://discord.com/api/v9/users/@me/guilds/'+guild ['id'],headers ={'Authorization':token },proxies =get_proxy ())#line:26
                if response .status_code ==204 :#line:27
                    print (f"\t[!] Left this server: "+guild ['name'])#line:28
                else :#line:29
                    print (f"\t[!] Failed to leave the server: "+guild ['name'])#line:30
            except Exception as e :#line:31
                print (f"\t[!] The following error occurred: {e}")#line:32
        else :#line:33
            print (f"[!] Did not leave {guild['name']} as it appeared in exceptions")#line:34
    print (f"\n[+] Deleted all available guilds for this token: {token}")#line:35
except Exception as e :#line:36
    print (f"\t[!] Token: {token} | The following error occurred: {e}")#line:37
proxy_index =0 