# KONFIG KONŠTANTY PRE HRU #
import os

# Rozmery okna
SIRKA_OKNA: int = 1000
VYSKA_OKNA: int = 800

# Rozmery jednotiek
VELKOST_UNITU: int = 120
MEDZERA: int = 20

# Herné nastavenia
INTERVAL: int = 100  # ms medzi útokmi
FPS: int = 60

# Cesty k súborom
BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR: str = os.path.join(BASE_DIR, "assets")