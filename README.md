# AI Phishing Email Detector

https://phishing-email-detector-m7dvtnpq8cwyznjeqf26lr.streamlit.app/
A machine learning project that classifies email text as either phishing or legitimate.

## Technologies

- Python
- Pandas
- Scikit-learn
- TF-IDF
- Logistic Regression
- Streamlit
- Git / GitHub

## Project Structure

```text
phishing-email-detector/
├── data/
│   └── phishing_emails.csv
├── model/
│   └── phishing_model.pkl
├── train_model.py
├── predict.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Dataset Format

Place your dataset here:

```text
data/phishing_emails.csv
```

The CSV needs two columns:

```text
text,label
```

Use:

- `0` = legitimate email
- `1` = phishing email

Example:

```csv
text,label
"Reminder: our meeting is at 2 PM tomorrow.",0
"URGENT: Verify your account immediately by clicking this link.",1
```

## Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Train the Model

```bash
python train_model.py
```

## Test in the Terminal

```bash
python predict.py
```

## Run the Web App

```bash
streamlit run app.py
```

## Results
Test Dataset: 1,200 emails

Accuracy: 97.83%

Phishing:
Precision: 97%
Recall: 99%
F1 Score: 98%

Legitimate:
Precision: 99%
Recall: 97%
F1 Score: 98%

