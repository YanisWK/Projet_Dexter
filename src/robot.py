from math import cos, sin, radians

"""Documentation : 

    Description generale : Fichier contenant la classe Robot avec ces attributs de position,direction ainsi que sa longueur et largeur
    Listes des methodes :
    - __init__ => crée une instance Robot
                  la classe utilise des listes velociteD et velociteR, pour stocker les déplacements et les 
                  rotations à chaque rafraîchissement
    -avancer =>
    -tourner =>
    - coeff_directeur => retourne le couple (a,b) de la droite directionelle ax+by
                    Ces coefficients sont les composantes du vecteur unitaire dirigeant le robot  
                    - a est la composante horizontale (abscisse)
                    - b est la composante verticale (ordonnée)
                    Ils décrivent la direction associée à l'angle dans le cercle trigonométrique.

    - rafraichir => effectue les déplacements avancer/tourner à l'aide des listes velociteD et velociteR et 
                    gère les collisions avec les bords de l'environnement

    - pos_coins_Robot => calcule la position des 4 coins à l'aide de la direction et de la taille du robot

    - deplacementRobot => fait avancer ou reculer le robot dans sa direction actuelle, 
                        en fonction des déplacements contenus dans velociteD et en fonction de la vitesse

    - rotationRobot => fait tourner le robot en fonction des modifs d'angles contenues dans velociteR et 
                    en fonction de la vitesse

"""


class Robot:
    def __init__(self, id, longueur, largeur, x, y):
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
        self.vitesseRoueG = 0
        self.vitesseRoueD = 0
        self.pret = False  #Si la simulation est en pause et le robot est prêt, le robot se rafraichit 
        #Les 4 coins du robot delon la position du centre et la taille du robot
        L = self.longueur / 2
        l = self.largeur / 2
        dir = self.direction
        x = self.x
        y = self.y


        self.coordRobot = [(x-l, y-L), (x+l, y-L), (x+l, y+L), (x-l, y+L)]

    def __repr__(self):
        return "C'est le robot d'identifiant " + str(self.id) + " qui se trouve en (" + str(self.x) + "," + str(self.y) + ")" + " et est tourné de " + str(self.direction) + "°"

        self.direction = 0
        self.unite_de_temps = 10 #inutile pour le moment

    #à déterminer selon la taille des roues? Pour l'instant 1 tour = 10cm 
    #Et on part du principe que la roue tourne à 6 tour / min (ce qui est très lent)

    #Les instructions pour faire tourner les roues sont a déterminer, 
    #Les roues a priori tourneront tout le temps à la même vitesse, mais pas nécessairement dans le même sens
    #Il faut donc déterminer le nb de tours à faire pour parcourir une distance donnée
    #Ces fonctions vous permettront de faire tourner les roues dans un sens ou dans l'autre
    #Il faudt les appeler dans les méthodes avancer, reculer, tourner_a_gauche et tourner_a_droite
    #Fin des méthodes pour faire tourner les roues


    #Fonction non réaliste permettant de simuler les mouvements du robot
    def avancer(self, distance):
        #calcule le nb de tours nécessaires pour parcourir la distance donnée
        #nb_tours = float(distance)/10

        #Il faut les faire tourner en même temps
        #fait tourner les roues gauche et droite en avant pendant le nb de tours calculé
        #self.tourner_roue_gauche_avant(nb_tours)
        #self.tourner_roue_droite_avant(nb_tours)

        print("Le Robot a avancé de ", distance, "cm")

        self.x += round( distance * cos(radians(self.direction)) , 10)
        self.y -= round( distance * sin(radians(self.direction)) , 10)
        #Mettre à jour les coordonnées x et y en fonction de la direction et de la distance
        #arrondit les résultats à 10 chiffres après la virgule

    def tourner(self, angle):
        #calcule le nb de tours pour tourner à gauche de l'angle donné
        #nb_tours = float(angle) / 10

        #tourne la roue droite en avant pendant le nb de tours 
        #self.tourner_roue_droite_avant(nb_tours)

        self.direction += angle

        #ajuste la direction pour rester dans [0, 360)
        if (self.direction > 360):
            self.direction -= 360
        if (self.direction < 0):
            self.direction += 360

        print("Le robot a tourné de ", angle, "°")
    

    def coeff_directeur(self, angle):
        """
        Retourne (a,b) tel que ax+by représente la droite de la direction dans laquelle le robot est orienté
        Cette droite permet au robot de se déplacer dans la direction voulue en variant x et y

        """
        a = cos(radians(angle))
        b = sin(radians(angle))
        return (a,b)
    
   
    def pos_coins_Robot(self):
        """
        - Calcule, à l'aide des dimensions du robot et de la direction, la position des 4 coins du robot
        - Nécessite obtenirAngle
        - Le centre du rectangle est la position x y du robot
        - Modifie self.coordRobot par la liste des coordonnees des 4 coins

        """
        L = self.longueur / 2
        l = self.largeur / 2
        dir = self.direction
        x = self.x
        y = self.y


        c1 = ( (x + L*cos(radians(dir))) + l*cos(radians(dir + 90)), (y - L*sin(radians(dir))) - l*sin(radians(dir + 90)) )
        c2 = ( (x + L*cos(radians(dir))) + l*cos(radians(dir - 90)), (y - L*sin(radians(dir))) - l*sin(radians(dir - 90)) )
        c3 = ( (x - L*cos(radians(dir))) + l*cos(radians(dir - 90)), (y + L*sin(radians(dir))) - l*sin(radians(dir - 90)) )
        c4 = ( (x - L*cos(radians(dir))) + l*cos(radians(dir + 90)), (y + L*sin(radians(dir))) - l*sin(radians(dir + 90)) )
        self.coordRobot = [c1, c2, c3, c4]
        
    
    def deplacementRobot(self, temps):
        """
        Effectue les calculs nécessaires afin de déplacer le robot :
        - Ajoute dans velociteD les distances à faire à chaque rafraichissement en fonction de la distance 
        à parcourir et la vitesse, dans la direction du robot

        """

        #Calcule de la distance que parcoure le robot à chaque rafraîchissement
        #distance_par_rafraichissement = vitesse / temps

        vitesse_deplacement = self.vitesseRoueG + self.vitesseRoueD
        deplacement_par_rafraichissement = vitesse_deplacement / temps
        self.avancer(deplacement_par_rafraichissement)

        #Calcule de la rotation que le robot doit tourner à chaque rafraîchissement

        vitesse_rotation = self.vitesseRoueG - self.vitesseRoueD
        rotation_par_rafraichissement = vitesse_rotation / temps
        self.tourner(rotation_par_rafraichissement)
        

    def rafraichir(self,temps):
        """
        Met à jour les positions des coins du robot et les déplacements du robot
        """
        self.deplacementRobot(temps)
        self.pos_coins_Robot()