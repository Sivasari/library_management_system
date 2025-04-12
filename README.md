# 📚 Library Management System

A Django-based Library Management System designed to manage books, track issues/returns, and handle user/admin functionalities.

## 🚀 Features
- Add, edit, and delete books
- Issue and return book tracking
- User and Admin roles
- Search and filter books
- Django admin dashboard

## 🛠️ Tech Stack
- Python
- Django
- SQLite (default DB, can be replaced)
- HTML/CSS (for templates)

---

## ⚙️ Setup Instructions

Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/Sivasari/library_management_system.git
cd library_management_system
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser
```bash
python manage.py createsuperuser
```

Follow the prompts to set username, email, and password.

### 7. Run the Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 🧪 Admin Panel

You can access the admin panel at:
```
http://127.0.0.1:8000/admin/
```
Use the credentials you created with `createsuperuser`.

---

## 📄 License

This project is licensed under the MIT License.

---

## 💡 Future Improvements
- Add pagination for large book lists
- Add user authentication for book issuing
- Export book lists as CSV/PDF
