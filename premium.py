# -*- coding: utf-8

import os,sys,time

P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
K = "\x1b[0;93m" # Kuning

def jalan(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)

def banner():
    print("\x1b[0;37m   ___                   \n  / _ \_______             ® \n / ___/ __/ -_) Multi Brute  ┌──────────────────────────────┐\n/_/  /_/__\__/(_) Force 4.0  │  Script By Dapunta Khurayra  │\n       /  ^ \/ / // /  ^ \   │   •• Github.com/Dapunta ••   │\n      /_/_/_/_/\_,_/_/_/_/   └──────────────────────────────┘")

def mulai():
    os.system('clear')
    banner()
    jalan('\n%s[%s•%s] %sChecking Phone Bit...'%(K,P,K,P))
    print('%s[%s•%s] %sYour Phone Bit Is :'%(K,P,K,P))
    print('')
    os.system("uname -a")
    print('')
    print('\n%s[ %sChoose Your Phone Bit %s]'%(K,P,K))
    print('\n%s[%s1%s] %sarmv32 [32 Bit]'%(K,P,K,P))
    print('%s[%s2%s] %sarmv64 [64 Bit]'%(K,P,K,P))
    pil = input('%s[%s•%s] %sChoose : '%(K,P,K,P))
    if pil in ['']:
        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
        mulai()
    elif pil in ['1','01','001','a']:
        try:
            #os.system("cd 32 && python premium.py")
            jalan('%s[%s!%s] %sScript Was Updating. Please Wait Until Coming Soon'%(M,P,M,P))
        except:
            print('\n%s[ %sWrong Choice %s]'%(M,P,M))
    elif pil in ['2','02','002','b']:
        try:
            #os.system("cd 64 && python premium.py")
            jalan('%s[%s!%s] %sScript Was Updating. Please Wait Until Coming Soon'%(M,P,M,P))
        except:
            print('\n%s[ %sWrong Choice %s]'%(M,P,M))
    else:
        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
        mulai()

if __name__ == "__main__":
    mulai()
