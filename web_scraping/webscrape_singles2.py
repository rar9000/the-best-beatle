import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.billboard.com/artist/john-lennon/chart-history/hsi/"
soup = BeautifulSoup(requests.get(url).content, "html.parser")

data = []

for row in soup.select('.o-chart-results-list-row'):
    song = row.find('h3', class_='artist-chart-row-title').text.strip()
    artist = row.find('span', class_='artist-chart-row-artist').text.strip()
    debut = row.find('span', class_='artist-chart-row-debut-date').text.strip()
    peak_pos = row.find('span', class_='artist-chart-row-peak-pos').text.strip()
    peak_week = row.find('span', class_='artist-chart-row-peak-week').text.strip()
    peak_date = row.find('span', class_='artist-chart-row-peak-date').text.strip()
    wks = row.find("span", class_='artist-chart-row-week-on-chart').text.strip()
    
    data.append(
        {
            "Song": song,
            "Artist": artist,
            "Debut Date": debut,
            "Peak Pos": peak_pos,
            "Peak Week": peak_week,
            "Weeks on Chart": wks,
        }
    )

df = pd.DataFrame(data)
df.index += 1
df.to_csv('singles_test.csv')
