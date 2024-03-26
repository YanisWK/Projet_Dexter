from math import degrees

"""
Documentation:
Ce module définit plusieurs classes contrôlant un robot simulé qui peut avancer, tourner, tracer un carré et avancer vite vers un mur.
Chaque classe propose des méthodes pour démarrer, effectuer une étape, et s'arrêter en fonction de l'état du robot.

Classes:
- CompareDistance
- AvancerRobot
- TournerRobot
- AvancerViteRobot
- Instructions
- Strat_if

"""

class CompareDistance():
    def __init__(self,robot,distance,longueurSimu,largeurSimu):
        """
        Paramètres:
        - robot : robot à faire avancer
        - distance : distance à parcourir
        - longueurSimu, largeurSimu : dimensions de la simulation
        """
        self.robot=robot
        self.distance=distance
        self.longueurSimu=longueurSimu
        self.largeurSimu=largeurSimu
    def start(self):
        """Démarre la comparaison de la distance entre le robot et distance"""
        capteur=self.robot.detect_distance(self.longueurSimu,self.largeurSimu)
        if(self.distance<0):
            return abs(self.distance)>capteur
        else:
            return self.distance<capteur
        

class AvancerRobot():
    """
    Classe qui gére l'avancement du robot
    """
    def __init__(self, robot, distance, vitesse, fps):
        """
        Paramètres:
        - robot : robot à faire avancer
        - distance : distance à parcourir
        - vitesse : vitesse de l'avancement
        - fps : frame par seconde
        """
        self.robot = robot
        self.distance = distance
        self.vitesse = vitesse
        self.fps = fps
        self.derniere_position_moteurs = robot.get_position_moteurs()

    def start(self):
        """Démarre l'avancement"""
        print("DEBUT AVANCER")
        self.parcouru = 0
        self.robot.set_position_moteurs(3, 0)
        self.derniere_position_moteurs = self.robot.get_position_moteurs()

    def etape(self):
        """Effectue une étape de l'avancement en déplaçant le robot en fonction de la vitesse de déplacement
        et du nombre de rafraichissement, tant que la distance n'a pas été entièrement parcourue."""

        self.robot.set_vitesse_roue(3,self.vitesse)
        nouvelle_position_moteurs = self.robot.get_position_moteurs()

        dist_RG = abs(self.derniere_position_moteurs[0] - nouvelle_position_moteurs[0]) * (self.robot.rayon_des_roues/100)
        dist_RD = abs(self.derniere_position_moteurs[1] - nouvelle_position_moteurs[1]) * (self.robot.rayon_des_roues/100)
        self.parcouru += (dist_RG + dist_RD) / 2

        self.derniere_position_moteurs = nouvelle_position_moteurs

        print("Distance parcourue: ", self.parcouru)

        if self.stop() :
            return
        
    def stop(self):
        """Vérifie si l'avancement doit s'arrêter"""
        return self.parcouru >= abs(self.distance) or self.parcouru >= abs(self.distance) - 2
    

class TournerRobot():
    """    
    Classe qui gére la rotation du robot
    """
    def __init__(self, robot, angle, fps):
        """
        Paramètres:
        - robot : robot à faire avancer
        - angle : taille de l'angle en degrés
        - fps : frame par seconde
        """
        self.robot = robot
        self.angle = angle
        self.fps = fps
        self.derniere_position_moteurs = robot.get_position_moteurs()

    def start(self):
        """Démarre la rotation"""
        print("DEBUT TOURNER")
        self.angle_parcouru = 0
        self.robot.set_position_moteurs(3, 0)
        self.derniere_position_moteurs = self.robot.get_position_moteurs()

    def etape(self):
        """Effectue une étape de la rotation en déplaçant le robot en fonction de la vitesse de rotation
        et du nombre de rafraichissement, tant que l'angle n'est pas atteint."""
        if self.stop():
            return

        vit = 10
        if (self.angle > 0):
            self.robot.set_vitesse_roue(1 , -vit)
            self.robot.set_vitesse_roue(2 , vit)
        else:
            self.robot.set_vitesse_roue(1 , vit)
            self.robot.set_vitesse_roue(2 , -vit)

        nouvelle_position_moteurs = self.robot.get_position_moteurs()

        angle_RG = nouvelle_position_moteurs[0] - self.derniere_position_moteurs[0]
        angle_RD = nouvelle_position_moteurs[1] - self.derniere_position_moteurs[1]

        self.angle_parcouru += degrees(abs(((self.robot.rayon_des_roues/100) * (angle_RD - angle_RG)) / self.robot.largeur))

        self.derniere_position_moteurs = nouvelle_position_moteurs

        print("Angle parcouru: ", self.angle_parcouru)

    def stop(self):
        """Vérifie si la rotation doit s'arrêter"""
        return abs(self.angle) <= self.angle_parcouru or self.angle_parcouru >= abs(self.angle) - 2
    

class AvancerViteRobot():
    """Gère le déplacement rapide linéaire du robot"""
    def __init__(self, robot, simu, vitesse):
        """
        Paramètres:
        - robot : robot à faire avancer
        - simu : simulation dans laquelle se déplace le robot
        - vitesse : vitesse du robot
        """
        self.robot = robot
        self.simu = simu
        self.vitesse = vitesse

    def start(self):
        """Démarre l'avancement en fonction de la vitesse spécifiée"""
        self.robot.set_vitesse_roue(3,self.vitesse)

    def etape(self):
        """
        Fait avancer le robot tant que le mur n'est pas atteint et
        arrête le robot en réglant la vitesse de ses roues à zéro, sinon
        """
        if self.stop():
            return

    def stop(self):
        """Arrête le robot en fonction de la distance qui le sépare des bordures de la simulation"""
        return self.robot.detect_distance(self.simu.longueur, self.simu.largeur) <= self.robot.largeur
        

class Instructions():
    def __init__(self, strats):
        """
        Paramètre:
        - strats : liste d'instructions à effectuer
        """
        self.current = -1
        self.strats = strats

    def start(self):
        """Démarre l'exécution de lla liste de stratégies"""
        self.current = -1

    def etape(self):
        """Exécute chaque instruction de la liste avec ses fonctions start et etape tout en testant sa fonction stop"""
        if self.stop():
            return
        if self.current < 0 or self.strats[self.current].stop():
            self.current += 1
            self.strats[self.current].start()
        self.strats[self.current].etape()

    def stop(self):
        """Stoppe le robot si la dernière instruction est terminée"""
        return self.current == len(self.strats)-1 and self.strats[self.current].stop()
    

class Strat_if():
    def __init__(self, condition, strats):
        """
        Paramètres:
        - condition : condition à checker avant de faire une instruction
        - strats : stratégie séquentielle à effectuer si la condition est remplie
        """
        self.condition = condition
        self.strats = strats
        self.current = -1
        self.bool = False
    
    def start(self):
        """"""
        self.bool = self.condition.start()
        self.current = -1

    def etape(self):
        """"""
        if self.stop():
            return
        if self.current < 0 or self.strats[self.current].stop():
            self.current += 1
            self.strats[self.current].start()
        self.strats[self.current].etape()

    def stop(self):
        """"""
        return (self.current == len(self.strats)-1 and self.strats[self.current].stop()) or not(self.bool)