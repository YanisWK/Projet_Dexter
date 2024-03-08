from turret import robot
from turret.robot2I013Fake import Robot2IN013Fake
class adaptateur(Robot2IN013Fake):
    """
    Classe adaptateur 
    """
    def __init__(self):
        """Initialise l'adaptateur"""
        Robot2IN013Fake.__init__()

    def stop(robot,vitesse):
        """Arrête le robot avec une vitesse spécifiée"""
        pass
    
    def set_vitesse_roue(self,port, vitesse):
        """Définit la vitesse des roues du robot"""
        """
        dps = 0 #Mettre le calcule pour mettre en Centimère par seconde
        self.set_motor_dps(port, dps)"""
        print("La vitesse des roue a été set a ",vitesse)

    def detect_distance(self,_simu_longueur, _simu_largeur):
        """Calcule la distance entre le robot et les bordures de l'environnement de la simulation"""
        #return self.get_distance()
        pass




    
        