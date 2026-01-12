# UI FUNKCIE / VYKRESĽOVANIE HEALTH BAROV A ĎALŠÍCH PRVKOV #
import pygame
from config import SIRKA_OKNA, VYSKA_OKNA, VELKOST_UNITU, MEDZERA
from units import Warrior, Knight, Defender, Vampire, UNIT_PRICES
from levels import LEVELS

def draw_menu(screen):
    """Vykreslí hlavné menu."""
    screen.fill((255, 255, 255))
    
    font_nadpis = pygame.font.SysFont("Helvetica", 70)
    nadpis = font_nadpis.render("Menu", True, (67, 67, 67))
    screen.blit(nadpis, (
        SIRKA_OKNA // 2 - nadpis.get_width() // 2,
        VYSKA_OKNA // 3 - nadpis.get_height() // 3
    ))
    
    tlacidlo_start = pygame.Rect(
        SIRKA_OKNA // 2 - 100,
        VYSKA_OKNA // 2,
        200, 50)
    pygame.draw.rect(screen, (0, 200, 0), tlacidlo_start, border_radius=8)
    
    font_tlacidla = pygame.font.SysFont("Helvetica", 35)
    text_tlacidla = font_tlacidla.render("ŠTART", True, (255, 255, 255))
    screen.blit(text_tlacidla, (
        tlacidlo_start.centerx - text_tlacidla.get_width() // 2,
        tlacidlo_start.centery - text_tlacidla.get_height() // 2
    ))
    
    return tlacidlo_start

def draw_level_select(screen):
    """Vykreslí menu výberu levelov."""
    screen.fill((255, 255, 255))
    
    font_title = pygame.font.SysFont("Helvetica", 70)
    title = font_title.render("VÝBER LEVELU", True, (67, 67, 67))
    screen.blit(title, (
        SIRKA_OKNA // 2 - title.get_width() // 2,
        VYSKA_OKNA // 5 - title.get_height() // 5
    ))
    
    spat_do_menu = pygame.Rect(10, VYSKA_OKNA - 50, 120, 40)
    pygame.draw.rect(screen, (100, 100, 100), spat_do_menu, border_radius=5)
    font_btn = pygame.font.SysFont("Helvetica", 25)
    spat_text = font_btn.render("<- Späť", True, (255, 255, 255))
    screen.blit(spat_text, (
        spat_do_menu.centerx - spat_text.get_width() // 2,
        spat_do_menu.centery - spat_text.get_height() // 2
    ))
    
    tlacidlo_level_1 = draw_level_button(screen, 1)
    tlacidlo_level_2 = draw_level_button(screen, 2)
    tlacidlo_level_3 = draw_level_button(screen, 3)
    tlacidlo_level_4 = draw_level_button(screen, 4)
    
    return tlacidlo_level_1, tlacidlo_level_2, tlacidlo_level_3, tlacidlo_level_4, spat_do_menu 

