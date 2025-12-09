import sqlite3 as sql
import random as rd

conn = sql.connect("Škola-hodiny/Hodiny/25.11.2025 - databazy/mojadatabaza.sqlite")

# 1. Vytvorenie kurzora na vykonávanie príkazov
cursor = conn.cursor()

def generovac_mien(dlzka: int) -> str:
    samohlasky = "aeiouy"
    spoluhlasky = "bcdfghjklmnpqrstvwxz"
    vysledok = ""
    for i in range(dlzka):
        if i % 2 == 0:
            vysledok += rd.choice(samohlasky)
        else:
            vysledok += rd.choice(spoluhlasky)
    return f"{vysledok[0].upper()}{vysledok[1:]}"

# 3. Generovanie a vkladanie 100 náhodných mien a priezvisk
for _ in range(100):
    nove_meno = generovac_mien(rd.randint(4, 7))
    nove_priezvisko = generovac_mien(rd.randint(5, 10))
    farba_oci = rd.randrange(1, 6)
    velkost_nohy = rd.randrange(29, 49)
    print(f"Vkladám: {nove_meno} {nove_priezvisko}, {farba_oci}, {velkost_nohy}")
    cursor.execute("INSERT INTO spoluziaci (meno, priezvisko, oci, nohy) VALUES (?, ?, ?, ?)", (nove_meno, nove_priezvisko, farba_oci, velkost_nohy))

# 4. Uloženie zmien (commit) a zatvorenie spojenia
conn.commit()
conn.close()
print("\nDáta boli úspešne vložené do databázy 'mojadatabaza.sqlite'.")
