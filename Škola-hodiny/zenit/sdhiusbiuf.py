#fuj
inp = input()

slov = {
    "(": 0,
    ")": 0,
    "[": 0,
    "]": 0,
    "{": 0,
    "}": 0
} 
for i in inp:
    slov[i] += 1

def skuska():
    if slov["("] == slov[")"]:
        if slov["["] == slov["]"]:
            if slov["{"] == slov["}"]:
                return True
    return False

if skuska():
    print(f"ano")
else:
    print(f"nie")