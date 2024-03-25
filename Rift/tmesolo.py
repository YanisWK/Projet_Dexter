from tkinter import IntVar,Button,Label
import Dexturret.interface as interface
import Dexturret.turret as turret
from time import sleep, time
import logging
import Dexturret.controller as controller
from Dexturret import stratAvancer, stratTournerDroite, stratTournerGauche, stratCarre, stratCarres, stratCroix, robotSim, robotSimu, robotIRL, simu, long, larg, fps,stratcinqfois


#Question 1.1
#Initialisation des paramètres du robot et de la simulation
larg = 700
long = 1000
robot = turret.Robot(1, 50, 25, 0.05, long/2, larg/2, time())
simu = turret.Simulation(1, robot, larg, long, 60)

window, couleur, canvas, frame, text_distance = interface.creer_graphique(robot,simu)
interface.affiche_robot(simu,canvas)

vitesse_roue_gauche = IntVar()
scale_roue_gauche = interface.creer_scale(frame, "Vitesse roue gauche", vitesse_roue_gauche, -100, 100)

#Ajout d'un espace entre les éléments de la frame
scale_roue_gauche.pack(ipady=20)

vitesse_roue_droite = IntVar()
scale_roue_droite = interface.creer_scale(frame, "Vitesse roue droite", vitesse_roue_droite, -100, 100)

scale_roue_droite.pack(ipady=20)

window.bind('<KeyPress>',lambda event: interface.onKeyPress(robot, couleur,event))
b = True
controller_choisi = stratcinqfois

robotSim.dernier_rafraichissement = time()
#Boucle principale de la simu
while simu.awake and not controller_choisi.stop():

    #Mise a jour tous les 1/temps
    sleep(1/fps)

    controller_choisi.etape()
    robot.vitesse_lineaire_roue_droite = vitesse_roue_droite.get()
    robot.vitesse_lineaire_roue_gauche = vitesse_roue_gauche.get()
    #On efface tout et on redessine le robot
    simu.rafraichir()
    interface.rafraichir_graphique(simu, canvas)

    #Affichage de la ligne rouge pour la direction du robot
    canvas.pack()
    robot.dessine(b,canvas)
    for elem in range(1,len(robot.trace)):
        x,y = robot.trace[elem-1]
        x1,y1 = robot.trace[elem]
        canvas.create_line(x, y, x1, y1, fill="black")
        canvas.pack()
    canvas.update()
    interface.affichage_distance(text_distance,robot,simu.longueur,simu.largeur)
    if (len(robot.trace)==500):
        b=False



window.mainloop()