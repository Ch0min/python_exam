import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../../data/January-March-CLEAN.csv')

df['Platform(s)'] = df['Platform(s)'].str.split(', ')
df = df.explode('Platform(s)')

# Her sørger vi for at bruge fillna til at håndtere de steder hvor der ikke er en genre tilstede
df['Genre(s)'].fillna('Unknown', inplace=True)

# Her bruger vi matplob til at visuelisere vores data
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Genre(s)', hue='Platform(s)')
plt.xticks(rotation=90)
plt.xlabel('Genre')
plt.ylabel('Count')
plt.title('Distribution of Platforms by Genre')
plt.legend(title='Platform')
plt.tight_layout()
plt.show()
