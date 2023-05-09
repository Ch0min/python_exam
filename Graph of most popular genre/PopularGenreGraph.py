import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('../data/October-December-CLEAN.csv')

# Group the data by genre and count the number of games in each genre
genre_counts = df['Genre(s)'].value_counts()

# Plot the graph
plt.bar(genre_counts.index, genre_counts.values)
plt.xlabel('Genre')
plt.ylabel('Number of Games')
plt.title('Number of Games by Genre')
plt.xticks(rotation=90)

# Show the graph
plt.show()
