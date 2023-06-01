import requests #line:1
import random #line:2
import os #line:3
import base64 #line:4
webhook_url =input ("Enter the webhook URL: ")#line:5
channel_id =int (input ("Enter the channel ID: "))#line:6
num_messages =int (input ("Enter the number of messages to send: "))#line:7
webhooks =[webhook_url ]*num_messages #line:8
with open ("names.txt",encoding ="utf-8")as f :#line:9
    names =[O0OO0OO00OOOO0OOO .strip ()for O0OO0OO00OOOO0OOO in f .readlines ()]#line:10
vouch_messages =["Flawless transaction, would definitely recommend this seller!","Quick and easy trade, thanks for the smooth transaction.","Trusted seller, pleasure doing business with you.","Very professional, highly recommended!","Great experience, would trade with again.","Thanks for the excellent service and quick transaction!","Reliable and trustworthy seller, would recommend to anyone.","Smooth trade, would definitely do business again.","Fantastic seller, couldn't be happier with the transaction.","Quick and easy trade, thanks for the great service.","Excellent communication and quick transaction, highly recommended.","A+ seller, thank you for the easy and hassle-free transaction.","Trusted and reliable seller, thank you for the smooth trade.","Great trader, highly recommended!","Flawless transaction, thanks for the excellent service.","Quick and easy trade, pleasure doing business with you.","Professional and reliable seller, would trade with again.","Excellent seller, highly recommended!","Smooth transaction, thanks for the great service.","Pleasure doing business with you, thanks for the quick and easy trade.","A+ transaction, would definitely recommend this seller.","Trusted and reliable seller, thank you for the smooth trade.","Great seller, excellent service and quick transaction.","Fast and easy trade, highly recommended!","Professional and trustworthy seller, would do business again.","Excellent experience, thanks for the smooth transaction.","Quick and reliable seller, pleasure doing business with you.","A+ seller, thank you for the hassle-free transaction.","Trusted and reliable, highly recommended!","Great communication and fast transaction, would trade with again.","Excellent seller, thanks for the smooth trade.","Quick and easy transaction, pleasure doing business with you.","Professional and trustworthy, highly recommended!","Smooth trade, thanks for the great service.","A+ transaction, would definitely do business again.","Trusted and reliable seller, thank you for the excellent service.","Great experience, highly recommended!","Flawless transaction, thanks for the smooth trade.","Quick and easy trade, pleasure doing business with you.","Professional and reliable seller, would definitely recommend.","Excellent seller, thank you for the hassle-free transaction.","Smooth transaction, highly recommended!","Trusted and reliable, thanks for the great service.","Great trader, would trade with again.","Quick and easy trade, thanks for the excellent service.","Professional and trustworthy, highly recommended!","Excellent experience, thanks for the smooth transaction.","Reliable seller, pleasure doing business with you.","A+ seller, would definitely do business again.","Trusted and reliable, highly recommended!","Great communication and fast transaction, thanks for the smooth trade.","Smooth trade, pleasure doing business with you.","Professional and trustworthy seller, would definitely recommend.","Excellent seller, thanks for the great service.","Quick and easy transaction, highly recommended!","Reliable seller, pleasure doing business with you.","A+ transaction, thanks for the smooth trade.","Trusted and reliable, highly recommended!","Great trader, would definitely do business again.",]#line:11
image_folder ="images"#line:12
image_files =os .listdir (image_folder )#line:13
random .shuffle (image_files )#line:14
num_images =len (image_files )#line:15
for i ,webhook in enumerate (webhooks ):#line:16
    new_name =random .choice (names )#line:17
    image_filename =image_files [i %num_images ]#line:18
    with open (os .path .join (image_folder ,image_filename ),"rb")as f :#line:19
        avatar_bytes =f .read ()#line:20
    avatar_base64 =base64 .b64encode (avatar_bytes ).decode ()#line:21
    data ={"name":new_name ,"avatar":f"data:image/jpeg;base64,{avatar_base64}"}#line:22
    requests .patch (webhook ,json =data )#line:23
    vouch_message =random .choice (vouch_messages )#line:24
    data ={"content":vouch_message }#line:25
    requests .post (webhook ,json =data )#line:26
print ("Vouch messages sent successfully!")#line:27
