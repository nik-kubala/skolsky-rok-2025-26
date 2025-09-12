import random

studenti = [i for i in range(1, int(input("Zadaj počet študentov:")) + 1)]
otazky = [i for i in range(1, int(input("Zadaj počet otázok:")) + 1)]

random.shuffle(studenti)

if len(otazky) < len(studenti):
    print(f"Počet otázok je menej ako počet štdentov = kód sa vypína.")
    exit()

parne = []
neparne = []
finalne_poradie_cisel = []
for cislo in otazky:
    if cislo % 2 == 0:
        parne.append(cislo)
    else:
        neparne.append(cislo)
random.shuffle(parne)
random.shuffle(neparne)
for i in range(len(neparne)):
    finalne_poradie_cisel.append(parne[i])
    finalne_poradie_cisel.append(neparne[i])

for i in range(len(studenti)):
    print(f"{i + 1}. študent: {studenti[i]}, otázka:{finalne_poradie_cisel[i]}")
