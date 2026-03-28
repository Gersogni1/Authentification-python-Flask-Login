# 🔐 Système d'Authentification (Python) avec Flask

## 📌 Description

Ce projet implémente un système d'authentification sécurisé en Python
avec Flask.\
Il inclut l'inscription, la connexion, la gestion des sessions et la
protection des routes.

------------------------------------------------------------------------

## 🚀 Fonctionnalités

-   Inscription utilisateur
-   Connexion sécurisée
-   Hachage des mots de passe
-   Gestion des sessions avec Flask-Login
-   Protection des routes
-   Déconnexion

------------------------------------------------------------------------

## 🛠️ Technologies utilisées

-   Python 3.14.3
-   Flask
-   Flask-Login
-   Werkzeug
-   MysQl

------------------------------------------------------------------------


### 1. Structure du projet

``` bash
auth-system/
│
├── app.py
├── config.py
│
├── models/
│   ├── __init__.py
│   ├── users.py
│   ├── cours.py
│   ├── professeurs.py
│
├── routes/
│   ├── __init__.py
│   ├── cours_routes.py
│   ├── professeur_routes.py
│   ├── users_routes.py
│
├── templates/
│   ├── cours/
│   │  ├── create.html
│   │  ├── edit.html
│   │  ├── index.html
│   ├── professeurs/
│   │  ├── create.html
│   │  ├── edit.html
│   │  ├── index.html
│   ├── users/
│   │  ├── create.html
│   │  ├── edit.html
│   │  ├── index.html
│
└── venv/
```
------------------------------------------------------------------------

## ⚙️ Installation les packages

### 1. packages flask-login et werkzeug

``` bash
cd auth-system
pip install flask-login werkzeug
```

### 2. Dans ton model models/user.py

``` bash
from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))  # 🔐 mot de passe hashé

    def __repr__(self):
        return self.name
```

### 3. Configurer Flask-Login

-   📄 app.py

``` bash
from flask import Flask
from config import Config
from models import db, User
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = "secret123"  # 🔑 obligatoire

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"  # redirection si non connecté

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```


------------------------------------------------------------------------

### 4.Créer Blueprint Auth

-   📁 routes/auth_routes.py

``` bash
from flask import Blueprint, render_template, request, redirect, url_for
from models import db, User
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

# LOGIN
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
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
```

------------------------------------------------------------------------


### 6. Enregistrer le Blueprint

-   Dans app.py :

``` bash
from routes.auth_routes import auth_bp

app.register_blueprint(auth_bp)
```

------------------------------------------------------------------------

### 6. 🔐 Protéger les routes

## Dans tes fichiers : 📄 cours_routes.py

``` bash
from flask_login import login_required

@prof_bp.route('/')
@login_required
def index():
```
## Résultat : si non connecté → redirection vers /login
------------------------------------------------------------------------

### 7. Templates

## 📄 templates/auth/login.html


``` bash
{% extends 'base.html' %}

{% block content %}
<h2>Login</h2>
<form method="POST">
    <input type="email" class="form-control" name="email" placeholder="Email"><br>
    <input type="password" class="form-control" name="password" placeholder="Mot de passe"><br>
    <button type="submit" class="btn btn-primary btn-sm mt-3">Se connecter</button>
</form>
<a href="/register">Créer un compte</a>
{% endblock %}
```

------------------------------------------------------------------------

## templates/auth/register.html

``` bash
{% extends 'base.html' %}

{% block content %}
<h2>Register</h2>
<form method="POST">
    <input type="text" class="form-control" name="name" placeholder="Nom"><br>
    <input type="email"  class="form-control" name="email" placeholder="Email"><br>
    <input type="password" class="form-control" name="password" placeholder="Mot de passe"><br>
    <button type="submit" class="btn btn-primary btn-sm mt-3">S'inscrire</button>
</form>
{% endblock %}
```

------------------------------------------------------------------------

### 🚀 Résultat final
#  👉 Accès :

-   /login → connexion
-   /register → inscription
-   /logout → déconnexion

#  👉 Accès :

-   /cours ❌ sans login
-   /cours ✅ après login

------------------------------------------------------------------------

## 👤 Auteur

Gersogni BASHIYA
gersogniyampanya@gmail.com
