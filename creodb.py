import sqlite3

# Connessione al database (se non esiste, verrà creato un nuovo database)
conn = sqlite3.connect('rentorino.db')

# Creazione di un cursore per eseguire comandi SQL
cursor = conn.cursor()

# Creazione della tabella Utenti
cursor.execute('''
    CREATE TABLE if not exists Utenti (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Cognome TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE,
    Password TEXT NOT NULL,
    Tipo TEXT CHECK (Tipo IN ('Cliente', 'Locatore')))
''')

# Creazione della tabella Annunci
cursor.execute('''
    CREATE TABLE if not exists Annunci (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Titolo TEXT NOT NULL,
    Indirizzo TEXT NOT NULL,
    TipoCasa TEXT NOT NULL,
    NumeroLocali INTEGER NOT NULL,
    Descrizione TEXT NOT NULL,
    PrezzoMensile REAL NOT NULL,
    Arredato INTEGER CHECK (Arredato IN (0, 1)),
    Immagine TEXT,
    IDLocatore INTEGER,
    Disponibile INTEGER CHECK (Disponibile IN (0, 1)),
    FOREIGN KEY (IDLocatore) REFERENCES Utenti(ID))
''')

# Creazione della tabella Prenotazioni
cursor.execute('''
    CREATE TABLE if not exists Prenotazioni (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    IDCliente INTEGER,
    IDAnnuncio INTEGER,
    DataVisita DATE NOT NULL,
    FasciaOraria TEXT NOT NULL,
    ModalitaVisita TEXT CHECK (ModalitaVisita IN ('In Persona', 'Da Remoto')),
    Stato TEXT CHECK (Stato IN ('Richiesta', 'Accettata', 'Rifiutata')),
    MotivoRifiuto TEXT,
    FOREIGN KEY (IDCliente) REFERENCES Utenti(ID),
    FOREIGN KEY (IDAnnuncio) REFERENCES Annunci(ID))
''')

# Commit delle modifiche
conn.commit()

# Chiusura del cursore e della connessione al database
cursor.close()
conn.close()