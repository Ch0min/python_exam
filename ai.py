import pandas as pd
import glob
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Define the path to the CSV files
path = r'data'

# Identify all CSV files with the specific pattern
all_files = glob.glob(os.path.join(path, "*CLEAN.csv"))

# Merge all CSV files into one DataFrame
df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)

# Remove 'Ref.' column from the DataFrame
df.drop('Ref.', axis=1, inplace=True)

# Read the game awards CSV file
game_awards = pd.read_csv('./data/cleaned_file.csv', na_values=['—'])

game_awards = game_awards.iloc[2:, 2:].apply(pd.Series.value_counts).fillna(0)

# Sum up the awards across different categories for each game
# and combine them with the game release data
# maybe not need astype()
total_awards = game_awards.astype('int64').sum(axis=1)
df_other = total_awards.reset_index()
df_other.columns = ['Title', 'Awards']

# dataframe with games and the amount of awards
df_with_awards = pd.merge(df, df_other, on='Title', how='left').fillna(0)
print(df_with_awards)

game_data = df_with_awards
# game_data['Day'] = game_data['Day'].astype(int)
# game_data['Awards'] = game_data['Awards'].astype(int)

# drop the bottom row as it only contains 0
game_data.drop(index=df.index[-1], axis=0, inplace=True)
# game_data = game_data['Awards'].astype(int)
print(game_data)

# Preprocess the data
label_encoder = LabelEncoder()
categorical_columns = ['Month', 'Day',
                       'Platform(s)', 'Genre(s)', 'Developer(s)', 'Publisher(s)']
# categorical_columns = [
#     'Month', 'Platform(s)', 'Genre(s)', 'Developer(s)', 'Publisher(s)']
game_data[categorical_columns] = game_data[categorical_columns].apply(
    lambda col: label_encoder.fit_transform(col))

# Split the data into features (X) and target (y)
X = game_data.drop(columns=['Title', 'Awards'])
y = game_data['Awards']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train the kNN model
k = 5  # Choose an appropriate value for k
knn = KNeighborsRegressor(n_neighbors=k)
knn.fit(X_train, y_train)

# Predictions on the test set
y_pred = knn.predict(X_test)

# Calculate evaluation metrics
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("Mean Absolute Error:", mae)
print("R-squared:", r2)

# Predict the success of a new game
# Replace this with the actual feature values
new_game_features = np.array([[5, 15, 1, 3, 0, 1]])
predicted_success = knn.predict(new_game_features)
print("Predicted Success:", predicted_success)
