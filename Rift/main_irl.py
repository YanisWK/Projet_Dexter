from robot2IN013 import Robot2IN013
from Dexturret import adaptateurIRL
import Dexturret.controller as controller
from time import sleep

robotIRL = Robot2IN013()
robotAdapt = adaptateurIRL(robotIRL)

controller_choisi = controller.getStrat_AvancerViteMur(robotAdapt, 10, 100, 60, 0, 0)

fichier = open("data.txt", "w")

while not controller_choisi.stop():

    #Mise a jour tous les 1/temps
    sleep(1/60)
    print("ENCODER: ", robotAdapt.get_position_moteurs())
    #fichier.write(Robot2IN013.get_image)
    controller_choisi.etape()

fichier.close()
robotAdapt.set_vitesse_roue(3, 0)