import datetime
import tkinter as tk

# --- KONFIGURÁCIA VZHĽADU ---
OKNO_SIRKA = 1000
OKNO_VYSKA = 800

CISLICA_SIRKA = 80
CISLICA_VYSKA = 140
HRUBKA_SEGMENTU = 20
MEDZERA_SEGMENTU = 5

MEDZERA_MEDZI_CISLICAMI = 50
MEDZERA_PRE_DVOJBODKU = 40

FARBA_POZADIA = "black"
FARBA_SEGMENTU_ZAPNUTY = "#ff3333"
FARBA_SEGMENTU_VYPNUTY = "#1a0000" # Veľmi tmavá červená

class Cislo:
    def __init__(self, canvas, x: int, y: int) -> None:
        self.canvas = canvas
        self.x = x
        self.y = y
        skosenie = HRUBKA_SEGMENTU / 2
        
        self.segmenty_body = [
            # 0 (Horný) - No shift
            [
                self.x + skosenie + MEDZERA_SEGMENTU, self.y,
                self.x + CISLICA_SIRKA - skosenie - MEDZERA_SEGMENTU, self.y,
                self.x + CISLICA_SIRKA - MEDZERA_SEGMENTU, self.y + skosenie,
                self.x + CISLICA_SIRKA - skosenie - MEDZERA_SEGMENTU, self.y + HRUBKA_SEGMENTU,
                self.x + skosenie + MEDZERA_SEGMENTU, self.y + HRUBKA_SEGMENTU,
                self.x + MEDZERA_SEGMENTU, self.y + skosenie
            ],
            # 1 (Horný pravý) - x+10, y+10
            [
                self.x + CISLICA_SIRKA - HRUBKA_SEGMENTU + 10, self.y + skosenie + MEDZERA_SEGMENTU + 10,
                self.x + CISLICA_SIRKA - skosenie + 10, self.y + MEDZERA_SEGMENTU + 10,
                self.x + CISLICA_SIRKA + 10, self.y + skosenie + MEDZERA_SEGMENTU + 10,
                self.x + CISLICA_SIRKA + 10, self.y + CISLICA_VYSKA / 2 - skosenie - MEDZERA_SEGMENTU + 10,
                self.x + CISLICA_SIRKA - skosenie + 10, self.y + CISLICA_VYSKA / 2 - MEDZERA_SEGMENTU + 10,
                self.x + CISLICA_SIRKA - HRUBKA_SEGMENTU + 10, self.y + CISLICA_VYSKA / 2 - skosenie - MEDZERA_SEGMENTU + 10
            ],
            # 2 (Dolný pravý) - x+10, y+20
            [
                self.x + CISLICA_SIRKA - HRUBKA_SEGMENTU + 10, self.y + CISLICA_VYSKA / 2 + skosenie + MEDZERA_SEGMENTU + 20,
                self.x + CISLICA_SIRKA - skosenie + 10, self.y + CISLICA_VYSKA / 2 + MEDZERA_SEGMENTU + 20,
                self.x + CISLICA_SIRKA + 10, self.y + CISLICA_VYSKA / 2 + skosenie + MEDZERA_SEGMENTU + 20,
                self.x + CISLICA_SIRKA + 10, self.y + CISLICA_VYSKA - skosenie - MEDZERA_SEGMENTU + 20,
                self.x + CISLICA_SIRKA - skosenie + 10, self.y + CISLICA_VYSKA - MEDZERA_SEGMENTU + 20,
                self.x + CISLICA_SIRKA - HRUBKA_SEGMENTU + 10, self.y + CISLICA_VYSKA - skosenie - MEDZERA_SEGMENTU + 20
            ],
            # 3 (Dolný) - y+30
            [
                self.x + skosenie + MEDZERA_SEGMENTU, self.y + CISLICA_VYSKA - HRUBKA_SEGMENTU + 30,
                self.x + CISLICA_SIRKA - skosenie - MEDZERA_SEGMENTU, self.y + CISLICA_VYSKA - HRUBKA_SEGMENTU + 30,
                self.x + CISLICA_SIRKA - MEDZERA_SEGMENTU, self.y + CISLICA_VYSKA - skosenie + 30,
                self.x + CISLICA_SIRKA - skosenie - MEDZERA_SEGMENTU, self.y + CISLICA_VYSKA + 30,
                self.x + skosenie + MEDZERA_SEGMENTU, self.y + CISLICA_VYSKA + 30,
                self.x + MEDZERA_SEGMENTU, self.y + CISLICA_VYSKA - skosenie + 30
            ],
            # 4 (Dolný ľavý) - x-10, y+20
            [
                self.x + HRUBKA_SEGMENTU - 10, self.y + CISLICA_VYSKA / 2 + skosenie + MEDZERA_SEGMENTU + 20,
                self.x + skosenie - 10, self.y + CISLICA_VYSKA / 2 + MEDZERA_SEGMENTU + 20,
                self.x - 10, self.y + CISLICA_VYSKA / 2 + skosenie + MEDZERA_SEGMENTU + 20,
                self.x - 10, self.y + CISLICA_VYSKA - skosenie - MEDZERA_SEGMENTU + 20,
                self.x + skosenie - 10, self.y + CISLICA_VYSKA - MEDZERA_SEGMENTU + 20,
                self.x + HRUBKA_SEGMENTU - 10, self.y + CISLICA_VYSKA - skosenie - MEDZERA_SEGMENTU + 20
            ],
            # 5 (Horný ľavý) - x-10, y+10
            [
                self.x + HRUBKA_SEGMENTU - 10, self.y + skosenie + MEDZERA_SEGMENTU + 10,
                self.x + skosenie - 10, self.y + MEDZERA_SEGMENTU + 10,
                self.x - 10, self.y + skosenie + MEDZERA_SEGMENTU + 10,
                self.x - 10, self.y + CISLICA_VYSKA / 2 - skosenie - MEDZERA_SEGMENTU + 10,
                self.x + skosenie - 10, self.y + CISLICA_VYSKA / 2 - MEDZERA_SEGMENTU + 10,
                self.x + HRUBKA_SEGMENTU - 10, self.y + CISLICA_VYSKA / 2 - skosenie - MEDZERA_SEGMENTU + 10
            ],
            # 6 (Stredný) - y+15
            [
                self.x + skosenie + MEDZERA_SEGMENTU, self.y + CISLICA_VYSKA / 2 - skosenie + 15,
                self.x + CISLICA_SIRKA - skosenie - MEDZERA_SEGMENTU, self.y + CISLICA_VYSKA / 2 - skosenie + 15,
                self.x + CISLICA_SIRKA - MEDZERA_SEGMENTU, self.y + CISLICA_VYSKA / 2 + 15,
                self.x + CISLICA_SIRKA - skosenie - MEDZERA_SEGMENTU, self.y + CISLICA_VYSKA / 2 + skosenie + 15,
                self.x + skosenie + MEDZERA_SEGMENTU, self.y + CISLICA_VYSKA / 2 + skosenie + 15,
                self.x + MEDZERA_SEGMENTU, self.y + CISLICA_VYSKA / 2 + 15
            ]
        ]
        
        self.mapa_segmentov = {
            #      0,     1,     2,     3,     4,     5,     6
            0: (True,  True,  True,  True,  True,  True,  False), # 0
            1: (False, True,  True,  False, False, False, False), # 1
            2: (True,  True,  False, True,  True,  False, True),  # 2
            3: (True,  True,  True,  True,  False, False, True),  # 3
            4: (False, True,  True,  False, False, True,  True),  # 4
            5: (True,  False, True,  True,  False, True,  True),  # 5
            6: (True,  False, True,  True,  True,  True,  True),  # 6
            7: (True,  True,  True,  False, False, False, False), # 7
            8: (True,  True,  True,  True,  True,  True,  True),  # 8
            9: (True,  True,  True,  True,  False, True,  True),  # 9
        }
        
        self.zoznam_id = []
        
        for segment_body in self.segmenty_body:
            id = self.canvas.create_polygon(
                segment_body,
                fill=FARBA_SEGMENTU_ZAPNUTY
            )
            self.zoznam_id.append(id)
    
    def zobrazovat(self, cislo: int):
        for index, state in enumerate(self.mapa_segmentov[cislo]):
            if state:
                self.on(index)
            else:
                self.off(index)
    
    def on(self, index: int):
        self.canvas.itemconfig(self.zoznam_id[index], fill = FARBA_SEGMENTU_ZAPNUTY)
    
    def off(self, index: int):
        self.canvas.itemconfig(self.zoznam_id[index], fill = FARBA_SEGMENTU_VYPNUTY)

