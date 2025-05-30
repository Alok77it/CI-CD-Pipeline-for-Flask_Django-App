from app import app
from flask import render_template, request, redirect, url_for

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def login():
    username = request.form['username']
    password = request.form['password']
    if users.get(username) == password:
        return redirect(url_for('feedback'))
    return "Invalid Credentials", 401

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/submit-feedback', methods=["POST"])
def submit_feedback():
    feedback = request.form['feedback']
    return f"Feedback received: {feedback}"
