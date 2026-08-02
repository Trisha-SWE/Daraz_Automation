# 🛒 Daraz Automation Testing Framework

A Selenium Automation Testing project for Daraz Bangladesh developed using **Python**, **Pytest**, and the **Page Object Model (POM)** design pattern.

---

## 📌 Project Overview

This project automates the basic search functionality of Daraz Bangladesh.

Current automated flow:

- Open Daraz website
- Search for a product
- Click the Search button
- Open the first product
- Verify the product title
- Capture screenshot
- Generate execution logs

---

## 🛠️ Technologies Used

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Git & GitHub

---

## 📁 Project Structure

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
│   └── home_page.py
│
├── screenshots/
│
├── testcases/
│   └── test_search.py
│
├── utilities/
│   ├── logger.py
│   └── read_properties.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/Trisha-SWE/Daraz_Automation.git
```

Go to the project folder:

```bash
cd Daraz_Automation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the test:

```bash
pytest -v -s
```

---

## ✅ Current Features

- Open Browser
- Open Daraz Website
- Search Product
- Click Search Button
- Click First Product
- Verify Product Title
- Screenshot Capture
- Logging Support
- Configuration File Support
- BasePage Implementation
- Page Object Model (POM)

---

## 🚀 Future Improvements

- Verify Product Price
- Verify Product Image
- HTML Report
- Data Driven Testing (Excel)
- Login Test
- Add to Cart Test
- GitHub Actions (CI/CD)

---

## 👩‍💻 Author

**Rukaiya Akter Trisha**

Software Engineering Student

Daffodil International University