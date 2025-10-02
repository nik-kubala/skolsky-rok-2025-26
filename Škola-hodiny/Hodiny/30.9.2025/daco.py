from PIL import Image, ImageDraw
#nájde rozloženie 8 dám všetkých možných rozložení na šachovnici
#urobíme funkciu check(x, y) pozície a tá pozrie či to je v pohode
#pole 8*8 a 0/1 podla toho ci tam je dama
size = 8
sachovnica = [([0] * size) for i in range(0, size)]

def check(x, y):        #1, 1       #1 2
    for index in range(size):
        if sachovnica[y][index] == 1 or sachovnica[index][x] == 1:
            return False
    for index1 in range(size):
        for index2 in range(size):
            if index1 + index2 == x + y and sachovnica[index1][index2] == 1:
                return False
            if index1 - index2 == y - x and sachovnica[index1][index2] == 1:
                return False
    return True

def kreslenie(cislo_riesenia):
    velkost_policka = 50
    velkost_plochy = velkost_policka * size
    
    obrazok = Image.new("RGB", (velkost_plochy, velkost_plochy), "white")
    kresli = ImageDraw.Draw(obrazok)
    
    for y in range(size):
        for x in range(size):
            if (x + y) % 2 == 1:
                kresli.rectangle(
                    [(x * velkost_policka, y * velkost_policka), 
                     ((x + 1) * velkost_policka, (y + 1) * velkost_policka)], 
                    fill="black"
                )
    
    for y in range(size):
        for x in range(size):
            if sachovnica[y][x] == 1:
                kresli.ellipse(
                    [(x * velkost_policka + 5, y * velkost_policka + 5), 
                     ((x + 1) * velkost_policka - 5, (y + 1) * velkost_policka - 5)], 
                    fill="red"
                )
    
    obrazok.save(f"{"Hodiny/30.9.2025/Stavy"}/riesenie_{cislo_riesenia}.png")
    print(f"Uložený obrázok riesenie_{cislo_riesenia}.png")

count = 0
def rekurzivna_drticka(n):      #n dámy
    global sachovnica
    global count
    if n == size:
        for riadok in sachovnica:
            print(riadok)
        count += 1
        kreslenie(count)
        print("------------------------")
    else:
        for x in range(size):
            if check(x, n):
                sachovnica[n][x] = 1
                rekurzivna_drticka(n+1)
                sachovnica[n][x] = 0

rekurzivna_drticka(0)
print(count)