pocet_fotiek = int(input())
zoznam = input().split()
zoznam = [int(i) for i in zoznam]
indexy_fotiek = [idx for idx, hodnota in enumerate(zoznam) if hodnota == 1]

i = len(indexy_fotiek) - 1
if i == -1:
    print(0)
else:
    pocet_pohybov = 1
    while i >= 1:
        if indexy_fotiek[i] - indexy_fotiek[i - 1] < 3:
            pocet_pohybov += indexy_fotiek[i] - indexy_fotiek[i - 1]
        else:
            pocet_pohybov += 2
        i -= 1
    print(pocet_pohybov)