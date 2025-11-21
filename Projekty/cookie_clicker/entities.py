import pygame
import os
from settings import *

class Cookie:
    def __init__(self, game):
        self.game = game
        
        # --- Načítanie a príprava obrázka ---
        
        # Zostavíme cestu k obrázku. os.path.join to urobí správne pre každý operačný systém.
        assets_dir = os.path.join(os.path.dirname(__file__), 'assets')
        cookie_path = os.path.join(assets_dir, 'Cookie.png')
        
        # Načítame obrázok. .convert_alpha() je dôležitá optimalizácia pre obrázky s priehľadnosťou.
        original_image = pygame.image.load(cookie_path).convert_alpha()
        
        self.size = 350
        self.image = pygame.transform.scale(original_image, (self.size, self.size))
        
        # --- Pozícia ---
        
        # get_rect() vytvorí obdĺžnik (Rect) okolo obrázka. S ním sa ľahko manipuluje a zisťuje kolízia.
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    def draw(self, surface):
        # Vykreslí obrázok koláčika na daný povrch (v našom prípade na obrazovku).
        # 'blit' je termín pre kopírovanie pixelov z jedného obrázka na druhý.
        surface.blit(self.image, self.rect)

class Upgrade:
    def __init__(self, game, name: str, base_cost: int, base_cps: int, description: str):
        self.game = game
        
        self.name = name
        self.base_cost = base_cost
        self.base_cps = base_cps
        self.description = description
        
        # Počet upgradu.
        self.count = 0
        # Aktuálna cena upgradu.
        self.current_cost = base_cost
        # Aktuálne cps.
        self.cps = 0.0
    
    def get_total_cps(self):
        return self.base_cps * self.count
    
    def buy(self):
        if self.game.cookies >= self.current_cost:
            self.game.cookies -= self.current_cost
            self.count += 1
            self.current_cost = int(self.base_cost * (1.5 ** self.count))
            celkove_cps = self.get_total_cps()
            return True
        else:
            return False