from time import *
from tkinter import *

#Spécificité de notre interface graphique
window = Tk()
longueur = 1080
largeur = 720
window.title("Simulation")
window.geometry(f"{longueur+200}x{largeur+5}")
window.minsize(480,360)
window.maxsize(1920,1080)

window.resizable(height=True, width=True)

rec_base = Canvas(window, bg='blue', width=longueur, height=largeur)
rec_base.place(x='0',y='0')
window.mainloop()