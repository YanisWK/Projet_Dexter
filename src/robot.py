from math import cos, sin, radians

"""Documentation : 

    Description generale : Fichier contenant la classe Robot avec ces attributs de position,direction ainsi que sa longueur et largeur
    Listes des methodes : 
    -avancer
    -tourner
    -coeff_directeur
    -
    
"""


class Robot:
    def __init__(self, id, longueur, largeur, x, y):
        self.id=id 
        self.x = x 
        self.y = y
        self.direction = 90
        self.longueur = longueur
        self.largeur = largeur
        self.velociteD = []                 #Liste des déplacements vers l'avant à chaque rafraichissement
        self.velociteR = []                 #Liste des changements de direction à chaque rafraichisement

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


    def avancer(self, distance):
        #calcule le nb de tours nécessaires pour parcourir la distance donnée
        nb_tours = float(distance)/10

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
        -Fonction qui retourne (a,b) tel que ax+by représente la droite de la direction dans laquelle le robot est orienté
        """
        a = cos(radians(angle))
        b = sin(radians(angle))
        return (a,b)
    
   
    def pos_coins_Robot(self):
        """
        -Fonction qui calcule, à l'aide de la taille et de la drection, la position des 4 coins du robot
        -Nécessite obtenirAngle
        -Le centre du rectangle est la position x y du robot
        -Modifier self.coordRobot par la liste des coordonnees des 4 coins
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
    
    def deplacementRobot(self, distance, vitesse, temps):
        """
        -Fonction qui effectue les calcules nécessaire afin de déplacer le robot
        -Ajout dans velociteD les distances à faire à chaque rafraichissement selon la distance à parcourir et la vitesse,
            dans la direction du robot
        -Ne retourne rien
        """
        self.velociteD = []

        #Calcule de la distance que parcoure le robot à chaque rafraîchissement
        distance_par_rafraichissement = vitesse / temps

        #(à voir) Calcule du nombre de rafraîchissements nécessaires pour que le robot puisse parcourir la distance totale
        #nombre_rafraichissements = self.distance / distance_par_rafraichissement

        #La distance que le robot doit parcourir
        distance_a_parcourir = distance

        #Ajout de la distance que le robot parcoure à chaque rafraîchissement dans la liste velociteD 
        if (distance_a_parcourir > 0):
            while distance_a_parcourir > distance_par_rafraichissement:
                    self.velociteD.append(distance_par_rafraichissement)
                    distance_a_parcourir -= distance_par_rafraichissement
        else:
            while distance_a_parcourir < -distance_par_rafraichissement:
                    self.velociteD.append(-distance_par_rafraichissement)
                    distance_a_parcourir += distance_par_rafraichissement
        self.velociteD.append(distance_a_parcourir)
    
    def rotationRobot(self, angle, vitesse, temps):
        """
        -Fonction qui effectue les calcules nécessaire afin de faire une rotation au robot
        -Ajout dans velociteR les modifications d'angles à faire à chaque rafraichissement selon la vitesse
        -Ne retourne rien
        """
        self.velociteR = []
        #Calcule de la rotation que le robot doit tourner à chaque rafraîchissement
        Rotation_par_rafraichissement = vitesse / temps
        
        Angle_a_parcourir = angle
        
        #Ajout de la rotation que le robot parcoure à chaque rafraîchissement dans la liste velociteR
        if (Angle_a_parcourir > 0):
            while Angle_a_parcourir > Rotation_par_rafraichissement:
                self.velociteR.append(Rotation_par_rafraichissement)
                Angle_a_parcourir -= Rotation_par_rafraichissement
        else:
            while Angle_a_parcourir < -Rotation_par_rafraichissement:
                self.velociteR.append(-Rotation_par_rafraichissement)
                Angle_a_parcourir += Rotation_par_rafraichissement

        self.velociteR.append(Angle_a_parcourir)
        return

    def rafraichir(self):
        if self.velociteD or self.velociteR :
            #si le tableau velociteD n'est pas vide alors on avance
            if self.velociteD : 
                self.avancer(self.velociteD.pop(0))
            
            #si le tableau velociteR n'est pas vide alors on tourne
            if self.velociteR : 
                self.tourner(self.velociteR.pop(0))

        self.pos_coins_Robot()