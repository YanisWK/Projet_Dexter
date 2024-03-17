import turret
import controller
from math import sqrt, degrees, radians

"""
Documentation:
Ce module définit plusieurs classes contrôlant un robot simulé qui peut avancer, tourner, tracer un carré et avancer vite vers un mur.
Chaque classe propose des méthodes pour démarrer, effectuer une étape, et s'arrêter en fonction de l'état du robot.

Classes:
- AvancerRobot
- TournerRobot
- AvancerViteRobot
- TracerCarre
- AvancerViteMur

"""

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
        self.parcouru = 0
        self.derniere_position_moteurs = self.robot.get_position_moteurs()

    def etape(self):
        """Effectue une étape de l'avancement en déplaçant le robot en fonction de la vitesse de déplacement
        et du nombre de rafraichissement, tant que la distance n'a pas été entièrement parcourue."""
        self.robot.set_vitesse_roue(3,self.vitesse)

        nouvelle_position_moteurs = self.robot.get_position_moteurs()

        dist_RG = abs(self.derniere_position_moteurs[0] - nouvelle_position_moteurs[0]) * self.robot.rayon_des_roues
        dist_RD = abs(self.derniere_position_moteurs[1] - nouvelle_position_moteurs[1]) * self.robot.rayon_des_roues
        self.parcouru += (dist_RG + dist_RD) / 2

        self.derniere_position_moteurs = self.robot.get_position_moteurs()

        if self.stop() :
            self.robot.set_vitesse_roue(3,0)
            return
        
    def stop(self):
        """Vérifie si l'avancement doit s'arrêter"""
        return self.parcouru >= self.distance or self.parcouru >= self.distance - 2
    

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
        self.angle_parcouru = 0
        self.derniere_position_moteurs = self.robot.get_position_moteurs()

    def etape(self):
        """Effectue une étape de la rotation en déplaçant le robot en fonction de la vitesse de rotation
        et du nombre de rafraichissement, tant que l'angle n'est pas atteint."""
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

        self.angle_parcouru += degrees(abs((self.robot.rayon_des_roues * (angle_RD - angle_RG)) / self.robot.largeur))

        self.derniere_position_moteurs = nouvelle_position_moteurs

        if self.stop():
            return

    def stop(self):
        """Vérifie si la rotation doit s'arrêter"""
        print(self.angle_parcouru)
        print(self.robot.direction)
        return abs(self.angle) <= self.angle_parcouru or self.angle_parcouru >= abs(self.angle) - 1
    

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
            self.robot.vitesse_lineaire_roue_gauche = 0
            self.robot.vitesse_lineaire_roue_droite = 0
            return

    def stop(self):
        """Arrête le robot en fonction de la distance qui le sépare des bordures de la simulation"""
        return self.robot.detect_distance(self.simu.longueur, self.simu.largeur) <= self.robot.largeur



class TracerCarre():
    """Classe qui permet au robot de tracer un carré"""
    def __init__(self, robot, tailleCote, vitesse, fps):
        """
        Paramètres:
        - robot : robot à faire avancer
        - tailleCote : taille du coté du carré
        - vitesse : vitesse du robot
        - fps : frame par seconde
        """
        self.robot = robot
        self.tailleCote = tailleCote
        self.vitesse = vitesse
        stratAvancer = AvancerRobot(self.robot, self.tailleCote, self.vitesse, fps)
        stratTourner = TournerRobot(self.robot, 90, fps)
         #Besoin de savoir a chaque fois qu'on tourne de combien de degrès il faut tourner.

        self.strats = [stratAvancer,stratTourner,stratAvancer,stratTourner,stratAvancer,stratTourner,stratAvancer,stratTourner]
        self.current = -1

    def start(self):
        """Démarre le traçage du carré"""
        self.current = -1

    def etape(self):
        """Effectue le traçage du carré en appelant les classes AvancerRobot et TournerRobot alternativement"""
        if self.stop():
            return
        if self.current < 0 or self.strats[self.current].stop():
            self.current += 1
            self.strats[self.current].start()
        self.strats[self.current].etape()

    def stop(self):
        """Arrête le traçage du carré en appelant la méthode stop() de la dernière stratégie"""
        return self.current == len(self.strats)-1 and self.strats[self.current].stop()

class AvancerViteMur():
    """Fait avancer le robot rapidement en fonction des limites de la simulation"""
    def __init__(self, robot, simu, vitesse, fps):
        """
        Paramètres:
        - robot : robot à faire avancer
        - simu : simulation dans laquelle se déplace le robot
        - vitesse : vitesse du robot
        - fps : frame par seconde
        """
        self.robot = robot
        self.simu = simu
        self.vitesse = vitesse
        StratAvancerVite = AvancerViteRobot(self.robot, self.simu, self.vitesse, fps)
        self.strats = [StratAvancerVite]
        self.current = -1

    def start(self):
        """Démarre l'avancement du robot"""
        self.current = -1

    def etape(self):
        """Effectue l'avancement en appelant la méthode etape de la stratégie AvancerVite et
        met les vitesses des roues à 0, sinon"""
        if self.stop():
            return
        if self.current < 0 or self.strats[self.current].stop():
            self.current += 1
            self.strats[self.current].start()
        self.strats[self.current].etape()

    def stop(self):
        """Arrête le robot en appelant la méthode stop() de la dernière stratégie"""
        return self.current == len(self.strats)-1 and self.strats[self.current].stop()
    

class Instructions():
    def __init__(self, strats):
        """
        Paramètres:
        - robot : robot à faire avancer
        - simu : simulation dans laquelle se déplace le robot
        - vitesse : vitesse du robot
        - fps : frame par seconde
        """
        self.current = -1
        self.strats = strats

    def start(self):
        """Démarre l'avancement du robot"""
        self.current = -1

    def etape(self):
        """Effectue l'avancement en appelant la méthode etape de la stratégie AvancerVite et
        met les vitesses des roues à 0, sinon"""
        if self.stop():
            return
        if self.current < 0 or self.strats[self.current].stop():
            self.current += 1
            self.strats[self.current].start()
        self.strats[self.current].etape()

    def stop(self):
        """Arrête le robot en appelant la méthode stop() de la dernière stratégie"""
        return self.current == len(self.strats)-1 and self.strats[self.current].stop()