from turret import robot
from turret.robot2I013Fake import Robot2IN013Fake
class adaptateur(Robot2IN013Fake):

    def __init__(self):
        Robot2IN013Fake.__init__()

    def stop(robot,vitesse):
        pass
    
    def set_vitesse_roue(self,port, vitesse):
        """
        dps = 0 #Mettre le calcule pour mettre en Centimère par seconde
        self.set_motor_dps(port, dps)"""
        pass

    def detect_distance(self,_simu_longueur, _simu_largeur):
        #return self.get_distance()
        pass




    
        