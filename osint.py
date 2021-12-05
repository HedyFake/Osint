
import os 
import sys
import requests
import json
import time
import termcolor
import colored
from tqdm import tqdm
import pyfiglet

def banner():

    print("""\33[0;36m
             ..,,;;;;;;,,,,
       .,;'';;,..,;;;,,,,,.''';;,..               
    ,,''                    '';;;;,;''           \33[37;1mAuthor  : HedyFake \33[0;36m
   ;'    ,;@@;'  ,@@;, @@, ';;;@@;,;';.          \33[37;1mYoutube : CatatanNewbie \33[0;36m
  ''  ,;@@@@@'  ;@@@@; ''    ;;@@@@@;;;;         \33[37;1mTwiter  : @iAmHere96509046 \33[0;36m
     ;;@@@@@;    '''     .,,;;;@@@@@@@;;;        \33[37;1mOsint V.01 \33[0;36m
    ;;@@@@@@;           , ';;;@@@@@@@@;;;.
     '';@@@@@,.  ,   .   ',;;;@@@@@@;;;;;;
        .   '';;;;;;;;;,;;;;@@@@@;;' ,.:;'
          ''..,,     ''''    '  .,;'
               ''''''::''''''''
        \33[37;1m|-=[Youtube Osint]=-|\33[0;36m
""")
def yt():
    os.system('clear')
    banner()
    id = input('\33[30;1m[-]\33[37;1mMasukkan id pengguna youtube:\33[1;33m')
    r = requests.get('https://youtube.googleapis.com/youtube/v3/channels?part=snippet,statistics&id='+id+'&key=AIzaSyBAer1fK1IHxojU0vYq1ZwzchSPmgoLBmM')
    a = json.loads(r.text)
    
    hedy = open('yt.txt', 'w')
    for i in a['items']:
        print ('\33[32;1m[+]\33[37;1mMencari Data!')
        loading()
        time.sleep(3)
        try:
            print (f"\33[32;1m[+]\33[37;1mChannel   :{i['snippet']['title']}")
            print 
            print (f"\33[32;1m[+]\33[37;1mDeskripsi :{i['snippet']['description']}")
            print
            print (f"\33[32;1m[+]\33[37;1mDibuat    :{i['snippet']['publishedAt']}")
            print 
            print (f"\33[32;1m[+]\33[37;1mProfile   :{i['snippet']['thumbnails']['high']['url']}")
            print (f"\33[32;1m[+]\33[37;1mLocation  :{i['snippet']['country']}")
            print (f"\33[32;1m[+]\33[37;1mSubscribe :{i['statistics']['subscriberCount']}")
            print (f"\33[32;1m[+]\33[37;1mVideo     :{i['statistics']['videoCount']}")
            print('\x1b[6;30;42m' + '[+]Success mengambil data!' + '\x1b[0m')
            hedy.write(i['snippet']['title'] + i['snippet']['description'] + i['snippet']['publishedAt'] + i['snippet']['thumbnails']['high']['url'] + i['snippet']['country'] + i['statistics']['subscriberCount'] + i['statistics']['videoCount'])

        except KeyError:
            pass


def loading():
    for i in tqdm(range(25)):
        time.sleep(0.5)

