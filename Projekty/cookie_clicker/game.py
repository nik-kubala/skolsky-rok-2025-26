import pygame
from settings import *
from entities import *

class Game:
    def __init__(self):
        # --- Inicializácia Pygame a okna ---
        pygame.init()
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()    # Vytvorí hodiny, ktoré nám pomôžu kontrolovať rýchlosť hry.
        self.running = True
        
        self.cookies = 0
        self.font = pygame.font.Font(None, 50)
        
        # --- Načítanie obrázka pozadia ---
        assets_dir = os.path.join(os.path.dirname(__file__), 'assets')
        backround_path = os.path.join(assets_dir, 'Backround.png')
        
        self.background_image = pygame.image.load(backround_path).convert()
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
        # --- Vytvorenie herných objektov ---
        self.cookie = Cookie(self) # Vytvoríme inštanciu koláčika.
        
        # Vytvoríme upgrady.
        self.upgrades = [Upgrade(upgrade) for upgrade in UPGRADES_DATA]
        
        
    
    def run(self):
        # --- Hlavná herná slučka ---
        while self.running:
            self.clock.tick(FPS) # Zabezpečí, že slučka sa zopakuje maximálne FPS-krát za sekundu.
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        # --- Spracovanie udalostí (vstupov) ---
        for event in pygame.event.get(): # Prejde všetky udalosti, ktoré sa stali.
            if event.type == pygame.QUIT:   # Ak je udalosť ukončenie okna, ukonči hru.
                self.running = False    
    
    def update(self):
        # --- Aktualizácia hernej logiky ---
        ...
    
    def draw(self):
        # --- Vykreslenie na obrazovku ---
        self.screen.blit(self.background_image, (0, 0)) # Vykreslíme pozadie.
        
        # Týmto vytvárame povrch, ktorým zatmavíme trochu pozadie.
        dark_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        
        # Teraz tomu povrchu priradíme farbu. (R, G, B, A) Alpha je priehľadnosť.
        dark_overlay.fill((0, 0, 0, 128))
        
        self.screen.blit(dark_overlay, (0, 0)) # Vykreslíme pozadie.
        
        # Vykreslíme koláčik.
        self.cookie.draw(self.screen)
        
        # --- Vykreslíme počet koláčikov ---
        cookies_text = self.font.render(f"Cookies: {self.cookies}", True, WHITE)
        text_rect = cookies_text.get_rect()
        text_rect.topleft = (10, 10)
        self.screen.blit(cookies_text, text_rect,)
        
        
        pygame.display.flip()   # Zobrazí vykreslený obraz na obrazovku, aby ho bolo vidieť.