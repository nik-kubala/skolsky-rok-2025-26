from itertools import count


riadok, stlpec = input().split()
riadok = int(riadok)
stlpec = int(stlpec)

def spocitas(riadok):
    return sum(riadok)

i = riadok
sachovnica = []
while i >= 1:
    riadok_list = input().split()
    riadok_list = [int(cislo) for cislo in riadok_list]
    sachovnica.append(riadok_list)
    i -= 1

counter = 0
    
if riadok == 2 and stlpec == 2:
    zaciatok = sachovnica[1][0]
    konec = sachovnica[0][1]
    rohy = [sachovnica[1][1], sachovnica[0][0]]
    najvacsie = max(rohy)
    counter = zaciatok + konec + najvacsie
elif riadok % 2 == 0 and stlpec % 2 == 0:
    najmensie = []
    for i in range(1, len(sachovnica)):
        najmensie.extend(sachovnica[i][1:-2])
    najmensie.append((sachovnica[0][0]))
    najmensie.append((sachovnica[0][-2]))
    najmensie.append((sachovnica[1][-1]))
    najmensie.append((sachovnica[-2][0]))
    najmensie.append((sachovnica[-2][-1]))
    najmensie.append((sachovnica[-1][1]))
    najmensie.append((sachovnica[-1][-1]))
    najmensie_cislo = min(najmensie)
    for i in range(0, len(sachovnica)):
        counter += spocitas(sachovnica[i])
    counter -= najmensie_cislo
else:
    for i in range(0, len(sachovnica)):
        counter += spocitas(sachovnica[i])
print(counter)