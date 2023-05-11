import pandas as pd
import glob
import os
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Define the path to the CSV files
path = r'data'

# Identify all CSV files with the specific pattern
all_files = glob.glob(os.path.join(path, "*CLEAN.csv"))

# Merge all CSV files into one DataFrame
df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)
print(df)

# One-hot encode categorical features
columns_to_encode = ['Month', 'Day', 'Title',
                     'Platform(s)', 'Genre(s)', 'Developer(s)', 'Publisher(s)', 'Ref.']
column_transformer = make_column_transformer(
    (OneHotEncoder(), columns_to_encode),
    remainder='passthrough'
)
encoded_df = column_transformer.fit_transform(df)

# Split the dataset into training and testing sets
X = encoded_df.drop('Ref.', axis=1)
y = encoded_df['Ref.']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

# Apply the k-nearest neighbors algorithm
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Predict the quality of new games
new_game_data = pd.DataFrame({
    'Month': [1, 1],
    'Day': [1, 1],
    'Title': ['New Game 1', 'New Game 2'],
    'Platform(s)': ['PS4, PS5', 'PC'],
    'Genre(s)': ['Action role-playing', 'Simulation'],
    'Developer(s)': ['Developer 1', 'Developer 2'],
    'Publisher(s)': ['Publisher 1', 'Publisher 2'],
    'Ref.': [0, 0]
})

encoded_new_game_data = column_transformer.transform(new_game_data)
predicted_quality = knn.predict(encoded_new_game_data)

print(predicted_quality)
