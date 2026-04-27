# 🧪 Web Application Test Automation Framework

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?logo=selenium)
![Pytest](https://img.shields.io/badge/Tested%20with-Pytest-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📖 Overview

A professional-grade test automation framework built using **Python**, **Selenium WebDriver**, and **Pytest**. The framework follows the **Page Object Model (POM)** design pattern and automates login test scenarios on [SauceDemo](https://www.saucedemo.com/) — an industry-standard e-commerce simulation used for automation practice.

---

## ✅ Features

- Automated browser testing using Selenium WebDriver
- Page Object Model (POM) for clean, maintainable code
- Positive and negative login test cases
- Explicit waits for reliable test execution
- Auto HTML report generation via `pytest-html`
- Zero-config driver management via `WebDriver Manager`

---

## 🗂️ Project Structure

```
selenium_project/
├── pages/
│   ├── __init__.py
│   └── login_page.py       # Page Object for Login page
├── tests/
│   ├── __init__.py
│   └── test_login.py       # Test cases for login functionality
├── reports/                # Auto-generated HTML reports
├── conftest.py             # Pytest configuration & path setup
├── .gitignore
└── README.md
```

---

## 🧪 Test Cases

| Test ID | Test Name          | Type     | Expected Result                        |
|---------|--------------------|----------|----------------------------------------|
| TC-001  | test_login         | Positive | Redirects to `/inventory` page         |
| TC-002  | test_invalid_login | Negative | Displays "Epic sadface" error message  |

---

## 🛠️ Tech Stack

| Tool               | Purpose                    |
|--------------------|----------------------------|
| Python 3.x         | Core language              |
| Selenium WebDriver | Browser automation         |
| Pytest             | Test runner                |
| WebDriver Manager  | Auto ChromeDriver setup    |
| pytest-html        | HTML report generation     |
| Google Chrome      | Test browser               |

---

## ⚙️ Setup & Installation

**1. Clone the repository**

```bash
git clone https://github.com/nawadeakshay/selenium-test-automation.git
cd selenium-test-automation
```

**2. Create & activate virtual environment**

```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install selenium pytest pytest-html webdriver-manager
```

**4. Run the tests**

```bash
pytest -v --html=reports/report.html
```

**5. View the report**

Open `reports/report.html` in your browser.

---

## 🌐 Application Under Test

**SauceDemo** — https://www.saucedemo.com

> A purpose-built e-commerce simulation by Sauce Labs, widely used for Selenium automation practice.

---

## 📌 Future Enhancements

- [ ] Pytest fixtures for driver lifecycle management
- [ ] Data-driven testing with `@pytest.mark.parametrize`
- [ ] Cross-browser support (Firefox, Edge)
- [ ] CI/CD integration with GitHub Actions
- [ ] Allure Report integration with screenshots on failure

---

## 👨‍💻 Author

**Akshay Nawade**
GitHub: [@nawadeakshay](https://github.com/nawadeakshay)

---

## 📄 License

This project is licensed under the MIT License.
