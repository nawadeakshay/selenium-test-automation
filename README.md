<div align="center">

# 🧪 Web Automation Testing Project

### Selenium-Powered Automated Testing with Pytest & Page Object Model

*Automatically test web application flows — login, validation, edge cases — with clean reports.*

---

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-orange?style=for-the-badge&logo=pytest&logoColor=white)
![POM](https://img.shields.io/badge/Design-Page%20Object%20Model-blueviolet?style=for-the-badge)
![HTML Report](https://img.shields.io/badge/Report-HTML-red?style=for-the-badge&logo=html5&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-Academic-lightgrey?style=for-the-badge)

</div>

---

## 📌 Overview

**Web Automation Testing Project** is a Python-based test automation suite that uses **Selenium WebDriver** and **Pytest** to automatically test web application functionality — including login flows, positive/negative test cases, and generates detailed HTML reports.

👉 In simple words:

Instead of manually clicking through a website to check if it works, this framework does it automatically — fast, repeatable, and reliable.

> 🌐 **Website Under Test:** [saucedemo.com](https://www.saucedemo.com/)

---

## 🧾 Real-World Example

| Test Case | Action | Expected Result | Status |
|-----------|--------|-----------------|--------|
| Valid login | Enter correct credentials | Redirects to dashboard | ✅ Pass |
| Invalid password | Enter wrong password | Shows error message | ✅ Pass |
| Empty username | Submit blank form | Shows validation error | ✅ Pass |
| Locked-out user | Login with locked account | Shows locked error | ✅ Pass |

---

## 🎯 Features

- 🔐 Automated login functionality (positive & negative cases)
- 🐞 Edge case & validation testing
- 🏗️ Page Object Model (POM) design pattern for clean, reusable code
- 📊 HTML test report generation
- ⚙️ Easy setup with WebDriver Manager (no manual driver downloads)
- 🔁 Scalable structure — add new pages and tests effortlessly
- 🧩 `conftest.py` for shared fixtures and path configuration

---

## 🧠 How It Works

### 🔄 Test Execution Pipeline

```text
Test Triggered (pytest)
        ↓
conftest.py loads fixtures & sys.path
        ↓
WebDriver Manager launches Browser
        ↓
Page Object (POM) interacts with UI
        ↓
Assertions validate outcomes
        ↓
HTML Report generated
```

---

## 🏗️ Architecture

### 📦 System Components

```
web_automation_testing/
│
├── conftest.py           → Pytest config, fixtures & sys.path setup
├── .gitignore            → Excludes venv, cache, reports, .pyc files
│
├── pages/                → Page Object Model classes
│   └── login_page.py     → Login page locators & actions
│
├── tests/                → Test cases
│   └── test_login.py     → Login positive & negative test cases
│
├── reports/              → Auto-generated HTML test reports (git-ignored)
│
├── requirements.txt      → Project dependencies
└── README.md
```

---

### 🔧 Module Explanation

#### 1. conftest.py

- Appends project root to `sys.path` for clean imports
- Houses shared Pytest fixtures (browser setup/teardown)
- Auto-discovered by Pytest on every run

#### 2. Pages (POM Layer)

- Each web page has its own Python class
- Locators and actions are kept together
- Tests never interact with the DOM directly — only via page classes

#### 3. Tests Layer

- Contains all test functions using `def test_*` naming
- Uses fixtures from `conftest.py` for browser instance
- Positive and negative scenarios clearly separated

#### 4. Reports

- HTML report auto-generated at `reports/report.html`
- Excluded from Git via `.gitignore` (generated on every run)

---

## 🛠️ Tech Stack

| Component        | Technology          | Why Used                          |
|------------------|---------------------|-----------------------------------|
| Language         | Python              | Core development                  |
| Browser Control  | Selenium WebDriver  | UI interaction & automation       |
| Test Framework   | Pytest              | Test discovery, fixtures, running  |
| Driver Setup     | WebDriver Manager   | Auto-manages ChromeDriver         |
| Design Pattern   | Page Object Model   | Clean, maintainable test structure|
| Reporting        | pytest-html         | HTML test reports                 |

---

## 📂 Project Structure

```bash
web_automation_testing/
│
├── conftest.py
├── .gitignore
│
├── pages/
│   └── login_page.py
│
├── tests/
│   └── test_login.py
│
├── reports/              # git-ignored, generated on run
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/nawadeakshay/selenium-test-automation
cd web_automation_testing

# Create virtual environment
python -m venv .venv

# Activate environment
source .venv/bin/activate      # Mac/Linux
# OR
.venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

### 🔹 Run All Tests

```bash
pytest -v
```

### 🔹 Run Tests with HTML Report

```bash
pytest -v --html=reports/report.html
```

📊 Report saved at:

```
reports/report.html
```

### 🔹 Run a Specific Test File

```bash
pytest tests/test_login.py -v
```

---

### 📊 Sample Report Output

| Test | Duration | Result |
|------|----------|--------|
| test_valid_login | 2.3s | ✅ PASSED |
| test_invalid_password | 1.8s | ✅ PASSED |
| test_empty_fields | 1.5s | ✅ PASSED |

> Open `reports/report.html` in any browser to view the full interactive report.

---

## 💡 Example

```
Test: test_valid_login

Steps:
  1. Open https://www.saucedemo.com/
  2. Enter username: standard_user
  3. Enter password: secret_sauce
  4. Click Login

Expected: Redirected to /inventory.html
Result: ✅ PASSED
```

---

## 🌍 Real-World Applications

- 🛒 E-commerce checkout flow testing
- 🔐 Authentication & session management testing
- 📱 SaaS product regression testing
- 🏢 CI/CD pipeline integration for automated QA

---

## ✅ Advantages

- ⚡ Faster than manual testing — runs in seconds
- 🔁 Fully repeatable and consistent
- 🧹 POM keeps code clean and easy to maintain
- 📊 HTML reports ready for sharing with team/client

---

## ⚠️ Limitations

- Chrome browser required (WebDriver Manager handles version)
- Tests depend on live website availability
- No parallel test execution (yet)

---

## 🔮 Future Improvements

- Parallel test execution with `pytest-xdist`
- Cross-browser testing (Firefox, Edge)
- CI/CD integration (GitHub Actions)
- Data-driven testing with external CSV/Excel input
- Screenshot capture on test failure

---

## 📁 .gitignore Highlights

The following are excluded from version control:

```
.venv/          → Virtual environment
__pycache__/    → Python bytecode cache
*.pyc           → Compiled Python files
reports/        → Auto-generated HTML reports
.pytest_cache/  → Pytest internal cache
*.docx          → Word documents
```

---

## 👨‍💻 Author

**Akshay Nawade**  
Python | Selenium | Test Automation |

[![GitHub](https://img.shields.io/badge/GitHub-nawadeakshay-181717?style=for-the-badge&logo=github)](https://github.com/nawadeakshay)

---

## ⭐ Support

If you like this project:

- ⭐ Star this repository
- 🔁 Share with others

---

## 📜 License

This project is for academic and learning purposes.
