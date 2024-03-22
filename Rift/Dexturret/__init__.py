from Dexturret.interface import creer_canvas, creer_couleur, creer_fenetre, creer_frame, creer_scale, affiche_robot, popup_collision, rafraichir_graphique, change_color
from Dexturret.turret import robot, simulation
from Dexturret.controller import AvancerRobot, TournerRobot, adaptateurSimu, adaptateurIRL

from time import time

#Initialisation des paramètres des robot et des variables pour la simulation
larg = 700
long = 1000
fps=60
robotSimu = adaptateurSimu(1, 50, 25, 5, long/2, larg/2, fps)
robotIRL = adaptateurIRL()

stratAvancer= AvancerRobot(robot, 100, 100, fps)
stratTournerDroite = TournerRobot(robot, -90, fps)
stratTournerGauche = TournerRobot(robot, 90, fps)

carre = [stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, 
         stratTournerDroite, stratAvancer, stratTournerDroite]

strats = [stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche,\
          stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche,\
            stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche,\
                stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche]
