#podmnozina grafov su stromy
import os

domovska_cesta = os.path.expanduser("~") 

def walker(cesta, hlbka):
    try:
        for item in os.listdir(cesta):
            if os.path.isdir(cesta + "/" + item):
                print("-" * hlbka + item)
                walker(cesta + "/" + item, hlbka + 1)
            # else:
            #    print("-" * hlbka + item)
    except PermissionError:
        print(f"Nie sú permisie.")

walker(domovska_cesta, 1)