from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.orm import joinedload
from models import db, Cours, Professeur
from flask_login import login_required

cours_bp = Blueprint('cours', __name__, url_prefix='/cours')

# LIST
@cours_bp.route('/list')
@login_required
def index():
    # cours = Cours.query.all()
    cours = Cours.query.options(joinedload(Cours.professeur)).all()
    return render_template('cours/index.html', cours=cours)

# CREATE
@cours_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    profs = Professeur.query.all()

    if request.method == 'POST':
        titre = request.form['titre']
        description = request.form['description']
        professeur_id = request.form['professeur_id']

        cours = Cours(
            titre=titre,
            description=description,
            professeur_id=professeur_id
        )

        db.session.add(cours)
        db.session.commit()

        return redirect(url_for('cours.index'))

    return render_template('cours/create.html', profs=profs)

# UPDATE
@cours_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    cour = Cours.query.get_or_404(id)
    profs = Professeur.query.all()

    if request.method == 'POST':
        cour.titre = request.form['titre']
        cour.description = request.form['description']
        cour.professeur_id = request.form['professeur_id']

        db.session.commit()
        return redirect(url_for('cours.index'))

    return render_template('cours/edit.html', cour=cour, profs=profs)

# DELETE
@cours_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    cours = Cours.query.get_or_404(id)

    db.session.delete(cours)
    db.session.commit()

    return redirect(url_for('cours.index'))