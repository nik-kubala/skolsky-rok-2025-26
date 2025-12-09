import pygame
import sys

"""
1. INIALIZÁCIA -------------------------------
"""

pygame.init() # Naštartujeme pygame moduly

obrazovka = pygame.display.set_mode((800, 400)) # Vytvorenie a nastavenie okna
pygame.display.set_caption("Kartový bojovníci") # Zadanie názvu okna

clock = pygame.time.Clock() # Hodiny na riadenie FPS

"""
2. HERNÁ LOGIKA -------------------------------
"""

hra_bezi = True
while hra_bezi:
    # A. Event handeling / Spracovanie vstupov
    for event in pygame.event.get(): # Prechádzame každú udalosť
        if event.type == pygame.QUIT: # Ak zavrieme okno
            hra_bezi = False
    
    # B. Vykreslovanie
    obrazovka.fill((67, 67, 67))
    
    # C. Update dispaly / Vykreslia sa zmeny na obrazovku
    pygame.display.flip()
    
    # D. FPS - iba jej dáme fps
    clock.tick(60)

"""
3. UKONČENIE -------------------------------
"""

pygame.quit()
sys.exit()