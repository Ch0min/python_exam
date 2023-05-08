import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('./data/Major_awards.csv')

# Replace multiple words in the DataFrame
replacements = {
    'Christopher Judge as Kratos God of War Ragnarök': 'God of War Ragnarök',
    'Manon Gage as Marissa Marcel Immortality': 'Immortality',
    'Laya Deleon Hayes as Angrboda God of War Ragnarök': 'God of War Ragnarök'
}
df = df.replace(replacements)

# Write the cleaned DataFrame to a new CSV file
df.to_csv('data/cleaned_file.csv', index=False)

# Read the cleaned CSV file into a new DataFrame
cleaned_df = pd.read_csv('./data/cleaned_file.csv')

# Perform additional edits on the cleaned DataFrame
# ...

# Write the modified DataFrame to the same CSV file
cleaned_df.to_csv('data/cleaned_file.csv', index=False)
