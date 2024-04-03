import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Category:Song_recordings_produced_by_George_Harrison'
url2 = 'https://en.wikipedia.org/w/index.php?title=Category:Song_recordings_produced_by_George_Harrison&pagefrom=Plug+Me+In+%28song%29#mw-pages'

data = requests.get(url)
soup = BeautifulSoup(data.content, "html.parser")
divs = soup.find_all("div", {"class":"mw-category"})

data2 = requests.get(url2)
soup2 = BeautifulSoup(data2.content, "html.parser")
divs2 = soup2.find_all("div", {"class":"mw-category"})


songs = []
songs2 = []

for div in divs:
    song_list = div.find_all('li')
    for song in song_list:
     songs.append(song.find_next("a").text.strip())

for div2 in divs2:
    song_list2 = div2.find_all('li')
    for song2 in song_list2:
     songs2.append(song2.find_next("a").text.strip())


df = pd.DataFrame(songs, columns= ["Songs"])

df2 = pd.DataFrame(songs2, columns= ["Songs"])

df3 = pd.concat([df,df2], ignore_index=True)
df3.index += 1

df3.to_csv('harrison_as_producer.csv')
    

    
    
    

