import pandas as pd

try:
    # Read the CSV file into a DataFrame, replacing '—' with NaN values
    df = pd.read_csv('../data/cleaned_file.csv', na_values=['—'])

    # Calculate the frequency of each game receiving awards in different categories
    # Exclude the first two rows (header) and first two columns (category/organization)
    game_awards = df.iloc[2:, 2:].apply(pd.Series.value_counts).fillna(0)

    # Sum up the awards across different categories for each game
    total_awards = game_awards.sum(axis=1)

    # Find the game with the highest number of awards
    most_awarded_game = total_awards.idxmax()

    # Get the count of awards for the most awarded game
    most_awards_count = total_awards.loc[most_awarded_game]

    # Print the result
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
