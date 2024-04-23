from robot2IN013 import Robot2IN013
from Dexturret import adaptateurIRL
import Dexturret.controller as controller
from Dexturret import stratAvancer, stratTournerDroite, stratTournerGauche, stratCarreD, stratCarreG, stratCarres, stratCarresFor, robotSim, robotSimu, robotFake, robotIRL, simu, long, larg, fps, choix_robot, cote_condition, carre_condition, dist_sup_25, avancerPeu, avancerViteMur
from time import sleep

robotIRL = Robot2IN013()
robotAdapt = adaptateurIRL(robotIRL)

robotAdapt.set_vitesse_roue(3, 0)