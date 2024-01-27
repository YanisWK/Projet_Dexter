class Simulation:
    def __init__(self, id, robot, environnement, temps):
        self.id = id
        self.robot = robot                  #Le robot
        self.environnement = environnement  #L'environnement
        self.temps = temps                  #Le nombre de rafraichissement par seconde
        self.vitesse = 100                  #La vitesse à laquelle le robot se déplace
        self.distance = 100                 #La distance que le robot va parcourir (1 pixel = 1 cm)
        self.velociteD = []                 #Liste des déplacements vers l'avant à chaque rafraichissement
        self.velociteR = []                 #Liste des changements de direction à chaque rafraichisement

        #Les 4 coins du robot delon la position du centre et la taille du robot
        L = robot.longueur/2
        l = robot.largeur/2
        x = robot.x
        y = robot.y
        coordRobot = ([(x-l, y-L), (x+l, y-L), (x+l, y+L), (x-l, y+L)], 90)
        self.coordRobot = coordRobot

    def setRobot(self, robot):
        self.robot = robot

    def droiteDirection(self, px, py):
        #px et py sont les coordonnées d'un point donné
        """
        -Fonction qui retourne (a,b) tel que ax+by représente la droite de la direction dans laquelle le robot est orienté
        """
        a= (px-self.x) / (py-self.y) #pente
        b= py - a*px #ax+b=y => b=y-ax
        return a,b

    def obtenirAngle():
        """
        -Fonction qui permet d'obtenir l'angle du segment entre 2 points passés en paramètre
            (par rapport à l'angle trigonométrique)
        """
    
    def rafraichir():
        """
        -Fonction qui effectue les actions nécessaires à chaque rafraichissement
        -Avancer d'une distance (celle de velociteD[0]) et/ou tourner d'un certain angle (celle de velocitéR[0]) si les tableaux ne sont pas vides
        -Mettre à jour les coordonnées des coins du robot (avec coinsRobot)
        """
        return
    
    def coinsRobot():
        """
        -Fonction qui calcule, à l'aide de la taille et de la drection, la position des 4 coins du robot
        -Nécessite obtenirAngle
        -Le centre du rectangle est la position x y du robot
        """
        return
    
    def deplacementRobot():
        """
        -Fonction qui effectue les calcules nécessaire afin de déplacer le robot
        -Ajout dans velociteD les distances à faire à chaque rafraichissement selon la distance à parcourir et la vitesse,
            dans la direction du robot
        -Ne retourne rien
        """
        return
    
    def rotationRobot():
        """
        -Fonction qui effectue les calcules nécessaire afin de faire une rotation au robot
        -Ajout dans velociteR les modifications d'angles à faire à chaque rafraichissement selon la vitesse
        -Ne retourne rien
        """
        return
