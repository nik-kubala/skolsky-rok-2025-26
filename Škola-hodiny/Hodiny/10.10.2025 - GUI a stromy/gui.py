#systemovo riadene udalosti
#veci ako gombik slider platno... sa volaju komponent alebo widget
#objekty ktore nakreslis na kanvas budu mat pridelene vlastne idcka  dokazes ich menit
#canvas je interaktivny, dokaze reagovat na udalosti co robi uzivatel
import tkinter as tk
win = tk.Tk()
win.title("Moje prvé okienko")
canvas = tk.Canvas(win, width = 800, height = 600, bg = "white")
canvas.pack()

def zmena_farby():
    if canvas.itemcget(obejkt_1, "fill") == "red":
        canvas.itemconfig(obejkt_1, fill = "blue")
    else:
        canvas.itemconfig(obejkt_1, fill = "red")
    if canvas.itemcget(obejkt_2, "fill") == "yellow":
        canvas.itemconfig(obejkt_2, fill="pink")
    else:
        canvas.itemconfig(obejkt_2, fill="yellow")
    

obejkt_2 = canvas.create_oval(400, 200, 500, 300, fill="yellow", outline="black")

obejkt_1 = canvas.create_rectangle(100, 200, 300, 100, fill = "blue", outline = "red")
print(obejkt_1)

#existuje getter ktora zisti info o objekte pomocou idcka
#setter ktory menii info objektu

canvas.itemconfig(obejkt_1, fill = "green")
print(canvas.itemcget(obejkt_1, "outline"))

#ak chcem manipulovat s nejakym objektom, musim poznat id

button1 = tk.Button(win, text = "Click me", command = zmena_farby)
button1.pack()

win.mainloop()