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


boucle = True

while (boucle):
    print("Choix du controller:\n(1) Tracer un carré\n(2) Foncer vers un mur")
    choix = input()

    if (choix != 1 and choix != 2):
        print("Choix invalide, veuillez recommencer")
    else:
        print("Entrez la vitesse du robot:")
        vitesse = input()
        if not (isinstance(vitesse, int)):
            print("Entrée invalide, veuillez recommencer depuis le début (l'entrée doit être un entier)")
        else:
            if (choix == 1):
                print("Entrez la distance d'un coté du carré:")
                distance = input()
                if not (isinstance(distance, int)):
                    print("Entrée invalide, veuillez recommencer depuis le début (l'entrée doit être un entier)")
                else:
                    controller_choisi = controller.TracerCarre(robot, distance, vitesse)
            else:
                controller_choisi = controller.AvancerViteMur(robot, simu, vitesse)
            boucle = False


controller_choisi.start()

#Boucle principale de la simu
while simu.awake and not controller_choisi.stop():
    #Mise a jour tous les 1/temps
    sleep(1/simu.fps)

    controller_choisi.etape()
    
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
if not boucle:
    window.mainloop()
