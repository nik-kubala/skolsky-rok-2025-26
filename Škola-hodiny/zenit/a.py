inp = input()
vysledok = 25
for i in inp:
    if i != " ":
        if i != "-":
            vysledok += int(i)
        else:
            idx = inp.index(i)
            vysledok += -(int(inp[idx + 1]))
print(vysledok)