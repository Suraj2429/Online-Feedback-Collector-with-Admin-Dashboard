from flask import Flask, render_template, request, redirect, url_for, Response, session
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret123"

# Database Connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create Table
def create_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS Feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            rating INTEGER,
            comments TEXT,
            date_submitted TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_table()

# Home Route
@app.route('/')
def home():
    success = request.args.get('success')
    return render_template('index.html', success=success)

# Submit Feedback
@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    rating = request.form['rating']
    comments = request.form['comments']
    date_submitted = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO Feedback (name, email, rating, comments, date_submitted) VALUES (?, ?, ?, ?, ?)",
        (name, email, rating, comments, date_submitted)
    )
    conn.commit()
    conn.close()

    return redirect(url_for('home', success=1))

# ✅ Admin Login
@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    error = request.args.get('error')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "admin123":
            session['admin'] = True
            return redirect(url_for('admin'))
        else:
            return redirect(url_for('admin_login', error=1))

    return render_template('login.html', error=error)

# ✅ Protected Admin Dashboard (FIXED)
@app.route('/admin-dashboard')
def admin():
    if not session.get('admin'):
        return redirect(url_for('admin_login'))

    conn = get_db_connection()
    feedbacks = conn.execute("SELECT * FROM Feedback").fetchall()

    total_feedback = len(feedbacks)

    if total_feedback > 0:
        avg_rating = sum([int(f["rating"]) for f in feedbacks]) / total_feedback
    else:
        avg_rating = 0

    conn.close()

    return render_template(
        'admin.html',
        feedbacks=feedbacks,
        total_feedback=total_feedback,
        avg_rating=round(avg_rating, 2)
    )

# Download CSV
@app.route('/download-csv')
def download_csv():
    conn = get_db_connection()
    feedbacks = conn.execute("SELECT * FROM Feedback").fetchall()
    conn.close()

    def generate():
        yield "id,name,email,rating,comments,date_submitted\n"
        for f in feedbacks:
            yield f"{f['id']},{f['name']},{f['email']},{f['rating']},{f['comments']},{f['date_submitted']}\n"

    return Response(
        generate(),
        mimetype='text/csv',
        headers={"Content-Disposition": "attachment; filename=feedback.csv"}
    )

# ✅ API
@app.route('/api/feedback')
def api_feedback():
    conn = get_db_connection()
    feedbacks = conn.execute("SELECT * FROM Feedback").fetchall()
    conn.close()

    data = [dict(row) for row in feedbacks]
    return {"feedback": data}

# ✅ Logout
@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)