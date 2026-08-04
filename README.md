# 🛒 Daraz Automation Testing Framework

A Selenium-based Test Automation Framework for Daraz Bangladesh built using **Python**, **Pytest**, and the **Page Object Model (POM)** design pattern.

---

## 🚀 Technologies Used

- Python 3
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- HTML Reports
- Logging
- ChromeDriver

---

## 📂 Project Structure

```
Daraz_Automation/
│
├── config/
│   └── config.ini
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
│   ├── test_login.py
│   ├── test_search.py
│   ├── test_product_price.py
│   └── test_cart.py
│
├── utilities/
│   ├── logger.py
│   ├── read_properties.py
│   └── excel_utils.py
│
├── pytest.ini
├── conftest.py
└── README.md
```

---

# ✅ Automated Test Scenarios

### 🔹 Login Test

- Open Daraz
- Click Login
- Enter Email & Password
- Click Login Button
- Capture Screenshot

---

### 🔹 Search Product Test

- Search Product
- Open First Product
- Capture Product Title
- Capture Product Price
- Capture Product URL

---

### 🔹 Product Price Test

- Search Product
- Open Product
- Verify Product Price
- Capture Screenshot

---

### 🔹 Add To Cart Test

- Search Product
- Open Product
- Add Product to Cart
- Capture Screenshot

---

# 📸 Screenshots

Screenshots are automatically saved inside:

```
screenshots/
```

Example:

```
login_result.png
search_result.png
product.png
product_price.png
cart.png
```

---

# 📊 HTML Report

Generate Report

```bash
pytest --html=reports/report.html
```

Open

```
reports/report.html
```

---

# ▶️ Run Tests

Run All Tests

```bash
pytest -v
```

Run Login Test

```bash
pytest testcases/test_login.py -v
```

Run Search Test

```bash
pytest testcases/test_search.py -v
```

Run Product Price Test

```bash
pytest testcases/test_product_price.py -v
```

Run Cart Test

```bash
pytest testcases/test_cart.py -v
```

---

# 📋 Current Features

- ✅ Page Object Model (POM)
- ✅ Selenium WebDriver
- ✅ Pytest Framework
- ✅ HTML Report
- ✅ Logging
- ✅ Screenshot Capture
- ✅ Product Search
- ✅ Product Price Verification
- ✅ Login Automation
- ✅ Add to Cart Automation

---

# 📈 Test Result

```
==========================
4 Tests Passed
==========================

✔ Login Test
✔ Search Test
✔ Product Price Test
✔ Add To Cart Test
```

---

# 🔮 Future Improvements

- Data Driven Testing (Excel)
- Cross Browser Testing
- Headless Execution
- GitHub Actions CI/CD
- Docker Support
- Allure Report

---

# 👩‍💻 Author

**Rukaiya Akter Trisha**

Software Engineering Student

Daffodil International University

Major: Software Quality Assurance & Testing (SQAT)

GitHub:
https://github.com/Trisha-SWE

---

⭐ If you found this project useful, don't forget to Star this repository.