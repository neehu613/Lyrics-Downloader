import os
from bs4 import BeautifulSoup
import urllib.request

os.system('clear')
url = 'https://search.azlyrics.com/search.php?q='
songName = input("Enter the full song name for perfect results: ")
newName = songName.replace(' ', '+')

url = url + newName
http = urllib.request.urlopen(url)

soup = BeautifulSoup(http, "lxml")
x = soup.find_all('div', {'class':'panel'})

allSongs = x[1].find_all('a')
allSongLinks = []
count = 1
for item in allSongs:
	print(str(count) + " : " + item.string)
	link = item['href']
	allSongLinks.append(link)
	count += 1
	print(link + '\n')


choice = int(input("Select the song from the above list: "))
url = allSongLinks[choice-1]
http = urllib.request.urlopen(url)
soup = BeautifulSoup(http, "lxml")

lyrics = soup.find_all('div', class_=False, id=False)
print(lyrics)