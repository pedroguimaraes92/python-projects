import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

cntx = ssl.create_default_context()
cntx.check_hostname = False
cntx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
pos = int(input("Enter Position: "))-1
count = int(input("Enter Count: "))
html = urllib.request.urlopen(url, context=cntx).read()
soup = BeautifulSoup(html, 'html.parser')
sqc = []
tags = soup('a')
for i in range(count):
    link = tags[pos].get('href', None)
    print("Retrieving:",link)
    sqc.append(tags[pos].contents[0])
    html = urllib.request.urlopen(link, context=cntx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link = tags[pos].get('href', None)
print(sqc[-1])
