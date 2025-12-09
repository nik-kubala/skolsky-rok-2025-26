subor = "Škola-hodiny/Precvičovanie/Material_dudo/29/kompresia_obrazka_1.txt"

with open(subor, "r", encoding = "UTF-8")as fr:
    nacitane_riadky = fr.readlines()

rozmery = nacitane_riadky[0].split()
print(f"Rozmery obrázka -> šírka: {rozmery[0]}, výška: {rozmery[1]}")

vysledok = []
for riadok in nacitane_riadky[1:]:
    riadok_temp = []
    aktualny_znak = "0"
    kaunter = 0
    for znak in riadok:
        if znak == aktualny_znak:
            kaunter += 1
        else:
            riadok_temp.append(kaunter)
            kaunter = 1
            aktualny_znak = znak

    vysledok.append(" ".join(map(str,riadok_temp)))

for riadok in vysledok:
    print(riadok)
