class Simulation:
    def __init__(self, id, robot, environnement, temps):
        self.id = id
        self.robot = robot                  #Le robot
        self.environnement = environnement  #L'environnement
        self.temps = temps                  #Le nombre de rafraichissement par seconde
        self.vitesse = 100                  #La vitesse à laquelle le robot se déplace
        self.distance = 100                 #La distance que le robot va parcourir (1 pixel = 1 cm)
        self.velociteX = []                 #Liste des déplacements sur l'axe x à chaque rafraichissement
        self.velociteY = []                 #Liste des déplacements sur l'axe y à chaque rafraichissement
        self.velociteR = []                 #Liste des changements de direction à chaque rafraichisement

    def setRobot(self, robot):
        self.robot = robot

    def droiteDirection(self):
        """
        -Fonction qui retourne (a,b) tel que ax+by représente la droite de la direction dans laquelle le robot est orienté
        """
        #a= calcul pente
        #b=self.y - a*self.x
        #return a,b

    
    def rafraichir():
        """
        -Fonction qui effectue les actions nécessaires à chaque rafraichissement
        """
        return
    
    def coinsRobot():
        """
        -Fonction qui calcule, à l'aide de la taille et de la drection, la position des 4 coins du robot
        -Le centre du rectangle est la position x y du robot
        """
        return
    
    def deplacementRobot():
        """
        -Fonction qui effectue les calcules nécessaire afin de déplacer le robot
        -Nécessite droiteDirection() 
        -Ajout dans velociteX et velociteY les déplacements à faire à chaque rafraichissement selon la distance à parcourir et la vitesse,
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
