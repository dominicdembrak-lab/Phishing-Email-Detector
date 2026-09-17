import os
import joblib

MODEL_PATH = "model/phishing_model.pkl"

def main():
    if not os.path.exists(MODEL_PATH):
        print("Model not found.")
        print("Run train_model.py first.")
        return

    model = joblib.load(MODEL_PATH)
    email = input("Paste an email:\n\n")

    prediction = model.predict([email])[0]
    probabilities = model.predict_proba([email])[0]
    phishing_probability = probabilities[1]

    print()
    if prediction == 1:
        print("WARNING: Potential phishing email")
    else:
        print("Email appears legitimate")

    print(f"Phishing probability: {phishing_probability:.2%}")

if __name__ == "__main__":
    main()
