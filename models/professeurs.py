from . import db

class Professeur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    cours = db.relationship('Cours', backref='professeur', lazy=True)
    specialite = db.Column(db.String(100))
    
    def __repr__(self):
        return self.nom