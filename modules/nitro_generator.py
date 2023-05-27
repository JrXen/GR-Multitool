from time import localtime ,strftime ,sleep #line:1
from colorama import Fore #line:2
import requests #line:3
import random #line:4
import string #line:5
import os #line:6
import json #line:7
class GrGen :#line:10
    def __init__ (O0O00000OOO00O000 ,prox =None ,codes =None ,webhook_url =None ):#line:11
        O0O00000OOO00O000 .type ="boost"#line:12
        O0O00000OOO00O000 .codes =codes #line:13
        O0O00000OOO00O000 .proxies =prox #line:14
        O0O00000OOO00O000 .session =requests .Session ()#line:15
        O0O00000OOO00O000 .prox_api ="https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"#line:16
        O0O00000OOO00O000 .webhook_url =webhook_url #line:17
    def generate (OOOOOOOOO000O00O0 ):#line:19
        os .system ("clear")#line:20
        OO000O0O00O00O00O =[]#line:21
        for _OO0000OOO0000OOO0 in range (int (OOOOOOOOO000O00O0 .codes )):#line:23
            O0000OOO0O0O0OOOO ="".join ([random .choice (string .ascii_letters +string .digits )for O000O00O0O000000O in range (24 )])#line:29
            OO000O0O00O00O00O .append (O0000OOO0O0O0OOOO )#line:30
            print (f"{Fore.GREEN}[{strftime('%H:%M', localtime())}] Generated discord.gift/{O0000OOO0O0O0OOOO}")#line:31
        print (f"{Fore.LIGHTMAGENTA_EX}[{strftime('%H:%M', localtime())}] Successfully generated {OOOOOOOOO000O00O0.codes} codes.")#line:35
        sleep (1.5 )#line:36
        os .system ("clear")#line:37
        if OOOOOOOOO000O00O0 .webhook_url and OO000O0O00O00O00O :#line:38
            OOOOOOOOO000O00O0 .send_to_webhook (OO000O0O00O00O00O )#line:39
        if OO000O0O00O00O00O :#line:40
            OOOOOOOOO000O00O0 .save_to_file (OO000O0O00O00O00O )#line:41
        return True #line:44
    def send_to_webhook (O00OO0OOOO00OOOO0 ,OOO0OO0OO0OOOO0OO ):#line:46
        try :#line:47
            for OO0OO00O0OO00OOO0 in OOO0OO0OO0OOOO0OO :#line:48
                OO0OO0O0OOOOO00O0 ={"content":f"https://discord.gift/{OO0OO00O0OO00OOO0}","username":"Gr Nitro"}#line:52
                O0OOOOOO00OOOOOO0 ={"Content-Type":"application/json"}#line:55
                OO0O0O000O000O0OO =O00OO0OOOO00OOOO0 .session .post (O00OO0OOOO00OOOO0 .webhook_url ,data =json .dumps (OO0OO0O0OOOOO00O0 ),headers =O0OOOOOO00OOOOOO0 )#line:56
                if OO0O0O000O000O0OO .status_code ==204 :#line:57
                    print (f"{Fore.GREEN}[{strftime('%H:%M', localtime())}] Sent to webhook: https://discord.gift/{OO0OO00O0OO00OOO0}")#line:58
                else :#line:59
                    print (f"{Fore.RED}[{strftime('%H:%M', localtime())}] Failed to send to webhook: https://discord.gift/{OO0OO00O0OO00OOO0}")#line:60
        except Exception as OO00OOO0OO000OO00 :#line:61
            print (f"{Fore.RED}[{strftime('%H:%M', localtime())}] Error while sending to webhook: {OO00OOO0OO000OO00}")#line:62
    def save_to_file (O0OO0OO0O00O0OO00 ,O00OO0O00OO0OO000 ):#line:64
        try :#line:65
            with open ("output/nitro.txt","a")as OO00O000OO0O00O0O :#line:66
                for OOO0OOOO0O0O0O000 in O00OO0O00OO0OO000 :#line:67
                    OO00O000OO0O00O0O .write (f"https://discord.gift/{OOO0OOOO0O0O0O000}\n")#line:68
            print (f"{Fore.GREEN}[{strftime('%H:%M', localtime())}] Generated codes saved to 'output/nitro.txt'.")#line:69
        except Exception as OOO0O0OOOO00OO00O :#line:70
            print (f"{Fore.RED}[{strftime('%H:%M', localtime())}] Error while saving generated codes: {OOO0O0OOOO00OO00O}")#line:71
if __name__ =="__main__":#line:74
    while True :#line:75
        prox =input (f"{Fore.LIGHTMAGENTA_EX}[{strftime('%H:%M', localtime())}] Proxies (True, False): ")#line:78
        if prox =="True":#line:79
            scrape_proxy =input (f"{Fore.LIGHTMAGENTA_EX}[{strftime('%H:%M', localtime())}] Scrape proxies (True, False): ")#line:82
        else :#line:83
            scrape_proxy =False #line:84
        codes =input (f"{Fore.LIGHTMAGENTA_EX}[{strftime('%H:%M', localtime())}] Number of codes: ")#line:87
        webhook_url =input (f"{Fore.LIGHTMAGENTA_EX}[{strftime('%H:%M', localtime())}] Webhook URL (leave blank if not sending to webhook): ")#line:90
        generator =GrGen (prox ,codes ,webhook_url )#line:91
        if generator .generate ():#line:92
            break #line:93
