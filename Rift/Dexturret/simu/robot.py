from math import cos, sin, radians, degrees, sqrt, pi
import logging
from time import time


"""Documentation : 

    Classe du robot pour la simulation.

    - coordRobot
    - __repr__
    - avancer
    - tourner
    - coeff_directeur
    - deplacementRobot
    - rafraichir
    - detect_distance
"""


class Robot:
    def __init__(self, id, longueur, largeur, rayon_des_roues, x, y, dernier_rafraichissement):
        """
        Constructeur de la classe Robot
        Paramètres :
        - id : identifiant du robot
        - longueur, largeur : dimensions du robot
        - rayon_des_roues : rayon des roues du robot
        - x,y : position du robot
        - dernier_rafraichissement : timestamp du dernier rafraîchissement des données du robot
        - vitesses_lineaires_roues : vitesses de rotation des roues gauche et droite
        - pret : booléen qui indique si la simulation est activée et le robot est en mouvement
        - position_moteurs : position des moteurs
        - trace : liste des positions du robot

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

        self.pret = False  #La simulation est activée et le robot est en mouvement

        self.dernier_rafraichissement = dernier_rafraichissement
        self.temps_ajustement = 0

        self.position_moteurs = [0,0]
        
        self.trace = []


    @property
    def coordRobot(self):
        """
        Met à jour les coordonnées des coins du robot

        Paramètre :
        - longueur, largeur : dimensions du robot
        - direction : direction du robot
        - x,y : position du robot

        Variable locale :
        - demi_longueur, demi_largeur : demi-longueur et demi-largeur du robot
        - c1, c2, c3, c4 : coordonnées des coins du robot

        Retourne :
        - liste des coordonnées des coins du robot

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
        """Décrit le robot"""
        return "Le robot d'identifiant " + str(self.id) + " qui se trouve en (" + str(self.x) + "," + str(self.y) + ")" + " et est tourné de " + str(self.direction) + "° \n" \
                + "La vitesse de sa roue gauche est de " + str(self.vitesse_lineaire_roue_gauche) + " et celle de sa roue droite est de " + str(self.vitesse_lineaire_roue_droite)


    def avancer(self, distance):
        """
        Fait avancer le robot d'une certaine distance en mettant à jour les coordonnées du robot 

        Paramètre :
        - distance : distance à parcourir (en cm)

        Retourne :
        - les nouvelles coordonnées du robot après avancement de la distance donnée en paramètre
        
        """
        logging.info(f'Le Robot a avancé de {distance} cm')

        #mise à jour des coordonnées grâce aux fonctions cosinus/sinus
        self.x += distance * cos(radians(self.direction))
        self.y -= distance * sin(radians(self.direction))


    def tourner(self, angle):
        """
        Fait tourner le robot d'un certain angle en ajustant la direction pour rester dans [0, 360]
        Si l'angle n'est pas compris dans [0,360], c'est l'angle modulo 360 qui est ajouté 
        à la direction actuelle

        Paramètre :
        - angle : angle de rotation (en degrés)

        Retourne :
        - la nouvelle direction du robot après rotation de l'angle donné en paramètre

        """
        self.direction += angle

        if (self.direction > 360):
            self.direction -= 360
        if (self.direction < 0):
            self.direction += 360

        logging.info(f'Le robot a tourné de {angle}°')
    

    def coeff_directeur(self, angle):
        """
        Retourne le coefficient directeur de la droite représentant la trajectoire du robot

        Paramètre:
        - angle : angle de direction du robot

        Variable locale :
        - a,b : coordonnées du coefficient directeur

        Retourne :
        - le coefficient directeur de la droite représentant la trajectoire du robot
        
        """
        a = cos(radians(angle))
        b = sin(radians(angle))
        return (a,b)
            
    
    def deplacementRobot(self):
        """
        Calcule la distance parcourue en ligne droite et la rotation du robot à chaque rafraîchissement, 
        puis met à jour la position et la direction du robot en appelant avancer et tourner
        
        Paramètre :
        - fps : nombre de rafraichissement par seconde
        - temps_ajustement : temps écoulé entre deux rafraichissements
        - vitesse_rotation_roue_gauche, vitesse_rotation_roue_droite : vitesse de rotation des roues gauche et droite
        - rayon_des_roues : rayon des roues du robot
        - position_moteurs : position des moteurs
        - dernier_rafraichissement : timestamp du dernier rafraîchissement des données du robot
        
        Variable locale :
        - vitesse_deplacement : vitesse de déplacement du robot (moyenne des vitesses des roues)
        - deplacement_par_rafraichissement : distance parcourue par le robot à chaque rafraîchissement (en cm)
        - vitesse_rotation : vitesse de rotation du robot (en degrés)
        - rotation_par_rafraichissement : rotation du robot à chaque rafraîchissement (en degrés)

        Retourne :
        - les nouvelles coordonnées du robot après déplacement et rotation

        """       

        #Calcul de la distance que parcourt le robot à chaque rafraîchissement distance_par_rafraichissement = vitesse/temps

        vitesse_rotation_roue_gauche = self.vitesse_lineaire_roue_gauche * 360 / (2 * self.rayon_des_roues * pi)
        vitesse_rotation_roue_droite = self.vitesse_lineaire_roue_droite * 360 / (2 * self.rayon_des_roues * pi)


        vitesse_deplacement = (self.vitesse_lineaire_roue_gauche + self.vitesse_lineaire_roue_droite) / 2
        deplacement_par_rafraichissement = vitesse_deplacement * (self.temps_ajustement)
        self.avancer(deplacement_par_rafraichissement)

        #Calcul de la rotation que le robot doit faire à chaque rafraîchissement

        vitesse_rotation = ( self.rayon_des_roues * (vitesse_rotation_roue_droite - vitesse_rotation_roue_gauche)) / self.largeur
        rotation_par_rafraichissement = vitesse_rotation * (self.temps_ajustement)

        self.position_moteurs[0] += vitesse_rotation_roue_gauche * (self.temps_ajustement)
        self.position_moteurs[1] += vitesse_rotation_roue_droite * (self.temps_ajustement)

        self.tourner(rotation_par_rafraichissement)
        

    def rafraichir(self):
        """
        Met à jour les positions des coins du robot et les déplacements du robot
        à chaque rafraichissement.

        Paramètre :
        - fps : frame par seconde

        Variable locale :
        - temps_ajustement : temps écoulé entre deux rafraichissements (en secondes)
        - dernier_rafraichissement : timestamp du dernier rafraîchissement des données du robot (en secondes)

        Retourne :
        - les nouvelles coordonnées du robot après déplacement et rotation
        """
        self.temps_ajustement = round((time() - self.dernier_rafraichissement), 3)
        self.dernier_rafraichissement = time()
        if self.pret:
            self.deplacementRobot()
        

    def detect_distance(self, simu_longueur, simu_largeur):
        """
        Retourne la distance détectée par le capteur (en cm)

        Paramètre :
        - simu_longueur, simu_largeur : dimensions de l'environnement de simulation

        Variable locale :
        - pas : pas de déplacement du rayon
        - dist : distance parcourue par le rayon
        - rayon : coordonnées du rayon

        Retourne :
        - la distance détectée par le capteur (en cm)

        """

        pas = 0.1
        dist = 0
        rayon = [self.x + (self.longueur/2)*cos(radians(self.direction)), self.y - (self.longueur/2)*sin(radians(self.direction))]

        while (rayon[0] > 0 and rayon[1] > 0 and rayon[0] < simu_longueur and rayon[1] < simu_largeur):
            rayon[0] += pas * cos(radians(self.direction))
            rayon[1] -= pas * sin(radians(self.direction))
            dist += 1
        return pas * dist