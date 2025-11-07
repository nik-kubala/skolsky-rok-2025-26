import tkinter as tk
import random as rd

def yes(event):
    global hadane_slovo
    global vybrane_slovo
    stlacene_pismenko = event.char
    print("stlačil som")
    if stlacene_pismenko in vybrane_slovo:
        pozicia = vybrane_slovo.find(stlacene_pismenko)
        hadane_slovo = stlacene_pismenko
        canvas.itemconfig(sprite, text = hadane_slovo)

def padanie():
    global pos_y
    canvas.move(sprite, 0, pos_y)
    canvas.move(elipsa, 0, pos_y)
    
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

zoznam_slov = ["a", "b", "c"]
vybrane_slovo = rd.choice(zoznam_slov)
hadane_slovo = "*"
nahodna_pozicia = rd.randrange(0, width)
sprite = canvas.create_text(nahodna_pozicia - 25, pos_y - 25, text = hadane_slovo, fill = "black")
elipsa = canvas.create_oval(nahodna_pozicia - 50, pos_y - 50, nahodna_pozicia, pos_y, outline = "black")
padanie()
win.bind("<Key>", yes)

win.mainloop()