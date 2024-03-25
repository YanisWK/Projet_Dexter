import Dexturret.turret

"""Documentation : 

Classe qui simule le déplacement d'un robot dans un environnement donné

La simulation inclut des fonctions permettant de mettre à jour les coordonnées du robot, 
et d'effectuer les calculs nécessaires pour simuler un déplacement fluide et réaliste :

- __init__ => crée une simulation liant le robot et l'environnement avec un temps de rafraichissement

- rafraichir => effectue les déplacements et rotations à l'aide des vitesses des roues gauches et 
                droite

- check_collision => vérifie si le robot se cogne contre une bordure et stoppe la simulation

"""

class Simulation:
    def __init__(self, id, robot, largeur, longueur, fps, ballon):
        """
        Initialise une simulation avec un identifiant, un robot, un environnement et un temps de rafraîchissement

        Paramètres :
        - id : identifiant 
        - robot : instance de la classe Robot         
        - longueur : longueur de l'environnement dans lequel le robot se déplace
        - largeur : largueur de l'environnement 
        - fps : nombre de rafraîchissements par seconde dans la simulation

        """
        self.id = id
        self.robot = robot                  #Le robot
        self.longueur = longueur            #La longueur de l'environnement
        self.largeur = largeur              #La largueur de l'environnement
        self.fps = fps                      #Temps de rafraichissement
        self.awake=True
        
        self.ballon = ballon
        
    
    def rafraichir(self):
        """
        Met à jour la fonction rafraichir du robot si la simu est active et si le robot est prêt
        
        """
        if (self.awake):
            self.robot.rafraichir()
            self.robot.detect_distance(self.longueur,self.largeur)
            self.check_collision()

            self.check_touche_balle()
            self.ballon.rafraichir()

        
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
    
    def check_collision(self):    
        """
        Checke si le robot se cogne contre une bordure et stoppe la simulation
        """
        Coord = self.robot.coordRobot
        for i in range(4):
            if (Coord[i][0] > self.longueur) or (Coord[i][0] < 0):
                self.awake = False
            elif (Coord[i][1] > self.largeur) or (Coord[i][1] < 0):
                self.awake = False

    def check_touche_balle(self):
        for coin in self.robot.coordRobot:
            cote = self.ballon.taille / 2
            if (coin[0] <= self.ballon.x + cote and coin[0] >= self.ballon.x - cote) and (coin[1] <= self.ballon.y + cote and coin[1] >= self.ballon.y - cote):
                self.ballon.toucher(self.robot.vitesse_lineaire_roue_gauche, self.robot.vitesse_lineaire_roue_droite, self.robot.direction)