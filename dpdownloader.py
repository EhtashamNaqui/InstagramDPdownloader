import requests
from bs4 import BeautifulSoup

usrnam = input("enter username: ")
print(usrnam)
username = (usrnam)
URL = "http://www.instagram.com/{}/"

r = requests.get(URL.format(usrnam))
s = BeautifulSoup(r.text,"html.parser")
u = s.find("meta",property="og:image")
url = u.attrs['content']

with open(username+'.jpg' , "wb") as pic:
    binary = requests.get(url).content
    pic.write(binary)