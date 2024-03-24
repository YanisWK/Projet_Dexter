from tkinter import IntVar,Button,Label
import Dexturret.interface as interface
import Dexturret.turret as turret
from time import sleep, time
import logging
import Dexturret.controller as controller
from Dexturret import stratCarre, stratCarres, stratCroix, robotSim, robotSimu, robotIRL, simu, long, larg, fps

#Configuration des logs 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S", filemode="w",filename="test.log")

#Initialisation du robot qu'on va utiliser dans le suite du programme
try:
    choix = int(input("Quel robot voulez-vous désigner ? (Tapez 1 pour le robotSimu ou 2 pour le robotIRL) : "))
    if choix == 1:
        robotAdapt = robotSimu
        window, couleur, canvas, frame, text_distance = interface.creer_graphique(robotAdapt,simu)
        refresh = 1
    elif choix == 2:
        robotAdapt = robotIRL
        refresh = 2
    else:
        print("Arrêt du programme\n")
        exit()
except ValueError:
    print("Arrêt du programme \n")
    exit()

controller_choisi = stratCarres

robotSim.dernier_rafraichissement = time()
#Boucle principale de la simu
while simu.awake and not controller_choisi.stop():

    #Mise a jour tous les 1/temps
    sleep(1/fps)

    controller_choisi.etape()
    if refresh == 1 :
        simu.rafraichir()
        interface.rafraichir_graphique(simu, canvas)
        #Affichage de la ligne rouge pour la direction du robot
        canvas.pack()
        if (len(robotAdapt.trace) == 0) or (robotAdapt.x,robotAdapt.y) != robotAdapt.trace[-1]:
            if len(robotAdapt.trace) > 500:
                robotAdapt.trace.pop(0)
            robotAdapt.trace.append((robotAdapt.x,robotAdapt.y))
        for elem in range(1,len(robotAdapt.trace)):
            x,y = robotAdapt.trace[elem-1]
            x1,y1 = robotAdapt.trace[elem]
            canvas.create_line(x, y, x1, y1, fill="black")
            canvas.pack()
        canvas.update()
        interface.affichage_distance(text_distance,robotAdapt,simu.longueur,simu.largeur)
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