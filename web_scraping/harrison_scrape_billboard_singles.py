import pandas as pd
import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.billboard.com/artist/george-harrison/chart-history/hsi/')
soup = BeautifulSoup(url.content, 'html.parser')
result = soup.find_all('div','o-chart-results-list-row')

data = []

for res in result:
    song = res.find('h3', class_='artist-chart-row-title').text.strip()
    artist = res.find('span', class_='artist-chart-row-artist').text.strip()
    debute = res.find('span', class_='artist-chart-row-debut-date').text.strip()
    peak = res.find('span', class_='artist-chart-row-peak-pos').text.strip()
    peak_week = res.find('span', class_='artist-chart-row-peak-week').text.strip()
    peak_date = res.find('span', class_='artist-chart-row-peak-date').text.strip()
    wks = res.find("span", class_='artist-chart-row-week-on-chart').text.strip()
   
    data.append({"Song": song, 
                 "Artist": artist, 
                 "Debute": pd.to_datetime(debute, format='%m.%d.%y', errors='coerce'), 
                 "Peak": peak, 
                 "Peak Date": pd.to_datetime(peak_date, format='%m.%d.%y', errors='coerce'), 
                 "Weeks": wks})
    

    df = pd.DataFrame.from_dict(data)
    df.index += 1
    df.to_csv('harrison_singles.csv')