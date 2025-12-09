import sqlite3 as sql

# Pripojenie k databáze
con = sql.connect("Škola-hodiny/Hodiny/25.11.2025 - databazy/mojadatabaza.sqlite")

# Vytvorenie kurzora na vykonávanie príkazov
cursor = con.cursor()

# Vykonanie SQL dopytu na výber študentov s veľkosťou nohy 42.
# Poznámka: Tabuľka sa volá 'spoluziaci', nie 'studenti'.
cursor.execute("SELECT * FROM spoluziaci WHERE 41 <= nohy AND nohy <= 43")

# Získanie všetkých výsledkov z dopytu
vysledky = cursor.fetchall()

print("Spolužiaci s veľkosťou nohy 42:")
for riadok in vysledky:
    print(riadok)

# Zatvorenie spojenia s databázou
con.close()
