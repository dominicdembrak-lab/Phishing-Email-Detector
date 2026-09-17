import os
import re
import joblib
import streamlit as st


MODEL_PATH = "model/phishing_model.pkl"

st.set_page_config(
    page_title="Phishing Email Detector",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ AI Phishing Email Detector")

st.write(
    "Analyze an email using a machine-learning model trained to identify "
    "phishing attempts."
)

st.divider()

# Sidebar
with st.sidebar:
    st.header("Model Information")

    st.write("**Algorithm:** Logistic Regression")
    st.write("**Text Processing:** TF-IDF")
    st.write("**Training Emails:** 4,800")
    st.write("**Testing Emails:** 1,200")
    st.write("**Test Accuracy:** 97.83%")
    st.write("**Phishing Recall:** 99%")

    st.divider()

    st.caption(
        "This application was created for educational purposes and "
        "should not replace professional email security software."
    )


def find_indicators(email):
    indicators = []

    email_lower = email.lower()

    suspicious_words = [
        "urgent",
        "verify",
        "password",
        "suspended",
        "click here",
        "confirm",
        "account locked",
        "immediately",
        "payment",
        "login"
    ]

    for word in suspicious_words:
        if word in email_lower:
            indicators.append(f"Suspicious phrase detected: '{word}'")

    if re.search(r"https?://", email_lower):
        indicators.append("Email contains a URL")

    if re.search(r"\b\d{6,}\b", email_lower):
        indicators.append("Email contains a long numeric sequence")

    return indicators


if not os.path.exists(MODEL_PATH):

    st.error(
        "The trained model could not be found. "
        "Run train_model.py before starting the application."
    )

else:

    model = joblib.load(MODEL_PATH)

    email_text = st.text_area(
        "Email Content",
        height=275,
        placeholder="Paste the email you want to analyze here..."
    )

    analyze = st.button(
        "Analyze Email",
        type="primary",
        use_container_width=True
    )

    if analyze:

        if not email_text.strip():

            st.warning("Please paste an email before analyzing.")

        else:

            probabilities = model.predict_proba([email_text])[0]

            phishing_probability = probabilities[1]

            st.divider()

            st.subheader("Analysis Results")

            st.metric(
                "Phishing Probability",
                f"{phishing_probability:.1%}"
            )

            st.progress(float(phishing_probability))

            # More cautious display around the 50% boundary
            if 0.40 <= phishing_probability <= 0.60:

                st.warning(
                    "⚠️ Uncertain Result — The model is not strongly "
                    "confident in either classification."
                )

            elif phishing_probability > 0.60:

                st.error("🚨 Potential Phishing Email")

            else:

                st.success("✅ Likely Legitimate Email")

            indicators = find_indicators(email_text)

            st.subheader("Email Indicators")

            if indicators:

                for indicator in indicators:
                    st.write(f"• {indicator}")

            else:

                st.write(
                    "No obvious rule-based phishing indicators were detected."
                )

            st.caption(
                "The indicators above are simple rule-based observations "
                "and are separate from the machine-learning model."
            )