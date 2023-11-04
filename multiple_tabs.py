#! python3
import requests, webbrowser
import bs4
import sys

if len(sys.argv) > 1:    
    search = " ".join(sys.argv[1])
    
    res=requests.get('http://www.google.com/search?q='+search)
    res.raise_for_status()
    print("Googling ...")
    soup=bs4.BeautifulSoup(res.text)
    soup.find    