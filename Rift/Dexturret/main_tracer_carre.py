from tkinter import IntVar,Button,Label
import Interface
import Turret
from time import sleep, time
import logging
import controller

#Configuration des logs 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S", filemode="w",filename="test.log")

#Initialisation des paramètres du robot et de la simulation
larg = 700
long = 1000
robot = Turret.Robot(1, 50, 25, 0.05, long/2, larg/2, time())
robot.pret = True
simu = Turret.Simulation(1, robot, larg, long, 60)

window, couleur, canvas, frame, text_distance = Interface.creer_graphique(robot,simu)

controller_carre = controller.TracerCarre(robot, 100, 50)
controller_carre.start()

#Boucle principale de la simu
while simu.awake and not controller_carre.stop():
    #Mise a jour tous les 1/temps
    sleep(1/simu.fps)

    controller_carre.etape()
    
    #On efface tout et on redessine le robot
    simu.rafraichir()
    Interface.rafraichir_graphique(simu, canvas)

    #Affichage de la ligne rouge pour la direction du robot
    canvas.pack()
    canvas.update()
    Interface.affichage_distance(text_distance,robot,simu.longueur,simu.largeur)

#Affichage d'une fenêtre pop-up en cas de collision
if not simu.awake:
    Interface.popup_collision(window)
    logging.info(f'Le Robot est entré en collision avec un obstacle')

#Lancement de la boucle principale
window.mainloop()
