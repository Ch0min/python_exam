import pandas as pd

try:
    # Read the CSV file
    data = pd.read_csv('../data/cleaned_file.csv')

    # Category to check
    category = 'The Game Awards 2022 December 8, 2022[3]'

    # Filter the DataFrame to include only the relevant columns for "The Game Awards 2022"
    game_awards_2022 = data[["Category/Organization", category]]

    # Create an empty dictionary to store the game titles and their award counts
    game_awards_count = {}

    # Iterate over each row in the DataFrame
    for index, row in game_awards_2022.iterrows():
        try:
            # Get the game titles (including mixed information)
            game_titles = row["The Game Awards 2022 December 8, 2022[3]"].split(',')

            # Iterate over each game title
            for title in game_titles:
                # Strip any leading/trailing whitespaces
                title = title.strip()

                # Check if the game title already exists in the dictionary
                if title in game_awards_count:
                    # Increment the award count for the existing game title
                    game_awards_count[title] += 1
                else:
                    # Create a new entry for the game title with an initial award count of 1
                    game_awards_count[title] = 1
        except KeyError:
            print("Error: The specified category does not exist in the DataFrame.")
            break

    # Find the maximum award count
    max_awards = max(game_awards_count.values())

    # Find all the games with the maximum award count
    games_with_max_awards = [game_title for game_title, award_count in game_awards_count.items() if award_count == max_awards]

    # Print the games with the most awards won
    print("The game(s) that won the most awards at " + category + ":")
    for game in games_with_max_awards:
        print(game)

except FileNotFoundError:
    print("Error: The specified CSV file was not found.")
except Exception as e:
    print("An error occurred:", str(e))
