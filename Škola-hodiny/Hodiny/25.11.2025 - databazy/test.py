import sqlite3

# Zadajte cestu k vášmu databázovému súboru
database_file = 'mojadatabaza.sqlite'

try:
    # Pripojenie k SQLite databáze
    con = sqlite3.connect(database_file)
    cursor = con.cursor()

    # Získanie zoznamu všetkých tabuliek v databáze
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    if not tables:
        print("V databáze sa nenachádzajú žiadne tabuľky.")
    else:
        print("Tabuľky nájdené v databáze:")
        for table in tables:
            print(f"- {table[0]}")

except sqlite3.Error as e:
    print(f"Nastala chyba pri práci s databázou: {e}")

finally:
    # Zatvorenie spojenia
    if con:
        con.close()