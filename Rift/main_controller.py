from tkinter import IntVar,Button,Label
import Dexturret.interface as interface
import Dexturret.turret as turret
from time import sleep, time
import logging
import Dexturret.controller as controller

#Configuration des logs 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S", filemode="w",filename="test.log")

#Initialisation des paramètres du robot et de la simulation
larg = 700
long = 1000
robotAdapt = controller.adaptateurSimu(1, 50, 25, 0.05, long/2, larg/2, time())
robotAdapt.direction = 135
robotAdapt.pret = True
fps = 60
simu = turret.Simulation(1, robotAdapt, larg, long, fps)


stratAvancer = controller.AvancerRobot(robotAdapt, 100, 200, fps)
stratTournerDroite = controller.TournerRobot(robotAdapt, -90, fps)
stratTournerGauche = controller.TournerRobot(robotAdapt, 90, fps)

strats = [stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche,\
          stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche,\
            stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche,\
                stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche]


boucle = True
boucle = False #a supprimer
'''
while (boucle):
    print("Choix du controller:\n(1) Tracer un carré\n(2) Foncer vers un mur")
    choix = int(input())

    if (choix != 1 and choix != 2):
        print("Choix invalide, veuillez recommencer")
    else:
        print("Entrez la vitesse du robot:")
        vitesse = int(input())
        if not (isinstance(vitesse, int)):
            print("Entrée invalide, veuillez recommencer depuis le début (l'entrée doit être un entier)")
        else:
            if (choix == 1):
                print("Entrez la distance d'un coté du carré:")
                distance = int(input())
                if not (isinstance(distance, int)):
                    print("Entrée invalide, veuillez recommencer depuis le début (l'entrée doit être un entier)")
                else:
                    controller_choisi = controller.TracerCarre(robotAdapt, distance, vitesse, fps)
            else:
                controller_choisi = controller.AvancerViteMur(robotAdapt, simu, vitesse, fps)
            boucle = False
'''

window, couleur, canvas, frame, text_distance = interface.creer_graphique(robotAdapt,simu)

controller_choisi = controller.Instructions(strats)

robotAdapt.dernier_rafraichissement = time()
tab = [(robotAdapt.x,robotAdapt.y)]
tailleMax = 500
#Boucle principale de la simu
while simu.awake and not controller_choisi.stop():

    #Mise a jour tous les 1/temps
    sleep(1/simu.fps)

    controller_choisi.etape()
    
    #On efface tout et on redessine le robot
    simu.rafraichir()
    interface.rafraichir_graphique(simu, canvas)

    #Affichage de la ligne rouge pour la direction du robot
    canvas.pack()
    if (robotAdapt.x,robotAdapt.y) != tab[-1]:
        if len(tab) > tailleMax:
            tab.pop(0)
        tab.append((robotAdapt.x,robotAdapt.y))
    for elem in range(1,len(tab)):
        x,y = tab[elem-1]
        x1,y1 = tab[elem]
        canvas.create_line(x, y, x1, y1, fill="black")
        canvas.pack()
    canvas.update()
    interface.affichage_distance(text_distance,robotAdapt,simu.longueur,simu.largeur)

#Affichage d'une fenêtre pop-up en cas de collision
if not simu.awake:
    interface.popup_collision(window)
    logging.info(f'Le Robot est entré en collision avec un obstacle')

#Lancement de la boucle principale
print("ok")
if not boucle:
    window.mainloop()
