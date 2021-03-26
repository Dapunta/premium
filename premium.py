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
mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

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
		print("   [!] Login Success").format(G,N)
		bot_komen()
		menu()
	except KeyError:
		print ("   [!] Invalid Token").format(R,N)
		time.sleep(1.0)
		logs()
















