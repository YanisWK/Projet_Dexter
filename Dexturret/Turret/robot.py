from math import cos, sin, radians, sqrt 
import logging





"""Documentation : 

    Description generale : Fichier contenant la classe Robot, les fonctions de mises à jour de coordonnées et de déplacement
    Listes des methodes :
    - __init__ => crée une instance Robot
                  la classe utilise des listes velociteD et velociteR, pour stocker les déplacements et les 
                  rotations à chaque rafraîchissement
    - avancer => fait avancer le robot sur une distance donnée
    - tourner => fait tourner le robot dans un angle donné
    - coeff_directeur => retourne le couple (a,b) de la droite directionelle ax+by
                    Ces coefficients sont les composantes du vecteur unitaire dirigeant le robot  
                    - a est la composante horizontale (abscisse)
                    - b est la composante verticale (ordonnée)
                    Ils décrivent la direction associée à l'angle dans le cercle trigonométrique.
    - deplacementRobot => effectue les déplacements du robot avec les fonctions avancer et tourner

    - rafraichir => met à jour les déplacements et positions des coins du robot sur un temps de rafraichissement donné

    - pos_coins_Robot => calcule la position des 4 coins à l'aide de la direction et de la taille du robot

    - detect_distance =>
    - detect_limites =>
"""


class Robot:
    def __init__(self, id, longueur, largeur, rayon_des_roues, x, y):
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

        self.rayon_des_roues = rayon_des_roues

        self.vitesse_lineaire_roue_gauche = 0
        self.vitesse_lineaire_roue_droite = 0

        self.vitesse_de_rotation_roue_gauche = 0
        self.vitesse_de_rotation_roue_droite = 0

        self.pret = False  #La simulation est activée et le robot est en mouvement

    def __getattr__(self,name):
        if name == "coordRobot":
            L = self.longueur / 2
            l = self.largeur / 2
            dir = self.direction
            x = self.x
            y = self.y

            c1 = ( (x + L*cos(radians(dir))) + l*cos(radians(dir + 90)), (y - L*sin(radians(dir))) - l*sin(radians(dir + 90)) )
            c2 = ( (x + L*cos(radians(dir))) + l*cos(radians(dir - 90)), (y - L*sin(radians(dir))) - l*sin(radians(dir - 90)) )
            c3 = ( (x - L*cos(radians(dir))) + l*cos(radians(dir - 90)), (y + L*sin(radians(dir))) - l*sin(radians(dir - 90)) )
            c4 = ( (x - L*cos(radians(dir))) + l*cos(radians(dir + 90)), (y + L*sin(radians(dir))) - l*sin(radians(dir + 90)) )
            return [c1, c2, c3, c4]
        
    
    def __repr__(self):
        return "C'est le robot d'identifiant " + str(self.id) + " qui se trouve en (" + str(self.x) + "," + str(self.y) + ")" + " et est tourné de " + str(self.direction) + "°"


    def avancer(self, distance):
        """
        Déplace le robot en ligne droite en mettant à jour les coordonnées de robot 

        Paramètre :
        - distance : distance à parcourir
        
        """
        logging.info(f'Le Robot a avancé de {distance} cm')

        #mise à jour des coordonnées grâce aux fonctions cosinus/sinus
        self.x += round( distance * cos(radians(self.direction)) , 10)
        self.y -= round( distance * sin(radians(self.direction)) , 10)


    def tourner(self, angle):
        """
        Effectue une rotation en ajustant la direction pour rester dans [0, 360]
        si l'angle n'est pas compris dans [0,360], c'est le modulo 360 sur cet angle qui est ajouté 
        à la direction actuelle

        Paramètre :
        - angle : angle de rotation

        """
        self.direction += angle

        if (self.direction > 360):
            self.direction -= 360
        if (self.direction < 0):
            self.direction += 360

        logging.info(f'Le robot a tourné de {angle}°')
    

    def coeff_directeur(self, angle):
        """
        Retourne (a,b) tel que ax+by représente la droite de la direction dans laquelle le robot est orienté
        Cette droite permet au robot de se déplacer dans la direction voulue en variant x et y

        """
        a = cos(radians(angle))
        b = sin(radians(angle))
        return (a,b)
            
    
    def deplacementRobot(self, temps):
        """
        Calcule la distance de déplacement en ligne droite et la rotation du robot à chaque rafraîchissement, 
        puis met à jour la position et la direction du robot en appelant avancer et tourner
        
        Paramètre :
        - temps : temps par rafraichissement
        
        """       

        #Calcul de la distance que parcourt le robot à chaque rafraîchissement distance_par_rafraichissement = vitesse/temps
        
        self.vitesse_de_rotation_roue_gauche = self.vitesse_lineaire_roue_gauche / self.rayon_des_roues
        self.vitesse_de_rotation_roue_droite = self.vitesse_lineaire_roue_droite / self.rayon_des_roues


        vitesse_deplacement = (self.vitesse_lineaire_roue_gauche+ ( - self.vitesse_lineaire_roue_droite)) / 2
        deplacement_par_rafraichissement = vitesse_deplacement / temps
        self.avancer(deplacement_par_rafraichissement)

        #Calcul de la rotation que le robot doit faire à chaque rafraîchissement

        vitesse_rotation = - ( self.rayon_des_roues*(self.vitesse_de_rotation_roue_gauche + self.vitesse_de_rotation_roue_droite)) / (2 * (self.largeur/2))
        rotation_par_rafraichissement = vitesse_rotation / temps
        self.tourner(rotation_par_rafraichissement)
        

    def rafraichir(self,fps):
        """
        Met à jour les positions des coins du robot et les déplacements du robot

        Paramètre :
        - fps : 
        """
        self.deplacementRobot(fps)


    def detect_limites(self,simu, distx,disty):
        """
        Vérifie si la distance de détection du robot touche une bordure

        Paramètre :
        - simulation : simulation contenant l'environnement dans lequel se déplace le robot
        - distx : point x de l'extremité de la distance de détection
        - disty : point y de l'extremité de la distance de détection
        
        """
        if distx > simu.longueur or disty > simu.largeur:
            return True
        else:
            return False
    

    def detect_distance(self,simu):
        """
        Retourne une distance dans la direction dans laquelle le robot est orienté

        Paramètre :
        - simulation : simulation contenant l'environnement dans lequel se déplace le robot

        """
        #Distance de détection maximale du robot
        dist_max = 1000 #1000 car la dimension max de l'environnement

        px= self.x + dist_max *cos(radians(self.direction ))
        py= self.y + dist_max *sin(radians(self.direction))

        if self.detect_limites(simu):
            #Calcule la distance entre la position du robot et le point d'intersection 
            #entre les coord. des extremités de la distance de détection du robot et la bordure la + proche
            dist = sqrt((self.x - px)**2 + (self.y - py)**2)
            return dist
        else:
            #Retourne la distance de détection max si la distance de détection ne touche pas de bordure
            return dist_max     