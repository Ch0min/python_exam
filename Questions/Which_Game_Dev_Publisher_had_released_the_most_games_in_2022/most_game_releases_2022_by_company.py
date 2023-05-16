import csv

def most_releases_by_platform():
    game_counts = {}

    for filename in ["../data/January-March.csv", "../data/July-September.csv", "../data/October-December.csv"]:
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                developers = row["Developer(s)"].split("; ")
                for dev in developers:
                    if dev in game_counts:
                        game_counts[dev] += 1
                    else:
                        game_counts[dev] = 1

    most_releases = max(game_counts, key=game_counts.get)
    count = game_counts[most_releases]
    return [most_releases, count]
