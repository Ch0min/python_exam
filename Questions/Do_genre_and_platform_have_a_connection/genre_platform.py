import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

# Read the CSV files
df1 = pd.read_csv('../data/January-March-CLEAN.csv')
df2 = pd.read_csv('../data/April-June-CLEAN.csv')
df3 = pd.read_csv('../data/July-September-CLEAN.csv')
df4 = pd.read_csv('../data/October-December-CLEAN.csv')

# Concatenate the dataframes
df = pd.concat([df1, df2, df3, df4], ignore_index=True)

# Create a label encoder
label_encoder = LabelEncoder()

# Encode the Genre(s) column
df['Genre_encoded'] = label_encoder.fit_transform(df['Genre(s)'])

# Split the Platform(s) column into separate binary features
platforms = df['Platform(s)'].str.get_dummies(', ')

# Concatenate the original dataframe with the platform features
df_encoded = pd.concat([df, platforms], axis=1)

# Select the relevant columns for clustering
columns_to_cluster = ['Genre_encoded'] + list(platforms.columns)

# Perform K-means clustering
kmeans = KMeans(n_clusters=3)  # Specify the number of clusters
kmeans.fit(df_encoded[columns_to_cluster])

# Retrieve the cluster labels
cluster_labels = kmeans.labels_

# Add the cluster labels to the dataframe
df_encoded['Cluster'] = cluster_labels

# Print the clusters
for cluster in range(kmeans.n_clusters):
    print(f"Cluster {cluster}:")
    cluster_data = df_encoded[df_encoded['Cluster'] == cluster]
    print(cluster_data[['Genre(s)', 'Platform(s)']])
    print()

