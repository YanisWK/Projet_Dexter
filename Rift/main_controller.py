from tkinter import IntVar,Button,Label
import Dexturret.interface as interface
import Dexturret.turret as turret
from time import sleep, time
import logging
import Dexturret.controller as controller
from Dexturret import stratAvancer, stratTournerDroite, stratTournerGauche, stratCarre, stratCarres, stratCroix, robotSim, robotSimu, robotIRL, simu, long, larg, fps, choix_robot, cote_condition, carre_condition

#Configuration des logs 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S", filemode="w",filename="test.log")

#Initialisation du robot qu'on va utiliser dans le suite du programme
try:
    choix = int(input("Quel robot voulez-vous désigner ? (Tapez 1 pour le robotSimu ou 2 pour le robotIRL) : "))
    if choix == 1:
        robotAdapt = robotSimu
        window, couleur, canvas, frame, text_distance = interface.creer_graphique(simu)
        refresh = 1

    elif choix == 2:
        robotAdapt = robotIRL
        refresh = 2
        stratAvancer.robot = robotIRL
        stratTournerDroite.robot = robotIRL
        stratTournerGauche.robot = robotIRL

    else:
        print("Arrêt du programme\n")
        exit()

except ValueError:
    print("Arrêt du programme \n")
    exit()

controller_choisi = carre_condition

robotSim.dernier_rafraichissement = time()
#Boucle principale de la simu
while simu.awake and not controller_choisi.stop():

    #Mise a jour tous les 1/temps
    sleep(1/fps)

    controller_choisi.etape()
    if refresh == 1 :
        simu.rafraichir()
        interface.dessiner(robotAdapt,simu,canvas,text_distance)
    if refresh == 2:
        robotAdapt.rafraichir()

#Affichage d'une fenêtre pop-up en cas de collision
if (robotAdapt == robotIRL):
    print("Fin du programme robot IRL")
    exit()

if not simu.awake:
    interface.popup_collision(window)
    logging.info(f'Le Robot est entré en collision avec un obstacle')

print("Fin du programme robotSimu")

window.mainloop()