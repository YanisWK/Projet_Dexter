from time import sleep
from tkinter import Canvas, Label, Tk, Frame, StringVar, IntVar, Scale, RIGHT, LEFT, HORIZONTAL, BOTH
from src.simulation import Simulation
from src.robot import Robot
from math import cos,radians,sin

"""Documentation : 
    - initialise les paramètres de la simulation
    - configure de l'interface graphique
    - affiche l'environnement à l'aide d'un canvas (fond gris)
    - affiche les échelles de la distance, la vitesse et l'angle pour l'utilisateur
    - affiche le robot sous forme de rectangle
    - configure les touches du clavier permettant de faire avancer/reculer/tourner le robot
    - affiche une ligne rouge pointant vers le point centre du robot

"""


larg = 700
long = 1000
robot1 = Robot(1,50,25,long/2,larg/2)
simu = Simulation(1,robot1,larg,long,60)


def espace (f):
    ''' 
    Ajoute un espace entre les éléments d'une frame

    Paramètres : 
    - f : frame

    '''
    espace = Label(f, text="", font=("Helvetica", 16))
    espace.pack()
    espace = Label(f, text="", font=("Helvetica", 16))
    espace.pack()

#Spécificité de notre interface graphique
window = Tk()
window.title("Simulation")
window.geometry(f"{simu.longueur+250}x{simu.largueur+5}")
window.resizable(height=False, width=False)

#Première frame/boîte
frame = Frame(window,borderwidth=5, relief="raise")
frame.pack(fill = BOTH,side = RIGHT)

#Canvas où sera simulé l'environnement du robot et ses déplacements
rec_base = Canvas(window, bg='#cccccc', width=simu.longueur, height=simu.largueur)
rec_base.place(x='0',y='0')

#Pour le scale de la vitesse
texte_var_vit = StringVar()
texte_var_vit.set("Vitesse")
label = Label(frame, textvariable=texte_var_vit, font=("Helvetica", 16))
label.pack()
vitesse = IntVar()
scale = Scale(frame, from_=10, to=200, length=240,variable=vitesse, orient=HORIZONTAL)
scale.pack(pady=1)

espace(frame)

#Pour le scale de la distance
dist = Label(frame, text="Distance", font=("Helvetica", 16))
dist.pack()
distance = IntVar()
scale2 = Scale(frame, from_=10, to=200, length=240,variable=distance, orient=HORIZONTAL)
scale2.pack(pady=1)


espace(frame)

#Pour le scale de l'angle à tourner
dist = Label(frame, text="Angle", font=("Helvetica", 16))
dist.pack()
angle = IntVar()
scale3 = Scale(frame, from_=0, to=180, length=240,variable=angle, orient=HORIZONTAL)
scale3.pack(pady=1)

#Implementation du robot dans l'environnement
coord = simu.robot.coordRobot
rec_base.create_polygon(coord[0][0],coord[0][1],coord[1][0],coord[1][1],coord[2][0],coord[2][1],coord[3][0],coord[3][1])
rec_base.pack()

def onKeyPress(event):
    """
    Choisit les fonctions à executer en fonction des touches directionnelles

    Paramètres :
    - event : événement de clavier dans l'interface utilisateur, crée quand une touche est pressée
    """
    if event.keysym == "Right":
        simu.robot.rotationRobot(-angle.get(), vitesse.get(), simu.temps)
    elif event.keysym == "Left":
        simu.robot.rotationRobot(angle.get(), vitesse.get(), simu.temps)
    elif event.keysym == "Up":
        simu.robot.deplacementRobot(distance.get(), vitesse.get(), simu.temps)
    elif event.keysym == "Down":
        simu.robot.deplacementRobot(-distance.get(), vitesse.get(), simu.temps)

#Sert a utiliser la fonction onKeyPress lorsque on clique sur une touche du clavier
window.bind('<KeyPress>', onKeyPress)

#Boucle qui permet de rafraichir l'interface mais ça bouffe TROP DE RESSOURCES
while True:
    #Mise a jour tous les 1/temps
    sleep(1/simu.temps)

    #On efface tout et on redessine le robot
    rec_base.delete("all")
    simu.rafraichir()
    rec_base.create_polygon(simu.robot.coordRobot)

    #Affichage de la ligne rouge pour la direction du robot
    x = robot1.x
    y = robot1.y
    L = robot1.longueur / 2
    l = robot1.largeur / 2
    x1 = x + L*cos(radians(robot1.direction))
    y1 = y - L*sin(radians(robot1.direction))
    rec_base.create_line(x, y, x1, y1, fill="red")

    rec_base.pack()
    rec_base.update()

window.mainloop()







#boutton_moins_distance = Button(frame, text="-10",font =("verdana", 13), fg='black', bg='white')
#boutton_moins_distance.pack(side = LEFT)