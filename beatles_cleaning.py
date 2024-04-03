import pandas as pd

beatles = pd.read_csv('all_beatles_catalog.csv')


beatles['Song'] = beatles['Song'].map(lambda x: x.rstrip('[abcdefghijklmnopqrstuvwxyz]#'))
beatles['Song'] = beatles['Song'].map(lambda x: x.lstrip('"').rstrip('"'))

beatles['Songwriter(s)'] = beatles['Songwriter(s)'].map(lambda x: x.rstrip('†'))

beatles