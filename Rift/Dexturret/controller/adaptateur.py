import turret


class adaptateurIRL(turret.Robot2IN013Fake):

    def __init__(self):
        super.__init__()

    def set_vitesse_roue(self,port, vitesse):
        dps = 0 #Mettre le calcule pour mettre en Centimère par seconde
        self.set_motor_dps(port, dps)
        #print("La vitesse des roue a été set a ",vitesse)


    def detect_distance(self,_simu_longueur, _simu_largeur):
        dist=self.get_distance()/10
        if (dist==819):
            return 800
        return dist

    def get_position_moteurs(self):
        return self.get_motor_position()
    
    
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