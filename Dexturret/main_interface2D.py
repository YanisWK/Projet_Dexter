from tkinter import IntVar,Button,Label
from Interface import creer_canvas, creer_couleur, creer_fenetre, creer_frame, creer_scale, affiche_robot, popup_collision, rafraichir_graphique, change_color
from Turret import Robot
from Turret import Simulation
from time import sleep
import logging

#Configuration des logs 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S", filemode="w",filename="test.log")

#Initialisation des paramètres du robot et de la simulation
larg = 700
long = 1000
robot = Robot(1,50,25,0.05,long/2,larg/2)
simu = Simulation(1,robot,larg,long,60)

#Création de la fenêtre principale, de la frame et du canvas pour la simulation
window = creer_fenetre(long, larg)

frame = creer_frame(window)

canvas = creer_canvas(window, simu.longueur, simu.largeur)

#Création des variables de vitesse des roues gauche et droite et configuration de leur scale de vitesse
vitesse_roue_gauche = IntVar()
scale_roue_gauche = creer_scale(frame, "Vitesse roue gauche", vitesse_roue_gauche, -100, 100)

#Ajout d'un espace entre les éléments de la frame
scale_roue_gauche.pack(ipady=20)

vitesse_roue_droite = IntVar()
scale_roue_droite = creer_scale(frame, "Vitesse roue droite", vitesse_roue_droite, -100, 100)

scale_roue_droite.pack(ipady=20)

def affichage_distance(long,larg):
    text_distance.config(text = f"Distance : {robot.detect_distance(long,larg)}")
    print("SA MARCHE OU PAS SALO")

text_distance = Label(frame, text="Distance : 0.0")
text_distance.pack()
#Création d'une couleur 
couleur = creer_couleur(frame)

def onKeyPress(event):
    """
    Gère l'événement lorsqu'une touche du clavier est pressée.

    Paramètre :
    - event : évènement crée lorsqu'une touche du clavier est pressée

    """
    if event.keysym == "space":
        robot.pret = not robot.pret
        change_color(robot.pret, couleur)
window.bind('<KeyPress>', onKeyPress)

#Boucle principale de la simu
while simu.awake:
    #Mise a jour tous les 1/temps
    sleep(1/simu.fps)

    #On efface tout et on redessine le robot
    simu.rafraichir(vitesse_roue_gauche.get(), vitesse_roue_droite.get())
    rafraichir_graphique(simu, canvas)

    #Affichage de la ligne rouge pour la direction du robot
    canvas.pack()
    canvas.update()
    affichage_distance(simu.longueur,simu.largeur)

#Affichage d'une fenêtre pop-up en cas de collision
popup_collision(window)
logging.info(f'Le Robot est entré en collision avec un obstacle')

#Lancement de la boucle principale
window.mainloop()
