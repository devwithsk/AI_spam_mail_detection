import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# =========================
# LOAD DATASET
# =========================

df = pd.read_csv("mail_data.csv", encoding="latin-1")

print("Dataset Loaded Successfully!")
print(df.head())

# =========================
# CLEAN DATASET COLUMNS
# =========================

# If dataset has extra unnamed columns, remove them
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

# Rename columns if needed
if "v1" in df.columns and "v2" in df.columns:
    df = df.rename(columns={"v1": "Category", "v2": "Message"})

# Keep only required columns
df = df[["Category", "Message"]]

# Remove missing values
df = df.dropna()

print("\nCleaned Dataset:")
print(df.head())

# =========================
# FEATURES & TARGET
# =========================

X = df["Message"]
y = df["Category"]

# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# TEXT VECTORIZATION
# =========================

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# =========================
# MODEL TRAINING
# =========================

model = MultinomialNB()
model.fit(X_train_vectorized, y_train)

print("\nModel Training Completed!")

# =========================
# MODEL EVALUATION
# =========================

predictions = model.predict(X_test_vectorized)

accuracy = accuracy_score(y_test, predictions)

print(f"\nAccuracy: {accuracy:.2f}")

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# =========================
# CUSTOM PREDICTION
# =========================

sample_message = ["Congratulations! You won a free iPhone. Click here now."]

sample_vector = vectorizer.transform(sample_message)

result = model.predict(sample_vector)

print("\nSample Message Prediction:")
print(result[0])

# =========================
# SAVE MODEL
# =========================

joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("\nModel and Vectorizer Saved Successfully!")