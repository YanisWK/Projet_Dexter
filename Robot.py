class Robot:
    def __init__(self, id):
        self.id = id
        self.x = 0.0
        self.y = 0.0
        self.direction = 0
        self.unite_de_temps = 10 #inutile pour le moment

    def __repr__(self):
        return "C'est le robot d'identifiant " + str(self.id) + " se trouve en (" + str(self.x) + "," + str(self.y) + ")" + " et est tourné de " + str(self.direction) + "°"
    
    def tourner_roue_gauche_avant(self, nb_tours):
        #à déterminer selon la taille des roues? Pour l'instant 1 tour = 10°, 1 tour = 10cm
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

    def avancer(self, distance):
        nb_tours = float(distance)/10

        #Il faut les faire tourner en même temps
        self.tourner_roue_gauche_avant(nb_tours)
        self.tourner_roue_droite_avant(nb_tours)

        print("La voiture a avancé de ", distance, "cm")

        #Mettre à jour les coordonnées x et y (triginonmétrie)

    def reculer(self, distance):
        nb_tours = float(distance)/10

        #Il faut les faire tourner en même temps
        self.tourner_roue_gauche_arriere(nb_tours)
        self.tourner_roue_droite_arriere(nb_tours)

        print("La voiture a reculé de ", distance, "cm")

        #Mettre à jour les coordonnées


    def tourner_a_gauche(self, angle):
        nb_tours = float(angle) / 10
        self.tourner_roue_droite_avant(nb_tours)
        self.direction -= angle
        if (self.direction < 0):
            self.direction += 360
        print("Le robot a tourné de ", angle, "° à gauche")

    def tourner_a_droite(self, angle):
        nb_tours = float(angle) / 10
        self.tourner_roue_gauche_avant(nb_tours)
        self.direction += angle
        if (self.direction > 360):
            self.direction -= 360
        print("Le robot a tourné de ", angle, "° à droite")