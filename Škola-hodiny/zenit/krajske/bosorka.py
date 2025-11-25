def bosorka():
    cislo = int(input())
    binarne = bin(cislo)[2:]
    if len(binarne) % 2 != 0:
        binarne = '0' + binarne
    i = len(binarne) - 1
    vysledok = ""
    while i >= 1:
        temp1 = binarne[i]
        temp2 = binarne[i - 1]
        vysledok += temp2 + temp1
        i -= 2
    vysledok = int(vysledok[::-1], 2)
    print(vysledok)


bosorka()