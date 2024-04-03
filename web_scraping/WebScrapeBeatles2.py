import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen

url =  requests.get('https://en.wikipedia.org/wiki/List_of_songs_recorded_by_the_Beatles').text
soup = BeautifulSoup(url, 'lxml')      



#url = 'https://en.wikipedia.org/wiki/List_of_songs_recorded_by_the_Beatles'
#html = urlopen(url) 
#soup = BeautifulSoup(html, 'html.parser')            

#soup.select("th:nth-of-type(1) a")

table = soup.find('table',{'class':'wikitable sortable plainrowheaders'})

song_links = table.select("th:nth-of-type(1)")
album_links = table.select("td:nth-of-type(1)")
writers_list = table.select("td:nth-of-type(2)")


songs = []
for song_link in song_links:
    songs.append(song_link.text.strip())

#albums = []
#for album_link in album_links:
 #   albums.append(album_link.text.strip())

writers = []
for writer_list in writers_list:
    writers.append(writer_list.text.strip())

#df = pd.DataFrame()
#df['Songs'] = songs,

#df = df[df["Song"].str.contains("None") == False]

df1 = pd.DataFrame()
df1['Song'] = songs

df1
#df1.to_csv('beatles_albums_test.csv')