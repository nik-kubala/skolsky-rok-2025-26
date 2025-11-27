n = int(input())
riadky = n

cisla = []
for i in range(n):
    cislo = int(input())
    cisla.append(cislo)

sucet = float("inf")

cisla.sort()

for idx in range(n // 2):
    najmensie = cisla[idx]
    najvacsie = cisla[-(idx + 1)]
    sucet2 = najmensie + najvacsie
    if sucet2 < sucet:
        sucet = sucet2

print(sucet)