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
total_awards = game_awards.sum(axis=1)
df_other = total_awards.reset_index()
df_other.columns = ['Title', 'Awards']

# dataframe with games and the amount of awards
df_with_awards = pd.merge(df, df_other, on='Title', how='left').fillna(0)
