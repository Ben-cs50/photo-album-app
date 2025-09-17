#!/bin/python3
from flask import Flask, flash, redirect, render_template, request, url_for, session, jsonify
import requests
import json
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os, secrets


app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or secrets.token_hex(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

API_BASE = "https://jsonplaceholder.typicode.com"


def login_required(view_func):
    def wrapped(*args, **kwargs):
        if not session.get("user"):
            flash("Please log in to continue")
            return redirect(url_for("login"))
        return view_func(*args, **kwargs)
    wrapped.__name__ = view_func.__name__
    return wrapped


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}


with app.app_context():
    db.create_all()

@app.route("/")
def index():
     return render_template('landing.html')

@app.route("/home")
@login_required
def home():
     return render_template('index.html')

@app.route("/profile")
@login_required
def profile():
    user = session.get("user")
    # Pull user's albums for quick summary
    albums = []
    try:
        if user and user.get("id"):
            resp = requests.get(f"{API_BASE}/albums", params={"userId": user["id"]}, timeout=10)
            if resp.ok:
                albums = resp.json()
    except Exception:
        albums = []
    return render_template('profile.html', user=user, albums=albums)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        if not email:
            flash('Email is required!')
            return render_template('login.html')
        # First check local database
        db_user = User.query.filter_by(email=email).first()
        if db_user and check_password_hash(db_user.password_hash, password):
            session['user'] = {"id": db_user.id, "name": db_user.name, "email": db_user.email}
            return redirect(url_for('home'))
        # Fallback: JSONPlaceholder (no password validation)
        try:
            resp = requests.get(f"{API_BASE}/users", params={"email": email}, timeout=10)
            if resp.ok and isinstance(resp.json(), list) and len(resp.json()) > 0:
                user = resp.json()[0]
                session['user'] = {"id": user.get("id"), "name": user.get("name"), "email": user.get("email")}
                flash('Logged in via JSONPlaceholder demo user')
                return redirect(url_for('home'))
        except Exception:
            pass
        flash('Invalid credentials')
    return render_template('login.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        name = request.form.get('name', '').strip()
        password = request.form.get('password', '')
        if not email or not name or not password:
            flash('Name, email and password are required')
            return render_template('signup.html')
        existing = User.query.filter_by(email=email).first()
        if existing:
            flash('A user with that email already exists')
            return render_template('signup.html')
        # Create user in JSONPlaceholder (mock persistence)
        try:
            jp_payload = {"name": name, "email": email, "username": name.split(' ')[0] or name}
            requests.post(f"{API_BASE}/users", json=jp_payload, timeout=10)
        except Exception:
            pass
        # Persist locally for real login support
        user = User(name=name, email=email, password_hash=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully. Please log in.')
        return redirect(url_for('login'))
    return render_template('signup.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/forgot', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        if not email:
            flash('Please enter your email')
            return render_template('forgot.html')
        # Demo: pretend to send email and set a one-time token in session
        session['reset_email'] = email
        session['reset_token'] = 'demo-token'
        flash('Reset link sent. Use the form below to set a new password.')
        return redirect(url_for('reset_password', token='demo-token'))
    return render_template('forgot.html')


@app.route('/reset/<token>', methods=['GET', 'POST'])
def reset_password(token: str):
    if token != session.get('reset_token'):
        flash('Invalid or expired reset token')
        return redirect(url_for('forgot_password'))
    if request.method == 'POST':
        new_password = request.form.get('password', '')
        if not new_password:
            flash('Please enter a new password')
            return render_template('reset.html')
        # Demo: just clear token and pretend success
        session.pop('reset_token', None)
        flash('Password reset successful. Please log in.')
        return redirect(url_for('login'))
    return render_template('reset.html')


@app.route('/user/<int:user_id>')
@login_required
def user_page(user_id: int):
    user = None
    albums = []
    try:
        u = requests.get(f"{API_BASE}/users/{user_id}", timeout=10)
        if u.ok:
            user = u.json()
        a = requests.get(f"{API_BASE}/albums", params={"userId": user_id}, timeout=10)
        if a.ok:
            albums = a.json()
    except Exception:
        pass
    return render_template('user.html', user=user, albums=albums)

@app.route('/albums')
@login_required
def albums_page():
    return render_template('albums.html')


@app.route('/photos')
@login_required
def photos_page():
    return render_template('photos.html')



@app.route('/album/<int:album_id>')
@login_required
def album_page(album_id: int):
    album = None
    photos = []
    try:
        a = requests.get(f"{API_BASE}/albums/{album_id}", timeout=10)
        if a.ok:
            album = a.json()
        p = requests.get(f"{API_BASE}/photos", params={"albumId": album_id}, timeout=10)
        if p.ok:
            photos = p.json()
    except Exception:
        pass
    return render_template('album.html', album=album, photos=photos)


@app.route('/photo/<int:photo_id>')
@login_required
def photo_page(photo_id: int):
    photo = None
    try:
        r = requests.get(f"{API_BASE}/photos/{photo_id}", timeout=10)
        if r.ok:
            photo = r.json()
    except Exception:
        pass
    return render_template('photo.html', photo=photo)


# Simple Users API (local DB)
@app.route('/api/users', methods=['GET'])
def api_users_list():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])


@app.route('/api/users/<int:user_id>', methods=['GET'])
def api_users_get(user_id: int):
    u = User.query.get_or_404(user_id)
    return jsonify(u.to_dict())


@app.route('/api/users', methods=['POST'])
def api_users_create():
    data = request.get_json(silent=True) or {}
    name = (data.get('name') or '').strip()
    email = (data.get('email') or '').strip()
    password = data.get('password') or ''
    if not name or not email or not password:
        return jsonify({"error": "name, email, password are required"}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "email already exists"}), 409
    # Create on JSONPlaceholder (mock) and then persist locally
    try:
        jp_payload = {"name": name, "email": email, "username": name.split(' ')[0] or name}
        requests.post(f"{API_BASE}/users", json=jp_payload, timeout=10)
    except Exception:
        pass
    u = User(name=name, email=email, password_hash=generate_password_hash(password))
    db.session.add(u)
    db.session.commit()
    return jsonify(u.to_dict()), 201


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
