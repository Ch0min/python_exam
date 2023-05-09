import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/Critically_acclaimed_games.csv")
ax = df.plot(x='Title', y='Average score', kind='bar', figsize=(10, 6))
ax.set_xlabel("Title", fontsize=10)
ax.set_ylabel("Average score", fontsize=10)
ax.set_ylim(89, 100)

plt.xticks(rotation=60, fontsize=10)
plt.title("Critically Acclaimed Games")
plt.tight_layout()
plt.show()
