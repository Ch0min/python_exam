import csv

def get_most_releases_by_platform():
    platform_counts = {}

    for filename in ["../../data/January-March.csv", "../../data/July-September.csv", "../../data/October-December.csv"]:
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                platforms = row["Platform(s)"].split(", ")
                for platform in platforms:
                    if platform in platform_counts:
                        platform_counts[platform] += 1
                    else:
                        platform_counts[platform] = 1

    most_releases = max(platform_counts, key=platform_counts.get)
    count = platform_counts[most_releases]
    return [most_releases, count]


print(get_most_releases_by_platform())