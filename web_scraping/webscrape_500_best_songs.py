import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service(r'chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=s)

# just setting some vars, I used Xpath because I know that
top_500 = 'https://www.rollingstone.com/music/music-lists/best-songs-of-all-time-1224767/'
cookie_button_xpath = "// button [@id = 'onetrust-accept-btn-handler']"
div_containing_links_xpath = "// div [@id = 'pmc-gallery-list-nav-bar-render'] // child :: a"
song_names_xpath = "// article [@class = 'c-gallery-vertical-album'] / child :: h2"

links = []
songs = []


driver.get(top_500)


# accept cookies, give time to load
time.sleep(3)
cookie_btn = driver.find_element(By.XPATH, cookie_button_xpath)
cookie_btn.click()
time.sleep(1)


# extracting all the links since there are only 50 songs per page
links_to_next_pages = driver.find_elements(By.XPATH, div_containing_links_xpath)

for element in links_to_next_pages:
    l = element.get_attribute('href')
    links.append(l)

# extracting the songs, then going to next page and so on until we hit 500
counter = 1         # were starting with 1 here since links[0] is the current page we are already on

while True:
    list = driver.find_elements(By.XPATH, song_names_xpath)

    for element in list:
        s = element.text
        songs.append(s)
    
    if len(songs) == 500:
        break

    driver.get(links[counter])
    counter += 1

    time.sleep(2)


# verify that there are no duplicates, if there were, something would be off
if len(songs) != len( set(songs) ):
    print('you f***** up')
else:
    print('seems fine')


with open('output_songs.txt', 'w') as file:
    file.writelines(line + '\n' for line in songs)