#!/bin/python3
from flask import Flask, flash, redirect, render_template, request, url_for
import requests
import json


app = Flask(__name__)

@app.route("/")
def index():
     return render_template('login.html')

@app.route("/home")
def home():
     return render_template('index.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        if not email:
            flash('Email is required!')
        else:
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')



 
app.run(host="0.0.0.0", port=80)