def draw_army_build(screen, level: int, peniaze: int, armada_pocty: dict):
    """Vykreslí obrazovku zostavovania armády."""
    screen.fill((240, 240, 240))
    
    font_nadpis = pygame.font.SysFont("Helvetica", 70)
    nadpis = font_nadpis.render("ZOSTAVOVANIE ARMÁDY", True, (67, 67, 67))
    screen.blit(nadpis, (
        SIRKA_OKNA // 2 - nadpis.get_width() // 2,
        30
    ))
    
    font_level = pygame.font.SysFont("Helvetica", 30)
    text_level = font_level.render(f"Level {level}: {LEVELS[level]['nazov']}", True, (100, 100, 100))
    screen.blit(text_level, (
        SIRKA_OKNA // 2 - text_level.get_width() // 2,
        110
    ))
    
    font_peniaze = pygame.font.SysFont("Helvetica", 35)
    farba_penazi = (0, 150, 0) if peniaze > 0 else (200, 0, 0)
    text_peniaze = font_peniaze.render(f"Peniaze: {peniaze}", True, farba_penazi)
    screen.blit(text_peniaze, (
        SIRKA_OKNA // 2 - text_peniaze.get_width() // 2,
        150
    ))
    
    spat_do_level_menu = pygame.Rect(10, VYSKA_OKNA - 50, 120, 40)
    pygame.draw.rect(screen, (100, 100, 100), spat_do_level_menu, border_radius=5)
    font_spat = pygame.font.SysFont("Helvetica", 25)
    text_spat = font_spat.render("<- Späť", True, (255, 255, 255))
    screen.blit(text_spat, (
        spat_do_level_menu.centerx - text_spat.get_width() // 2,
        spat_do_level_menu.centery - text_spat.get_height() // 2
    ))
    
    zoznam_jednotiek = [Warrior, Knight, Defender, Vampire]
    tlacidla_plus = {}
    tlacidla_minus = {}
    
    zaciatok_y = 200
    vyska_riadku = 70
    
    for index, typ_jednotky in enumerate(zoznam_jednotiek):
        pozicia_y = zaciatok_y + index * vyska_riadku
        cena_jednotky = UNIT_PRICES[typ_jednotky]
        pocet_jednotiek = armada_pocty.get(typ_jednotky, 0)
        
        # Tlačidlo mínus (-)
        tlacidlo_minus = pygame.Rect(150, pozicia_y, 50, 50)
        farba_minus = (200, 50, 50) if pocet_jednotiek > 0 else (180, 180, 180)
        pygame.draw.rect(screen, farba_minus, tlacidlo_minus, border_radius=5)
        text_minus = font_peniaze.render("-", True, (255, 255, 255))
        screen.blit(text_minus, (
            tlacidlo_minus.centerx - text_minus.get_width() // 2,
            tlacidlo_minus.centery - text_minus.get_height() // 2
        ))
        tlacidla_minus[typ_jednotky] = tlacidlo_minus
        
        text_pocet = font_peniaze.render(str(pocet_jednotiek), True, (50, 50, 50))
        screen.blit(text_pocet, (220, pozicia_y + 10))
        
        # Tlačidlo plus (+)
        tlacidlo_plus = pygame.Rect(270, pozicia_y, 50, 50)
        farba_plus = (50, 200, 50) if peniaze >= cena_jednotky else (180, 180, 180)
        pygame.draw.rect(screen, farba_plus, tlacidlo_plus, border_radius=5)
        text_plus = font_peniaze.render("+", True, (255, 255, 255))
        screen.blit(text_plus, (
            tlacidlo_plus.centerx - text_plus.get_width() // 2,
            tlacidlo_plus.centery - text_plus.get_height() // 2
        ))
        tlacidla_plus[typ_jednotky] = tlacidlo_plus
        
        font_nazov = pygame.font.SysFont("Helvetica", 30)
        text_nazov = font_nazov.render(typ_jednotky.__name__, True, (50, 50, 50))
        screen.blit(text_nazov, (350, pozicia_y + 10))
        
        text_cena = font_nazov.render(f"({cena_jednotky} evro)", True, (100, 100, 100))
        screen.blit(text_cena, (500, pozicia_y + 10))
    
    celkovy_pocet = sum(armada_pocty.get(jednotka, 0) for jednotka in zoznam_jednotiek)
    
    tlacidlo_do_boja = pygame.Rect(SIRKA_OKNA // 2 - 100, 620, 200, 60)
    farba_do_boja = (0, 200, 0) if celkovy_pocet > 0 else (150, 150, 150)
    pygame.draw.rect(screen, farba_do_boja, tlacidlo_do_boja, border_radius=8)
    font_do_boja = pygame.font.SysFont("Helvetica", 35)
    text_do_boja = font_do_boja.render("DO BOJA!", True, (255, 255, 255))
    screen.blit(text_do_boja, (
        tlacidlo_do_boja.centerx - text_do_boja.get_width() // 2,
        tlacidlo_do_boja.centery - text_do_boja.get_height() // 2
    ))
    
    return spat_do_level_menu, tlacidlo_do_boja, tlacidla_plus, tlacidla_minus

MAX_HEALTH = {
    Warrior: 50,
    Knight: 50,
    Defender: 60,
    Vampire: 40
}


def draw_health_bar(surface, x, y, current_hp, unit_type):
    """Vykreslí health bar pod jednotkou."""
    max_hp = MAX_HEALTH.get(unit_type, 50)
    ratio = max(0, min(1, current_hp / max_hp))
    
    bar_width: int = VELKOST_UNITU
    bar_height: int = 10
    bar_y: int = y + VELKOST_UNITU + MEDZERA
    
    pygame.draw.rect(surface, (255, 0, 0), (x, bar_y, bar_width, bar_height))
    pygame.draw.rect(surface, (0, 255, 0), (x, bar_y, bar_width * ratio, bar_height))
    pygame.draw.rect(surface, (0, 0, 0), (x, bar_y, bar_width, bar_height), 1)


def draw_button(surface, rect, is_active):
    """Vykreslí tlačidlo (zelené ak aktívne, červené ak nie)."""
    color: tuple[int, int, int] = (0, 255, 0) if is_active else (255, 0, 0)
    pygame.draw.rect(surface, color, rect)

def draw_level_button(screen, cislo_levelu: int):
    """Vykreslí tlačidlo pre výber levelu."""
    tlacidlo_level_x = pygame.Rect(
        SIRKA_OKNA // 2 - 100,
        VYSKA_OKNA // 3 + (60 * (cislo_levelu - 1)),
        200, 50)
    pygame.draw.rect(screen, (0, 200, 0), tlacidlo_level_x, border_radius=8)
    
    font_of_button = pygame.font.SysFont("Helvetica", 35)
    button_text = font_of_button.render(f"Level {cislo_levelu}", True, (255, 255, 255))
    screen.blit(button_text, (
        tlacidlo_level_x.centerx - button_text.get_width() // 2,
        tlacidlo_level_x.centery - button_text.get_height() // 2
    ))
    
    return tlacidlo_level_x


def draw_battle_result(screen, vyhral: bool):
    """Vykreslí obrazovku s výsledkom boja."""
    screen.fill((240, 240, 240))
    
    # Nadpis podľa výsledku
    font_nadpis = pygame.font.SysFont("Helvetica", 80)
    if vyhral:
        text = "VYHRAL SI!"
        farba = (0, 180, 0)
    else:
        text = "PREHRAL SI"
        farba = (200, 0, 0)
    
    nadpis = font_nadpis.render(text, True, farba)
    screen.blit(nadpis, (
        SIRKA_OKNA // 2 - nadpis.get_width() // 2,
        VYSKA_OKNA // 3
    ))
    
    # Tlačidlo späť
    tlacidlo_spat = pygame.Rect(SIRKA_OKNA // 2 - 100, VYSKA_OKNA // 2 + 50, 200, 50)
    pygame.draw.rect(screen, (100, 100, 100), tlacidlo_spat, border_radius=8)
    
    font_btn = pygame.font.SysFont("Helvetica", 35)
    text_btn = font_btn.render("<- Späť", True, (255, 255, 255))
    screen.blit(text_btn, (
        tlacidlo_spat.centerx - text_btn.get_width() // 2,
        tlacidlo_spat.centery - text_btn.get_height() // 2
    ))
    
    return tlacidlo_spat