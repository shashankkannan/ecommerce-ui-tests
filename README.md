# 🧪 E-Commerce UI Automation with Selenium, Pytest & Jenkins

A complete end-to-end test automation framework for a sample e-commerce application, featuring:

- ✅ **Selenium + Pytest** for UI automation
- ✅ **Jenkins CI** integration with HTML test reports
- ✅ **Headless Chrome** execution using WebDriver Manager
- ✅ **Dockerized Jenkins** setup for consistent, container-based testing

---

## 🔧 What I Built

- ✅ A full **Selenium + Pytest automation suite** for testing login, cart, and checkout flows
- ✅ A **Jenkins CI pipeline** that runs tests and generates clean, shareable HTML reports
- ✅ Configured **headless Chrome** via `webdriver-manager` for seamless execution
- ✅ Resolved Chrome/Chromedriver dependency issues inside **Dockerized Jenkins**
- ✅ Verified consistent and reliable test execution across both **local** and **CI** environments

---

## 📁 Project Structure

```

ecommerce-ui-tests/
│
├── tests/                         # Pytest test cases
│   ├── test\_login.py
│   ├── test\_add\_to\_cart.py
│   └── test\_checkout.py
│
├── conftest.py                    # Pytest fixture: browser setup
├── requirements.txt               # Python dependencies
├── pytest.ini                     # Pytest config
├── report.html                    # Generated HTML report (CI output)
└── Jenkinsfile (optional)         # Jenkins pipeline config

````

---

## 🚀 Getting Started

### ✅ 1. Setup Locally

```bash
git clone https://github.com/shashankkannan/ecommerce-ui-tests.git
cd ecommerce-ui-tests
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
pytest --html=report.html
````

### ✅ 2. Run via Jenkins CI

* Configure a **Jenkins job** (freestyle or pipeline)
* Add the following to the Jenkins Shell build step:

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
pytest --html=report.html
```

* Publish the `report.html` via **HTML Publisher Plugin**

---

## 🛠️ Technologies Used

* Python 3.11
* Selenium
* Pytest
* WebDriver Manager
* Jenkins
* Headless Chrome
* HTML Test Reports
* Docker (for Jenkins CI)

---

## 🧩 Sample Test Flow

* Visit [https://www.saucedemo.com](https://www.saucedemo.com)
* Log in with test credentials
* Add a product to the cart
* Proceed to checkout
* Assert product presence in cart

---

## 🗂️ Reports

Test results are output as an HTML file (`report.html`) after every run.

---
