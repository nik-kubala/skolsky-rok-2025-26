def pocetnost(vstup):
    with open(vstup, "r", encoding = "UTF-8") as fr:
        nacitane_riadky = fr.readlines()
    
    for riadok in nacitane_riadky:
        print(riadok.strip())
    
    abeceda = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
    pocty = {znak: 0 for znak in abeceda}
    
    for riadok in nacitane_riadky:
        for char in riadok.upper():
            if char in abeceda:
                pocty[char] += 1
    
    pouzite = {znak: pocet for znak, pocet in pocty.items() if pocet > 0}
    nepouzite = [znak for znak, pocet in pocty.items() if pocet == 0]
    print(f"Počty jednotlivých znakov v texte:")
    for znak, pocet in pouzite.items():
        print(f"{znak} - {pocet}")
    print(f"Nepouzité znaky: {(", ".join(nepouzite))}")

vstup = "Precvičovanie/Material_dudo/20/tabulka_pocetnosti.txt"
pocetnost(vstup)