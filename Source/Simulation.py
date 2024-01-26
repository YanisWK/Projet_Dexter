class Simulation:
    def __init__(self, id, robot, environnement, temps):
        self.id = id
        self.robot = robot                  #Le robot
        self.environnement = environnement  #L'environnement
        self.temps = temps                  #Le nombre de rafraichissement par seconde
        self.vitesse = 100                  #La vitesse à laquelle le robot se déplace
        self.distance = 100                 #La distance que le robot va parcourir
        self.velociteX = []                 #Liste des déplacements sur l'axe x à chaque rafraichissement
        self.velociteY = []                 #Liste des déplacements sur l'axe y à chaque rafraichissement
        self.velociteR = []                 #Liste des changements de direction à chaque rafraichisement

    def setRobot(self, robot):
        self.robot = robot

    def droiteDirection(self):
        """
        Fonction qui retourne (a,b) tel que ax+by représente la droite de la direction dans laquelle le robot regarde
        """
        #a= calcul pente
        b=self.y - a*self.x
        return a,b

    
    def rafraichir():
        """
        Fonction qui effectue les actions nécessaires à chaque rafraichissement
        """
        return
    
    def coinsRobot():
        """
        Fonction qui calcule, à l'aide de la taille et de la drection, la position des 4 coins du robot
        """
        return
    
    def deplacementRobot():
        """
        Fonction qui effectue les calcules nécessaire afin de déplacer le robot
        """
        return
    
    def rotationRobot():
        """
        Fonction qui effectue les calcules nécessaire afin de faire une rotation au robot
        """
        return
