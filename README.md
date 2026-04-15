# 🚀 Online Feedback Collector with Admin Dashboard

## 📌 Project Overview
The **Online Feedback Collector** is a full-stack web application that allows users to submit feedback and enables administrators to view, analyze, and manage feedback data through an interactive dashboard.

This project demonstrates real-world web development skills including frontend design, backend processing, database integration, and data visualization.

---

## 🎯 Features

### 👤 User Side
- Submit feedback with:
  - Name
  - Email
  - Rating (⭐ 1–5 star system)
  - Comments
- Responsive and modern UI
- Success popup notification after submission

### 🛠️ Admin Dashboard
- View all feedback in a structured table
- Total feedback count
- Average rating calculation
- Visual analytics using charts (Chart.js)
- Download feedback data as CSV

---

## 🧰 Tech Stack

### Frontend
- HTML5
- CSS3 (Custom + Responsive Design)
- Bootstrap
- JavaScript

### Backend
- Python
- Flask

### Database
- SQLite

### Visualization
- Chart.js

---

## 📂 Project Structure
OnlineFeedbackCollector/
│
├── app.py # Flask backend
├── database.db # SQLite database
├── requirements.txt # Python dependencies
│
├── static/
│ ├── css/
│ │ └── style.css # Styling
│ ├── js/
│ │ └── script.js # JS logic
│ └── images/
│ └── feedback.jpg # UI image
│
├── templates/
│ ├── index.html # User form
│ ├── admin.html # Dashboard
│ └── layout.html # Base template
│
└── README.md # Documentation


---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone <your-repo-link>
cd OnlineFeedbackCollector


### 2️⃣ Create Virtual Environment
``` bash 
python -m venv venv
venv\Scripts\activate


### 3️⃣ Install Dependencies
``` bash 
pip install -r requirements.txt


### 4️⃣ Run Application
``` bash 
python app.py


### 5️⃣ Open in Browser
``` bash 
http://127.0.0.1:5000/
