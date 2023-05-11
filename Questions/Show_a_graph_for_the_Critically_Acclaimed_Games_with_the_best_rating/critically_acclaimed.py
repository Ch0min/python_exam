import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

df = pd.read_csv("../data/Critically_acclaimed_games.csv")

# Split the 'Platform(s)' column into separate rows
df['Platform(s)'] = df['Platform(s)'].str.split(', ')
df = df.explode('Platform(s)')

# Different colors for each platform
platform_color_map = {'NS': 'red', 'PS5': 'blue',
                      'XSX': 'darkgreen', 'XBO': 'limegreen', 'Win': 'yellow'}
colors = df['Platform(s)'].map(platform_color_map).tolist()

axes = df.plot(x='Title', y='Average score',
               color=colors, kind='bar', figsize=(10, 6))
axes.set_xlabel("Game Title", fontsize=10)
axes.set_ylabel("Average score", fontsize=10)
axes.set_ylim(89, 100)

# Create a list of legend handles using platform_color_map
legend_handles = [mpatches.Patch(color=color, label=platform)
                  for platform, color in platform_color_map.items()]

# Add the legend to the plot
axes.legend(handles=legend_handles, loc='upper right')

plt.xticks(rotation=90, fontsize=10)
plt.title("Critically Acclaimed Games")
plt.tight_layout()
plt.show()
