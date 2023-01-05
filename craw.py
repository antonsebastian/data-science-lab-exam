
import requests
from bs4 import BeutifulSoup
URL="http://ww.ajce.in"
r=requests.get(URL)
soup=BeutifulSoup(r.content,'html.parser')
print(soup)
