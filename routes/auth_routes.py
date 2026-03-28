from flask import Blueprint, render_template, request, redirect, url_for
from models import db, User
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

# LOGIN
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # 🔥 SI DEJA CONNECTÉ
    if current_user.is_authenticated:
        return redirect(url_for('cours.index'))
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('cours.index'))

    return render_template('auth/login.html')

# REGISTER
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')

# LOGOUT
@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))