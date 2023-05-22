import pandas as pd
import glob
import os
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

try:
    # kombiner csv filer
    path = "../data/"
    all_files = glob.glob(os.path.join(path, "*CLEAN.csv"))
    df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)

    df.drop('Ref.', axis=1, inplace=True)

    # sum af awards for hvert spil
    game_awards = pd.read_csv('../data/cleaned_file.csv', na_values=['—'])
    game_awards = game_awards.iloc[2:, 2:].apply(
        pd.Series.value_counts).fillna(0)

    # kombiner spildata og awards
    total_awards = game_awards.astype('int64').sum(axis=1)
    df_awards = total_awards.reset_index()
    df_awards.columns = ['Title', 'Awards']

    game_data = pd.merge(df, df_awards, on='Title', how='left').fillna(0)
    game_data.drop(index=df.index[-1], axis=0, inplace=True)

    # onehot encode
    categorical_columns = ['Month', 'Day',
                           'Platform(s)', 'Genre(s)', 'Developer(s)', 'Publisher(s)']

    onehot_encoder = OneHotEncoder()

    onehot_encoded = onehot_encoder.fit_transform(
        game_data[categorical_columns])

    onehot_encoded_df = pd.DataFrame(onehot_encoded.toarray(),
                                     columns=onehot_encoder.get_feature_names_out(categorical_columns))

    # erstat game_data med onehot encoded data
    game_data.drop(columns=categorical_columns, inplace=True)
    game_data = pd.concat([game_data, onehot_encoded_df], axis=1)

    # split data i features og target
    X = game_data.drop(columns=['Title', 'Awards'])
    y = game_data['Awards']

    # columnnames
    feature_names = X.columns

    # split data training og testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # skaler features for at standardisere data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # GridSearchCV optimal k_value
    k_values = range(1, 50)
    param_grid = {'n_neighbors': k_values}
    grid_search = GridSearchCV(
        KNeighborsRegressor(), param_grid, cv=5, n_jobs=-1)
    grid_search.fit(X_train_scaled, y_train)

    # brug bedste k_value
    best_k = grid_search.best_params_['n_neighbors']
    knn = KNeighborsRegressor(n_neighbors=best_k)
    knn.fit(X_train_scaled, y_train)

    # test set
    y_pred = knn.predict(X_test_scaled)

    # evaluer model
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Mean Squared Error:", mse)
    print("Mean Absolute Error:", mae)
    print("R-squared:", r2)

    # test model med nyt spil
    new_game_data = pd.DataFrame({
        'Month': [2],
        'Day': [25],
        'Platform(s)': ['Win, PS4, PS5, XBO, XSX'],
        'Genre(s)': ['Action-Role-playing'],
        'Developer(s)': ['FromSoftware'],
        'Publisher(s)': ['Bandai Namco Entertainment']
    })

    # ny dataframe ligesom test dataframe med nyt test spil
    new_game_encoded_df = pd.DataFrame(np.zeros((1, len(onehot_encoder.get_feature_names_out(categorical_columns))),
                                                dtype=int),
                                       columns=onehot_encoder.get_feature_names_out(categorical_columns))

    for col in categorical_columns:
        column_name = f"{col}_{new_game_data[col].iloc[0]}"
        if column_name in new_game_encoded_df.columns:
            new_game_encoded_df[column_name] = 1

    # skaler nyt spil data
    new_game_scaled = scaler.transform(new_game_encoded_df)

    # predict awards
    new_game_pred = knn.predict(new_game_scaled)
    print("Predicted awards for the new game:", new_game_pred[0])

except FileNotFoundError:
    print("Error: File not found. Please make sure the file path is correct.")

except Exception as e:
    print("An error occurred:", str(e))
