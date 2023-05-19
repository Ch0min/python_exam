import pandas as pd
import glob
import os
<<<<<<< HEAD
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Combine all CSV files into one DataFrame
path = "data/"
# path = r'data'
all_files = glob.glob(os.path.join(path, "*CLEAN.csv"))
df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)

# Remove Ref column
df.drop('Ref.', axis=1, inplace=True)

# Sum up the awards across different categories for each game
game_awards = pd.read_csv('./data/cleaned_file.csv', na_values=['—'])
game_awards = game_awards.iloc[2:, 2:].apply(pd.Series.value_counts).fillna(0)

# Combine awards with the game release data
total_awards = game_awards.astype('int64').sum(axis=1)
df_other = total_awards.reset_index()
df_other.columns = ['Title', 'Awards']

game_data = pd.merge(df, df_other, on='Title', how='left').fillna(0)
game_data.drop(index=df.index[-1], axis=0, inplace=True)

# onehot encode
categorical_columns = ['Month', 'Day',
                       'Platform(s)', 'Genre(s)', 'Developer(s)', 'Publisher(s)']

onehot_encoder = OneHotEncoder()

onehot_encoded = onehot_encoder.fit_transform(game_data[categorical_columns])

onehot_encoded_df = pd.DataFrame(onehot_encoded.toarray(),
                                 columns=onehot_encoder.get_feature_names_out(categorical_columns))

# Drop the original columns from the game_data DataFrame
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

# Scale the features to standardize
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Use GridSearchCV to find the optimal value of k
k_values = range(1, 50)
param_grid = {'n_neighbors': k_values}
grid_search = GridSearchCV(KNeighborsRegressor(), param_grid, cv=5)
grid_search.fit(X_train_scaled, y_train)

# Get the best value of k and use it to train
best_k = grid_search.best_params_['n_neighbors']
knn = KNeighborsRegressor(n_neighbors=best_k)
knn.fit(X_train_scaled, y_train)

# Predictions on the test set
y_pred = knn.predict(X_test_scaled)

# Calculate evaluation metrics
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("Mean Absolute Error:", mae)
print("R-squared:", r2)

# Predict the success of a new game
# Create a DataFrame with the new game's features
new_game_data = pd.DataFrame({
    'Month': [2],
    'Day': [25],
    'Platform(s)': ['Win, PS4, PS5, XBO, XSX'],
    'Genre(s)': ['Action-Role-playing'],
    'Developer(s)': ['FromSoftware'],
    'Publisher(s)': ['Bandai Namco Entertainment']
})

# Create a DataFrame with the same columns as the one-hot encoded training data and fill it with zeros
new_game_encoded_df = pd.DataFrame(np.zeros((1, len(onehot_encoder.get_feature_names_out(categorical_columns))),
                                            dtype=int),
                                   columns=onehot_encoder.get_feature_names_out(categorical_columns))

# Update this DataFrame with the new game data
for col in categorical_columns:
    column_name = f"{col}_{new_game_data[col].iloc[0]}"
    if column_name in new_game_encoded_df.columns:
        new_game_encoded_df[column_name] = 1

# Scale the new game data
new_game_scaled = scaler.transform(new_game_encoded_df)

# Predict the success of the new game
new_game_pred = knn.predict(new_game_scaled)
print("Predicted awards for the new game:", new_game_pred[0])
=======
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
>>>>>>> 2285336 (rebased main into oscar)
