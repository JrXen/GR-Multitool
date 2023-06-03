import discord #line:1
import asyncio #line:2
import random #line:3
import requests #line:4
from colorama import Fore ,init ,Style #line:5
class Clone :#line:8
    @staticmethod #line:9
    async def roles_delete (OO0OO0OOOOOOOO0O0 :discord .Guild ):#line:10
        for O00OO0O0OO0O000OO in OO0OO0OOOOOOOO0O0 .roles :#line:11
            try :#line:12
                if O00OO0O0OO0O000OO .name !="@everyone":#line:13
                    await O00OO0O0OO0O000OO .delete ()#line:14
                    print_delete (f"The role {Fore.YELLOW}{O00OO0O0OO0O000OO.name}{Fore.BLUE} has been deleted")#line:17
                    await asyncio .sleep (random .randint (0.15 ,0.10 ))#line:18
            except discord .Forbidden :#line:19
                print_error (f"Error deleting role: {Fore.YELLOW}{O00OO0O0OO0O000OO.name}{Fore.RED} Insufficient permissions.{Fore.RESET}")#line:22
            except discord .HTTPException as OO00O00OO0OOO0OO0 :#line:24
                if OO00O00OO0OOO0OO0 .status ==429 :#line:25
                    print_warning (f"Many requests were made. Waiting 60 seconds. Details: {OO00O00OO0OOO0OO0}")#line:28
                    await asyncio .sleep (60 )#line:29
    @staticmethod #line:31
    async def roles_create (OOO0O0O000000O00O :discord .Guild ,O0O00O0O0OOO0OO0O :discord .Guild ):#line:32
        O0O0O0OO000OO00OO =[]#line:33
        O0OOO00O0000OOOOO :discord .Role #line:34
        for O0OOO00O0000OOOOO in O0O00O0O0OOO0OO0O .roles :#line:35
            if O0OOO00O0000OOOOO .name !="@everyone":#line:36
                O0O0O0OO000OO00OO .append (O0OOO00O0000OOOOO )#line:37
        O0O0O0OO000OO00OO =O0O0O0OO000OO00OO [::-1 ]#line:38
        for O0OOO00O0000OOOOO in O0O0O0OO000OO00OO :#line:39
            try :#line:40
                await OOO0O0O000000O00O .create_role (name =O0OOO00O0000OOOOO .name ,permissions =O0OOO00O0000OOOOO .permissions ,colour =O0OOO00O0000OOOOO .colour ,hoist =O0OOO00O0000OOOOO .hoist ,mentionable =O0OOO00O0000OOOOO .mentionable )#line:45
                print_add (f"The role {Fore.YELLOW}{O0OOO00O0000OOOOO.name}{Fore.BLUE} has been created")#line:47
                await asyncio .sleep (random .uniform (0.3 ,0.6 ))#line:48
            except discord .Forbidden :#line:49
                print_error (f"Error creating role: {Fore.YELLOW}{O0OOO00O0000OOOOO.name}{Fore.RED} Insufficient permissions.{Fore.RESET}")#line:52
                await asyncio .sleep (random .randint (0.20 ,0.40 ))#line:53
            except discord .HTTPException as O0OO0OO000O00O0OO :#line:54
                if O0OO0OO000O00O0OO .status ==429 :#line:55
                    print_warning (f"Many requests were made. Waiting 60 seconds. Details: {O0OO0OO000O00O0OO}")#line:58
                    await asyncio .sleep (60 )#line:59
    @staticmethod #line:61
    async def channels_delete (OOO0OO00OOOOO0000 :discord .Guild ):#line:62
        for OOO0OOO0000OO00O0 in OOO0OO00OOOOO0000 .channels :#line:63
            try :#line:64
                await OOO0OOO0000OO00O0 .delete ()#line:65
                print_delete (f"The category {Fore.YELLOW}{OOO0OOO0000OO00O0.name}{Fore.BLUE} has been deleted")#line:68
                await asyncio .sleep (0.6 )#line:69
            except discord .Forbidden :#line:70
                print_error (f"Error deleting category: {Fore.YELLOW}{OOO0OOO0000OO00O0.name}{Fore.RED} Insufficient permissions.{Fore.RESET}")#line:73
                await asyncio .sleep (random .randint (2 ,3 ))#line:74
            except discord .HTTPException as OOO00O0OO000OO0OO :#line:75
                if OOO00O0OO000OO0OO .status ==429 :#line:76
                    print_warning (f"Many requests were made. Waiting 60 seconds. Details: {OOO00O0OO000OO0OO}")#line:79
                    await asyncio .sleep (60 )#line:80
            except :#line:81
                print_error (f"Unable to delete channel {Fore.YELLOW}{OOO0OOO0000OO00O0.name}{Fore.RED} Unidentified error")#line:84
                await asyncio .sleep (random .randint (9 ,12 ))#line:85
    @staticmethod #line:87
    async def categories_create (O0O00OO0OO0O00O0O :discord .Guild ,O000O0000O0OO0OOO :discord .Guild ):#line:89
        OOOOO0O00OO000O00 =O000O0000O0OO0OOO .categories #line:90
        O00OO0OO0000O0O00 :discord .CategoryChannel #line:91
        O00OOO0OOO00000O0 :discord .CategoryChannel #line:92
        for O00OO0OO0000O0O00 in OOOOO0O00OO000O00 :#line:93
            try :#line:94
                OOO00O0O0OOOO0OO0 ={}#line:95
                for OOOOO0000OOO00OO0 ,OO0O0OOOOOO00O000 in O00OO0OO0000O0O00 .overwrites .items ():#line:96
                    OOOO00O0OOO0000OO =discord .utils .get (O0O00OO0OO0O00O0O .roles ,name =OOOOO0000OOO00OO0 .name )#line:97
                    OOO00O0O0OOOO0OO0 [OOOO00O0OOO0000OO ]=OO0O0OOOOOO00O000 #line:98
                O00OOO0OOO00000O0 =await O0O00OO0OO0O00O0O .create_category (name =O00OO0OO0000O0O00 .name ,overwrites =OOO00O0O0OOOO0OO0 )#line:100
                await O00OOO0OOO00000O0 .edit (position =O00OO0OO0000O0O00 .position )#line:101
                print_add (f"The category {Fore.YELLOW}{O00OO0OO0000O0O00.name}{Fore.BLUE} has been created")#line:104
                await asyncio .sleep (random .randint (1 ,3 ))#line:105
            except discord .Forbidden :#line:106
                print_error (f"Error creating category: {Fore.YELLOW}{O00OO0OO0000O0O00.name}{Fore.RED} Insufficient permissions.{Fore.RESET}")#line:109
                await asyncio .sleep (random .randint (2 ,3 ))#line:110
            except discord .HTTPException as O0OO0O0O0OO000O00 :#line:111
                if O0OO0O0O0OO000O00 .status ==429 :#line:112
                    print_warning (f"Many requests were made. Waiting 60 seconds. Details: {O0OO0O0O0OO000O00}")#line:115
                    await asyncio .sleep (60 )#line:116
            except :#line:117
                print_error (f"Unable to create category {Fore.YELLOW}{O00OO0OO0000O0O00.name}{Fore.RED} Unidentified error")#line:120
                await asyncio .sleep (random .randint (9 ,12 ))#line:121
    @staticmethod #line:123
    async def channels_create (O00O0000000O00O00 :discord .Guild ,O0OOO0O00OOOO0OO0 :discord .Guild ):#line:125
        O0O0000O0O000OO0O :discord .TextChannel #line:126
        O000O0O0OOOOOOO0O :discord .VoiceChannel #line:127
        OO0OO000OO0O00O00 =None #line:128
        for O0O0000O0O000OO0O in O0OOO0O00OOOO0OO0 .text_channels :#line:129
            try :#line:130
                for OO0OO000OO0O00O00 in O00O0000000O00O00 .categories :#line:131
                    try :#line:132
                        if OO0OO000OO0O00O00 .name ==O0O0000O0O000OO0O .category .name :#line:133
                            break #line:134
                    except AttributeError :#line:135
                        OO0OO000OO0O00O00 =None #line:136
                        break #line:137
                OO0O0O00O0OO0O00O ={}#line:139
                for O0O000O000OO00O0O ,O0OO00OO000O00O00 in O0O0000O0O000OO0O .overwrites .items ():#line:140
                    OOO0O0OO000O00O00 =discord .utils .get (O00O0000000O00O00 .roles ,name =O0O000O000OO00O0O .name )#line:141
                    OO0O0O00O0OO0O00O [OOO0O0OO000O00O00 ]=O0OO00OO000O00O00 #line:142
                try :#line:143
                    OOO000O00OO00000O =await O00O0000000O00O00 .create_text_channel (name =O0O0000O0O000OO0O .name ,overwrites =OO0O0O00O0OO0O00O ,position =O0O0000O0O000OO0O .position ,topic =O0O0000O0O000OO0O .topic ,slowmode_delay =O0O0000O0O000OO0O .slowmode_delay ,nsfw =O0O0000O0O000OO0O .nsfw )#line:150
                except :#line:151
                    OOO000O00OO00000O =await O00O0000000O00O00 .create_text_channel (name =O0O0000O0O000OO0O .name ,overwrites =OO0O0O00O0OO0O00O ,position =O0O0000O0O000OO0O .position )#line:155
                if OO0OO000OO0O00O00 is not None :#line:156
                    await OOO000O00OO00000O .edit (category =OO0OO000OO0O00O00 )#line:157
                print_add (f"The text channel {Fore.YELLOW}{O0O0000O0O000OO0O.name}{Fore.BLUE} has been created")#line:160
                await asyncio .sleep (0.59 )#line:161
            except discord .Forbidden :#line:162
                print_error (f"Error creating text channel: {O0O0000O0O000OO0O.name}")#line:164
                await asyncio .sleep (random .randint (8 ,10 ))#line:165
            except discord .HTTPException as OO0O0O0000O0OO0O0 :#line:166
                if OO0O0O0000O0OO0O0 .status ==429 :#line:167
                    print_warning (f"Many requests were made. Waiting 60 seconds. Details: {OO0O0O0000O0OO0O0}")#line:170
                    await asyncio .sleep (60 )#line:171
                    OOO000O00OO00000O =await O00O0000000O00O00 .create_text_channel (name =O0O0000O0O000OO0O .name ,overwrites =OO0O0O00O0OO0O00O ,position =O0O0000O0O000OO0O .position )#line:175
                if OO0OO000OO0O00O00 is not None :#line:176
                    await OOO000O00OO00000O .edit (category =OO0OO000OO0O00O00 )#line:177
                print_add (f"The channel {Fore.YELLOW}{O0O0000O0O000OO0O.name}{Fore.BLUE} has been created")#line:180
            except :#line:181
                print_error (f"Error creating text channel: {O0O0000O0O000OO0O.name}")#line:183
                await asyncio .sleep (random .randint (9 ,12 ))#line:184
        OO0OO000OO0O00O00 =None #line:186
        for O000O0O0OOOOOOO0O in O0OOO0O00OOOO0OO0 .voice_channels :#line:187
            try :#line:188
                for OO0OO000OO0O00O00 in O00O0000000O00O00 .categories :#line:189
                    try :#line:190
                        if OO0OO000OO0O00O00 .name ==O000O0O0OOOOOOO0O .category .name :#line:191
                            break #line:192
                    except AttributeError :#line:193
                        print_warning (f"Voice channel {O000O0O0OOOOOOO0O.name} has no category!")#line:196
                        OO0OO000OO0O00O00 =None #line:197
                        break #line:198
                OO0O0O00O0OO0O00O ={}#line:200
                for O0O000O000OO00O0O ,O0OO00OO000O00O00 in O000O0O0OOOOOOO0O .overwrites .items ():#line:201
                    OOO0O0OO000O00O00 =discord .utils .get (O00O0000000O00O00 .roles ,name =O0O000O000OO00O0O .name )#line:202
                    OO0O0O00O0OO0O00O [OOO0O0OO000O00O00 ]=O0OO00OO000O00O00 #line:203
                try :#line:204
                    OOO000O00OO00000O =await O00O0000000O00O00 .create_voice_channel (name =O000O0O0OOOOOOO0O .name ,overwrites =OO0O0O00O0OO0O00O ,position =O000O0O0OOOOOOO0O .position ,bitrate =O000O0O0OOOOOOO0O .bitrate ,user_limit =O000O0O0OOOOOOO0O .user_limit ,)#line:211
                except :#line:212
                    OOO000O00OO00000O =await O00O0000000O00O00 .create_voice_channel (name =O000O0O0OOOOOOO0O .name ,overwrites =OO0O0O00O0OO0O00O ,position =O000O0O0OOOOOOO0O .position )#line:216
                if OO0OO000OO0O00O00 is not None :#line:217
                    await OOO000O00OO00000O .edit (category =OO0OO000OO0O00O00 )#line:218
                print_add (f"The voice channel {Fore.YELLOW}{O000O0O0OOOOOOO0O.name}{Fore.BLUE} has been created")#line:221
                await asyncio .sleep (0.48 )#line:222
            except discord .Forbidden :#line:223
                print_error (f"Error creating voice channel: {O000O0O0OOOOOOO0O.name}")#line:225
                await asyncio .sleep (random .randint (6 ,7 ))#line:226
            except discord .HTTPException as OO0O0O0000O0OO0O0 :#line:227
                if OO0O0O0000O0OO0O0 .status ==429 :#line:228
                    print_warning (f"Many requests were made. Waiting 60 seconds. Details: {OO0O0O0000O0OO0O0}")#line:231
                    await asyncio .sleep (60 )#line:232
                    OOO000O00OO00000O =await O00O0000000O00O00 .create_voice_channel (name =O000O0O0OOOOOOO0O .name ,overwrites =OO0O0O00O0OO0O00O ,position =O000O0O0OOOOOOO0O .position )#line:236
                if OO0OO000OO0O00O00 is not None :#line:237
                    await OOO000O00OO00000O .edit (category =OO0OO000OO0O00O00 )#line:238
                print_add (f"The voice channel {Fore.YELLOW}{O000O0O0OOOOOOO0O.name}{Fore.BLUE} has been created")#line:241
            except :#line:242
                print_error (f"Error creating voice channel: {O000O0O0OOOOOOO0O.name}")#line:244
    @staticmethod #line:246
    async def emojis_create (O00O00000O00OO0OO :discord .Guild ,OOO00000O000OO00O :discord .Guild ):#line:248
        OO00OO00O00OO00O0 =OOO00000O000OO00O .emojis #line:249
        if not OO00OO00O00OO00O0 :#line:250
            print_warning ("No emoji found.")#line:251
            return #line:252
        for O0OOOO00000000000 in OOO00000O000OO00O .emojis :#line:253
            try :#line:254
                O0OO00O0OOO0OO000 =await O0OOOO00000000000 .url .read ()#line:255
                await O00O00000O00OO0OO .create_custom_emoji (name =O0OOOO00000000000 .name ,image =O0OO00O0OOO0OO000 )#line:257
                print_add (f"The {Fore.YELLOW}{O0OOOO00000000000.name}{Fore.BLUE} emoji has been created.")#line:260
                O000000O00OO0OOOO =random .randint (1 ,100 )#line:261
                if O000000O00OO0OOOO <=85 :#line:262
                    await asyncio .sleep (random .uniform (0.3 ,0.6 ))#line:263
            except discord .Forbidden :#line:264
                print_error (f"Error creating emoji: {Fore.YELLOW}{O0OOOO00000000000.name}{Fore.RED} Insufficient permissions.{Fore.RESET}")#line:267
                await asyncio .sleep (random .uniform (2 ,3 ))#line:268
            except discord .HTTPException as O000O0O0OOO0O00O0 :#line:269
                if O000O0O0OOO0O00O0 .status ==429 :#line:270
                    print_warning (f"Many requests were made. Waiting 10 seconds. Details: {O000O0O0OOO0O00O0}")#line:273
                    await asyncio .sleep (10 )#line:274
                    await O00O00000O00OO0OO .create_custom_emoji (name =O0OOOO00000000000 .name ,image =O0OO00O0OOO0OO000 )#line:276
            except Exception :#line:277
                print_warning (f"An error occurred in {O0OOOO00000000000.name}")#line:278
    @staticmethod #line:280
    async def guild_edit (O0O0OOOO0O00OO000 :discord .Guild ,OOO00000O00OOO0O0 :discord .Guild ):#line:281
        try :#line:282
            try :#line:283
                O00000000OO000OO0 =requests .get (OOO00000O00OOO0O0 .icon_url ).content #line:284
            except requests .exceptions .RequestException :#line:285
                print_error (f"Unable to download icon from {OOO00000O00OOO0O0.name}")#line:287
                O00000000OO000OO0 =None #line:288
            await O0O0OOOO0O00OO000 .edit (name =OOO00000O00OOO0O0 .name )#line:289
            if O00000000OO000OO0 is not None :#line:290
                try :#line:291
                    await O0O0OOOO0O00OO000 .edit (icon =O00000000OO000OO0 )#line:292
                    print_add (f"Changed group icon: {O0O0OOOO0O00OO000.name}")#line:293
                except :#line:294
                    print_error (f"Error changing group icon: {O0O0OOOO0O00OO000.name}")#line:296
        except discord .LoginFailure :#line:297
            print ("Unable to authenticate to account. Check that the token is correct.")#line:300
        except discord .Forbidden :#line:301
            print_error (f"Error changing group icon: {O0O0OOOO0O00OO000.name}")#line:302
def print_add (O00OO0O0OO0OO0O0O ):#line:305
    print (f'{Style.BRIGHT}{Fore.CYAN} {O00OO0O0OO0OO0O0O}{Fore.RESET}')#line:306
def print_delete (OOOO0OO00O0000OO0 ):#line:309
    print (f'{Style.BRIGHT}{Fore.CYAN} {OOOO0OO00O0000OO0}{Fore.RESET}')#line:310
def print_warning (OOO000OOOO00O0O0O ):#line:313
    print (f'{Style.BRIGHT}{Fore.YELLOW} {OOO000OOOO00O0O0O}{Fore.RESET}')#line:314
def print_error (OOOOOO0000OOOOOO0 ):#line:317
    print (f'{Style.BRIGHT}{Fore.RED} {OOOOOO0000OOOOOO0}{Fore.RESET}')#line:318
