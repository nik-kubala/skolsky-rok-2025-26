n, k = input().split()
n = int(n)
k = int(k)

cisla = input().split()
cisla_int = [int(cislo) for cislo in cisla]
cisla_int = sorted(set(cisla))

vysledky = []
for i in range(len(cisla_int), 0, -k):
    vysledky_temp = []
    cislo1 = cisla_int[i - 1]
    cislo2 = cisla_int[i - k]
    vysledky_temp.append(cislo1)
    vysledky_temp.append(cislo2)
    vysledky.append(vysledky_temp)

uplny_vysledok = []
for pole in vysledky:
    idx = str(cisla.index(str(pole[1])))
    uplny_vysledok.append(idx)
uplny_vysledok.reverse()

print(" ".join(uplny_vysledok))