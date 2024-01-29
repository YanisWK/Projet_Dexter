from time import *
from tkinter import *
from Simulation import *
from Robot import *
from Environnement import *

"""Documentation : """



#Fonction dans lequel on pourra faire bouger le robot grâce au touches du clavier. (A ajouter les fonction du robot plus tard)
'''
def onKeyPress(event):
    if event.keysym == "Right":
    elif event.keysym == "Left":
    elif event.keysym == "Up":
    elif event.keysym == "Down":


'''

def espace (f):
    ''' Hypothèse : f est une frame '''
    espace = Label(f, text="", font=("Helvetica", 16))
    espace.pack()
    espace = Label(f, text="", font=("Helvetica", 16))
    espace.pack()

#Spécificité de notre interface graphique
window = Tk()
longueur = 1000
largeur = 700
window.title("Simulation")
window.geometry(f"{longueur+250}x{largeur+5}")
window.resizable(height=False, width=False)

#Première frame/boîte
frame = Frame(window,borderwidth=5, relief="raise")
frame.pack(fill = BOTH,side = RIGHT)

#Canvas ou sera simuler l'environnement du robot et ces déplacement
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

espace(frame)

#Pour le scale de la distance
dist = Label(frame, text="Distance", font=("Helvetica", 16))
dist.pack()
Distance = IntVar()
scale2 = Scale(frame, from_=0, to=1000, length=240,variable=Distance, orient=HORIZONTAL)
scale2.pack(pady=1)


espace(frame)

#Pour le scale de l'angle à tourner
dist = Label(frame, text="Angle", font=("Helvetica", 16))
dist.pack()
Angle = IntVar()
scale2 = Scale(frame, from_=-180, to=180, length=240,variable=Angle, orient=HORIZONTAL)
scale2.pack(pady=1)

#window.bind('<KeyPress>', onKeyPress) #
window.mainloop()





#boutton_moins_distance = Button(frame, text="-10",font =("verdana", 13), fg='black', bg='white')
#boutton_moins_distance.pack(side = LEFT)