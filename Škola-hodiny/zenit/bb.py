def rek():
    while True:
        try:
            riadok = input().split()
            if "kod:" in riadok:
                idx = riadok.index("kod:")
                if idx + 1 < len(riadok):
                    print(riadok[idx + 1])
                    break
        except EOFError:
            break
rek()