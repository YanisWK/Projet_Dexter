from turret import robot
from turret import robot2I013Fake
class adaptateur(robot2I013Fake):

    def __init__(self):
        robot2I013Fake.__init__()

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




    
        