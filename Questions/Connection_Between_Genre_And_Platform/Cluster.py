import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import OneHotEncoder

# Read the CSV file
df = pd.read_csv("../../data/January-March-CLEAN.csv")

# Initialize the data structure
genre_platform_count = {}

# Iterate through rows
for index, row in df.iterrows():
    genre = row["Genre(s)"]
    platforms = row["Platform(s)"].split(",")

    # Increment count for each platform
    for platform in platforms:
        key = (genre, platform.strip())
        genre_platform_count[key] = genre_platform_count.get(key, 0) + 1

# Convert the genre_platform_count into a DataFrame
rows = []
for key, count in genre_platform_count.items():
    genre, platform = key
    rows.append({"genre": genre, "platform": platform, "count": count})

df = pd.DataFrame(rows)

# Encode the genre and platform columns
encoder = OneHotEncoder()
encoded_data = encoder.fit_transform(df[["genre", "platform"]])

# Create a new DataFrame with encoded columns and count
encoded_df = pd.DataFrame(encoded_data.toarray())
encoded_df["count"] = df["count"]

# Apply k-means clustering
kmeans = KMeans(n_clusters=5)  # Adjust the number of clusters as needed
clusters = kmeans.fit_predict(encoded_df)

# Add the cluster labels to the original DataFrame
df["cluster"] = clusters

# Analyze the resulting clusters
for cluster_id in set(clusters):
    print(f"Cluster {cluster_id}:")
    print(df[df["cluster"] == cluster_id][["genre", "platform", "count"]])
