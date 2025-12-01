
# 🚗 Motors – Playwright Python Automation Framework To Test Filters

This repository contains a complete **end-to-end automation framework** for testing the
Ayshei Motors web application using **Python + Playwright**.  
It includes filters testing, sorting validation, seller types, more-filters coverage, and car details validation.

---

## 📦 Tech Stack

- **Python 3.13+**
- **Playwright (sync API)**
- **Pytest**
- **Pytest-HTML (reports)**
- **Page Object Model (POM)**
- **Reusable Components + Fixtures**

---

# 🛠️ Installation Guide

Follow these steps to set up the framework on any machine.

---

## 1️⃣ **Clone the Repository**

```sh
git clone https://github.com/<your-repo>/Filters_Automation.git
cd Filters_Automation

## 2️⃣ Create Virtual Environment
python3 -m venv .venv
source .venv/bin/activate      # Mac / Linux
.\.venv\Scripts\activate       # Windows

## 3️⃣ Install Dependencies
pip install -r requirements.txt

## 4️⃣ Install Playwright Browsers
playwright install


Choose (Only required once)

## ▶️ Running Tests:

✅ Run all tests
pytest -s

🎯 Run single test file
pytest tests/test_filters.py -s

🧪 Run tests by keyword
pytest -k "filters" -s

🌐 Run in headed mode
pytest --headed -s

📊 Test Reports (HTML)

After each test run, Playwright/pytest generates an HTML report here:

reports/report.html


To open manually:

open reports/report.html
