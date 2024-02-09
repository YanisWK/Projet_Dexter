from tkinter import IntVar
from Interface import espace, creer_canvas, creer_couleur, creer_fenetre, creer_frame, creer_scale, affiche_robot, popup_collision, rafraichir_graphique, change_color
from Turret import Robot
from Turret import Simulation
from time import sleep
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S", filemode="w",filename="test.log")


larg = 700
long = 1000
robot = Robot(1,50,25,5,long/2,larg/2)
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

couleur = creer_couleur(frame)

def onKeyPress(event):
    """
    Paramètre :
    - event : évènement crée lorsqu'une touche du clavier est pressée

    """
    if event.keysym == "space":
        robot.pret = not robot.pret
        change_color(robot.pret, couleur)

window.bind('<KeyPress>', onKeyPress)

while True:
    if (simu.awake):
        #Mise a jour tous les 1/temps
        sleep(1/simu.fps)

        #On efface tout et on redessine le robot
        simu.rafraichir(vitesse_roue_gauche.get(), vitesse_roue_droite.get())
        rafraichir_graphique(simu, canvas)

        #Affichage de la ligne rouge pour la direction du robot

        canvas.pack()
        canvas.update()
    else:
        break
popup_collision(window)
logging.info(f'Le Robot est entré en collision avec un obstacle')

window.mainloop()