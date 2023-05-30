from bs4 import BeautifulSoup
import requests
import pandas as pd

wiki_url = 'https://en.wikipedia.org/wiki/2022_in_video_games'
response = requests.get(wiki_url)
soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('table', attrs={'class': "wikitable"})

for index, table in enumerate(tables):
    # Find the closest h2 or h3 tag before the table
    h2_or_h3_tag = table.find_previous(['h2', 'h3'])

    # Get the text content of the h2 or h3 tag, if available, or use the index
    table_name = h2_or_h3_tag.get_text().strip(
    ) if h2_or_h3_tag else f'table_{index + 1}'

    # Remove the [edit] text from table name
    table_name = table_name.replace("[edit]", "").strip()

    # Replace spaces with underscores
    table_name = table_name.replace(" ", "_")
    # Replace wikipedia weird dash with normal dash
    table_name = table_name.replace("–", "-")

    df = pd.read_html(str(table))[0]
    df.to_csv(f'./data/{table_name}.csv', index=False, sep=',')

