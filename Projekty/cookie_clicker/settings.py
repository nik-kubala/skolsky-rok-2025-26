# Nastavenia celej hry.

# Nastavenia okna.
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
FPS = 60
TITLE = "Cookie Clicker"

# Farby (RGB).
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BACKGROUND_COLOR = (240, 235, 220)

BACKGROUND_IMAGE_FILENAME = "Backround.png"

# Dáta o upgradoch.
UPGRADES_DATA = [
    {
        "name": "Cursor",
        "base_cost": 15,
        "base_cps": 0.1,
        "description": "Pomalý, ale istý klikač."
    },
    {
        "name": "Babka",
        "base_cost": 100,
        "base_cps": 1,
        "description": "Babička čo pečie koláčiky."
        
    },
    {
        "name": "Farma",
        "base_cost": 1100,
        "base_cps": 5,
        "description": "Pestuj koláčikové stromy."
    },
    {
        "name": "God",
        "base_cost": 10000,
        "base_cps": 100,
        "description": "Staň sa bohom."
    }
]