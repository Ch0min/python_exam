import pandas as pd

def get_most_releases_by_platform():
    platform_counts = {}

    file_paths = ["../../data/January-March.csv", "../../data/July-September.csv", "../../data/October-December.csv"]

    for file_path in file_paths:
        df = pd.read_csv(file_path)
        platforms = df["Platform(s)"].str.split(", ")
        for platform_list in platforms:
            # Check if platform_list is not NaN or float
            if isinstance(platform_list, list):
                for platform in platform_list:
                    if platform in platform_counts:
                        platform_counts[platform] += 1
                    else:
                        platform_counts[platform] = 1

    most_releases = max(platform_counts, key=platform_counts.get)
    print(most_releases)

get_most_releases_by_platform()
