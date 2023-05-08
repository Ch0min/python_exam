import bs4
import requests

r = requests.get('https://en.wikipedia.org/wiki/2022_in_video_games')
r.raise_for_status()
soup = bs4.BeautifulSoup(r.text, 'html.parser')

print(soup.prettify())

filename = './data/gamedata.html'

# Open the file in w mode and set encoding to UTF-8
with open(filename, "w", encoding='utf-8') as file:
    # Prettify the soup object and convert it into a string
    file.write(str(soup.prettify()))
