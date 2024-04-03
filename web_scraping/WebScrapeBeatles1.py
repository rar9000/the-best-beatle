import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from urllib.request import urlopen

url = 'https://en.wikipedia.org/wiki/List_of_songs_recorded_by_the_Beatles'
html = urlopen(url) 
soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table')

Songs = []
Albums = []
Writers = []
Singers = []
Years = []

for table in tables:
    rows = table.find_all('th')
    
    for row in rows:
        cells = row.find_all('td')
        
        
        if len(cells) > 1:
            Song = cells[0]
            Songs.append(Song.text.strip())
            
            Album = cells[1]
            Albums.append(Album.text.strip())
            
            Writer = cells[2]
            Writers.append(Writer.text.strip())

            Singer = cells[3]
            Singers.append(Singer.text.strip())

            Year = cells[4]
            Years.append(Year.text.strip())

df1 = pd.DataFrame(Songs, columns = ['Song'])
df1['Album'] = Albums, df1['Writer'] = Writers, df1['Singer'] = Singers, df1['Year'] = Years
df1.head(10)