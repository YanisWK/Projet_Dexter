from math import *
from src.robot import Robot

"""Documentation : 

Classe qui simule le déplacement d'un robot dans un environnement donné

La simulation inclut des fonctions permettant de mettre à jour les coordonnées du robot, 
et d'effectuer les calculs nécessaires pour simuler un déplacement fluide et réaliste :

- __init__ => crée une simulation liant le robot et l'environnement avec un temps de rafraichissement

- rafraichir => effectue les déplacements avancer/tourner à l'aide des listes velociteD et velociteR et 
                gère les collisions avec les bords de l'environnement
"""

class Simulation:
    def __init__(self, id, robot, largeur, longueur, temps):
        """
        Initialise une simulation avec un identifiant, un robot, un environnement et un temps de rafraîchissement

        Paramètres :
        - id : identifiant 
        - robot : instance de la classe Robot         
        - longueur : longueur de l'environnement dans lequel le robot se déplace
        - largeur : largueur de l'environnement 
        - temps : nombre de rafraîchissements par seconde dans la simulation

        """
        self.id = id
        self.robot = robot                  #Le robot
        self.longueur = longueur            #La longueur de l'environnement
        self.largeur = largeur             #La largueur de l'environnement
        self.temps = temps
        self.awake=True
        
    
    def rafraichir(self, vitesse_roue_g, vitesse_roue_d):
        """
        Met à jour la fonction rafraichir du robot si la simu est active et si le robot est prêt
        
        Paramètres: 
        - vitesse_roue_g : vitesse des roues gauche
        - vitesse_roue_d ; vitesse des roues droite
        
        """
        if (self.awake):
            if (self.robot.pret):
                self.robot.vitesseRoueG = vitesse_roue_g
                self.robot.vitesseRoueD = vitesse_roue_d
                self.robot.rafraichir(self.temps)
                self.check_collision()

        

    """
            for coin in self.coordRobot:
                if coin[0] < 0:
                    decal_x = max(decal_x, -coin[0])
                if coin[0] > self.longueur:
                    decal_x = min(decal_x, -(coin[0] - self.longueur))

                if coin[1] < 0:
                    decal_y = max(decal_y, -coin[1])
                if coin[1] > self.largeur:
                    decal_y = min(decal_y, -(coin[1] - self.largeur))

            self.robot.x += decal_x
            self.robot.y += decal_y

            self.coinsRobot()
    """
    #Fonction qui regarde si le robot est sortie de l'environnement 
    def check_collision(self):
        Coord = self.robot.coordRobot
        for i in range(4):
            if (Coord[i][0] > self.longueur) or (Coord[i][0] < 0):
                self.awake = False
            elif (Coord[i][1] > self.largeur) or (Coord[i][1] < 0):
                self.awake = False
    