import pandas as pd
import matplotlib.pyplot as plt

try:
    # Læser vores csv fil med panda
    df = pd.read_csv('../data/October-December-CLEAN.csv')

    # Her grupperer vi dataen ud fra genre og mængde af spil indenfor hver genre
    genre_counts = df['Genre(s)'].value_counts()

    # Her bruger vi matplot til at skabe en graf over dataen
    plt.bar(genre_counts.index, genre_counts.values)
    plt.xlabel('Genre')
    plt.ylabel('Number of Games')
    plt.title('Number of Games by Genre')
    plt.xticks(rotation=90)

    plt.show()

except FileNotFoundError:
    print("Error: File not found. Please make sure the file path is correct.")

except Exception as e:
    print("An error occurred:", str(e))
