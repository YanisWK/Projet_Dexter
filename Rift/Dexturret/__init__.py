from Dexturret.interface import creer_canvas, creer_couleur, creer_fenetre, creer_frame, creer_scale, affiche_robot, popup_collision, rafraichir_graphique, change_color
from Dexturret.turret import robot, simulation
from Dexturret.controller import AvancerRobot, TournerRobot
from time import time

stratAvancer= AvancerRobot(robot, 100, 100, time())
stratTournerDroite = TournerRobot(robot, -90, time())
stratTournerGauche = TournerRobot(robot, 90, time())

carre = [stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, 
         stratTournerDroite, stratAvancer, stratTournerDroite]

strats = [stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche,\
          stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche,\
            stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche,\
                stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche]
