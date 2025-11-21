pocet_kopok = int(input())
kopky = input().split()

kopky_int = [int(cislo) for cislo in kopky]

zvysok0 = []
zvysok1 = []
zvysok2 = []

for cislo in kopky_int:
    if cislo % 3 == 0:
        zvysok0.append(cislo)
    elif cislo % 3 == 1:
        zvysok1.append(cislo)
    else:
        zvysok2.append(cislo)

if len(zvysok0) >= 3:
    print(f"{zvysok0[0]} {zvysok0[1]} {zvysok0[2]}")
elif len(zvysok1) >= 3:
    print(f"{zvysok1[0]} {zvysok1[1]} {zvysok1[2]}")
elif len(zvysok2) >= 3:
    print(f"{zvysok2[0]} {zvysok2[1]} {zvysok2[2]}")
else:
    print(f"{zvysok0[0]} {zvysok1[0]} {zvysok2[0]}")