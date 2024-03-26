from Dexturret.interface import creer_canvas, creer_couleur, creer_fenetre, creer_frame, creer_scale, affiche_robot, popup_collision, rafraichir_graphique, change_color, creer_graphique, affichage_distance, onKeyPress, dessiner
from Dexturret.simu import Robot, Simulation
from Dexturret.irl import Robot2IN013Fake
from Dexturret.controller import AvancerRobot, TournerRobot, adaptateurSimu, adaptateurIRL, Instructions, Strat_if, CompareDistance

from time import time

#Initialisation des paramètres des robot et des variables pour la simulation
larg = 700
long = 1000
fps=60

robotSim = Robot(1, 50, 25, 5, long/2, larg/2, time())
robotSimu = adaptateurSimu(robotSim)
robotSim.direction = 135
robotSim.pret = True
simu = Simulation(1, robotSim, larg, long, fps)

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

dist_sup_50 = CompareDistance(robotSimu, 50, simu.longueur, simu.largeur)
cote_condition = Strat_if(dist_sup_50, [stratAvancer, stratTournerDroite])
carre_condition = Instructions([cote_condition, cote_condition, cote_condition, cote_condition])

def choix_robot():
  try:
      choix = int(input("Quel robot voulez-vous désigner ? (Tapez 1 pour le robotSimu ou 2 pour le robotIRL) : "))
      if choix == 1:
        robotAdapt = robotSimu
        return robotAdapt,1
      elif choix == 2:
        robotAdapt = robotIRL
        stratAvancer.robot = robotIRL
        stratTournerDroite.robot = robotIRL
        stratTournerGauche.robot = robotIRL
        return robotAdapt,2
  
      else:
          return None,None

  except ValueError:
      return None,None