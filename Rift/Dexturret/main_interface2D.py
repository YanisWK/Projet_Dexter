from tkinter import IntVar,Button,Label
import Interface
import Turret
from time import sleep, time
import logging

#Configuration des logs 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S", filemode="w",filename="test.log")

#Initialisation des paramètres du robot et de la simulation
larg = 700
long = 1000
robot = Turret.Robot(1, 50, 25, 0.05, long/2, larg/2, time())
simu = Turret.Simulation(1, robot, larg, long, 60)

window, couleur, canvas, frame, text_distance = Interface.creer_graphique(robot,simu)
#Création des variables de vitesse des roues gauche et droite et configuration de leur scale de vitesse
vitesse_roue_gauche = IntVar()
scale_roue_gauche = Interface.creer_scale(frame, "Vitesse roue gauche", vitesse_roue_gauche, -100, 100)

#Ajout d'un espace entre les éléments de la frame
scale_roue_gauche.pack(ipady=20)

vitesse_roue_droite = IntVar()
scale_roue_droite = Interface.creer_scale(frame, "Vitesse roue droite", vitesse_roue_droite, -100, 100)

scale_roue_droite.pack(ipady=20)


window.bind('<KeyPress>',lambda event: Interface.onKeyPress(robot, couleur,event))

#Boucle principale de la simu
while simu.awake:
    #Mise a jour tous les 1/temps
    sleep(1/simu.fps)
    robot.vitesse_lineaire_roue_droite = vitesse_roue_droite.get()
    robot.vitesse_lineaire_roue_gauche = vitesse_roue_gauche.get()
    #On efface tout et on redessine le robot
    simu.rafraichir()
    Interface.rafraichir_graphique(simu, canvas)

    #Affichage de la ligne rouge pour la direction du robot
    canvas.pack()
    canvas.update()
    Interface.affichage_distance(text_distance,robot,simu.longueur,simu.largeur)

#Affichage d'une fenêtre pop-up en cas de collision
Interface.popup_collision(window)
logging.info(f'Le Robot est entré en collision avec un obstacle')

#Lancement de la boucle principale
window.mainloop()
