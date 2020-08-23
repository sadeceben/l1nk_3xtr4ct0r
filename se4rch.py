#!/usr/bin/python3

"""
author : sadeceben
github : https://github.com/sadeceben?tab=repositories

"""

from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Back, Style
import time
import requests
import sys

now = time.time()
header = {'User-Agent':'Mozilla/5.0 (Android 4.3; Tablet; rv:50.0) Gecko/50.0 Firefox/50.0'}

url = sys.argv[1]
r = requests.get(url,headers=header)

html = r.text
soup = BeautifulSoup(html, 'html.parser')

print(Fore.RED + "Status code : " + Fore.YELLOW + str(r.status_code) +
      Fore.RESET)
print(Fore.MAGENTA +
      "|-----------------------| STARTED |-----------------------|\n\n" +
      Fore.RESET)

for link in soup.find_all('a'):
    print(Fore.BLUE + "Site Link |----> " + Fore.YELLOW + link.get('href') +
          Fore.RESET)

print(Fore.MAGENTA +
      "\n\n|-----------------------| FINISHED |-----------------------|" +
      Fore.RESET)

later = time.time()
print(Fore.RED + "\n\nElapsed Time : " + Fore.YELLOW + str(later - now) +
      Fore.RESET)
