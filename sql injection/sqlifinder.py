import os
import sys
import time
import requests
import string
from urllib.parse import urlparse, unquote
from tqdm import tqdm 
from huepy import *
from core import requester
from core import extractor
from core import crawler

start_time = time.time()

def clear():
    if 'linux' in sys.platform or 'darwin' in sys.platform:
        os.system('clear')
    else:
        os.system('cls')

def banner():
    ban =  '''
            ___ ____         __       
  ___ ___ _/ (_) _(_)__  ___/ /__ ____
 (_-</ _ `/ / / _/ / _ \/ _  / -_) __/
/___/\_, /_/_/_//_/_//_/\_,_/\__/_/   
      /_/       
      '''  

    print(green(ban))

def concatenate_list_data(list, result):
    for element in list:
        result = result + "\n" + str(element)
    return result

def main():
    domain = input("Enter the domain name of the target [ex. example.com]: ")
    subs = input("Set false or true [ex: False]: ").lower() == 'true'

    if subs:
        url = f"http://web.archive.org/cdx/search/cdx?url=*.{domain}/*&output=txt&fl=original&collapse=urlkey&page=/"
    else:
        url = f"http://web.archive.org/cdx/search/cdx?url={domain}/*&output=txt&fl=original&collapse=urlkey&page=/"

    

    clear()
    

    response = requester.connector(url)
    crawled_urls = crawler.spider(f"http://{domain}", 10)
    response = concatenate_list_data(crawled_urls, response)
    if response == False:
        return
    response = unquote(response)

    print("\n"+"["+blue("INF")+"]"+f" Scanning sql injection for {domain}")
    
    exclude = ['woff', 'js', 'ttf', 'otf', 'eot', 'svg', 'png', 'jpg']
    final_uris = extractor.param_extract(response , "high", exclude, "")

    file = open(r'C:\Users\gowrishankar\Desktop\projects\harish\sql injection\payloads.txt', 'r')
    payloads = file.read().splitlines()

    vulnerable_urls = []

    for uri in final_uris:
        for payload in payloads:
            final_url = uri+payload
            
            try:
                req = requests.get("{}".format(final_url))
                res = req.text
                if 'SQL' in res or 'sql' in res or 'Sql' in res:
                    print("["+green("sql-injection")+"] "+final_url)
                    break                           
            except:
                pass

def inject():
    clear()
    banner()
    main()


#inject()