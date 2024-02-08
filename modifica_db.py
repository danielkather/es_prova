import sqlite3
from flask import Flask

app = Flask(__name__)

# Connessione al database
conn = sqlite3.connect('rentorino.db')
cursor = conn.cursor()

# Inserimento di valori nella tabella Utenti
cursor.execute("INSERT INTO Utenti (Nome, Cognome, Email, Password, Tipo) VALUES (?, ?, ?, ?, ?)",
               ('danzo', 'pazzo', 'email@gmail.com', 'password', 'Cliente'))
conn.commit()

cursor.execute("INSERT INTO Utenti (Nome, Cognome, Email, Password, Tipo) VALUES (?, ?, ?, ?, ?)",
               ('frescoe', 'lino', 'email@hotmail.com', 'password', 'Locatore'))
conn.commit()

# Inserimento di valori nella tabella Annunci
cursor.execute("INSERT INTO Annunci (Titolo, Indirizzo, TipoCasa, NumeroLocali, Descrizione, PrezzoMensile, Arredato, Immagine, IDLocatore, Disponibile) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
               ('TitoloAnnuncio', 'IndirizzoCasa', 'Appartamento', 3, 'Descrizione dell\'annuncio', 1000.00, 1, 'img1.webp', 1, 1))
conn.commit()

# Inserimento di valori nella tabella Prenotazioni
cursor.execute("INSERT INTO Prenotazioni (IDCliente, IDAnnuncio, DataVisita, FasciaOraria, ModalitaVisita, Stato, MotivoRifiuto) VALUES (?, ?, ?, ?, ?, ?, ?)",
               (0, 0, '2024-02-09', '9-12', 'In Persona', 'Richiesta', None))
conn.commit()

# Chiusura della connessione
conn.close()