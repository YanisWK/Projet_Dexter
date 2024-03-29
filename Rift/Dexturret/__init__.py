from .interface2D import creer_canvas, creer_couleur, creer_fenetre, creer_frame, creer_scale, affiche_robot, popup_collision, rafraichir_graphique, change_color, creer_graphique, affichage_distance, onKeyPress, dessiner
from .simu import Robot, adaptateurSimu, Simulation
from .irl import Robot2IN013Fake, adaptateurIRL
from .controller import AvancerRobot, TournerRobot, Instructions, Strat_if, CompareDistance

from time import time
from .Constant import stratAvancer, stratTournerDroite, stratTournerGauche, stratCarre, stratCarres, stratCroix, robotSim, robotSimu, robotFake, robotIRL, simu, long, larg, fps, choix_robot, cote_condition, carre_condition

