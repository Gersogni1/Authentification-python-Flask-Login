from . import db

class Cours(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(150))
    description = db.Column(db.Text)
    professeur_id = db.Column(db.Integer, db.ForeignKey('professeur.id'))

    def __repr__(self):
        return self.titre