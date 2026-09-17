import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

DATA_PATH = "data/phishing_emails.csv"
MODEL_PATH = "model/phishing_model.pkl"

def main():
    if not os.path.exists(DATA_PATH):
        print(f"Dataset not found: {DATA_PATH}")
        print("Add a CSV file with columns named 'text' and 'label'.")
        return

    df = pd.read_csv(DATA_PATH)

    if "text" not in df.columns or "label" not in df.columns:
        print("Your CSV must contain columns named 'text' and 'label'.")
        print("Use 0 for legitimate emails and 1 for phishing emails.")
        return

    df = df[["text", "label"]].dropna()
    df["text"] = df["text"].astype(str)

    X = df["text"]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    model = Pipeline([
        ("tfidf", TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2),
            min_df=2,
            max_df=0.95,
            sublinear_tf=True
        )),
        ("classifier", LogisticRegression(
            max_iter=1000,
            class_weight="balanced"
        ))
    ])

    print("Training model...")
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print()
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print()
    print(classification_report(
        y_test, y_pred, target_names=["Legitimate", "Phishing"]
    ))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    os.makedirs("model", exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print()
    print(f"Model saved to: {MODEL_PATH}")

if __name__ == "__main__":
    main()
