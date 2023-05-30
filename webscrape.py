from bs4 import BeautifulSoup
import requests
import pandas as pd

wiki_url = 'https://en.wikipedia.org/wiki/2022_in_video_games'
response = requests.get(wiki_url)
soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('table', attrs={'class': "wikitable"})

for index, table in enumerate(tables):
    # Vi finder h2 eller h3 tags før tabellerne, så vi har overskrifterne.
    h2_or_h3_tag = table.find_previous(['h2', 'h3'])

    # Vi bruger h2 eler h3 som navn på filen, og tilføjer et index, hvis der ikke er nogen overskrift.
    table_name = h2_or_h3_tag.get_text().strip(
    ) if h2_or_h3_tag else f'table_{index + 1}'

    # Vi fjerner [edit] teksten fra wikipedia.
    table_name = table_name.replace("[edit]", "").strip()

    # Her erstatter vi mellemrum med underscore.
    table_name = table_name.replace(" ", "_")
    # Vi erstatter wikipedias dash med et normal dash.
    table_name = table_name.replace("–", "-")

    df = pd.read_html(str(table))[0]
    df.to_csv(f'./data/{table_name}.csv', index=False, sep=',')

