from bs4 import BeautifulSoup
import requests
import pandas as pd

wiki_url = 'https://en.wikipedia.org/wiki/2022_in_video_games'
response = requests.get(wiki_url)
soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('table', attrs={'class': "wikitable"})

for index, table in enumerate(tables):
    # titel fra h2/h3 tag
    h2_or_h3_tag = table.find_previous(['h2', 'h3'])
    table_name = h2_or_h3_tag.get_text().strip(
    ) if h2_or_h3_tag else f'table_{index + 1}'

    # fjern "[edit]" tekst
    table_name = table_name.replace("[edit]", "").strip()

    # cleaning
    table_name = table_name.replace(" ", "_")
    table_name = table_name.replace("–", "-")

    df = pd.read_html(str(table))[0]
    df.to_csv(f'./data/{table_name}.csv', index=False, sep=',')

"""
    import requests
    from bs4 import BeautifulSoup

    url = "https://en.wikipedia.org/wiki/2022_in_video_games"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table", {"class": "wikitable"})

    rows = table.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        cols = [col.text.strip() for col in cols]
        print(cols)

"""
