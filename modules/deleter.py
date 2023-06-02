import requests #line:1
def send_message (O000OOOOOOOO0OO0O ,O0000O0O0O00O000O ):#line:3
    OO00000OOOOOO0O00 =requests .post (O000OOOOOOOO0OO0O ,json ={"content":O0000O0O0O00O000O })#line:4
    if OO00000OOOOOO0O00 .status_code ==204 :#line:5
        print ("Message sent successfully!")#line:6
    else :#line:7
        print ("Failed to send the message with status code:",OO00000OOOOOO0O00 .status_code )#line:8
def delete_webhook (OOO0OOO0O00O0O0O0 ):#line:10
    O0OO0O0OOO0OO0000 =requests .delete (OOO0OOO0O00O0O0O0 )#line:11
    if O0OO0O0OOO0OO0000 .status_code ==204 :#line:12
        print ("Webhook deleted successfully!")#line:13
    else :#line:14
        print ("Failed to delete the webhook with status code:",O0OO0O0OOO0OO0000 .status_code )#line:15
def main ():#line:17
    O00O000OOOO0OO0OO =input ("Enter the webhook URL: ")#line:18
    OOO0OOOO00O00O00O =input ("Do you want to send a last message? (y/n): ")#line:19
    if OOO0OOOO00O00O00O .lower ()=="y":#line:21
        O0O00O0O0000OOO00 =input ("Enter the message you want to send: ")#line:22
        send_message (O00O000OOOO0OO0OO ,O0O00O0O0000OOO00 )#line:23
    delete_webhook (O00O000OOOO0OO0OO )#line:25

    
    input("Press any key to quit.")

if __name__ == "__main__":
    main()
