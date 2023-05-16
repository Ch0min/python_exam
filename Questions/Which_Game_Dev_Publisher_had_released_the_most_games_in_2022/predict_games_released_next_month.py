import csv
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

with open('../../data/January-March.csv', 'r') as f:
    reader = csv.reader(f)
    data = [row for row in reader]

# Få antal spil der er blevet udgivet af alle spiludviklere i de måneder der er valgt
developer_counts = {}
for row in data:
    month = row[0].strip().lower()
    if month != 'april':
        developer = row[5].strip()
        if developer not in developer_counts:
            developer_counts[developer] = 0
        developer_counts[developer] += 1

# Gør data klar til at træne model
X = np.array([[developer_counts[developer]] for developer in developer_counts.keys()])  # Convert to a 2D array
y = np.array(list(developer_counts.values()))

# Brug cross-validation til at estimere hvor god modellen er
model = make_pipeline(StandardScaler(), Ridge(alpha=0.1))
scores = cross_val_score(model, X, y, cv=5, scoring='r2')
mean_accuracy = np.mean(scores)

# Træner model med al dataen (lineær, derfor X, og y)
model.fit(X, y)

# Laver forudsigelser for alle spiludviklere
predictions = {}
for developer in developer_counts.keys():
    predicted_count = model.predict(np.array([[developer_counts[developer]]]).reshape(1, -1))[0]
    predictions[developer] = round(predicted_count)

# Print forudsigelserne
for developer, count in predictions.items():
    print(f"{developer} is predicted to release {count} games in April.")
print(f"Mean Accuracy: {mean_accuracy}")




# Sorter spiludviklerne og predicted_counts så den viser antallet af spil spiludviklerne har udgivet, fra flest udgivede og ned af til færrest udgivede
sorted_data = sorted(zip(predictions.keys(), predictions.values()), key=lambda x: x[1], reverse=True)

# Få de 10 spiludviklere som har udgivet flest spil og antallet af spil de har udgivet
developers = [d[0] for d in sorted_data[:10]]
predicted_counts = [d[1] for d in sorted_data[:10]]

# Ændrer størrelsen på figuren
plt.figure(figsize=(10, 6))

# Lav graf
plt.bar(developers, predicted_counts)
plt.xlabel("Game Developer")
plt.ylabel("Number of Games Predicted")
plt.title("Predicted Number of Games Released by Game Developers in April")

plt.xticks(rotation=45, ha='right', fontsize=6)

plt.tight_layout()
plt.show()
