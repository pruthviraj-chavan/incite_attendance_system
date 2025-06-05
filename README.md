
# 🎓 Incite Attendance System

> A simple Django-based attendance and fee management system for students and admins.

This project is a **student attendance and fee tracking system** built using **Django**, with support for student registration, login, profile editing, attendance requests, and admin dashboard features. It also includes additional pages like **Courses**, **AI Tools**, and **Downloadable Resources**.

---

## 🧾 Features

- ✅ Student Registration & Login
- ✅ Profile Management
- ✅ Request Daily Attendance (once per day)
- ✅ View Attendance and Fee Status
- 👩‍💼 Admin Dashboard to:
  - Approve/Reject Attendance
  - Update Fee Status (Paid / Partial / Pending)
  - View Analytics
- 📘 Additional Pages:
  - Courses
  - AI Tools
  - Downloadable Resources (PDFs)

---

## 🛠 Tech Stack

- **Python** – Backend logic
- **Django** – Web framework
- **SQLite** – Default database
- **HTML/CSS** – Frontend templates
- **CSRF Protection** – Security for forms

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/pruthviraj-chavan/incite_attendance_system.git
cd incite_attendance_system
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

#### Activate virtual environment:

- **Windows**
  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

Make sure you have a `requirements.txt` file. If not, create one:

```bash
pip install django
pip freeze > requirements.txt
```

Then install:

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. (Optional) Create Superuser

To access the admin dashboard:

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Open in browser:  
👉 http://localhost:8000

---

## 🧪 Usage

| User Type | How to Use |
|-----------|------------|
| **Students** | Register → Log in → Access Dashboard → Request Attendance → View Fee Status |
| **Admins** | Log in as superuser → Go to `/admin` or `/admin_dashboard` → Manage attendance and fees |

---

## 📁 Folder Structure

```
attendance_project/
├── manage.py
├── attendance_project/        # Project settings and URLs
└── student_app/               # App containing all logic
    ├── templates/             # HTML files
    ├── models.py              # Database schema
    ├── views.py               # Business logic
    ├── urls.py                # Page routes
    └── forms.py               # Form handling
```

---

## 📄 Templates Included

- `home.html` – Landing page
- `register.html` – Student registration
- `login.html` – User login
- `dashboard.html` – Student dashboard
- `profile.html` – Edit student info
- `admin_dashboard.html` – Admin actions
- `update_fee.html` – Admin edit fee status
- `courses.html`, `ai_tools.html`, `resources.html` – Extra student pages

---

## 🚀 Future Improvements

- Add Bootstrap or Tailwind CSS for better UI
- Allow file upload for resources via Admin
- Add search/filter in admin dashboard
- Export reports to CSV/PDF
- Integrate chart.js for analytics graphs

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo, make improvements, and submit pull requests.

---

## 📬 Contact

If you have questions or want to collaborate, reach out to Pruthviraj Chavan on GitHub or via email.

---

## 📌 License

MIT License – see `LICENSE` for details.

