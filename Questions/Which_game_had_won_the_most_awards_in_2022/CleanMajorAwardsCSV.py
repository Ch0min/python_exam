import pandas as pd

try:
    # Her læser vi csv filen med panda
    df = pd.read_csv('../../data/Major_awards.csv')

    # Vi laver et dictionary over vores replacements og bruger df.replace som er en funktion i panda til at erstatte værdierne
    replacements = {
        'Christopher Judge as Kratos God of War Ragnarök': 'God of War Ragnarök',
        'Manon Gage as Marissa Marcel Immortality': 'Immortality',
        'Laya Deleon Hayes as Angrboda God of War Ragnarök': 'God of War Ragnarök',
        'Kratos God of War Ragnarök': 'God of War Ragnarök'
    }
    df = df.replace(replacements)

    # Her skriver vi den nye data ind i en ny csv fil
    df.to_csv('../data/cleaned_file.csv', index=False)

except FileNotFoundError:
    print("File not found. Please check the file path.")

except Exception as e:
    print("An error occurred:", str(e))
