from bs4 import BeautifulSoup
import urllib.request
import csv

#open the url of finder.com.au movies and read the html. Then parse it through beautiful soup.
r = urllib.request.urlopen("http://www.finder.com.au/movies-internet-tv").read()
rtv = urllib.request.urlopen("http://www.finder.com.au/tv-shows-internet-tv").read()
soup = BeautifulSoup(r, "html.parser")
souptv = BeautifulSoup(r, "html.parser")

#find the table on the page and store to a variable
tablediv = soup.table
tabletv = souptv.table

#find all of the table row objects in the table
rows = tablediv.find_all("tr")

#define arrays
data = []
record = ["title","netflix","presto","stan","type"]
data.append(record)

#loop through the table rows and get all of the column data and append it to the data array
for row in rows[1:]:
    cells = row.findAll('td')
    record = [cells[0].get_text(), cells[1].get_text(), cells[2].get_text(), cells[3].get_text(), "movie"]
    data.append(record)
    
#open the url of finder.com.au tv and read the html. Then parse it through beautiful soup.
r = urllib.request.urlopen("http://www.finder.com.au/tv-shows-internet-tv").read()
soup = BeautifulSoup(r, "html.parser")

#find the table on the page and store to a variable
tablediv = soup.table

#find all of the table row objects in the table
rows = tablediv.find_all("tr")

#loop through the table rows and get all of the column data and append it to the data array
for row in rows[1:]:
    cells = row.findAll('td')
    record = [cells[0].get_text(), cells[1].get_text(), cells[2].get_text(), cells[3].get_text(), "tv-show"]
    data.append(record)
    
#write the data array to a csv
with open("streamingdata.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
f.close()