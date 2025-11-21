pocet = int(input())
znamky = input().split()

slovnik = {cislo: 0 for cislo in znamky}

vysledok = []
for znamka in znamky:
    if slovnik[znamka] < pocet:
        vysledok.append(znamka)
        slovnik[znamka] += 1

print((" ").join(vysledok))