
# AI-Driven Cyber Threat Awareness and Detection Prototype

Entry-level analyst prototype: classify login/network events as Normal (0) or Suspicious (1).

## Submitted by:
```
Name- Gopesh Aggarwal
Roll No.- 2301730158
Course- Btech CSE AIML Sec-C Sem-7
```

## Project Structure

```
data/cybersecurity_dataset.csv  # synthetic dataset (200 rows)
src/generate_data.py            # creates the dataset
src/01_threat_analysis.py       # Task 2: EDA + plots
src/02_ml_classification.py     # Task 3: Decision Tree classifier
src/03_dl_prototype.py          # Task 4: MLP neural net vs Decision Tree
outputs/                        # saved plots
```

## Dataset Columns

- `login_attempts`, `failed_logins`, `bytes_transferred`, `phishing_score`, `unusual_hour`, `label`

## Setup (Task 1)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/generate_data.py
```

## Run Analysis

```bash
python src/01_threat_analysis.py   # EDA + plots in outputs/
python src/02_ml_classification.py # accuracy, precision, recall, F1
python src/03_dl_prototype.py      # ML vs DL comparison
```

## Key Findings

- Suspicious events have higher `failed_logins` and `phishing_score`.
- Decision Tree gives high accuracy on this simple rule-based data.
- MLP (1 hidden layer, 10 neurons) gets similar accuracy but trains slower — overkill for small data.

## Ethical & Operational Notes

- False positives can block legit users; false negatives miss attacks — balance precision/recall.
- Do not use personal data without consent; anonymize logs.
- AI assists analysts, does not replace them; review flagged events manually.
- Retrain regularly as attackers change tactics (model drift).
