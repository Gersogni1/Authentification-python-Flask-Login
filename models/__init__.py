from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .users import User
from .cours import Cours
from .professeurs import Professeur