import sqlite3

def get_user_by_id(id_utente):
    query = 'SELECT * FROM utenti WHERE id = ?'

    connection = sqlite3.connect('db/mangiato.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(query, (id_utente,))

    result = cursor.fetchone()
    
    cursor.close()
    connection.close()

    return result

def get_user_by_email(email_utente):

    query = 'SELECT * FROM utenti WHERE email = ?'

    connection = sqlite3.connect('db/mangiato.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(query, (email_utente,))

    result = cursor.fetchone()
    
    cursor.close()
    connection.close()

    return result


def creare_utente(nuovo_utente):
    query = 'INSERT INTO utenti(nome,cognome,email,password) VALUES (?,?,?,?)'

    connection = sqlite3.connect('db/mangiato.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    success = False

    try:
        cursor.execute(query, (nuovo_utente['nome'],nuovo_utente['cognome'],nuovo_utente['email'], nuovo_utente['password']))
        connection.commit()
        success = True
    except Exception as e:
        print('Error', str(e))
        connection.rollback()

    cursor.close()
    connection.close()

    return success

   # CREATE TABLE IF NOT EXISTS annunci (
   #     id INTEGER PRIMARY KEY AUTOINCREMENT,
   #     descrizione TEXT NOT NULL,
   #     tipo_casa TEXT NOT NULL,
   #     numero_locali INTEGER CHECK (numero_locali > 0),
   #     prezzo INTEGER CHECK (prezzo > 0),
   #     id_locatore SMALL INT,
   #     disponibilità INTEGER,
   #     immagine TEXT NOT NULL
   # )
   # Inserimento di dati nella tabella
#cursor.execute('''
#    INSERT INTO annunci (descrizione, tipo_casa, numero_locali, prezzo, id_locatore, disponibilità,immagine)
#    VALUES (?, ?, ?, ?,?,?,?)
#''', ('casetta bella','villa',5,120000,1,1,'img1.webp'))