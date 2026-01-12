# NAČÍTANIE OBRÁZKOV A ZVUKOV #
import pygame
from config import ASSETS_DIR, VELKOST_UNITU
from units import Warrior, Knight, Defender, Vampire
import os


def load_image(filename):
    # Načíta obrázok a zmení jeho veľkosť
    path: str = os.path.join(ASSETS_DIR, filename)
    return pygame.transform.scale(
        pygame.image.load(path).convert_alpha(), 
        (VELKOST_UNITU, VELKOST_UNITU)
    )


def load_sound(filename):
    # Načíta zvuk
    path: str = os.path.join(ASSETS_DIR, filename)
    return pygame.mixer.Sound(path)


def init_assets():
    # Inicializuje a vráti všetky assety. Volať až po pygame.init()!
    units_me = {
        Warrior: load_image("warrior_b.png"),
        Knight: load_image("knight_b.png"),
        Defender: load_image("defender_b.png"),
        Vampire: load_image("vampire_b.png")
    }
    
    units_enemy = {
        Warrior: load_image("warrior_r.png"),
        Knight: load_image("knight_r.png"),
        Defender: load_image("defender_r.png"),
        Vampire: load_image("vampire_r.png")
    }
    
    sound_attack: Sound = load_sound("attack.ogg")
    sound_death: Sound = load_sound("death.ogg")
    
    # Rezervuj samostatný kanál pre zvuk smrti, aby nebol prerušený zvukom útoku
    death_channel = pygame.mixer.Channel(1)
    
    return units_me, units_enemy, sound_attack, sound_death, death_channel