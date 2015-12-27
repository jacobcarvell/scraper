from bs4 import BeautifulSoup
import urllib.request
r = urllib.request.urlopen("http://www.finder.com.au/movies-internet-tv").read()
soup = BeautifulSoup(r, "html.parser")
print(soup)
