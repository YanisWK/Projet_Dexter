import logging
from math import pi, degrees


class adaptateurIRL():
    """
    Classe simulant le robot IRL en convertissant les commandes en commandes compréhensibles pour le robot IRL.

    Paramètre :
    - turret.Robot2IN013Fake : robot IRL de la classe Robot2IN013Fake

    """

    def __init__(self,robot):
        """ Initialise le robot de la classe Robot2IN013Fake"""
        self.robot = robot
        self.rayon_des_roues = self.robot.WHEEL_DIAMETER/20
        self.largeur = self.robot.WHEEL_BASE_WIDTH/10
        self.derniere_position_moteurs = (0, 0)

    def set_vitesse_roue(self, port, vitesse):
        """
        Ajuste la vitesse linéaire d'une ou des deux roues du robot en fonction du port.

        Paramètres :
        - port : numéro du port de la roue 
                -> 1 pour roue gauche
                -> 2 pour roue droite
                -> 3 pour les deux roues
        - vitesse : nouvelle vitesse linéaire de la roue (en cm/s)
        """
        logging.info(f"Set vitesse de(s) roue(s)  {port} a {vitesse}")
        dps = vitesse * 2 * pi / (self.rayon_des_roues * 10)
        dps *= 10
        self.robot.set_motor_dps(port, dps)

    def detect_distance(self,_simu_longueur, _simu_largeur):
        """
        Simule le capteur distance et retourne la distance détectée
        
        Paramètres :
        - _simu_longueur : longueur de l'environnement du robot
        - _simu_largeur : largeur de l'environnement du robot
        """
        print("Utilisation du capteur de distance")
        dist=self.robot.get_distance()/10
        if (dist==819):
            return 800
        return dist

    def get_position_moteurs(self):
        """
        Retourne la position des moteurs du robot au dernier rafraichissement.
        """
        logging.info("Obtenir la position des moteurs")
        return self.robot.get_motor_position()
    
    def set_position_moteurs(self, port, offset):
        """
        Définit la position des moteurs avec un décalage spécifié.

        Paramètres :
        - port : numéro du port du moteur
        - offset : offset de décalage en degrés
        """
        return self.robot.offset_motor_encoder(port, offset)

    def calcule_avancer_tourner(self):
        nouvelle_position_moteurs = self.get_position_moteurs()

        dist_RG = (abs(self.derniere_position_moteurs[0] - nouvelle_position_moteurs[0]) / 360) * (2*self.rayon_des_roues * pi)
        dist_RD = (abs(self.derniere_position_moteurs[1] - nouvelle_position_moteurs[1]) / 360) * (2*self.rayon_des_roues * pi)

        distance_parcourue = (dist_RG + dist_RD) / 2

        angle_RG = nouvelle_position_moteurs[0] - self.derniere_position_moteurs[0]
        angle_RD = nouvelle_position_moteurs[1] - self.derniere_position_moteurs[1]

        angle_parcouru = degrees(abs(((self.rayon_des_roues/100) * (angle_RD - angle_RG)) / self.largeur)) * 1.5

        angle_parcouru = abs(self.rayon_des_roues * (angle_RD - angle_RG)) / self.largeur
        print("PARCOURU ", angle_parcouru)

        self.derniere_position_moteurs = nouvelle_position_moteurs

        return (distance_parcourue, angle_parcouru)

