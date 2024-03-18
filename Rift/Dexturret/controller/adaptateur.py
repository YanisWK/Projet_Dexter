import Dexturret.turret as turret
from math import pi 


class adaptateurIRL(turret.Robot2IN013Fake):
    """
    Classe simulant le robot IRL en convertissant les commandes en commandes compréhensibles pour le robot IRL.

    Paramètre :
    - turret.Robot2IN013Fake : robot IRL de la classe Robot2IN013Fake

    """

    def __init__(self):
        """ Initialise le robot de la classe Robot2IN013Fake"""
        super.__init__()

    def set_vitesse_roue(self,port, vitesse):
        """
        Ajuste la vitesse linéaire d'une ou des deux roues du robot en fonction du port.

        Paramètres :
        - port : numéro du port de la roue 
                -> 1 pour roue gauche
                -> 2 pour roue droite
                -> 3 pour les deux roues
        - vitesse : nouvelle vitesse linéaire de la roue (en cm/s)
        """
        dps = vitesse * pi * turret.Robot2IN013Fake.WHEEL_DIAMETER/360
        self.set_motor_dps(port, dps)

    def detect_distance(self,_simu_longueur, _simu_largeur):
        """
        Simule le capteur distance et retourne la distance détectée
        
        Paramètres :
        - _simu_longueur : longueur de l'environnement du robot
        - _simu_largeur : largeur de l'environnement du robot
        """
        dist=self.get_distance()/10
        if (dist==819):
            return 800
        return dist

    def get_position_moteurs(self):
        """
        Retourne la position des moteurs du robot au dernier rafraichissement.
        """
        return self.get_motor_position()
    
    def rafraichir(self):
        print("Le fake se rafraichit")
        self.position_moteurs[0] += self.vit_roue_gauche
        self.position_moteurs[1] += self.vit_roue_droite


class adaptateurSimu(turret.Robot):

    def __init__(self,id, longueur, largeur, rayon_des_roues, x, y, dernier_rafraichissement):
        super().__init__(id, longueur, largeur, rayon_des_roues, x, y, dernier_rafraichissement)

    def set_vitesse_roue(self,port,vitesse):
        """
        Ajuste la vitesse linéaire d'une ou des deux roues du robot en fonction du port.

        Paramètres :
        - port : numéro du port de la roue 
                -> 1 pour roue gauche
                -> 2 pour roue droite
                -> 3 pour les deux roues
        - vitesse : nouvelle vitesse linéaire de la roue (en cm/s)
        """
        if (port == 1):
            self.vitesse_lineaire_roue_gauche = vitesse
        elif (port == 2):
            self.vitesse_lineaire_roue_droite = vitesse
        elif (port == 3):
            self.vitesse_lineaire_roue_droite = vitesse
            self.vitesse_lineaire_roue_gauche = vitesse

    def get_position_moteurs(self):
        """Retourne la position des moteurs au dernier rafraîchissement"""
        return (self.position_moteurs[0], self.position_moteurs[1])