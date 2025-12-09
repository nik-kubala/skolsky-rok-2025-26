from .warrior import Warrior

class Knight(Warrior):
    def __init__(self, attack: int = 7):
        super().__init__(health=50, attack=attack) # volanie konštruktora z predchádzajúcej triedy