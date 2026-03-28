from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, User
from flask_login import LoginManager
from routes.auth_routes import auth_bp

from routes.users_routes import users_bp
from routes.cours_routes import cours_bp
from routes.professeur_routes import prof_bp

print("Application en cours de démarrage...")

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

# enregistrer les routes
app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)
app.register_blueprint(cours_bp)
app.register_blueprint(prof_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)