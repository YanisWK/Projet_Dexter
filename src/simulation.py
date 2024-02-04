from math import *

"""Documentation : 

Classe qui simule le déplacement d'un robot dans un environnement donné

La simulation inclut des fonctions permettant de mettre à jour les coordonnées du robot, 
et d'effectuer les calculs nécessaires pour simuler un déplacement fluide et réaliste :

- __init__ => crée une simulation liant le robot et l'environnement avec un temps de rafraichissement
              Le script utilise des listes velociteD et velociteR, pour stocker les déplacements et les 
              rotations à chaque rafraîchissement.

- droiteDirection => retourne le couple (a,b) de la droite directionelle ax+by
                    Ces coefficients sont les composantes du vecteur unitaire dirigeant le robot  
                    - a est la composante horizontale (abscisse)
                    - b est la composante verticale (ordonnée)
                    Ils décrivent la direction associée à l'angle dans le cercle trigonométrique.

- rafraichir => effectue les déplacements avancer/tourner à l'aide des listes velociteD et velociteR et 
                gère les collisions avec les bords de l'environnement

- coinsRobot => calcule la position des 4 coins à l'aide de la direction et de la taille du robot

- deplacementRobot => fait avancer ou reculer le robot dans sa direction actuelle, 
                      en fonction des déplacements contenus dans velociteD et en fonction de la vitesse

- rotationRobot => fait tourner le robot en fonction des modifs d'angles contenues dans velociteR et 
                   en fonction de la vitesse

"""

class Simulation:
    def __init__(self, id, robot, largeur, longueur, temps):
        """
        Initialise une simulation avec un identifiant, un robot, un environnement et un temps de rafraîchissement

        Paramètres :
        - id : identifiant 
        - robot : instance de la classe Robot         
        - environnement : instance de la classe Environnement dans lequel le robot se déplace
        - temps : nombre de rafraîchissements par seconde dans la simulation

        """
        self.id = id
        self.robot = robot                  #Le robot
        self.longueur = longueur            #La longueur de l'environnement
        self.largueur = largeur             #La largueur de l'environnement
        self.temps = temps
    
    def rafraichir(self):

            self.robot.rafraichir()

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