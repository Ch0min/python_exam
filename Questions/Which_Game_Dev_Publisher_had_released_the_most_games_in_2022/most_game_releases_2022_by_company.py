import pandas as pd
import numpy as np

game_counts = {}
file_paths = ["../../data/January-March.csv", "../../data/April-June.csv", "../../data/July-September.csv",
              "../../data/October-December.csv"]

for file_path in file_paths:
    df = pd.read_csv(file_path)
    developers = df["Developer(s)"].str.split("; ")

    for dev_list in developers:
        if isinstance(dev_list, list):
            for dev in dev_list:
                if dev in game_counts:
                    game_counts[dev] += 1
                else:
                    game_counts[dev] = 1

most_releases = max(game_counts, key=game_counts.get)
count = game_counts[most_releases]
print("Most releases: " + str(most_releases) + ", released " + str(count) + " times.")
