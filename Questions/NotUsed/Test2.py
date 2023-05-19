import pandas as pd
from sklearn import tree

# Read genre data from CSV
genre_data = pd.read_csv('../../data/January-March-CLEAN.csv', header=None)
# Read platform data from CSV
platform_data = pd.read_csv('../../data/January-March-CLEAN.csv', header=None)

# Training data
X = genre_data.values.tolist()
y = platform_data.values.tolist()

# Training the model
clf = tree.DecisionTreeClassifier()
clf.fit(X, y)

# Predicting the platform for a new gaming genre
new_genre = [['Action-adventure']]  # Example new genre
predicted_platform = clf.predict(new_genre)

print(f"The predicted platform for the new genre is: {predicted_platform[0]}")