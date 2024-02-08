import sqlite3

def creare_utente(nuovo_utente):
    query = 'INSERT INTO utenti(nome,cognome,email,password,tipo) VALUES (?,?,?,?,?)'

    connection = sqlite3.connect('db/rentorino.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    success = False

    try:
        cursor.execute(query, (nuovo_utente['nome'],nuovo_utente['cognome'],nuovo_utente['email'],nuovo_utente['password'],nuovo_utente['tipo']))
        connection.commit()
        success = True
    except Exception as e:
        print('Error', str(e))
        connection.rollback()

    cursor.close()
    connection.close()

    return success