import csv
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score

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

