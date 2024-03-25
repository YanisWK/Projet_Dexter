from Dexturret.interface import creer_canvas, creer_couleur, creer_fenetre, creer_frame, creer_scale, affiche_robot, popup_collision, rafraichir_graphique, change_color,affiche_obstacle,creer_obstacle
from Dexturret.turret import Robot, Robot2IN013Fake, Simulation,Obstacle
from Dexturret.controller import AvancerRobot, TournerRobot, adaptateurSimu, adaptateurIRL, Instructions, Strat_if

from time import time

#Initialisation des paramètres des robot et des variables pour la simulation
larg = 700
long = 1000
fps=60

robotSim = Robot(1, 50, 25, 5, long/2, larg/2, time())
robotSimu = adaptateurSimu(robotSim)
robotSim.direction = 135
robotSim.pret = True
obs1=turret.Obstacle(225,225,25)
obs2=turret.Obstacle(745,445,25)
obstacles=[obs1,obs2]
simu = Simulation(1, robotSim, larg, long, fps, obstacles)

robotFake = Robot2IN013Fake()
robotIRL = adaptateurIRL(robotFake)

stratAvancer= AvancerRobot(robotSimu, 100, 100, fps)
stratTournerDroite = TournerRobot(robotSimu, -90, fps)
stratTournerGauche = TournerRobot(robotSimu, 90, fps)

carre = [stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite,\
          stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite]
stratCarre = Instructions(carre)

carres = [stratCarre, stratCarre, stratCarre]
stratCarres = Instructions(carres)

croix = [stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche,\
          stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche,\
            stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche,\
                stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche]
stratCroix = Instructions(croix)