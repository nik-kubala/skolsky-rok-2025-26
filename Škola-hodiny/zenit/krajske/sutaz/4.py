inp = input().split()

male = []
velke = []
cisla = []

for slovo in inp:
    male_temp = []
    velke_temp = []
    cisla_temp = []
    for pismeno in slovo:
        if pismeno.islower():
            male_temp.append(pismeno)
        elif pismeno.isupper():
            velke_temp.append(pismeno)
        elif pismeno.isdigit():
            cisla_temp.append(pismeno)
    if len(male_temp) != 0:
        male.append("".join(male_temp))
    if len(velke_temp) != 0:
        velke.append("".join(velke_temp))
    if len(cisla_temp) != 0:
        cisla.append("".join(cisla_temp))

vysledok = []
if len(male) != 0:
    vysledok.append(" ".join(male))
if len(velke) != 0:
    vysledok.append(" ".join(velke))
if len(cisla) != 0:
    vysledok.append(" ".join(cisla))

print(" ".join(vysledok))