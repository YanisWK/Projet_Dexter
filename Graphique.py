from time import *
from tkinter import *

#Spécificité de notre interface graphique
window = Tk()
longueur = 1080
largeur = 720
window.title("Simulation")
window.geometry(f"{longueur+200}x{largeur+5}")
Vitesse = IntVar()
window.resizable(height=False, width=False)
frame = Frame(window)
frame.pack(fill = Y,side = RIGHT)
rec_base = Canvas(window, bg='blue', width=longueur, height=largeur)
rec_base.place(x='0',y='0')
boutton_moins_distance = Button(frame, text="-10",font =("verdana", 13), fg='black', bg='white')
boutton_moins_distance.pack(side = LEFT)
scale = Scale(frame, from_=0, to=100, variable=Vitesse, orient=HORIZONTAL)
scale.pack(pady=20,side = RIGHT)
text2 = Label(frame, text="Vitesse", font=("Courrier",40), fg="black")
text2.pack(side = BOTTOM)
window.mainloop()