import os
import sys
import requests
from requests import get

a='\033[1;30m' # Ini Adalah Warna Abu - abu / Grey
r='\033[1;31m' # Ini Adalah Warna Merah / red
g='\033[32;1m' # Ini Adalah Warna Hijau / green
y='\033[1;33m' # Ini Adalah Warna Kuning / yellow
b='\033[1;34m' # Ini Adalah Warna Biru / blue
p='\033[1;35m' # Ini Adalah Warna purple
c='\033[1;36m' # Ini Adalah Warna cyan / biru terang
w='\033[1;37m' # Ini Adalah Warna putih / white
n='\033[0;00m' # Ini Adalah Warna normal / warna default termux
o='\033[1;38;5;208m' # it's orange



def update():
      try:
            get('https://github.com')
      except requests.exceptions.ConnectionError:
            print('\n     '+r+'['+y+'!'+r+'] '+y+'Updating DfvXploit Failed ')
            print('     '+r+'['+y+'?'+r+']'+y+' Plaese check your connection internet')
            exit()
      sp.call('cd && rm -rf DfvXploit')      
      sp.call(['cd && git clone https://github.com/Dfv47/DfvXploit'],shell=True, stdout=sp.DEVNULL,stderr=sp.STDOUT)
      sp.call('cd ../DfvXploit && python2 DfvXploit.py')    
