#cukriky

n = int(input())
cisla = input().split()
cisla_int = [int(i) for i in cisla]

dlzka = len(cisla_int) - 1
def es():
    for idx1, cislo1 in enumerate(cisla_int):
        for cislo2 in cisla_int[idx1 + 1:]:
            for cislo3 in cisla_int[idx1 + 2:]:
                if (cislo1 + cislo2 + cislo3) % 3 == 0:
                    print(f"{cislo1} {cislo2} {cislo3}")
                    return
es()