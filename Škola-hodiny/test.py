import datetime
import pytz
from tkinter import Tk, Label, Canvas

# Funkcia na vykreslenie digitalných hodin
def draw_clock():
    now = datetime.datetime.now(pytz.utc).astimezone()
    
    # Získanie aktualnej času bez týdneho doba
    hours, minutes, seconds = now.hour % 12, now.minute, now.second
    
    # Vykreslenie digitalných hodin
    canvas.delete("all")
    canvas.create_text(100, 50, text=f"{hours:02d}:{minutes:02d}:{seconds:02d}", font=("Helvetica", 48))
    
    # Zvolenie nového času po 100ms
    root.after(100, draw_clock)

# Vytvorenie okna aplikácie
root = Tk()
root.title("Digitalne hodiny")

# Vytvorenie prazdného kontura
canvas = Canvas(root, width=200, height=150)
canvas.pack()

# Spustenie funkcie na vykreslenie digitalných hodin
draw_clock()

# Spustenie aplikácie
root.mainloop()
