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
print(x)
y = np.array(list(developer_counts.values()))

# Vi bruger cross-validation til at få et estimat om vores model er præcis.
model = make_pipeline(StandardScaler(), Ridge(alpha=0.1))

# Træn model med data (lineær, derfor x, og y)
model.fit(x, y)

predictions = {}

for developer in developer_counts:
    #list i en liste fordi predict kræver 2d array
    count = round(model.predict([[developer_counts[developer]]])[0])  # Forudsig antallet af spil udgivet af en spiludvikler
    predictions[developer] = count  # Gem forudsigelsen i dictionaryen predictions med udvikleren som nøgle

# Print forudsigelserne
for developer, count in predictions.items():
    print(f"{developer} forventes at udgive {count} spil i april.")

# Sorter spiludviklerne og predicted_counts så den viser antallet af spil spiludviklerne har udgivet, fra flest udgivede og ned af til færrest udgivede
# Få de 10 spiludviklere som har udgivet flest spil og antallet af spil de har udgivet
df = pd.DataFrame({'developer': list(predictions.keys()), 'predicted_counts': list(predictions.values())})

sorted_data = df.sort_values(by='predicted_counts', ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.bar(sorted_data['developer'], sorted_data['predicted_counts'])
plt.xlabel("Game Developer")
plt.ylabel("Number of games predicted")
plt.title("Predicted number of games released by game gevelopers in April")

plt.xticks(rotation=45, fontsize=6)

plt.tight_layout() # fjerener whitespace
plt.show()