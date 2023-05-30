import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

data = pd.read_csv('../../data/January-March.csv')

# Få antal spil der er blevet udgivet af alle spiludviklere i de måneder der er valgt
developer_counts = data.loc[~data['Month'].str.lower().str.contains('april'), 'Developer(s)'].str.strip().value_counts().to_dict()

# Gør data klar til at træne model
x = np.array([[developer_counts[developer]] for developer in developer_counts.keys()])
y = np.array(list(developer_counts.values()))

# Vi bruger cross-validation til at få et estimat om vores model er præcis.
model = make_pipeline(StandardScaler(), Ridge(alpha=0.1))
scores = cross_val_score(model, x, y, cv=5, scoring='r2')
mean_accuracy = np.mean(scores)

# Træn model med data (lineær, derfor x, og y)
model.fit(x, y)

# Lav forudsigelser for alle spiludviklere
predictions = {developer: round(model.predict([[developer_counts[developer]]])[0]) for developer in developer_counts.keys()}

# Vi printer en forudsigelse af mængden af spil fra en given udgiver.
for developer, count in predictions.items():
    print(f"{developer} is predicted to release {count} games in April.")
print(f"Mean Accuracy: {mean_accuracy}")

# Sorter spiludviklerne og predicted_counts så den viser antallet af spil spiludviklerne har udgivet, fra flest udgivede og ned af til færrest udgivede
# Få de 10 spiludviklere som har udgivet flest spil og antallet af spil de har udgivet
sorted_data = sorted(predictions.items(), key=lambda x: x[1], reverse=True)
developers = [d[0] for d in sorted_data[:10]]
predicted_counts = [d[1] for d in sorted_data[:10]]

# Lav graf
plt.figure(figsize=(10, 6))
plt.bar(developers, predicted_counts)
plt.xlabel("Game Developer")
plt.ylabel("Number of Games Predicted")
plt.title("Predicted Number of Games Released by Game Developers in April")

plt.xticks(rotation=45, ha='right', fontsize=6)

plt.tight_layout()
plt.show()
