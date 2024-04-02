from .interface2D import creer_canvas, creer_couleur, creer_fenetre, creer_frame, creer_scale, affiche_robot, popup_collision, rafraichir_graphique, change_color, creer_graphique, affichage_distance, onKeyPress, dessiner
from .simu import Robot, adaptateurSimu, Simulation
from .irl import Robot2IN013Fake, adaptateurIRL
from .controller import AvancerRobot, TournerRobot, Instructions, Strat_if, Strat_while, Strat_for, CompareDistance

from time import time

#Initialisation des paramètres des robot et des variables pour la simulation
larg = 700
long = 1000
fps=60

#Creation du robot simu, de son adaptateur et de la simulation
robotSim = Robot(1, 50, 25, 5, long/2, larg/2, time())
robotSimu = adaptateurSimu(robotSim)
robotSim.direction = 100
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
carreD = [stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite,\
          stratAvancer, stratTournerDroite, stratAvancer, stratTournerDroite]
carreG = [stratAvancer, stratTournerGauche, stratAvancer, stratTournerGauche,\
          stratAvancer, stratTournerGauche,stratAvancer, stratTournerGauche]
stratCarreD = Instructions(carreD)
stratCarreG = Instructions(carreG)

carres = [stratCarreD, stratCarreD, stratCarreD]
stratCarres = Instructions(carres)

stratCarresFor = Strat_for(3, [stratCarreD, stratAvancer])

#Creation des strategies conditionnelles
dist_sup_100 = CompareDistance(robotSimu, 100, simu.longueur, simu.largeur)
cote_condition = Strat_if(dist_sup_100, [stratAvancer, stratTournerDroite])
carre_condition = Instructions([cote_condition, cote_condition, cote_condition, cote_condition])

avancerPeu = AvancerRobot(robotSimu, 10, 200, 60)
dist_sup_25 = CompareDistance(robotSimu, 25, simu.longueur, simu.largeur)
avancerViteMur = Strat_while(dist_sup_25, [avancerPeu])

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
        dist_sup_25.robot = robotIRL
        avancerPeu.robot = robotIRL
        avancerViteMur.robot = robotIRL
        return robotAdapt,2
  
      else:
          return None,None

  except ValueError:
      return None,None