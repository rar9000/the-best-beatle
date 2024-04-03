import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.billboard.com/artist/john-lennon/chart-history/hsi/"
soup = BeautifulSoup(requests.get(url).content, "html.parser")

data = []

for row in soup.select(".o-chart-results-list-row"):
    song = row.select_one(".artist-chart-row-title").get_text(strip=True)
    artist = row.select_one(".artist-chart-row-artist").get_text(strip=True)
    debut_date = row.select_one(".artist-chart-row-debut-date").get_text(strip=True)
    peak_pos = row.select_one(".artist-chart-row-peak-pos").get_text(strip=True)
    peak_week = row.select_one(".artist-chart-row-peak-week").get_text(strip=True)
    peak_date = row.select_one(".artist-chart-row-peak-date").get_text(strip=True)
    wks_on_chart = row.select_one(".artist-chart-row-week-on-chart").get_text(strip=True)
    
    data.append(
        {
            "Title": song,
            "Artist": artist,
            "Debut Date": debut_date,
            "Peak Pos": peak_pos,
            "Peak Week": peak_week,
            "Weeks on Chart": wks_on_chart,
        }
    )


df = pd.DataFrame(data)
df.index += 1
df.to_csv('singles_test.csv')