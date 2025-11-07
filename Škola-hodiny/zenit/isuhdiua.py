n = int(input())
cisla_str = input().split()
cisla_int = [(int(i)) for i in cisla_str]

slov_idk = {cislo: 0 for cislo in cisla_int}

vysledok = []
for cislo in cisla_int:
    if slov_idk[cislo] < n:
        vysledok.append(cislo)
        slov_idk[cislo] += 1
print((" ").join(map(str, vysledok)))