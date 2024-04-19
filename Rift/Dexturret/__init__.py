from .interface2D import creer_canvas, creer_couleur, creer_fenetre, creer_frame, creer_scale, affiche_robot, popup_collision, rafraichir_graphique, change_color, creer_graphique, affichage_distance, onKeyPress, dessiner
from .simu import Robot, adaptateurSimu, Simulation
from .irl import Robot2IN013Fake, adaptateurIRL
from .controller import AvancerRobot, TournerRobot, Sequence, Strat_if, Strat_while, Strat_for, CompareDistance

from time import time
from .Constant import robotSim, robotAdaptSimu, robotFake, robotAdaptIRL, simu, LONGUEUR, LARGUEUR, FPS, choix_robot