class Dvojbodka:
    def __init__(self,canvas, x: int, y: int) -> None:
        self.canvas = canvas
        self.state = True
        self.id1 = self.canvas.create_rectangle(
            x, y,
            x + 25, y + 25,
            fill = FARBA_SEGMENTU_ZAPNUTY,
            outline = FARBA_SEGMENTU_ZAPNUTY
        )
        
        self.id2 = canvas.create_rectangle(
            x, y + 50,
            x + 25, y + 75,
            fill = FARBA_SEGMENTU_ZAPNUTY,
            outline = FARBA_SEGMENTU_ZAPNUTY
        )
        
        self.prepinanie()
    def prepinanie(self):
        if self.state:
            canvas.itemconfig(
                self.id1,
                fill = FARBA_SEGMENTU_VYPNUTY,
                outline = FARBA_SEGMENTU_VYPNUTY
            )
            canvas.itemconfig(
                self.id2,
                fill = FARBA_SEGMENTU_VYPNUTY,
                outline = FARBA_SEGMENTU_VYPNUTY
            )
            self.state = False 
        else:
            canvas.itemconfig(
                self.id1,
                fill = FARBA_SEGMENTU_ZAPNUTY,
                outline = FARBA_SEGMENTU_ZAPNUTY
            )
            canvas.itemconfig(
                self.id2,
                fill = FARBA_SEGMENTU_ZAPNUTY,
                outline = FARBA_SEGMENTU_ZAPNUTY
            )
            self.state = True 
        

