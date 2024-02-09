from tkinter import IntVar
from Interface import espace, creer_canvas, creer_couleur, creer_fenetre, creer_frame, creer_scale, affiche_robot, popup_collision, rafraichir, change_color
from Turret import Robot
from Turret import Simulation

larg = 700
long = 1000
robot = Robot(1,50,25,long/2,larg/2)
simu = Simulation(1,robot,larg,long,60)

window = creer_fenetre(long, larg)

frame = creer_frame(window)

canvas = creer_canvas(window, simu.longueur, simu.largeur)

vitesse_roue_gauche = IntVar()
scale_roue_gauche = creer_scale(frame, "Vitesse roue gauche", vitesse_roue_gauche, -100, 100)

espace(frame)

vitesse_roue_droite = IntVar()
scal_roue_droite = creer_scale(frame, "Vitesse roue droite", vitesse_roue_droite, -100, 100)

espace(frame)

creer_couleur(frame)

def onKeyPress(event):
    """
    Paramètre :
    - event : évènement crée lorsqu'une touche du clavier est pressée

    """
    if event.keysym == "space":
        if (robot.pret) :
            #fait bouger le robot si le robot est prêt et qu'on appuie sur espace
            robot.pret = False
            change_color(robot.pret)
        else:
            #stoppe le robot si le robot n'est pas prêt et qu'on appuie sur espace
            robot.pret = True
            change_color(robot.pret)
            
window.bind('<KeyPress>', onKeyPress)

#window.mainloop()