# import module
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash

import sqlite3

import case
import utenti
import crea_utente
from models import User

# create the application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'segreto'

login_manager = LoginManager()
login_manager.init_app(app)

# define the homepage
@app.route('/')
def index():
  case_db = case.tutti_annunci()
  return render_template('index.html', case=case_db)

@app.route('/case/<int:id>')
def casa_spec(id):
  casa_db = case.get_casa(id)
  return render_template('appartamento.html', casa = casa_db)

# define the about page
@app.route('/about')
def about():
  return render_template('about.html')

# define the profile page
@app.route('/profilo')
@login_manager.user_loader
@login_required
def profilo():
  db_user = utenti.get_user_by_id(user_id)
  return render_template('profilo.html',utente = db_user)

# define the signup page
@app.route('/iscriviti')
def iscriviti():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():

  new_user_from_form = request.form.to_dict()

  print(new_user_from_form)

  if new_user_from_form ['nome'] == '':
    app.logger.error('Il campo non può essere vuoto')
    return redirect(url_for('index'))

  if new_user_from_form ['cognome'] == '':
    app.logger.error('Il campo non può essere vuoto')
    return redirect(url_for('index'))

  if new_user_from_form ['email'] == '':
    app.logger.error('Il campo non può essere vuoto')
    return redirect(url_for('index'))

  if new_user_from_form ['password'] == '':
    app.logger.error('Il campo non può essere vuoto')
    return redirect(url_for('index'))
  
  new_user_from_form ['password'] = generate_password_hash(new_user_from_form ['password'])

  success = crea_utente.creare_utente(new_user_from_form)

  if success:
    return redirect(url_for('index'))

  return redirect(url_for('iscriviti'))

@app.route('/filtro',methods= ['POST'])
def filtro():
  
  #case_db = case.tutti_annunci(azione)
  #return render_template('index.html', case=case_db)
    azione = request.form.to_dict()
    query = 'SELECT *  FROM Annunci  ORDER BY ' + azione['scelta']
    connection = sqlite3.connect('db/rentorino.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return redirect(url_for('index',case = result))

@app.route('/login', methods=['POST'])
def login():

  utente_form = request.form.to_dict()


  utente_db = utenti.get_user_by_email(utente_form['email'])

  if not utente_db or not check_password_hash(utente_db['password'], utente_form['password']):
    flash("Non esiste l'utente")
    return redirect(url_for('index'))
  else:
    new = User(id=utente_db['id'], nome=utente_db['nome'], cognome=utente_db['cognome'], email=utente_db['email'], password=utente_db['password'],tipo =utente_db['tipo'])
    login_user(new, True)
    flash('Success!')

    return redirect(url_for('index'))

@app.route('/recensioni/new', methods=['POST'])
@login_required
@login_manager.user_loader
def add_recensione():

  recensione = request.form.to_dict()

  if recensione ['recensione'] == '':
    app.logger.error('Il campo non può essere vuoto')
    return redirect(url_for('index'))

  foto = request.files['imgRecensione']
  if foto.filename != '':
    foto.save('static/'+foto.filename)
    recensione['url_foto'] = foto.filename

  rec = {'testo_recensione': 'test', 'url_foto': 'test_url', 'valutazione': 4, 'piatto': 1}
  piatti_dao.add_recensione(rec)

  return redirect(url_for('index'))

@login_manager.user_loader
def load_user(user_id):
  db_user = utenti.get_user_by_id(user_id)
  if db_user:
        # Crea un oggetto User utilizzando i dati recuperati dal database
    user = User(id=db_user['id'],
            nome=db_user['nome'],
            cognome=db_user['cognome'],
            email=db_user['email'],
            password=db_user['password'],
            tipo=db_user['tipo'])
        # Restituisci l'oggetto User
    return user
  else:
        # Se l'utente non esiste nel database, restituisci None
    return None
    

    #user = User(id=db_user['id'],	nome=db_user['nome'],	cognome=db_user['cognome'],	email=db_user['email'],	password=db_user['password'],tipo=db_user['tipo'])

    #return user

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))