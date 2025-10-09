import tkinter as tk
obrazok = tk.Tk()
canvas = tk.Canvas(obrazok, width = 1000, height = 1000, bg = "white")
canvas.pack()

def trojuholnik(x, y, d):
    p1 = (x, y)
    p2 = (x + d, y)
    p3 = (x + d / 2, y -  (3 ** 0.5) * d / 2)   
    
    canvas.create_polygon(p1, p2, p3, outline = "black")  
    if d > 2:   
        
        trojuholnik(x, y, d / 2)
        trojuholnik(x + d / 2, y, d / 2)
        trojuholnik(x + d / 4, y - (3 ** 0.5) * d / 4, d / 2)

trojuholnik(0, 800, 800)

obrazok.mainloop()