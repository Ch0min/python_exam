import pandas as pd

try:
    # Vi læser vores csv fil ved at bruge panda
    data = pd.read_csv('../data/cleaned_file.csv')

    # Vi definerer den category som vi skal lave en graf ud fra
    category = 'The Game Awards 2022 December 8, 2022[3]'

    # Her sørger vi for at vi kun kigger på den katogorien som vi har defineret ovenover
    game_awards_2022 = data[["Category/Organization", category]]

    # Her laver vi et tomt dictionary til at gemme spil titlerne og deres mængde af awards
    game_awards_count = {}

    # Her looper vi over hver række i vores datasæt
    for index, row in game_awards_2022.iterrows():
        try:
            # Her får vi titlerne på spillet
            game_titles = row["The Game Awards 2022 December 8, 2022[3]"].split(',')

            # Her looper vi henover hvert spil title
            for title in game_titles:
                # Hvis der er noget whitespace eller tomme felter, så bruger vi strip() til at fjerne det
                title = title.strip()

                # Her tjekker vi om spillet allerede eksisterer i vores dictionary
                if title in game_awards_count:
                    # Vi ligger spillet oveni det nuværende count
                    game_awards_count[title] += 1
                else:
                    # Hvis spillet ikke findes i vores dictionary oprettes det her og tildeles count
                    game_awards_count[title] = 1
        except KeyError:
            print("Error: The specified category does not exist in the DataFrame.")
            break

    # Her finder vi det spil med flest awards
    max_awards = max(game_awards_count.values())

    # Her tjekker vi om der er flere spil med samme mængde awards i toppen
    games_with_max_awards = [game_title for game_title, award_count in game_awards_count.items() if award_count == max_awards]

    print("The game(s) that won the most awards at " + category + ":")
    for game in games_with_max_awards:
        print(game)

except FileNotFoundError:
    print("Error: The specified CSV file was not found.")
except Exception as e:
    print("An error occurred:", str(e))
