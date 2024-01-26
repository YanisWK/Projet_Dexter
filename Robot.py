from math import *

<<<<<<< HEAD

=======
>>>>>>> fedd047aa38d3cd32a4f5c07865148b5c238fff6
class Robot:
    def __init__(self, id):
        self.id = id
        self.x = 0.0
        self.y = 0.0
<<<<<<< HEAD
        self.direction = 90
=======
        self.direction = 90 #direction en degrés
>>>>>>> fedd047aa38d3cd32a4f5c07865148b5c238fff6
        self.unite_de_temps = 10 #inutile pour le moment

    def __repr__(self):
        return "C'est le robot d'identifiant " + str(self.id) + " qui se trouve en (" + str(self.x) + "," + str(self.y) + ")" + " et est tourné de " + str(self.direction) + "°"
<<<<<<< HEAD

        self.direction = 0
        self.unite_de_temps = 10 #inutile pour le moment

    def __repr__(self):
        return "C'est le robot d'identifiant " + str(self.id) + " se trouve en (" + str(self.x) + "," + str(self.y) + ")" + " et est tourné de " + str(self.direction) + "°"
=======
>>>>>>> fedd047aa38d3cd32a4f5c07865148b5c238fff6
    
    #Méthodes pour faire tourner les roues
    def tourner_roue_gauche_avant(self, nb_tours):
        #à déterminer selon la taille des roues? Pour l'instant 1 tour = 10cm 
        #Et on pars du principe que la roue tourne à 6 tour / min (ce qui est très lent)
        print("La roue gauche tourne de ", nb_tours, " tours vers l'avant")

    def tourner_roue_droite_avant(self, nb_tours):
        #même problème que pour la roue gauche
        print("La roue droite tourne de ", nb_tours, " tours vers l'avant")

    def tourner_roue_gauche_arriere(self, nb_tours):
        #même problème que vers l'avant
        print("La roue gauche tourne de ", nb_tours, " tours vers l'arrière")

    def tourner_roue_droite_arriere(self, nb_tours):
        #même problème que vers l'avant
        print("La roue droite tourne de ", nb_tours, " tours vers l'arrière")
    
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
        self.tourner_roue_gauche_avant(nb_tours)
        self.tourner_roue_droite_avant(nb_tours)

        print("La voiture a avancé de ", distance, "cm")

<<<<<<< HEAD
        self.x += round( distance * cos(radians(self.direction)) , 10)
        self.y += round( distance * sin(radians(self.direction)) , 10)
        #Mettre à jour les coordonnées x et y (triginonmétrie)
=======
        #màj des coordonnées (trigonométrie) en fonction de la direction actuelle
        self.x += round( distance * cos(radians(self.direction)) , 10)
        self.y += round( distance * sin(radians(self.direction)) , 10)
>>>>>>> fedd047aa38d3cd32a4f5c07865148b5c238fff6

    def reculer(self, distance):
        nb_tours = float(distance)/10

        #Il faut les faire tourner en même temps
        self.tourner_roue_gauche_arriere(nb_tours)
        self.tourner_roue_droite_arriere(nb_tours)

        print("La voiture a reculé de ", distance, "cm")

<<<<<<< HEAD

=======
        #màj des coordonnées (trigonométrie)
>>>>>>> fedd047aa38d3cd32a4f5c07865148b5c238fff6
        self.x -= round( distance * cos(radians(self.direction)) , 10)
        self.y -= round( distance * sin(radians(self.direction)) , 10)

        #Mettre à jour les coordonnées

    def tourner_a_gauche(self, angle):
        nb_tours = float(angle) / 10
        self.tourner_roue_droite_avant(nb_tours)
<<<<<<< HEAD

        self.direction += angle
        if (self.direction > 360):
            self.direction -= 360

        self.direction -= angle
        if (self.direction < 0):
            self.direction += 360

=======
        self.direction += angle
        if (self.direction > 360):
            self.direction -= 360
>>>>>>> fedd047aa38d3cd32a4f5c07865148b5c238fff6
        print("Le robot a tourné de ", angle, "° à gauche")

    def tourner_a_droite(self, angle):
        nb_tours = float(angle) / 10
        self.tourner_roue_gauche_avant(nb_tours)
<<<<<<< HEAD

=======
>>>>>>> fedd047aa38d3cd32a4f5c07865148b5c238fff6
        self.direction -= angle
        if (self.direction < 0):
            self.direction += 360
        print("Le robot a tourné de ", angle, "° à droite")
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getDirection(self):
        return self.direction
    
    def getUniteTemps(self):
        return self.unite_de_temps
    
    def setDirection(self, dire):
        self.direction = dire

    def setX(self,x):
        self.x = x

    def setY(self,y):
        self.y = y
    
<<<<<<< HEAD

        self.direction += angle
        if (self.direction > 360):
            self.direction -= 360
        print("Le robot a tourné de ", angle, "° à droite")

    def trace_carre(self, distance):
        for i in range(4):
            self.avancer(distance)
            self.tourner_a_droite(90)

=======
>>>>>>> fedd047aa38d3cd32a4f5c07865148b5c238fff6