def ig():
    os.system('clear')
    banner1()
    hedycok = input('\33[30;1m[-]\33[37;1mMasukkan nama:\33[1;33m')
    r = requests.get('https://www.instagram.com/'+hedycok+'?__a=1')
    a = json.loads(r.text)
    loading()
    i = a['graphql']['user']
    
    print (f"\33[32;1m[+]\33[37;1mUsername  :{i['username']}")
    print (f"\33[32;1m[+]\33[37;1mUser id   :{i['id']}")
    print (f"\33[32;1m[+]\33[37;1mFull name :{i['full_name']}")
    print (f"\33[32;1m[+]\33[37;1mProfile   :{i['profile_pic_url_hd']}")
    print (f"\33[32;1m[+]\33[37;1mPrifate   :{i['is_private']}")
    print (f"\33[32;1m[+]\33[37;1mVerived   :{i['is_verified']}")
    print (f"\33[32;1m[+]\33[37;1mBio       :{i['biography']}")
    print (f"\33[32;1m[+]\33[37;1mWebsite   :{i['external_url']}")
    print (f"\33[32;1m[+]\33[37;1mPengikut  :{i['edge_followed_by']['count']}")
    print (f"\33[32;1m[+]\33[37;1mMengikuti :{i['edge_follow']['count']}")
    print (f"\33[32;1m[+]\33[37;1mPostingan :{i['edge_owner_to_timeline_media']['count']}")
    print (f"\33[32;1m[+]\33[37;1mVideo     :{i['edge_felix_video_timeline']['count']}")
    print (f"\33[32;1m[+]\33[37;1mReels     :{i['highlight_reel_count']}")
    print (f"\33[32;1m[+]\33[37;1mBusiness  :{i['business_category_name']}")
    print (f"\33[32;1m[+]\33[37;1mCategori  :{i['category_enum']}")
    print (f"\33[32;1m[+]\33[37;1mLikes     :{i['edge_owner_to_timeline_media']['edges'][0]['node']['edge_liked_by']['count']}")
    print (f"\33[32;1m[+]\33[37;1mTimestamp :{i['edge_owner_to_timeline_media']['edges'][0]['node']['taken_at_timestamp']}")
    print (f"\33[32;1m[+]\33[37;1mComments  :{i['edge_owner_to_timeline_media']['edges'][0]['node']['edge_media_to_comment']['count']}")
    print (f"\33[32;1m[+]\33[37;1mLocation  :{i['edge_owner_to_timeline_media']['edges'][0]['node']['location']['name']}")
    print('\x1b[6;30;42m' + '[+]Success mengambil data!' + '\x1b[0m')

def banner1():

    print ("""\33[32;1m
          NO!                          MNO!
     MNO!!         [NBK]          MNNOO!
   MMNO!                           MNNOO!!
 MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!!
 !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO!
       ! MMMMMMMMMMMMMPPPPOOOOIII! !
        MMMMMMMMMMMMPPPPPOOOOOOII!!
        MMMMMOOOOOOPPPPPPPPOOOOMII!
        MMMMM..    OPPMMP    .,OMI!           \33[37;1mAuthor  : HedyFake \33[32;1m
        MMMM::   o.,OPMP,.o   ::I!!           \33[37;1mYoutube : CatatanNewbie \33[32;1m
          NNM:::.,,OOPM!P,.::::!!             \33[37;1mTwiter  : @iAmHere96509046 \33[32;1m
         MMNNNNNOOOOPMO!!IIPPO!!O!            \33[37;1mOsint V.01 \33[32;1m
         MMMMMNNNNOO:!!:!!IPPPPOO!
          MMMMMNNOOMMNNIIIPPPOO!!
             MMMONNMMNNNIIIOO!
           MN MOMMMNNNIIIIIO! OO
          MNO! IiiiiiiiiiiiI OOOO
     NNN.MNO!   O!!!!!!!!!O   OONO NO!
    MNNNNNO!    OOOOOOOOOOO    MMNNON!
      MNNNNO!    PPPPPPPPP    MMNON!
         OO!                   ON!
        \33[37;1m|-=[Instagram Osint]=-|\33[0;36m
    """)

def main():
    print("""\33[0;36m
    
▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓          \33[37;1mAuthor  : HedyFake \33[0;36m
▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒         \33[37;1mYoutube : CatatanNewbie \33[0;36m
▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░        \33[37;1mTwiter  : @iAmHere96509046 \33[0;36m
▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░         \33[37;1mOsint V.01 \33[0;36m
░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ 
░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   
  ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░    
░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░      
    ░ ░        ░   ░           ░          
    \33[37;1m|-=[Osint Tools]=-|\33[0;36m                                   
    
    """)
    print('[1]OsintIG')
    print('[2]OsintYt')
    print('[3]Out')

    pill = input('[<]Pillih salah satu :')

    if pill == '1':
        ig()
    elif pill == "2":
        yt()
    elif pill == "3":
         os.system('exit') 

    else:
        os.system('clear')
        main()
main()
