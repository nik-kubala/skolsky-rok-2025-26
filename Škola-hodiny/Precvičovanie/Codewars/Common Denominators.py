import numpy as np
from math import gcd

def convert_fracts(lst):
    if not lst:
        return []
    
    mensie_hodnoty = []
    for zlomok in lst:
        citatel_temp = zlomok[0] // gcd(*zlomok)
        menovatel_temp = zlomok[1] // gcd(*zlomok) 
        mensie_hodnoty.append([citatel_temp, menovatel_temp])
    
    nasobok = int(np.lcm.reduce([zlomok[1] for zlomok in mensie_hodnoty]))
    
    finalny_zoznam = []
    for zlomok in mensie_hodnoty:
        faktor = nasobok // zlomok[1]
        finalny_zoznam.append([zlomok[0] * faktor, zlomok[1] * faktor])
    return finalny_zoznam


convert_fracts([[6, 12], [4, 12], [3, 12]])