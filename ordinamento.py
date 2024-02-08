import sqlite3

# Connessione al database
conn = sqlite3.connect('rentorino.db')
cursor = conn.cursor()

# Query SQL per selezionare tutti gli annunci ordinati per prezzo decrescente
query = """
    SELECT *
    FROM Annunci
    ORDER BY PrezzoMensile DESC;
"""

# Esecuzione della query
cursor.execute(query)

# Recupero dei risultati
result = cursor.fetchall()

# Stampa dei risultati
for row in result:
    print(row)

# Chiusura del cursore e della connessione al database
cursor.close()
conn.close()