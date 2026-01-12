# HLAVNÁ HERNÁ SLUČKA #
import pygame

# Importy
from config import SIRKA_OKNA, VYSKA_OKNA, VELKOST_UNITU, MEDZERA, INTERVAL, FPS
from units import Warrior, Knight, Defender, Vampire, Army, UNIT_PRICES
from battle_logika import fight1v1
from assets_loader import init_assets
from ui import draw_menu, draw_level_select, draw_army_build, draw_health_bar, draw_battle_result
from levels import LEVELS


def run():
    pygame.init()
    
    screen: Surface = pygame.display.set_mode((SIRKA_OKNA, VYSKA_OKNA))
    pygame.display.set_caption("Kartová hra")
    
    # Načítanie assetov
    units_me, units_enemy, sound_attack, sound_death, death_channel = init_assets()
    
    # Vytvorenie armád
    moja_armada = Army()
    moja_armada.add_units(Warrior, 1)
    moja_armada.add_units(Knight, 1)
    moja_armada.add_units(Defender, 1)
    moja_armada.add_units(Vampire, 1)
    
    nepriatel = Army()
    nepriatel.add_units(Warrior, 1)
    nepriatel.add_units(Knight, 2)
    
    # Bojová logika
    bitka: Generator = fight1v1(moja_armada.warriors[0], nepriatel.warriors[0])
    
    def bijemsa():
        """Vykoná jeden krok boja."""
        nonlocal bitka, game_status
        try:
            frame: dict = next(bitka)
            
            sound_attack.play()
            
            if not frame["defender_alive"]:
                death_channel.play(sound_death)
                
                if frame["defender"] in moja_armada.warriors:
                    moja_armada.warriors.remove(frame['defender'])
                elif frame["defender"] in nepriatel.warriors:
                    nepriatel.warriors.remove(frame['defender'])
                
                # Skontroluj či boj skončil
                if len(moja_armada.warriors) == 0:
                    game_status = "prehra"
                    return
                elif len(nepriatel.warriors) == 0:
                    game_status = "vyhra"
                    return
        
        except StopIteration:
            # Generátor skončil, začni nový boj ak sú ešte bojovníci
            if len(moja_armada.warriors) > 0 and len(nepriatel.warriors) > 0:
                bitka = fight1v1(moja_armada.warriors[0], nepriatel.warriors[0])
    
    # Herné premenné
    running: bool = True
    clock = pygame.time.Clock()
    last_action_time: int = 0
    game_status: str = "menu" # menu, level_select, army_build, battle, vyhra, prehra
    # Inicializácia tlačidiel (zatiaľ None, naplnia sa pri vykresľovaní), na dlho vysvetľovania
    tlacidlo_start = None
    tlacidlo_level_1 = None
    tlacidlo_level_2 = None
    tlacidlo_level_3 = None
    tlacidlo_level_4 = None
    spat_do_menu = None
    vybrany_level: int | None = None
    spat_do_level_menu = None
    tlacidlo_do_boja = None
    tlacidla_plus = {}
    tlacidla_minus = {}
    tlacidlo_spat_vysledok = None
    
    # Army builder premenné
    peniaze = 0
    armada_pocty = {Warrior: 0, Knight: 0, Defender: 0, Vampire: 0}
    
    # Hlavná herná slučka
    while running:
        # Spracovanie udalostí
        # Kliknutie X na zatvorenie okna
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Kliknutie na tlačidlo
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Menu
                if game_status == "menu" and tlacidlo_start is not None and tlacidlo_start.collidepoint(event.pos):
                    game_status = "level_select"
                
                # Level select tlačidlá
                elif game_status == "level_select":
                    if tlacidlo_level_1 is not None and tlacidlo_level_1.collidepoint(event.pos):
                        vybrany_level = 1
                        peniaze = LEVELS[1]["peniaze"]
                        armada_pocty = {Warrior: 0, Knight: 0, Defender: 0, Vampire: 0}
                        game_status = "army_build"
                    elif tlacidlo_level_2 is not None and tlacidlo_level_2.collidepoint(event.pos):
                        vybrany_level = 2
                        peniaze = LEVELS[2]["peniaze"]
                        armada_pocty = {Warrior: 0, Knight: 0, Defender: 0, Vampire: 0}
                        game_status = "army_build"
                    elif tlacidlo_level_3 is not None and tlacidlo_level_3.collidepoint(event.pos):
                        vybrany_level = 3
                        peniaze = LEVELS[3]["peniaze"]
                        armada_pocty = {Warrior: 0, Knight: 0, Defender: 0, Vampire: 0}
                        game_status = "army_build"
                    elif tlacidlo_level_4 is not None and tlacidlo_level_4.collidepoint(event.pos):
                        vybrany_level = 4
                        peniaze = LEVELS[4]["peniaze"]
                        armada_pocty = {Warrior: 0, Knight: 0, Defender: 0, Vampire: 0}
                        game_status = "army_build"
                    elif spat_do_menu is not None and spat_do_menu.collidepoint(event.pos):
                        game_status = "menu"
                
                # Army build tlačidlá
                elif game_status == "army_build":
                    # Späť
                    if spat_do_level_menu is not None and spat_do_level_menu.collidepoint(event.pos):
                        game_status = "level_select"
                    
                    # DO BOJA
                    elif tlacidlo_do_boja is not None and tlacidlo_do_boja.collidepoint(event.pos):
                        # Skontroluj či má aspoň jednu jednotku
                        if sum(armada_pocty.values()) > 0:
                            # Vytvor hráčovu armádu
                            moja_armada = Army()
                            for unit_type, count in armada_pocty.items():
                                moja_armada.add_units(unit_type, count)
                            
                            # Vytvor nepriateľskú armádu z levelu
                            nepriatel = Army()
                            for unit_name, count in LEVELS[vybrany_level]["nepriatel"]:
                                unit_class = {"Warrior": Warrior, "Knight": Knight, "Defender": Defender, "Vampire": Vampire}[unit_name]
                                nepriatel.add_units(unit_class, count)
                            
                            # Spusti boj
                            bitka = fight1v1(moja_armada.warriors[0], nepriatel.warriors[0])
                            game_status = "battle"
                    
                    # Tlačidlá + (pridaj jednotku)
                    else:
                        for unit_type, btn in tlacidla_plus.items():
                            if btn is not None and btn.collidepoint(event.pos):
                                cena = UNIT_PRICES[unit_type]
                                if peniaze >= cena:
                                    peniaze -= cena
                                    armada_pocty[unit_type] += 1
                                break
                        
                        # Tlačidlá - (odober jednotku)
                        for unit_type, btn in tlacidla_minus.items():
                            if btn is not None and btn.collidepoint(event.pos):
                                if armada_pocty[unit_type] > 0:
                                    cena = UNIT_PRICES[unit_type]
                                    peniaze += cena
                                    armada_pocty[unit_type] -= 1
                                break
                
                # Výsledok boja - tlačidlo späť
                elif game_status in ("vyhra", "prehra"):
                    if tlacidlo_spat_vysledok is not None and tlacidlo_spat_vysledok.collidepoint(event.pos):
                        game_status = "level_select"
        
        # Výber obrazovky, aká časť hry
        if game_status == "menu":
            tlacidlo_start = draw_menu(screen)
            
        elif game_status == "level_select":
            tlacidlo_level_1, tlacidlo_level_2, tlacidlo_level_3, tlacidlo_level_4, spat_do_menu = draw_level_select(screen)
            
        elif game_status == "army_build":
            spat_do_level_menu, tlacidlo_do_boja, tlacidla_plus, tlacidla_minus = draw_army_build(screen, vybrany_level, peniaze, armada_pocty)
            
        elif game_status == "battle":
            
            # Nastavenie farby obrazovky
            screen.fill((240, 240, 240))
        
            # Bojová logika s časovačom
            current_time = pygame.time.get_ticks()
            if current_time - last_action_time > INTERVAL:
                if len(moja_armada.warriors) != 0 and len(nepriatel.warriors) != 0:
                    bijemsa()
                    last_action_time = current_time
            
            # Vykreslenie mojej armády
            for unit in moja_armada.warriors:
                index_unitu = moja_armada.warriors.index(unit)
                x = 0
                y = index_unitu * (VELKOST_UNITU + MEDZERA)
                
                screen.blit(units_me[type(unit)], (x, y))
                draw_health_bar(screen, x, y - 12, unit.health, type(unit))
            
            # Vykreslenie nepriateľskej armády
            for unit in nepriatel.warriors:
                index_unitu = nepriatel.warriors.index(unit)
                x = SIRKA_OKNA - VELKOST_UNITU
                y = index_unitu * (VELKOST_UNITU + MEDZERA)
                
                screen.blit(units_enemy[type(unit)], (x, y))
                draw_health_bar(screen, x, y - 12, unit.health, type(unit))
        
        elif game_status == "vyhra":
            tlacidlo_spat_vysledok = draw_battle_result(screen, vyhral=True)
        
        elif game_status == "prehra":
            tlacidlo_spat_vysledok = draw_battle_result(screen, vyhral=False)
        
        # Aktualizácia obrazovky
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()


# Ak je spustený priamo (nie cez main.py)
if __name__ == "__main__":
    run()