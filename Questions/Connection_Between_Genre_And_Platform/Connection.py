import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df_jan_mar = pd.read_csv('../data/January-March-CLEAN.csv')
df_apr_jun = pd.read_csv('../data/April-June-CLEAN.csv')
df_jul_sep = pd.read_csv('../data/July-September-CLEAN.csv')
df_oct_dec = pd.read_csv('../data/October-December-CLEAN.csv')

# Her bruger vi concat til at sætte vores 4 csv filer sammen i et samlet datasæt
df = pd.concat([df_jan_mar[['Platform(s)', 'Genre(s)']],
                df_apr_jun[['Platform(s)', 'Genre(s)']],
                df_jul_sep[['Platform(s)', 'Genre(s)']],
                df_oct_dec[['Platform(s)', 'Genre(s)']]])

# Her bruger vi fillna til at håndtere tomme genre kolonner
df['Genre(s)'].fillna('Unknown', inplace=True)

# Her bruger vi df.explode til at håndtere hvis et spil så flere platforme, den sætter hvert element ind i en ny række
df['Platform(s)'] = df['Platform(s)'].str.split(', ')
df = df.explode('Platform(s)')

# Her inddeler vi vores data i features, hvor vi har genres og platformer
X = df['Genre(s)']
y = df['Platform(s)']

# Her gør vi så X altså genres kun er en feature
X = X.values.reshape(-1, 1)

# Her fjerner vi rækkerne med en NaN value
nan_indices = pd.isnull(y)
X_train = X[~nan_indices]
y_train = y[~nan_indices]

# Vi opdeler vores datasæt i et træningssæt og et testingsæt
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# Her bruger vi CountVectorizer til at konvertere vores genre data til en numerisk feature
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train.flatten())
X_test = vectorizer.transform(X_test.flatten())

# Vi bruger vores data til at træne på en logistisk regressionsmodel
model = LogisticRegression()
model.fit(X_train, y_train)

# Her prøver vi at bruge vores test data til at forudse gaming platformen
y_pred = model.predict(X_test)

# Her beregner vi hvor præcis vores model er
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)