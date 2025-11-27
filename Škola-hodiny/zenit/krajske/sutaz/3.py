s, k = input().split()
s = int(s)
k = int(k)

if k < 100:
    vysledok = (100 * s) / (100 - k)
    print(vysledok)
else:
    print(-1)