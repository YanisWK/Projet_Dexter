from math import *

"""Documentation : """
class Simulation:
    def __init__(self, id, robot, largeur, longueur,temps):
        self.id = id
        self.robot = robot                  #Le robot
        self.longueur = longueur            #La longueur de l'environnement
        self.largueur = largeur             #La largueur de l'environnement
        self.temps = temps                  #Le nombre de rafraichissement par seconde
        self.vitesse = 100                  #La vitesse à laquelle le robot se déplace
        self.distance = 100                 #La distance que le robot va parcourir (1 pixel = 1 cm)
        self.angle = 90

        #Les 4 coins du robot delon la position du centre et la taille du robot
        L = robot.longueur/2
        l = robot.largeur/2
        x = robot.x
        y = robot.y
        self.coordRobot = [(x-l, y-L), (x+l, y-L), (x+l, y+L), (x-l, y+L)]

    def rafraichir(self):

        """
        -Fonction qui effectue les actions nécessaires à chaque rafraichissement 
        -Avancer d'une distance (celle de velociteD[0]) et/ou tourner d'un certain angle (celle de velocitéR[0]) si les tableaux ne sont pas vides
        -Mettre à jour les coordonnées des coins du robot (avec coinsRobot)
        """
        #Si l'un des tableaux n'est pas vide
        if self.velociteD or self.velociteR :
            #si le tableau velociteD n'est pas vide alors on avance
            if self.velociteD : 
                self.robot.avancer(self.velociteD.pop(0))
            
            #si le tableau velociteR n'est pas vide alors on tourne
            if self.velociteR : 
                self.robot.tourner(self.velociteR.pop(0))

            #Verification des bords de la simulation
            decal_x = 0
            decal_y = 0
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
    