import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

try:
    df = pd.read_csv("../data/Critically_acclaimed_games.csv")

    # split rækker med flere platforme
    df['Platform(s)'] = df['Platform(s)'].str.split(', ')
    df = df.explode('Platform(s)')

    # farver
    platform_color_map = {'NS': 'red', 'PS5': 'blue',
                          'XSX': 'darkgreen', 'XBO': 'limegreen', 'Win': 'yellow'}
    colors = df['Platform(s)'].map(platform_color_map).tolist()

    axes = df.plot(x='Title', y='Average score',
                   color=colors, kind='bar', figsize=(10, 6))
    axes.set_xlabel("Game Title", fontsize=10)
    axes.set_ylabel("Average score", fontsize=10)
    axes.set_ylim(89, 100)

    # visualiser farve platform
    legend_handles = [mpatches.Patch(color=color, label=platform)
                      for platform, color in platform_color_map.items()]
    axes.legend(handles=legend_handles, loc='upper right')

    plt.xticks(rotation=90, fontsize=10)
    plt.title("Critically Acclaimed Games")
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Error: File not found. Please make sure the file path is correct.")

except Exception as e:
    print("An error occurred:", str(e))
