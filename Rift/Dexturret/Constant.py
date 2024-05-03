from .interface2D import creer_canvas, creer_couleur, creer_fenetre, creer_frame, creer_scale, affiche_robot, popup_collision, rafraichir_graphique, change_color, creer_graphique, affichage_distance, onKeyPress, dessiner
from .simu import Robot, adaptateurSimu, Simulation
from .irl import Robot2IN013Fake, adaptateurIRL
from .controller import AvancerRobot, TournerRobot, Sequence, Strat_if, Strat_while, Strat_for, CompareDistance,getStrat_seq_carreD,getStrat_seq_carreG,getStrat_dessine_n_carre

from time import time

#Initialisation des paramètres des robot et des variables pour la simulation
LARGUEUR= 700
LONGUEUR= 700
FPS=60

#Creation du robot simu, de son adaptateur et de la simulation
robotSim = Robot(1, 50, 25, 5, LONGUEUR/2, LARGUEUR/2, time())
robotAdaptSimu = adaptateurSimu(robotSim)
robotSim.direction = 100
robotSim.pret = True
simu = Simulation(1, robotSim, LARGUEUR, LONGUEUR, FPS)

#Le robot fake et son adaptateur
robotFake = Robot2IN013Fake()
robotAdaptIRL = adaptateurIRL(robotFake)

def choix_robot():
  try:
      choix = int(input("Quel robot voulez-vous désigner ? (Tapez 1 pour le robotSimu ou 2 pour le robotIRL) : "))
      if choix == 1:
        robotAdapt = robotAdaptSimu
        return robotAdapt,1
      elif choix == 2:
        robotAdapt = robotAdaptIRL
        return robotAdapt,2
  
      else:
          return None,None

  except ValueError:
      return None,None