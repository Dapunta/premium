#!/usr/bin/python3
#-*-coding:utf-8-*-
# Trigger Khusus 64 Bit

import sys,os,bot_follow

if sys.version[0:3] != "3.9":
    sys.exit('[!] You Must Use Python 3.9 Version')

if __name__ == '__main__':
    try:
        os.system('git pull')
        __import__('premium64').menu()
    except Exception as e:
        exit(str(e))