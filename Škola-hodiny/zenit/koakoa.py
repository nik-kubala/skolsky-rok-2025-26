n = input()

cisla = input().split()
cisla_int = [int(i) for i in cisla]

nek = float("inf")

vela_nasobok = -nek
vela_nasobok_vysledok = [nek, 0]
malo_nasobok = nek
malo_nasobok_vysledok = [nek, 0]
vela_delenie = -nek
vela_delenie_vysledok = [nek, 0]
malo_delenie = nek
malo_delenie_vysledok = [nek, 0]

for i in range(len(cisla_int)):
        for k in range(len(cisla_int)):
                
                if i == k:
                        continue
                
                x = cisla_int[i]
                y = cisla_int[k]
                
                nasobok = x * y
                if nasobok > vela_nasobok:
                        vela_nasobok = nasobok
                        vela_nasobok_vysledok = [x, y]
                elif nasobok == vela_nasobok:
                        if x < vela_nasobok_vysledok[0]:
                                vela_nasobok_vysledok = [x, y]
                
                if nasobok < malo_nasobok:
                        malo_nasobok = nasobok
                        malo_nasobok_vysledok = [x, y]
                elif nasobok == malo_nasobok:
                        if x < malo_nasobok_vysledok[0]:
                                malo_nasobok_vysledok = [x, y]
                
                delennie = x / y
                if delennie > vela_delenie:
                        vela_delenie = delennie
                        vela_delenie_vysledok = [x, y]
                elif delennie == vela_delenie:
                        if x < vela_delenie_vysledok[0]:
                                vela_delenie_vysledok = [x, y]
                
                if delennie < malo_delenie:
                        malo_delenie = delennie
                        malo_delenie_vysledok = [x, y]
                elif delennie == malo_delenie:
                        if x < malo_delenie_vysledok[0]:
                                malo_delenie_vysledok = [x, y]

print(f"{vela_nasobok_vysledok[0]} {vela_nasobok_vysledok[1]}")
print(f"{malo_nasobok_vysledok[0]} {malo_nasobok_vysledok[1]}")
print(f"{vela_delenie_vysledok[0]} {vela_delenie_vysledok[1]}")
print(f"{malo_delenie_vysledok[0]} {malo_delenie_vysledok[1]}")