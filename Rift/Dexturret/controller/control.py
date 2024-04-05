from math import degrees
import logging
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
    def __init__(self, robot, distance, longueurSimu, largeurSimu):
        """
        -Est une condition
        -Utilise le capteur de distance de robot
        -Retourne si la distance que le robot capte est > a la distance en parametre si celle-ci est positive
        -Et verifie si la distance est < a la distance en parametre si celle-ci est negative
        """
        self.robot = robot
        self.distance = distance
        self.longueurSimu = longueurSimu
        self.largeurSimu = largeurSimu

    def start(self):
        """Démarre la comparaison de la distance entre le robot et distance"""
        capteur = self.robot.detect_distance(self.longueurSimu, self.largeurSimu)
        if(self.distance < 0):
            return abs(self.distance) > capteur
        return self.distance < capteur
        

class AvancerRobot():
    """
    Classe qui gére l'avancement du robot
    Est une strategie de base
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
        self.robot.derniere_position_moteurs = robot.get_position_moteurs()

    def start(self):
        """Démarre l'avancement"""
        print("DEBUT AVANCER")
        self.parcouru = 0
        self.robot.set_position_moteurs(1, self.robot.get_position_moteurs()[0])
        self.robot.set_position_moteurs(2, self.robot.get_position_moteurs()[1])
        self.robot.derniere_position_moteurs = self.robot.get_position_moteurs()

    def etape(self):
        """Effectue une étape de l'avancement en déplaçant le robot en fonction de la vitesse de déplacement
        et du nombre de rafraichissement, tant que la distance n'a pas été entièrement parcourue."""

        self.robot.set_vitesse_roue(3,self.vitesse)

        self.parcouru += self.robot.calcule_avancer_tourner()[0]


        logging.info(f"Distance parcourue: {self.parcouru}")

        if self.stop() :
            return
        
    def stop(self):
        """Vérifie si l'avancement doit s'arrêter"""
        return self.parcouru >= abs(self.distance) or self.parcouru >= abs(self.distance) - 2
    

class TournerRobot():
    """    
    Classe qui gére la rotation du robot
    Est une strategie de base
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
        self.robot.derniere_position_moteurs = robot.get_position_moteurs()

    def start(self):
        """Démarre la rotation"""
        print("DEBUT TOURNER")
        self.angle_parcouru = 0
        self.robot.set_position_moteurs(3, 0)
        self.robot.derniere_position_moteurs = self.robot.get_position_moteurs()

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

        
        self.angle_parcouru += self.robot.calcule_avancer_tourner()[1]

        logging.info(f"Angle parcouru: {self.angle_parcouru}")

    def stop(self):
        """Vérifie si la rotation doit s'arrêter"""
        return abs(self.angle) <= self.angle_parcouru or self.angle_parcouru >= abs(self.angle) - 2
        

class Sequence():
    """
    Est une strategie qui est compose d'autres strategies
    """
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
        return self.current >= len(self.strats)-1 and self.strats[self.current].stop()
    

class Strat_if():
    """
    Est une stratégie conditionnelle qui effectue la liste de strategie si que la condition est valide
    """ 
    def __init__(self, condition, strats):
        """
        Paramètres:
        - condition : condition à checker avant de faire une instruction
        - strats : stratégie séquentielle à effectuer si la condition est remplie
        """
        self.condition = condition
        self.strats = strats
        self.current = -1
        self.condi = False
    
    def start(self):
        """Démarre l'exécution"""
        self.current = -1
        self.condi = self.condition.start()

    def etape(self):
        """Effectue une étape de la stratégie en vérifiant si la condition est remplie"""
        if self.stop():
            return
        
        if self.current < 0 or self.strats[self.current].stop():
            self.current += 1
            self.strats[self.current].start()
        self.strats[self.current].etape()

    def stop(self):
        """Arrête la stratégie si la dernière instruction est terminée ou si la condition n'est pas remplie"""
        return (self.current >= len(self.strats)-1 and self.strats[self.current].stop()) or not(self.condi)
    
class Strat_while():
    """
    Est une stratégie conditionnelle qui effectue la liste de strategie tant que la condition est valide
    """
    def __init__(self, condition, strats):
        """
        Paramètres:
        - condition : condition a verifier a chaque tour de boucle
        - strats : liste des strategies a effectuer
        """
        self.condition = condition
        self.strats = strats
        self.current = -1
        self.condi = False

    def start(self):
        """Démarre l'exécution"""
        self.current = -1
        self.condi = self.condition.start()

    def etape(self):        
        """Effectue une étape de la stratégie en vérifiant la condition à chaque tour de boucle"""
        if self.stop():
            return
        
        if self.current < 0 or self.strats[self.current].stop():
            self.current += 1

            if (self.current == len(self.strats)):
                self.current = 0
                self.condi = self.condition.start()

            self.strats[self.current].start()
        self.strats[self.current].etape()

    def stop(self):
        """Arrête la stratégie si la condition n'est plus valide"""
        return not(self.condi)
    
class Strat_for():
    """
    Est une strategie séquentielle qui effectue un nombre défini de fois une liste de strategies
    """
    def __init__(self, max, strats):
        """
        Parametres:
        - max: le nombre de tour de boucle
        - strats: la liste des strategies a effectuer a chaque tour de boucle
        """
        self.max = max
        self.strats = strats
        self.current = -1
        self.boucle = 0

    def start(self):
        """Démarre l'exécution"""
        self.current = -1
        self.boucle = 0

    def etape(self):    
        """Effectue une étape"""
        if self.current < 0 or self.strats[self.current].stop():
            self.current += 1

            if (self.current == len(self.strats)):
                self.current = 0
                self.boucle += 1
            self.strats[self.current].start()

        if self.stop():
            return
        
        self.strats[self.current].etape()

    def stop(self):
        """Arrête la stratégie lorsque le nombre de tours de boucle atteint le max"""
        return self.boucle >= self.max
    
def getStrat_seq_carreD(Robot,distance,vitesse,fps,angle):
    strat_av = AvancerRobot(Robot, distance, vitesse, fps)
    strat_td = TournerRobot(Robot, -angle, fps)
    carreD = [strat_av, strat_td, strat_av, strat_td,\
             strat_av, strat_td, strat_av, strat_td]
    return Sequence(carreD)

def getStrat_seq_carreG(Robot,distance,vitesse,fps,angle):
    strat_av = AvancerRobot(Robot, distance, vitesse, fps)
    strat_tg = TournerRobot(Robot, angle, fps)
    carreG = [strat_av, strat_tg, strat_av, strat_tg,\
             strat_av, strat_tg, strat_av, strat_tg]
    return Sequence(carreG)

def getStrat_dessine_n_carre(nombre,Robot,distance,vitesse,fps,angle, direction):
    if direction == 1:
        stratCarre = getStrat_seq_carreG(Robot,distance,vitesse,fps,angle)
    else:
        stratCarre = getStrat_seq_carreD(Robot,distance,vitesse,fps,angle)
    carres = []
    for i in range(nombre):
        carres.append(stratCarre)
    return Sequence(carres)

def getStrat_CarresFor(Robot,distance,vitesse,fps,angle):
    strat_av =AvancerRobot(Robot, distance, vitesse, fps)
    strat_CarreD = getStrat_seq_carreD(Robot,distance,vitesse,fps,angle)
    return Strat_for(3, [strat_CarreD, strat_av])