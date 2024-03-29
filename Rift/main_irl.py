from robot2IN013 import Robot2IN013
from Dexturret import adaptateurIRL
import Dexturret.controller as controller
from Dexturret import stratAvancer, stratTournerDroite, stratTournerGauche, stratCarre, stratCarres, stratCroix, robotSim, robotSimu, robotFake, robotIRL, simu, long, larg, fps, cote_condition, carre_condition, dist_sup_100
from time import sleep

robotIRL = Robot2IN013()
robotAdapt = adaptateurIRL(robotIRL)

stratAvancer.robot = robotIRL
stratTournerDroite.robot = robotIRL
stratTournerGauche.robot = robotIRL
dist_sup_100.robot = robotIRL

controller_choisi = stratCarre

while simu.awake and not controller_choisi.stop():

    #Mise a jour tous les 1/temps
    sleep(1/fps)

    controller_choisi.etape()
        
robotAdapt.set_vitesse_roue(3, 0)