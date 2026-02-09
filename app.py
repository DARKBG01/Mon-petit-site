import os
import sqlite3
import csv
from io import StringIO
from flask import Flask, render_template, request, redirect, url_for, flash, make_response

app = Flask(__name__)
app.secret_key = 'une_cle_secrete_tres_securisee'  # Nécessaire pour les messages flash
DB_NAME = "edunotes.db"

def get_db_connection():
    """Crée une connexion à la base de données avec gestion des lignes comme dictionnaires."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Permet d'accéder aux colonnes par nom
    return conn

def init_db():
    """Initialise la base de données si elle n'existe pas."""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            matiere TEXT NOT NULL,
            note REAL NOT NULL,
            coefficient INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialisation de la DB au lancement
init_db()

def calculer_moyenne(notes):
    """Calcule la moyenne pondérée."""
    if not notes:
        return 0, 0
    
    total_points = sum(n['note'] * n['coefficient'] for n in notes)
    total_coef = sum(n['coefficient'] for n in notes)
    moyenne = total_points / total_coef if total_coef > 0 else 0
    return moyenne, total_coef

# --- ROUTES ---

@app.route('/')
def index():
    conn = get_db_connection()
    notes = conn.execute('SELECT * FROM notes').fetchall()
    conn.close()
    
    # Conversion en liste de dicts pour faciliter l'usage dans le template
    notes_list = [dict(row) for row in notes]
    moyenne, total_coef = calculer_moyenne(notes_list)
    
    return render_template('index.html', 
                         notes=notes_list, 
                         moyenne=moyenne, 
                         total_coef=total_coef)

@app.route('/releve')
def releve():
    conn = get_db_connection()
    notes = conn.execute('SELECT * FROM notes').fetchall()
    conn.close()
    return render_template('releve.html', notes=[dict(n) for n in notes])

@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'POST':
        try:
            matiere = request.form['matiere']
            note = float(request.form['note'])
            coef = int(request.form['coefficient'])

            if not (0 <= note <= 20):
                flash("La note doit être comprise entre 0 et 20.", "error")
                return render_template('ajouter.html')

            conn = get_db_connection()
            conn.execute('INSERT INTO notes (matiere, note, coefficient) VALUES (?, ?, ?)',
                         (matiere, note, coef))
            conn.commit()
            conn.close()
            
            flash(f"Note de {matiere} ajoutée avec succès !", "success")
            return redirect(url_for('index'))
        except ValueError:
            flash("Erreur de saisie. Vérifiez les valeurs.", "error")

    return render_template('ajouter.html')

@app.route('/modifier/<int:note_id>', methods=['GET', 'POST'])
def modifier(note_id):
    conn = get_db_connection()
    note_actuelle = conn.execute('SELECT * FROM notes WHERE id = ?', (note_id,)).fetchone()

    if not note_actuelle:
        conn.close()
        flash("Note introuvable.", "error")
        return redirect(url_for('releve'))

    if request.method == 'POST':
        try:
            matiere = request.form['matiere']
            note = float(request.form['note'])
            coef = int(request.form['coefficient'])

            if not (0 <= note <= 20):
                flash("La note doit être comprise entre 0 et 20.", "error")
                return render_template('modifier.html', note=dict(note_actuelle))

            conn.execute('UPDATE notes SET matiere = ?, note = ?, coefficient = ? WHERE id = ?',
                         (matiere, note, coef, note_id))
            conn.commit()
            conn.close()
            
            flash("Note modifiée avec succès.", "success")
            return redirect(url_for('releve'))
        except ValueError:
            flash("Erreur de format.", "error")

    conn.close()
    return render_template('modifier.html', note=dict(note_actuelle))

@app.route('/supprimer/<int:note_id>')
def supprimer(note_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.commit()
    conn.close()
    flash("Note supprimée.", "info")
    return redirect(url_for('releve'))

@app.route('/export/csv')
def export_csv():
    conn = get_db_connection()
    notes = conn.execute('SELECT * FROM notes').fetchall()
    conn.close()

    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(['Matière', 'Note', 'Coefficient'])
    for note in notes:
        cw.writerow([note['matiere'], note['note'], note['coefficient']])

    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=releve_notes.csv"
    output.headers["Content-type"] = "text/csv"
    return output

if __name__ == '__main__':
    app.run(debug=True)