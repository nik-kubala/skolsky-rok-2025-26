#cukriky

n = int(input())
cisla = input().split()
cisla_int = [int(i) for i in cisla]

dlzka = len(cisla_int)
def es():
    for i in range(dlzka):
        for j in range(i + 1, dlzka):
            for k in range(j + 1, dlzka):
                cislo1 = cisla_int[i]
                cislo2 = cisla_int[j]
                cislo3 = cisla_int[k]
                if (cislo1 + cislo2 + cislo3) % 3 == 0:
                    print(f"{cislo1} {cislo2} {cislo3}")
                    return
es()