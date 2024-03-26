from tkinter import IntVar,Button,Label
import Dexturret.interface as interface
import Dexturret.turret as turret
#from controller
from time import sleep, time
import logging

#Configuration des logs 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S", filemode="w",filename="test.log")

#Initialisation des paramètres du robot et de la simulation
larg = 700
long = 1000
robot = turret.Robot(1, 50, 25, 0.05, long/2, larg/2, time())
simu = turret.Simulation(1, robot, larg, long, 60)

window, couleur, canvas, frame, text_distance = interface.creer_graphique(simu)
#Création des variables de vitesse des roues gauche et droite et configuration de leur scale de vitesse
vitesse_roue_gauche = IntVar()
scale_roue_gauche = interface.creer_scale(frame, "Vitesse roue gauche", vitesse_roue_gauche, -100, 100)

#Ajout d'un espace entre les éléments de la frame
scale_roue_gauche.pack(ipady=20)

vitesse_roue_droite = IntVar()
scale_roue_droite = interface.creer_scale(frame, "Vitesse roue droite", vitesse_roue_droite, -100, 100)

scale_roue_droite.pack(ipady=20)


window.bind('<KeyPress>',lambda event: interface.onKeyPress(robot, couleur,event))
tab = [(robot.x,robot.y)]
tailleMax = 500

#Boucle principale de la simu
while simu.awake:
    #Mise a jour tous les 1/temps
    sleep(1/simu.fps)
    robot.vitesse_lineaire_roue_droite = vitesse_roue_droite.get()
    robot.vitesse_lineaire_roue_gauche = vitesse_roue_gauche.get()
    #On efface tout et on redessine le robot
    simu.rafraichir()
    interface.rafraichir_graphique(simu, canvas)

    #Affichage de la ligne rouge pour la direction du robot
    canvas.pack()
    interface.dessiner(robot,simu,canvas,text_distance)
    canvas.update()
    interface.affichage_distance(text_distance,robot,simu.longueur,simu.largeur)

#Affichage d'une fenêtre pop-up en cas de collision
interface.popup_collision(window)
logging.info(f'Le Robot est entré en collision avec un obstacle')

#Lancement de la boucle principale
window.mainloop()
