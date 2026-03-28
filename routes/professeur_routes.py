from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Cours, Professeur, User
from flask_login import login_required

prof_bp = Blueprint('professeurs', __name__, url_prefix='/professeurs')

# LIST
@prof_bp.route('/list')
@login_required
def index():
    profs = Professeur.query.all()
    return render_template('professeurs/index.html', profs=profs)

# CREATE
@prof_bp.route('/create', methods=['GET', 'POST'])
# proteger la route par l'authentification
@login_required
def create():
    if request.method == 'POST':
        nom = request.form['nom']
        specialite = request.form['specialite']

        prof = Professeur(nom=nom, specialite=specialite)

        db.session.add(prof)
        db.session.commit()

        return redirect(url_for('professeurs.index'))

    return render_template('professeurs/create.html')

# UPDATE
@prof_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    prof = Professeur.query.get_or_404(id)

    if request.method == 'POST':
        prof.nom = request.form['nom']
        prof.specialite = request.form['specialite']

        db.session.commit()
        return redirect(url_for('professeurs.index'))

    return render_template('professeurs/edit.html', prof=prof)

# DELETE
@prof_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    prof = Professeur.query.get_or_404(id)

    db.session.delete(prof)
    db.session.commit()

    return redirect(url_for('professeurs.index'))