n = int(input())
cisla = input()

cisla = [int(cislo) for cislo in cisla.split()]

if n > 3:

    max1 = max(cisla)
    cisla.pop(cisla.index(max1))
    max2 = max(cisla)
    cisla.pop(cisla.index(max2))

    min1 = min(cisla)
    cisla.pop(cisla.index(min1))
    min2 = min(cisla)
    cisla.pop(cisla.index(min2))

    if max1 * max2 > min1 * min2:
        print(max1, max2)
    else:
        print(min1, min2)
    print(min1, max1)
    if max1 / max2 > min1 / min2:
        print(max1, max2)
    else:
        print(min1, min2)
    print(max1, min1)

else:
    max1 = max(cisla)
    cisla.pop(cisla.index(max1))
    stred1 = max(cisla)
    cisla.pop(cisla.index(stred1))
    min1 = min(cisla)
    cisla.pop(cisla.index(min1))
    
    print(stred1, max1)
    print(min1, max1)
    print(max1, stred1)
    print(max1, min1)