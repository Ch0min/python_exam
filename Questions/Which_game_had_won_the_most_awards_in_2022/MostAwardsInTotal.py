import pandas as pd

try:
    # Her læser vi vores data med panda
    df = pd.read_csv('../data/cleaned_file.csv', na_values=['—'])

    # Her sørger vi for at eksludere de første to rows (header) og kolonner (category/organization)
    game_awards = df.iloc[2:, 2:].apply(pd.Series.value_counts).fillna(0)

    # Her finder vi den totale mængde awards hvert spil har fået
    total_awards = game_awards.sum(axis=1)

    # Her finder vi det spil med flest awards
    most_awarded_game = total_awards.idxmax()

    # Her får vi antallet for det spil med flest awards
    most_awards_count = total_awards.loc[most_awarded_game]

    print("The game with the most awards is:", most_awarded_game)
    print("Number of awards:", most_awards_count)

except FileNotFoundError:
    print("Error: The file could not be found.")

except pd.errors.EmptyDataError:
    print("Error: The file is empty or contains no data.")

except pd.errors.ParserError:
    print("Error: There was an error parsing the CSV file.")

except Exception as e:
    print("An error occurred:", str(e))