class Hodiny:
    def __init__(self, x: int, y: int) -> None:
        self.cislo1 = Cislo(canvas, x + 20, y + 20)
        self.cislo2 = Cislo(canvas, x + 145, y + 20)
        self.dvojbodka1 = Dvojbodka(canvas, x + 285, y + 70)
        self.cislo3 = Cislo(canvas, x + 370, y + 20)
        self.cislo4 = Cislo(canvas, x + 495, y + 20)
        self.dvojbodka2 = Dvojbodka(canvas, x + 635, y + 70)
        self.cislo5 = Cislo(canvas, x + 710, y + 20)
        self.cislo6 = Cislo(canvas, x + 835, y + 20)
        
    def update(self):
        self.hodina1 = datetime.datetime.now().hour // 10
        self.hodina2 = datetime.datetime.now().hour % 10
        self.minuta1 = datetime.datetime.now().minute // 10
        self.minuta2 = datetime.datetime.now().minute % 10
        self.sekunda1 = datetime.datetime.now().second // 10
        self.sekunda2 = datetime.datetime.now().second % 10
        
        self.cislo1.zobrazovat(self.hodina1)
        self.cislo2.zobrazovat(self.hodina2)
        self.dvojbodka1.prepinanie()
        self.cislo3.zobrazovat(self.minuta1)
        self.cislo4.zobrazovat(self.minuta2)
        self.dvojbodka2.prepinanie()
        self.cislo5.zobrazovat(self.sekunda1)
        self.cislo6.zobrazovat(self.sekunda2)
        win.after(1000, self.update)

# --- KONFIGURÁCIA OKNA ---
win = tk.Tk()
win.title("Digitálne hodiny")
canvas = tk.Canvas(
    win,
    width = OKNO_SIRKA,
    height= OKNO_VYSKA,
    background = FARBA_POZADIA
    )
canvas.pack()

hodiny1 = Hodiny(0, 0)
hodiny1.update()

hodiny2 = Hodiny(0, 200)
hodiny2.update()

win.mainloop()