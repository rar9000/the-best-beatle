from bs4 import BeautifulSoup
import requests
import pandas as pd

wiki_url = 'https://en.wikipedia.org/wiki/List_of_songs_recorded_by_John_Lennon'

response = requests.get(wiki_url)
soup = BeautifulSoup(response.text,'html.parser')

song_list = soup.find('table', attrs={'class':'wikitable sortable plainrowheaders'})

df = pd.read_html(str(song_list))[0]

df.to_csv('all_lennon_catalog.csv')