from .interface2D import creer_canvas, creer_couleur, creer_fenetre, creer_frame, creer_scale, affiche_robot, popup_collision, rafraichir_graphique, change_color, creer_graphique, affichage_distance, onKeyPress, dessiner
from .simu import Robot, adaptateurSimu, Simulation
from .irl import Robot2IN013Fake, adaptateurIRL
from .controller import AvancerRobot, TournerRobot, Instructions, Strat_if, CompareDistance

from time import time

#Initialisation des paramètres des robot et des variables pour la simulation
larg = 700
long = 1000
fps=60

#Creation du robot simu, de son adaptateur et de la simulation
robotSim = Robot(1, 30, 15, 5, long/2, larg/2, time())
robotSimu = adaptateurSimu(robotSim)
robotSim.direction = 135
robotSim.pret = True
simu = Simulation(1, robotSim, larg, long, fps)

#Le robot fake et son adaptateur
robotFake = Robot2IN013Fake()
robotIRL = adaptateurIRL(robotFake)

#Creation des strategies elementaires
stratAvancer= AvancerRobot(robotSimu, 50, 200, fps)
stratTournerDroite = TournerRobot(robotSimu, -90, fps)
stratTournerGauche = TournerRobot(robotSimu, 90, fps)

#Creation des strategies composees
carre = [stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite,\
          stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite]
carre2 = [stratAvancer, stratTournerGauche, stratAvancer, stratTournerGauche,\
          stratAvancer, stratTournerGauche,stratAvancer, stratTournerGauche]
stratCarre = Instructions(carre2)

carres = [stratCarre, stratCarre, stratCarre]
stratCarres = Instructions(carres)

croix = [stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche,\
          stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche,\
            stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche,\
                stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite, stratAvancer, stratTournerGauche]
stratCroix = Instructions(croix)

#Creation des strategies conditionnelles
dist_sup_100 = CompareDistance(robotSimu, 100, simu.longueur, simu.largeur)
cote_condition = Strat_if(dist_sup_100, [stratAvancer, stratTournerDroite])
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
        dist_sup_100.robot = robotIRL
        return robotAdapt,2
  
      else:
          return None,None

  except ValueError:
      return None,None