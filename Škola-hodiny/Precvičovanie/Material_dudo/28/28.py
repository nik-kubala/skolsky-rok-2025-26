from tkinter import N


a = "Škola-hodiny/Precvičovanie/Material_dudo/28/hlasovanie_2.txt"
with open(a, "r", encoding = "UTF-8")as fr:
    nacitane_riadky = fr.readlines()

slov = {}
for cislo in nacitane_riadky:
    if int(cislo) in slov:
        slov[int(cislo)] += 1
    else:
        slov[int(cislo)] = 1
print(slov)