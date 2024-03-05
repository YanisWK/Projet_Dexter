from math import cos, sin, radians, degrees, sqrt
import logging
from time import time


"""Documentation : 

    Classe du robot pour la simulation.

    Attributs :
    - id : identifiant du robot
    - longueur, largeur : dimensions du robot
    - x, y : coordonnées du robot dans l'environnement
    - direction : angle d'orientation du robot en degrés
    - rayon_des_roues : rayon des roues du robot
    - vitesse_lineaire_roue_gauche, vitesse_lineaire_roue_droite : vitesses linéaires des roues gauche et droite
    - vitesse_de_rotation_roue_gauche, vitesse_de_rotation_roue_droite : vitesses de rotation des roues gauche et droite
    - pret : indique l'activation de la simulation et du mouvement du robot
    - dernier_rafraichissement : temps du dernier rafraîchissement
    - temps_ajustement : temps d'ajustement pour le rafraîchissement
    
"""


class Robot:
    def __init__(self, id, longueur, largeur, rayon_des_roues, x, y, dernier_rafraichissement):
        """
        Paramètres :
        - id : identifiant du robot
        - longueur, largeur : dimensions du robot
        - x,y : coordonnées du robot dans l'environnement

        """
        self.id = id 

        self.x = x 
        self.y = y
        self.direction = 90

        self.longueur = longueur
        self.largeur = largeur

        self.rayon_des_roues = rayon_des_roues

        self.vitesse_lineaire_roue_gauche = 0
        self.vitesse_lineaire_roue_droite = 0

        self.vitesse_de_rotation_roue_gauche = 0
        self.vitesse_de_rotation_roue_droite = 0

        self.pret = False  #La simulation est activée et le robot est en mouvement

        self.dernier_rafraichissement = dernier_rafraichissement
        self.temps_ajustement = 0

    @property
    def coordRobot(self):
        """
        Met à jour les coordonnées des coins du robot

        Paramètre :
        - name : coordonnées des coins du robot
        """
        demi_longueur = self.longueur / 2
        demi_largeur = self.largeur / 2
        dir = self.direction
        x = self.x
        y = self.y

        c1 = ( (x + demi_longueur*cos(radians(dir))) + demi_largeur*cos(radians(dir + 90)), (y - demi_longueur*sin(radians(dir))) - demi_largeur*sin(radians(dir + 90)) )
        c2 = ( (x + demi_longueur*cos(radians(dir))) + demi_largeur*cos(radians(dir - 90)), (y - demi_longueur*sin(radians(dir))) - demi_largeur*sin(radians(dir - 90)) )
        c3 = ( (x - demi_longueur*cos(radians(dir))) + demi_largeur*cos(radians(dir - 90)), (y + demi_longueur*sin(radians(dir))) - demi_largeur*sin(radians(dir - 90)) )
        c4 = ( (x - demi_longueur*cos(radians(dir))) + demi_largeur*cos(radians(dir + 90)), (y + demi_longueur*sin(radians(dir))) - demi_largeur*sin(radians(dir + 90)) )
        return [c1, c2, c3, c4]

    def __repr__(self):
        return "Le robot d'identifiant " + str(self.id) + " qui se trouve en (" + str(self.x) + "," + str(self.y) + ")" + " et est tourné de " + str(self.direction) + "° \n" \
                + "La vitesse de sa roue gauche est de " + str(self.vitesse_lineaire_roue_gauche) + " et celle de sa roue droite est de " + str(self.vitesse_lineaire_roue_droite)


    def avancer(self, distance):
        """
        Déplace le robot en ligne droite en mettant à jour les coordonnées de robot 

        Paramètre :
        - distance : distance à parcourir
        
        """
        logging.info(f'Le Robot a avancé de {distance} cm')

        #mise à jour des coordonnées grâce aux fonctions cosinus/sinus
        self.x += distance * cos(radians(self.direction))
        self.y -= distance * sin(radians(self.direction))


    def tourner(self, angle):
        """
        Effectue une rotation en ajustant la direction pour rester dans [0, 360]
        Si l'angle n'est pas compris dans [0,360], c'est l'angle modulo 360 qui est ajouté 
        à la direction actuelle

        Paramètre :
        - angle : angle de rotation

        """
        self.direction += angle

        if (self.direction > 360):
            self.direction -= 360
        if (self.direction < 0):
            self.direction += 360

        logging.info(f'Le robot a tourné de {angle}°')
    

    def coeff_directeur(self, angle):
        """
        Retourne (a,b) tel que ax+by représente la droite de la direction dans laquelle le robot est orienté
        Cette droite permet au robot de se déplacer dans la direction voulue en variant x et y

        """
        a = cos(radians(angle))
        b = sin(radians(angle))
        return (a,b)
            
    
    def deplacementRobot(self, fps):
        """
        Calcule la distance de déplacement en ligne droite et la rotation du robot à chaque rafraîchissement, 
        puis met à jour la position et la direction du robot en appelant avancer et tourner
        
        Paramètre :
        - fps : nombre de rafraichissement par seconde
        
        """       

        #Calcul de la distance que parcourt le robot à chaque rafraîchissement distance_par_rafraichissement = vitesse/temps
        
        self.vitesse_de_rotation_roue_gauche = self.vitesse_lineaire_roue_gauche / self.rayon_des_roues
        self.vitesse_de_rotation_roue_droite = self.vitesse_lineaire_roue_droite / self.rayon_des_roues


        vitesse_deplacement = (self.vitesse_lineaire_roue_gauche + self.vitesse_lineaire_roue_droite) / 2
        deplacement_par_rafraichissement = vitesse_deplacement * ((1/fps) + self.temps_ajustement)
        print("robot deplacer avancer: ", deplacement_par_rafraichissement)
        self.avancer(deplacement_par_rafraichissement)

        #Calcul de la rotation que le robot doit faire à chaque rafraîchissement

        vitesse_rotation = ( self.rayon_des_roues * (self.vitesse_de_rotation_roue_droite - self.vitesse_de_rotation_roue_gauche)) / self.largeur
        rotation_par_rafraichissement = vitesse_rotation * ((1/fps) + self.temps_ajustement)
        print("robot rot/raf", degrees(rotation_par_rafraichissement))
        self.tourner(degrees(rotation_par_rafraichissement))
        

    def rafraichir(self,fps):
        """
        Met à jour les positions des coins du robot et les déplacements du robot

        Paramètre :
        - fps : frame par seconde
        """
        self.temps_ajustement = max(round((time() - self.dernier_rafraichissement) - 1/fps, 3), 0)
        self.dernier_rafraichissement = time()
        if self.pret:
            self.deplacementRobot(fps)
        
    def detect_distance(self, simu_longueur, simu_largeur):
        """
        Retourne une distance dans la direction dans laquelle le robot est orienté

        Paramètre :
        - simu_longueur, simu_largeur : dimensions de l'environnement d'une simulation

        Retourne :
        - la distance entre le robot et le mur dans la direction du robot

        """

        pas = 0.1
        dist = 0
        rayon = [self.x + (self.longueur/2)*cos(radians(self.direction)), self.y - (self.longueur/2)*sin(radians(self.direction))]

        while (rayon[0] > 0 and rayon[1] > 0 and rayon[0] < simu_longueur and rayon[1] < simu_largeur):
            rayon[0] += pas * cos(radians(self.direction))
            rayon[1] -= pas * sin(radians(self.direction))
            dist += 1
        return pas * dist
        
    
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
    
