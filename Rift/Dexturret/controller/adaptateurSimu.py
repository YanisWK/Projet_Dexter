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
            self.robot.position_moteurs[0] = offset
        if (port == 2 or port == 3):
            self.robot.position_moteurs[1] = offset