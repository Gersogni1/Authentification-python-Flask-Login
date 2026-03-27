# 🔐 Système d'Authentification avec Flask

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

## ⚙️ Sur votre projet installé le package flask login et werkzeug

### 1. flask login et werkzeug

``` bash
pip install flask-login werkzeug
```

### 2. Créer un environnement virtuel

``` bash
python -m venv venv
```

### 3. Activer l'environnement virtuel

-   Linux / Mac :

``` bash
source venv/bin/activate
```

-   Windows :

``` bash
venv\Scripts\activate
```

------------------------------------------------------------------------

### 4. Installer les dépendances

``` bash
pip install flask
pip install flask-login
pip install werkzeug
pip install sqlalchemy
```

Ou utiliser :

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

### 5. Structure du projet

    auth-system/
    │── app.py
    │── models.py
    │── auth.py
    │── database.db
    │── templates/
    │── static/
    │── requirements.txt
    │── README.md

------------------------------------------------------------------------

### 6. Lancer l'application

``` bash
python app.py
```

Puis ouvrir dans le navigateur :

    http://127.0.0.1:5000

------------------------------------------------------------------------

## 🔐 Sécurité

-   Hachage des mots de passe avec Werkzeug
-   Protection des routes avec Flask-Login
-   Sessions sécurisées
-   Validation des entrées utilisateur

------------------------------------------------------------------------

## 🧪 Tests

``` bash
pytest
```

------------------------------------------------------------------------

## 🤝 Contribution

1.  Fork le projet\
2.  Créer une branche\

``` bash
git checkout -b feature/auth
```

3.  Commit\

``` bash
git commit -m "Ajout auth"
```

4.  Push\

``` bash
git push origin feature/auth
```

5.  Pull Request

------------------------------------------------------------------------

## 📄 Licence

Licence MIT

------------------------------------------------------------------------

## 👤 Auteur

Gersogni BASHIYA
gersogniyampanya@gmail.com
