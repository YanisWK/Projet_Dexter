from time import *
from tkinter import *

#Spécificité de notre interface graphique
window = Tk()
longueur = 1080
largeur = 720
window.title("Simulation")
window.geometry(f"{longueur+250}x{largeur+5}")
window.resizable(height=False, width=False)


frame = Frame(window,borderwidth=5, relief="raise")
frame.pack(fill = BOTH,side = RIGHT)


rec_base = Canvas(window, bg='blue', width=longueur, height=largeur)
rec_base.place(x='0',y='0')

#Pour le scale de la vitesse
texte_var_vit = StringVar()
texte_var_vit.set("Vitesse")
label = Label(frame, textvariable=texte_var_vit, font=("Helvetica", 16))
label.pack()
Vitesse = IntVar()
scale = Scale(frame, from_=0, to=1000, length=240,variable=Vitesse, orient=HORIZONTAL)
scale.pack(pady=1)

#Pour le scale de la distance
Distance = IntVar()
scale = Scale(frame, from_=0, to=1000, length=240,variable=Distance, orient=HORIZONTAL)
scale.pack(pady=1)


window.mainloop()





#boutton_moins_distance = Button(frame, text="-10",font =("verdana", 13), fg='black', bg='white')
#boutton_moins_distance.pack(side = LEFT)