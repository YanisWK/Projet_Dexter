from tkinter import IntVar,Button,Label
import Dexturret.interface as interface
from time import sleep, time
import logging
import Dexturret.controller as controller
from Dexturret import stratAvancer, stratTournerDroite, stratTournerGauche, stratCarre, stratCarres, stratCroix, robotSim, robotSimu, robotFake, robotIRL, simu, long, larg, fps, choix_robot, cote_condition, carre_condition

#Configuration des logs 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S", filemode="w",filename="test.log")

robotAdapt,refresh = choix_robot()
if refresh == 1:
    window, couleur, canvas, frame, text_distance = interface.creer_graphique(simu)
elif refresh == None:
    print("Arrête du programme")
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
        

#Affichage d'une fenêtre pop-up en cas de collision
if (robotAdapt == robotIRL):
    print("Fin du programme robot IRL")
    exit()

if not simu.awake:
    interface.popup_collision(window)
    logging.info(f'Le Robot est entré en collision avec un obstacle')

print("Fin du programme robotSimu")

window.mainloop()