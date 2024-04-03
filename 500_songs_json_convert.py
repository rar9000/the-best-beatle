import pandas as pd

df = pd.read_json('top_500_songs.json')

filtered_df = df[df["artist"].str.contains("Beatles|Lennon|Harrison|McCartney|Starr")]

filtered_df .to_csv('filtered_top_500_songs_2021.csv')
