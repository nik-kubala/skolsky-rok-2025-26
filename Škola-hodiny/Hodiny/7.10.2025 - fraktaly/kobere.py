import tkinter as tk
obrazok = tk.Tk()
canvas = tk.Canvas(obrazok, width = 800, height = 800, bg = "white")
canvas.pack()

def koberec(x, y, d):
    p1 = (x, y)
    p2 = (x + d, y - d) 
    
    canvas.create_rectangle(p1, p2, outline = "black")
    if d > 3:   
        koberec(x, y, d / 3)
        koberec(x + d / 3, y, d / 3)
        koberec(x + 2 * (d / 3), y, d / 3)
        koberec(x, y - d / 3, d / 3)
        koberec(x + 2 * (d / 3), y - d / 3, d / 3)
        koberec(x, y - 2 * (d / 3), d / 3)
        koberec(x + d / 3, y - 2 * (d / 3), d / 3)
        koberec(x + 2 * (d / 3), y - 2 * (d / 3), d / 3)

koberec(0, 800, 800)

obrazok.mainloop()