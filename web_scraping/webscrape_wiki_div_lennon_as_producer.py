
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Category:Song_recordings_produced_by_John_Lennon'

data = requests.get(url)
soup = BeautifulSoup(data.content, "html.parser")
divs = soup.find_all("div", {"class":"mw-category"})


songs = []

for div in divs:
    song_list = div.find_all('li')
    for song in song_list:
     songs.append(song.find_next("a").text.strip())


df = pd.DataFrame(songs, columns= ["Songs"])
df.index += 1
df.to_csv('lennon_as_producer.csv')
    
    
    

