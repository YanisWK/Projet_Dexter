from robot2IN013 import Robot2IN013
from Dexturret import adaptateurIRL
import Dexturret.controller as controller
from Dexturret import stratAvancer, stratTournerDroite, stratTournerGauche, stratCarreD, stratCarreG, stratCarres, stratCarresFor, robotSim, robotSimu, robotFake, robotIRL, simu, long, larg, fps, choix_robot, cote_condition, carre_condition, dist_sup_25, avancerPeu, avancerViteMur
from time import sleep

robotIRL = Robot2IN013()
robotAdapt = adaptateurIRL(robotIRL)

stratAvancer.robot = robotAdapt
stratTournerDroite.robot = robotAdapt
stratTournerGauche.robot = robotAdapt
dist_sup_25.robot = robotAdapt

controller_choisi = stratCarreD

fichier = open("data.txt", "w")

while simu.awake and not controller_choisi.stop():

    #Mise a jour tous les 1/temps
    sleep(1/fps)
    print("ENCODER: ", robotAdapt.get_position_moteurs())
    fichier.write(Robot2IN013.get_image)
    controller_choisi.etape()
    robotAdapt.set_vitesse_roue(3, 0)

fichier.close()
robotAdapt.set_vitesse_roue(3, 0)