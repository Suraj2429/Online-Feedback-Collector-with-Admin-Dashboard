# 🚀 Online Feedback Collector with Admin Dashboard

## 📌 Project Overview
The **Online Feedback Collector** is a full-stack web application that allows users to submit feedback and enables administrators to view, analyze, and manage feedback data through an interactive dashboard.

This project demonstrates real-world web development skills including frontend design, backend logic, database integration, authentication, and data visualization.

---

## 🎯 Features

### 👤 User Side
- Submit feedback with:
  - Name
  - Email
  - Rating (⭐ 1–5 star system)
  - Comments
- Clean and responsive UI
- Custom validation popup for rating
- Success notification after submission

---

### 🛠️ Admin Dashboard
- Secure admin login system 🔐
- View all feedback in a structured table
- Total feedback count
- Average rating calculation
- Top rating display
- Visual analytics using **Chart.js**
- Download feedback as CSV
- Delete all feedback with confirmation popup
- Logout functionality

---

## 🧰 Tech Stack

### 🎨 Frontend
- HTML5
- CSS3 (Custom + Responsive Design)
- Bootstrap 5
- JavaScript

### ⚙️ Backend
- Python
- Flask

### 🗄️ Database
- SQLite

### 📊 Visualization
- Chart.js

---

## 📂 Project Structure
OnlineFeedbackCollector/
│
├── app.py # Flask backend
├── database.db # SQLite database
├── requirements.txt # Dependencies
│
├── static/
│ ├── css/
│ │ └── style.css # Styling
│ ├── js/
│ │ └── script.js # JS logic
│ └── images/
│ └── feedback.jpg # UI images
│
├── templates/
│ ├── index.html # User feedback form
│ ├── admin.html # Admin dashboard
│ ├── login.html # Admin login
│ └── layout.html # Base template
│
└── README.md # Documentation


---


---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/OnlineFeedbackCollector.git
cd OnlineFeedbackCollector
```

### 2️⃣ Create Virtual Environment
``` bash
python -m venv venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate   # Mac/Linux
```

### 3️⃣ Install Dependencies
``` bash
pip install -r requirements.txt
```

### 4️⃣ Run Application
``` bash
python app.py
```

### 5️⃣ Open in Browser
``` bash
http://127.0.0.1:5000/
```

---

### 🔐 Admin Login Credentials
Username: admin
Password: admin123
