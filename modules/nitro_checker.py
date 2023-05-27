import requests #line:1
import json #line:2
def check_nitro_codes (O0O0O0O0OOO0O0O00 ,O00OOO00000O00OOO ):#line:4
    O00000OO00O0OO0OO =requests .Session ()#line:5
    if O0O0O0O0OOO0O0O00 :#line:7
        OOOOO0OO00OOO000O ={"http":O0O0O0O0OOO0O0O00 [0 ],"https":O0O0O0O0OOO0O0O00 [0 ]}#line:8
        print (f"Using proxy: {O0O0O0O0OOO0O0O00[0]}")#line:9
    else :#line:10
        OOOOO0OO00OOO000O =None #line:11
        print ("Using current IP")#line:12
    with open ("output/nitro.txt","r")as O000O000000000OO0 :#line:14
        OOOO0000OO00OO000 =O000O000000000OO0 .read ().splitlines ()#line:15
    for OOO00O0OOOO000O00 in OOOO0000OO00OO000 :#line:17
        try :#line:18
            OOO0000OO0O0O00O0 =OOO00O0OOOO000O00 .split ("/")[-1 ]#line:19
            OOOOO0O0OOO0O0O0O =O00000OO00O0OO0OO .get (f"https://discordapp.com/api/v9/entitlements/gift-codes/{OOO0000OO0O0O00O0}",proxies =OOOOO0OO00OOO000O )#line:20
            if OOOOO0O0OOO0O0O0O .status_code ==200 :#line:21
                print (f"Valid Nitro code: {OOO00O0OOOO000O00}")#line:22
                send_to_webhook (O00OOO00000O00OOO ,OOO00O0OOOO000O00 )#line:23
            else :#line:24
                print (f"Invalid Nitro code: {OOO00O0OOOO000O00}")#line:25
        except Exception as O0OOO00OOOO0O00OO :#line:26
            print (f"Error occurred while checking Nitro code: {O0OOO00OOOO0O00OO}")#line:27
def send_to_webhook (OO0OO0O00OO00O0O0 ,OO0O0000O0O0OO000 ):#line:29
    try :#line:30
        OO0OOOO0O00O00OOO ={"content":OO0O0000O0O0OO000 ,"username":"Nitro Checker"}#line:34
        OO00OO0OO0O00O0O0 ={"Content-Type":"application/json"}#line:37
        O00OOO0OOO0OOOO0O =requests .post (OO0OO0O00OO00O0O0 ,data =json .dumps (OO0OOOO0O00O00OOO ),headers =OO00OO0OO0O00O0O0 )#line:38
        if O00OOO0OOO0OOOO0O .status_code ==204 :#line:39
            print (f"Sent Nitro code to webhook: {OO0O0000O0O0OO000}")#line:40
        else :#line:41
            print (f"Failed to send Nitro code to webhook: {OO0O0000O0O0OO000}")#line:42
    except Exception as O0OO0OOO000OOOOOO :#line:43
        print (f"Error occurred while sending Nitro code to webhook: {O0OO0OOO000OOOOOO}")#line:44
if __name__ =="__main__":#line:47
    proxies_file ="config/proxy.txt"#line:48
    webhook_url =input ("Enter the webhook URL: ")#line:49
    with open (proxies_file ,"r")as file :#line:51
        proxies =file .read ().splitlines ()#line:52
    if proxies :#line:54
        check_nitro_codes (proxies ,webhook_url )#line:55
    else :#line:56
        check_nitro_codes ([],webhook_url )#line:57
