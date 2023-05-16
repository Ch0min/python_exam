import pandas as pd
import glob
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
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
total_awards = game_awards.sum(axis=1)
df_other = total_awards.reset_index()
df_other.columns = ['Title', 'Awards']

# dataframe with games and the amount of awards
df_with_awards = pd.merge(df, df_other, on='Title', how='left').fillna(0)

game_data = df_with_awards
game_data.drop(index=df.index[-1], axis=0, inplace=True)

# Preprocess the data
categorical_columns = ['Month', 'Day',
                       'Platform(s)', 'Genre(s)', 'Developer(s)', 'Publisher(s)']

# Instantiate the OneHotEncoder
onehot_encoder = OneHotEncoder()

# Fit and transform the categorical columns
onehot_encoded = onehot_encoder.fit_transform(game_data[categorical_columns])

# Create a DataFrame from the one-hot encoded categorical features
onehot_encoded_df = pd.DataFrame(onehot_encoded.toarray(
), columns=onehot_encoder.get_feature_names_out(categorical_columns))

# Drop the original categorical columns from the game_data DataFrame
game_data.drop(columns=categorical_columns, inplace=True)

# Concatenate the one-hot encoded columns to the game_data DataFrame
game_data = pd.concat([game_data, onehot_encoded_df], axis=1)

# Split the data into features (X) and target (y)
X = game_data.drop(columns=['Title', 'Awards'])
y = game_data['Awards']

# Store feature names
feature_names = X.columns

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
# Get the number of columns in X after one-hot encoding
num_encoded_cols = X.shape[1]

# Replace this with the actual feature values, with the same number of columns as X after one-hot encoding
new_game_features = np.array(
    [[5, 15, 1, 3, 0, 1] + [0] * (num_encoded_cols - 6)])

# Create a DataFrame from the new_game_features array
new_game_features_df = pd.DataFrame(new_game_features, columns=feature_names)

# Predict the success of the new game
predicted_success = knn.predict(new_game_features_df)

print("Predicted Success:", predicted_success)
