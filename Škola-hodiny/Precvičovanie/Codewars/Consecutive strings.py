def longest_consec(strarr, k):
    zoznam = []
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ""
    else:
        for i in range(0, len(strarr) - k + 1):
            zoznam.append("".join(strarr[i : i + k]))
    #for 
    print(zoznam)
longest_consec(["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], 2)
