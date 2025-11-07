import tkinter as tk
import random as rd

def yes(event):
    global hadane_slovo
    global vybrane_slovo
    stlacene_pismenko = event.char
    print("stlačil som")
    if stlacene_pismenko in vybrane_slovo:
        pozicia = vybrane_slovo.find(stlacene_pismenko)
        hadane_slovo = hadane_slovo[:pozicia:] + stlacene_pismenko + hadane_slovo[pozicia + 1:]
        vybrane_slovo = vybrane_slovo[:pozicia] + "*" + vybrane_slovo[pozicia + 1:]
        canvas.itemconfig(sprite, text = hadane_slovo)

def padanie():
    global pos_y
    canvas.move(sprite, 0, pos_y)
    
    if canvas.coords(sprite)[1] > 950:
        canvas.create_text(
            width / 2, 500,
            text="Prehral si!", 
            font=("Arial", 50, "bold"),
            fill="red"
        )
    else:
        canvas.after(1000, padanie)
        if "*" not in hadane_slovo:
            canvas.create_text(
            width / 2, 500,
            text="Vyhral si!", 
            font=("Arial", 50, "bold"),
            fill="green"
        )

width = 600
pos_y = 10
win = tk.Tk()
win.title("Padajúca hra")
canvas = tk.Canvas(win, width = width, height = 1000, bg = "white")
canvas.pack()

zoznam_slov = ["beder", "danodrevo", "majo", "jano", "cernica"]

vybrane_slovo = rd.choice(zoznam_slov)
hadane_slovo = "*" * len(vybrane_slovo)
sprite = canvas.create_text(rd.randrange(0, width), pos_y, text = hadane_slovo, fill = "black")
padanie()
win.bind("<Key>", yes)

win.mainloop()