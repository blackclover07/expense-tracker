# 💰 Expense Tracker — V1

A simple **Django-based Expense Tracker** that allows users to create an account, log in, and manage their income and expenses.

This is **Version 1** of the project, focused on building the core authentication and transaction-management functionality.

---

## 🚀 Features

### 🔐 Authentication

* User registration
* User login
* User logout
* Authentication-protected transaction pages
* User-specific transactions

### 💸 Transaction Management

* Add income transactions
* Add expense transactions
* Transaction categories
* Transaction descriptions
* Transaction dates
* Transaction amounts
* Automatically associate transactions with the logged-in user

### 📊 Dashboard

The transaction dashboard displays:

* Total income
* Total expenses
* Current balance
* Recent transactions
* Transaction type indicators

### 🎨 UI

* Built with **Bootstrap 5**
* Responsive navigation bar
* Hero section
* Bootstrap carousel
* Login and registration pages
* Transaction dashboard
* Hover effects and cards
* Django message alerts

---

## 🛠️ Tech Stack

| Technology       | Purpose               |
| ---------------- | --------------------- |
| Python           | Programming language  |
| Django           | Backend web framework |
| SQLite           | Database              |
| Django Templates | Frontend templating   |
| Bootstrap 5      | UI and styling        |
| HTML             | Page structure        |
| CSS              | Custom styling        |

---

## 📂 Project Structure

```text
expense-tracker/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── home/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   └── urls.py
│
├── transactions/
│   ├── templates/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
│
├── users/
│   ├── templates/
│   ├── forms.py
│   ├── views.py
│   └── urls.py
│
├── templates/
│   └── base.html
│
├── manage.py
├── db.sqlite3
└── README.md
```

> The exact structure may vary depending on your Django app organization.

---

## 🗄️ Transaction Model

Each transaction contains:

* User
* Amount
* Category
* Transaction type
* Description
* Date
* Creation timestamp

The transaction type currently supports:

```text
INCOME
EXPENSE
```

Transactions are connected to Django's built-in `User` model using a foreign key.

This means every user can have their own separate collection of transactions.

---

## 📊 Transaction Calculations

The dashboard calculates:

```text
Total Income
      ↓
Total Expenses
      ↓
Balance = Income - Expenses
```

For example:

```text
Income     = ₹25,000
Expenses   = ₹12,500
--------------------
Balance    = ₹12,500
```

The calculations are performed using Django's ORM aggregation functionality.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Enter the project directory

```bash
cd expense-tracker
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install django
```

If the project contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

---

## 🔑 Authentication Flow

The basic user flow is:

```text
Register
   ↓
Login
   ↓
Transactions Dashboard
   ↓
Add Transaction
   ↓
Transaction saved for current user
   ↓
Dashboard updated
```

Users can only see the transactions associated with their own account.

---

## 📸 Screenshots

Add screenshots of your project here.

Example:

```markdown
![Home Page](./screenshots/home.png)

![Login Page](./screenshots/login.png)

![Register Page](./screenshots/register.png)

![Transactions Dashboard](./screenshots/transactions.png)

![Add Transaction](./screenshots/add-transaction.png)
```

---

## 🧠 What I Learned

While building Version 1, I worked with:

* Django project and app structure
* Django URL routing
* Django templates
* Template inheritance
* Static files
* Django authentication
* Login and logout
* Django messages framework
* Django forms
* ModelForms
* Django ORM
* ForeignKey relationships
* QuerySets
* `filter()`
* `aggregate()`
* `Sum()`
* Authentication decorators
* Bootstrap integration
* Responsive layouts
* Bootstrap components

---

## 🔮 Future Improvements — V2

Possible improvements for the next version:

* [ ] Edit transactions
* [ ] Delete transactions
* [ ] Search transactions
* [ ] Filter by category
* [ ] Filter by transaction type
* [ ] Filter by date
* [ ] Pagination
* [ ] Monthly expense reports
* [ ] Expense charts
* [ ] Category-wise spending analysis
* [ ] Better dashboard
* [ ] User profile
* [ ] Password reset
* [ ] Improved form validation
* [ ] REST API
* [ ] React/Next.js frontend
* [ ] PostgreSQL database
* [ ] Deployment

---

## 📌 Version

**Current Version:** `v1.0.0`

Version 1 focuses on the fundamental functionality of the application:

> **Authentication + Transaction Management + Basic Dashboard**

---

## 👨‍💻 Author

**Sagar Dey**

Built as a learning project to practice **Django, Python, databases, authentication, ORM, and Bootstrap**.

---

## ⭐ Future Goal

The long-term goal is to turn this simple tracker into a more complete personal-finance application with analytics, charts, budgeting tools, and a modern frontend.

---
