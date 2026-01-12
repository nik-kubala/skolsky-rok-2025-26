# BOJOVÁ LOGIKA / GENERÁTOR PRE FIGHT1V1 #
from units import Warrior

def fight1v1(warrior1: Warrior, warrior2: Warrior):
    # Generátor, ktorý vracia kroky boja medzi dvoma bojovníkmi.
    while warrior1.is_alive and warrior2.is_alive:
        warrior1.hit(warrior2)
        
        yield {
            "attacker": warrior1,
            "defender": warrior2,
            "defender_health": warrior2.health,
            "defender_alive": warrior2.is_alive
        }
        
        if not warrior2.is_alive:
            break
            
        warrior2.hit(warrior1)
        
        yield {
            "attacker": warrior2,
            "defender": warrior1,
            "defender_health": warrior1.health,
            "defender_alive": warrior1.is_alive
        }