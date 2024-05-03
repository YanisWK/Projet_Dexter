from robot2IN013 import Robot2IN013
from Dexturret import adaptateurIRL
import Dexturret.controller as controller
from time import sleep

robotIRL = Robot2IN013()
robotAdapt = adaptateurIRL(robotIRL)

#controller_choisi = controller.getStrat_AvancerViteMur(robotAdapt, 20, 100, 60, 0, 0)
controller_choisi = controller.Sequence([controller.AvancerRobot(robotAdapt, 5, 100, 60)]) # => saccadé
controller_choisi.start()

fichier = open("data.txt", "w")

print("DEBUT")
while not controller_choisi.stop():

    #Mise a jour tous les 1/temps
    sleep(1/60)
    print("ENCODER: ", robotAdapt.get_position_moteurs())
    #fichier.write(Robot2IN013.get_image)
    controller_choisi.etape()

# robotAdapt.set_vitesse_roue(3, 100) # => pas saccadé
# sleep(0.5)
# print("Changement vitesse")
# robotAdapt.set_vitesse_roue(3, 50)
# sleep(1)

print("FIN")
fichier.close()
robotAdapt.set_vitesse_roue(3, 0)