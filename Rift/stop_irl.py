from robot2IN013 import Robot2IN013
from Dexturret import adaptateurIRL
import Dexturret.controller as controller
from time import sleep

robotIRL = Robot2IN013()
robotAdapt = adaptateurIRL(robotIRL)

robotAdapt.set_vitesse_roue(3, 0)