from math import pi, degrees

class adaptateurSimu():

    def __init__(self,robot):
        """
        Initialise un adaptateur de simulation pour le robot.

        Paramètres :
        - id : identifiant du robot
        - longueur, largeur : dimensions du robot
        - rayon_des_roues : rayon des roues du robot
        - x,y : position du robot
        - dernier_rafraichissement : timestamp du dernier rafraîchissement des données du robot
        """
        self.robot=robot

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
        if (port == 1 or port == 3):
            self.robot.vitesse_lineaire_roue_gauche = vitesse
        if (port == 2 or port == 3):
            self.robot.vitesse_lineaire_roue_droite = vitesse

    def get_position_moteurs(self):
        """Retourne la position des moteurs au dernier rafraîchissement"""
        return (self.robot.position_moteurs[0], self.robot.position_moteurs[1])
    
    def set_position_moteurs(self, port, offset):
        """
        Définit la position des moteurs avec un décalage spécifié.

        Paramètres :
        - port : numéro du port du moteur
        - offset : offset de décalage en degrés
        """
        if (port == 1 or port == 3):
            self.robot.position_moteurs[0] -= offset
        if (port == 2 or port == 3):
            self.robot.position_moteurs[1] -= offset

    def detect_distance(self, simu_longueur, simu_largeur):
        return self.robot.detect_distance(simu_longueur, simu_largeur)
    
    def calcule_avancer_tourner(self):
        angle_RG, angle_RD = self.get_position_moteurs()

        dist_RG = (abs(angle_RG) / 360) * (2 * self.rayon_des_roues * pi)
        dist_RD = (abs(angle_RD) / 360) * (2 * self.rayon_des_roues * pi)
        print("angle_RG ", angle_RG)
        print("angle_RD ", angle_RD)

        distance_parcourue = (dist_RG + dist_RD) / 2
        print("DIST PARCOURUE ", distance_parcourue)

        angle_parcouru = abs(self.rayon_des_roues * (angle_RD - angle_RG)) / self.largeur
        print("ANGLE PARCOURU ", angle_parcouru)

        return (distance_parcourue, angle_parcouru)


    @property
    def rayon_des_roues(self):
        return self.robot.rayon_des_roues
    
    @property
    def x(self):
        return self.robot.x
    
    @property
    def y(self):
        return self.robot.y
    
    @property
    def longueur(self):
        return self.robot.longueur
    
    @property
    def largeur(self):
        return self.robot.largeur
    
    @property
    def trace(self):
        return self.robot.trace