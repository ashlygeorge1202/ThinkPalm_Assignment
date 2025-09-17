# Automation QA Engineer — Home Assignment

This project is a **Python-based API Test Automation Framework** for [httpbin.org](https://httpbin.org/), built with **pytest**.  
It demonstrates response validation, request inspection, dynamic test data generation, retry logic, configuration handling, and reporting with **Allure**.

---

## 📂 Project Structure

ThinkPalm_Assignment/
│── clients/ # API client wrapper for httpbin
│── tests/ # Test cases
│── utils/ # Retry decorator, helpers
│── config.yaml # Configuration file
│── requirements.txt # Python dependencies
│── .github/workflows/ # GitHub Actions CI/CD pipeline
│── README.md # Documentation (this file)


---

## ⚙️ Setup (Local)

### 1. Clone repository
```bash
git clone https://github.com/<your-username>/ThinkPalm_Assignment.git
cd ThinkPalm_Assignment

2. Create and activate virtual environment

python -m venv .venv
# Activate:
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

Running Tests Locally

1. Run pytest

pytest -v --alluredir=reports/allure-results

2. Generate and view Allure report

allure serve reports/allure-results
This will open a local web server in your browser with a detailed test report.

CI/CD (GitHub Actions)

On every push to main, GitHub Actions will:

Set up Python environment

Install dependencies

Run tests with pytest

Generate Allure results and reports

Upload reports as artifacts

Artifacts can be downloaded from the GitHub Actions run summary.

Features Implemented

✅ Configuration via YAML (config.yaml)
✅ Custom retry decorator with detailed logging
✅ Dynamic test data with Faker
✅ Allure reporting (local + CI artifacts)
✅ CI/CD via GitHub Actions

Notes

httpbin.org sometimes returns 503 Service Unavailable.
Our retry decorator handles retries before failing.

A dummy test ensures Allure always generates results, even if httpbin is down.

Author
Ashly George
Automation QA Engineer Assignment