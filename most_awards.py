import pandas as pd

test = pd.read_csv("./data/April-June.csv")
print(test)

df = pd.read_csv("./data/Major_awards.csv")

df2 = df["The Game Awards 2022 December 8, 2022[3]"]

game_counts = {}

for row in df2:
    game_name = row
    print(game_name)
    game_counts[game_name] = game_counts.get(game_name, 0) + 1


max_count = max(game_counts.values())
most_mentioned_game = [game for game,
                       count in game_counts.items() if count == max_count]

print("Most mentioned game(s):", most_mentioned_game)
