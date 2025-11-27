n = int(input())
pocet_riadkov = n

def menic(cislo):
    if cislo == 0:
        return "nula"

    jednotky_slovo = [
        "", "jeden", "dva", "tri", "styri", "pat", "sest", "sedem", "osem", "devat", "desat",
        "jedenast", "dvanast", "trinast", "strnast", "patnast", "sestnast", "sedemnast", "osemnast", "devatnast"
    ]
    desiatky = ["", "", "dvadsat", "tridsat", "styridsat", "patdesiat", "sestdesiat", "sedemdesiat", "osemdesiat", "devatdesiat"]
    stovky_slovo = ["", "sto", "dvesto", "tristo", "styrsto", "patsto", "seststo", "sedemsto", "osemsto", "devatsto"]

    if cislo < 20:
        return jednotky_slovo[cislo]

    slovo = ""
    
    stovky = cislo // 100
    if stovky > 100:
        slovo += stovky_slovo[stovky]
        
    desiatky_zvysok = cislo % 100
    if desiatky_zvysok > 0:
        if desiatky_zvysok < 20:
            slovo += jednotky_slovo[desiatky_zvysok]
        else:
            desiatky = desiatky_zvysok // 10
            jednotky = desiatky_zvysok % 10
            slovo += desiatky[desiatky]
            if jednotky > 0:
                slovo += jednotky_slovo[jednotky]
    
    return slovo

while pocet_riadkov >= 1:
    riadok = input()
    pocet = riadok.count("zenit")
    
    vysledok = menic(pocet)

    if pocet == 1:
        vysledok += " zenit"
    elif 2 <= pocet <= 4:
        vysledok += " zenity"
    else:
        vysledok += " zenitov"
    
    print(vysledok)
    
    pocet_riadkov -= 1