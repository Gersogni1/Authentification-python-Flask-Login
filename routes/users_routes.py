from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Cours, Professeur, User
from flask_login import login_required

users_bp = Blueprint('users', __name__, url_prefix='/users')

# LIST
@users_bp.route('/')
@login_required
def index():
    users = User.query.all()
    return render_template('users/index.html', users=users)

# CREATE
@users_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    users = User.query.all()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        users = User(
            name=name,
            email=email,
        )

        db.session.add(users)
        db.session.commit()

        return redirect(url_for('users.index'))

    return render_template('users/create.html', users=users)

# UPDATE
@users_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        
        db.session.commit()
        return redirect(url_for('users.index'))

    return render_template('users/edit.html', user=user)

# DELETE
@users_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    users = User.query.get_or_404(id)

    db.session.delete(users)
    db.session.commit()

    return redirect(url_for('users.index'))