import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/Critically_acclaimed_games.csv")

axes = df.plot(x='Title', y='Average score', kind='bar', figsize=(10, 6))
axes.set_xlabel("Game Title", fontsize=10)
axes.set_ylabel("Average score", fontsize=10)
axes.set_ylim(89, 100)

plt.xticks(rotation=90, fontsize=10)
plt.title("Critically Acclaimed Games")
plt.tight_layout()
plt.show()
