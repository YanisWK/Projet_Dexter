from time import *
from tkinter import *
from Simulation import *
from Robot import *
from Environnement import *

"""Documentation : """


Environnement_test = Environnement(1,1000,700)
Robot1 = Robot(1,100,50,Environnement_test.getLo()/2,Environnement_test.getLa()/2)
Simu = Simulation(1,Robot1,Environnement_test,10)

#Fonction dans lequel on pourra faire bouger le robot grâce au touches du clavier. (A ajouter les fonction du robot plus tard)


def espace (f):
    ''' Hypothèse : f est une frame '''
    espace = Label(f, text="", font=("Helvetica", 16))
    espace.pack()
    espace = Label(f, text="", font=("Helvetica", 16))
    espace.pack()

#Spécificité de notre interface graphique
window = Tk()
window.title("Simulation")
window.geometry(f"{Environnement_test.getLo()+250}x{Environnement_test.getLa()+5}")
window.resizable(height=False, width=False)

#Première frame/boîte
frame = Frame(window,borderwidth=5, relief="raise")
frame.pack(fill = BOTH,side = RIGHT)

#Canvas ou sera simuler l'environnement du robot et ces déplacement
rec_base = Canvas(window, bg='blue', width=Environnement_test.getLo(), height=Environnement_test.getLa())
rec_base.place(x='0',y='0')

#Pour le scale de la vitesse
texte_var_vit = StringVar()
texte_var_vit.set("Vitesse")
label = Label(frame, textvariable=texte_var_vit, font=("Helvetica", 16))
label.pack()
Vitesse = IntVar()
scale = Scale(frame, from_=10, to=200, length=240,variable=Vitesse, orient=HORIZONTAL)
scale.pack(pady=1)

espace(frame)

#Pour le scale de la distance
dist = Label(frame, text="Distance", font=("Helvetica", 16))
dist.pack()
Distance = IntVar()
scale2 = Scale(frame, from_=10, to=200, length=240,variable=Distance, orient=HORIZONTAL)
scale2.pack(pady=1)


espace(frame)

#Pour le scale de l'angle à tourner
dist = Label(frame, text="Angle", font=("Helvetica", 16))
dist.pack()
Angle = IntVar()
scale3 = Scale(frame, from_=10, to=180, length=240,variable=Angle, orient=HORIZONTAL)
scale3.pack(pady=1)

#Implementaiton du robot dans l'environnement
Coord = Simu.coordRobot
rec_base.create_polygon(Coord[0][0],Coord[0][1],Coord[1][0],Coord[1][1],Coord[2][0],Coord[2][1],Coord[3][0],Coord[3][1])
rec_base.pack()

#Fonction qui choisi les fonctions a executer en fonction des touches directionnel
def onKeyPress(event):
    Simu.vitesse = Vitesse.get()
    if event.keysym == "Right":
        Simu.angle = -Angle.get()
        Simu.rotationRobot()
    elif event.keysym == "Left":
        Simu.angle = Angle.get()
        Simu.rotationRobot()
    elif event.keysym == "Up":
        Simu.distance = Distance.get()
        Simu.deplacementRobot()
    elif event.keysym == "Down":
        Simu.distance = -Distance.get()
        Simu.deplacementRobot()
#Sert a utiliser la fonction onKeyPress lorsque on clique sur une touche du clavier
window.bind('<KeyPress>', onKeyPress)

#Boucle qui permet de rafraichir l'interface mais ça bouffe TROP DE RESSOURCES / Trouver une solution de préférence
while True:
    sleep(1/Simu.temps)
    rec_base.delete("all")
    Simu.rafraichir()
    rec_base.create_polygon(Simu.coordRobot)
    rec_base.pack()
    rec_base.update()

window.mainloop()







#boutton_moins_distance = Button(frame, text="-10",font =("verdana", 13), fg='black', bg='white')
#boutton_moins_distance.pack(side = LEFT)