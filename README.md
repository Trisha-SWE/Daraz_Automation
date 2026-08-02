# Daraz Automation Framework

A Selenium Automation Framework developed using Python, Pytest, and Page Object Model (POM) to automate core functionalities of the Daraz e-commerce website.

---

# Project Objective

The purpose of this project is to automate Daraz website functionalities by following industry-standard automation practices.

The framework demonstrates:

- Selenium WebDriver
- Python
- Pytest
- Page Object Model (POM)
- BasePage Design Pattern
- Explicit Wait
- Logging
- Screenshot Capture
- HTML Report
- Config Driven Framework

---

# Technologies Used

- Python 3
- Selenium
- Pytest
- WebDriver Manager
- OpenPyXL
- HTML Report

---

# Project Structure

```
Daraz_Automation/
│
├── config/
│   └── config.ini
│
├── logs/
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   └── cart_page.py
│
├── reports/
│   └── report.html
│
├── screenshots/
│
├── testcases/
│   ├── test_search.py
│   ├── test_login.py
│   └── test_cart.py
│
├── utilities/
│   ├── logger.py
│   ├── read_properties.py
│   └── excel_utils.py
│
├── conftest.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Features

- Login Automation
- Product Search
- Add To Cart
- Product Title Verification
- Product Price Capture
- Screenshot Capture
- Logging
- HTML Report
- Page Object Model

---

# Installation

Clone the repository

```bash
git clone https://github.com/Trisha-SWE/Daraz_Automation.git
```

Go to project directory

```bash
cd Daraz_Automation
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate

PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Run All Tests

```bash
pytest -v
```

---

# Run Individual Tests

Search Test

```bash
pytest testcases/test_search.py -v
```

Login Test

```bash
pytest testcases/test_login.py -v
```

Cart Test

```bash
pytest testcases/test_cart.py -v
```

---

# Generate HTML Report

```bash
pytest -v --html=reports/report.html --self-contained-html
```

Open

```
reports/report.html
```

in your browser.

---

# Automation Flow

```
Launch Browser
        ↓
Open Daraz
        ↓
Search Product
        ↓
Open Product
        ↓
Capture Product Title & Price
        ↓
Login
        ↓
Add To Cart
        ↓
Take Screenshot
        ↓
Generate HTML Report
        ↓
Close Browser
```

---

# Why Page Object Model?

Every webpage has its own class.

Benefits:

- Reusable code
- Easy maintenance
- Better scalability
- Clean framework

---

# Why BasePage?

BasePage stores reusable Selenium methods such as:

- click()
- type()
- get_title()
- get_current_url()
- take_screenshot()

This reduces duplicate code.

---

# Why Logging?

Logging records every important step.

Example

```
Opening Daraz Website

Searching Product

Opening Product

Clicking Add To Cart

Screenshot Taken

Test Passed
```

---

# Screenshots

Screenshots are automatically saved inside

```
screenshots/
```

---

# Test Coverage

✓ Search Product

✓ Login

✓ Add To Cart

✓ Product Title

✓ Product Price

✓ Screenshot Capture

✓ HTML Report

---

# Best Practices

- Page Object Model (POM)
- BasePage
- Explicit Wait
- Config Driven Framework
- Logging
- HTML Report
- Modular Design
- Clean Folder Structure

---

# Future Improvements

- Data Driven Testing
- Excel Integration
- Cross Browser Testing
- Parallel Execution
- Jenkins CI/CD
- GitHub Actions
- Docker Support

---

# Author

**Rukaiya Akter Trisha**

B.Sc. in Software Engineering

Daffodil International University