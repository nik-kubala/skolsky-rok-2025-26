n = int(input())

zoznam = []
for _ in range(n):
    riadok = input()
    zoznam.append(riadok.split())

diagonaly = {}
for riadok in range(n):
    for stlpec in range(n):
        rozdiel = riadok - stlpec
        if rozdiel not in diagonaly:
            diagonaly[rozdiel] = []

for index1, riadok in enumerate(zoznam):
    for index2, cislo in enumerate(riadok):
        rozdiel = index1 - index2
        diagonaly[rozdiel].append(int(cislo))

def checker():
    for diagonala, hodnoty in diagonaly.items():
        if len(set(hodnoty)) != 1:
            return False
    return True

if checker():
    print(f"dokonale diagonalne")
else:
    print(f"kopa smetia")