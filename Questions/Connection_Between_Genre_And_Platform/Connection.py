import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.impute import SimpleImputer

df_jan_mar = pd.read_csv('../../data/January-March-CLEAN.csv')
df_apr_jun = pd.read_csv('../../data/April-June-CLEAN.csv')
df_jul_sep = pd.read_csv('../../data/July-September-CLEAN.csv')
df_oct_dec = pd.read_csv('../../data/October-December-CLEAN.csv')

# Concat all dataframes into one and extract the "Month" and "Title" columns:
df = pd.concat([df_jan_mar[['Platform(s)', 'Genre(s)']],
                df_apr_jun[['Platform(s)', 'Genre(s)']],
                df_jul_sep[['Platform(s)', 'Genre(s)']],
                df_oct_dec[['Platform(s)', 'Genre(s)']]])

# Handle missing values in the genre column
df['Genre(s)'].fillna('Unknown', inplace=True)

# Split the data into features (genre) and target variable (platform)
X = df['Genre(s)']
y = df['Platform(s)']

# Reshape X to have a single feature
X = X.values.reshape(-1, 1)

# Remove rows with NaN values in y
nan_indices = pd.isnull(y)
X_train = X[~nan_indices]
y_train = y[~nan_indices]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# Convert genre text into numerical features using CountVectorizer
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train.flatten())
X_test = vectorizer.transform(X_test.flatten())

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict the gaming platform for the test data
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
