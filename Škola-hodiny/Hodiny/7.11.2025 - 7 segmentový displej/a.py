import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(win, width=1000, height=600, background = "white")
canvas.pack()

class Segment:
    def __init__(self, x, y, a, b, farba, canvas):     #konštruktor, 
        self.canvas = canvas
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.farba = farba
    
    def kresli(self):
        self.id = self.canvas.create_rectangle(
                    self.x, self.y,
                    self.x + self.a, self.y + self.b,
                    fill = self.farba,
                    state="hidden" # Start hidden
                    )
    
    def on(self):
        self.canvas.itemconfig(self.id, state = "normal")
    def off(self):
        self.canvas.itemconfig(self.id, state = "hidden")

class Cislica:
    def __init__(self, x, y, vs, ms, farba, canvas):
        self.parts = []
        # Poriadie segmentov: 0:top, 1:upper-right, 2:upper-left, 3:middle, 4:lower-right, 5:lower-left, 6:bottom
        self.parts.append(Segment(x + ms, y, vs, ms, farba, canvas))
        self.parts.append(Segment(x + ms + vs, y + ms, ms, vs, farba, canvas))
        self.parts.append(Segment(x, y + ms, ms, vs, farba, canvas))
        self.parts.append(Segment(x + ms, y + ms + vs, vs, ms, farba, canvas))
        self.parts.append(Segment(x + ms + vs, y + 2*ms + vs, ms, vs, farba, canvas))
        self.parts.append(Segment(x, y + 2*ms + vs, ms, vs, farba, canvas))
        self.parts.append(Segment(x + ms, y + 2*ms + 2*vs, vs, ms, farba, canvas))
        
        for part in self.parts:
            part.kresli()

    def all_on(self):
        for part in self.parts:
            part.on()
    
    def all_off(self):
        for part in self.parts:
            part.off()
    
    def zobraz(self, cislo):
        self.all_off()
        segment_map = {
            0: [0, 1, 2, 4, 5, 6],
            1: [1, 4],
            2: [0, 1, 3, 5, 6],
            3: [0, 1, 3, 4, 6],
            4: [2, 3, 1, 4],
            5: [0, 2, 3, 4, 6],
            6: [0, 2, 3, 4, 5, 6],
            7: [0, 1, 4],
            8: [0, 1, 2, 3, 4, 5, 6],
            9: [0, 1, 2, 3, 4, 6]
        }
        if cislo in segment_map:
            for index in segment_map[cislo]:
                self.parts[index].on()

# Vytvorenie a zobrazenie číslice 8
s1 = Cislica(100, 100, 100, 20, "blue", canvas)
s1.zobraz(1)

win.mainloop()
