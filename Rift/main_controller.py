from tkinter import IntVar,Button,Label
import Dexturret.interface as interface
import Dexturret.turret as turret
from time import sleep, time
import logging
import Dexturret.controller as controller

#Configuration des logs 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S", filemode="w",filename="test.log")

#Initialisation des paramètres des robot et des variables pour la simulation
larg = 700
long = 1000
robotSimu = controller.adaptateurSimu(1, 50, 25, 5, long/2, larg/2, time())
robotIRL = controller.adaptateurIRL()
fps = 60


#Initialisation du robot qu'on va utiliser dans le suite du programme
try:
    choix = int(input("Quel robot voulez-vous désigner ? (Tapez 1 pour le robotSimu ou 2 pour le robotIRL) : "))
    if choix == 1:
        robotAdapt = robotSimu
        robotAdapt.direction = 135
        robotAdapt.pret = True
        simu = turret.Simulation(1, robotAdapt, larg, long, fps)
        window, couleur, canvas, frame, text_distance = interface.creer_graphique(robotAdapt,simu)
        refresh = simu
    elif choix == 2:
        robotAdapt = robotIRL
        refresh = robotAdapt
    else:
        print("Arrêt du programme\n")
        exit()
except ValueError:
    print("Arrêt du programme \n")
    exit()

simu = turret.Simulation(1, robotAdapt, larg, long, fps)
#Initialisation des stratégies séquentielle 
stratAvancer = controller.AvancerRobot(robotAdapt, 100, 100, fps)
stratTournerDroite = controller.TournerRobot(robotAdapt, -90, fps)
stratTournerGauche = controller.TournerRobot(robotAdapt, 90, fps)

strats = [stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche,\
          stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche,\
            stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche,\
                stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche]

carre = [stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite]
stratCarre = controller.Instructions(carre)
carres = [stratCarre, stratCarre, stratCarre]

controller_choisi = controller.Instructions(carre)


if (robotAdapt == robotSimu):
    robotAdapt.dernier_rafraichissement = time()
    tab = [(robotAdapt.x,robotAdapt.y)]
    tailleMax = 500


#Boucle principale de la simu
while simu.awake and not controller_choisi.stop():

    #Mise a jour tous les 1/temps
    sleep(1/fps)

    controller_choisi.etape()
    
    refresh.rafraichir()
    if (robotAdapt == robotSimu):
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
if (robotAdapt == robotIRL):
    print("Fin du programme robot IRL")
    exit()

if not simu.awake:
    interface.popup_collision(window)
    logging.info(f'Le Robot est entré en collision avec un obstacle')

print("Fin du programme robotSimu")



window.mainloop()