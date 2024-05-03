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
- Strat_for
- Start_while

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
        print("Distance: ", capteur)
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

    def start(self):
        """Démarre l'avancement"""
        print("DEBUT AVANCER")
        self.parcouru = 0
        self.robot.set_position_moteurs(1, self.robot.get_position_moteurs()[0])
        self.robot.set_position_moteurs(2, self.robot.get_position_moteurs()[1])
        self.robot.set_vitesse_roue(3, self.vitesse)

    def etape(self):
        """Effectue une étape de l'avancement en déplaçant le robot en fonction de la vitesse de déplacement
        et du nombre de rafraichissement, tant que la distance n'a pas été entièrement parcourue."""

        if self.stop() :
            self.robot.set_position_moteurs(1, self.robot.get_position_moteurs()[0])
            self.robot.set_position_moteurs(2, self.robot.get_position_moteurs()[1])
            return
        
        self.parcouru = self.robot.calcule_avancer_tourner()[0]

        logging.info(f"Distance parcourue: {self.parcouru}")
        
    def stop(self):
        """Vérifie si l'avancement doit s'arrêter"""
        return self.parcouru >= abs(self.distance) #or self.parcouru >= abs(self.distance) - 2
    

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

    def start(self):
        """Démarre la rotation"""
        print("DEBUT TOURNER")
        self.angle_parcouru = 0
        self.robot.set_position_moteurs(1, self.robot.get_position_moteurs()[0])
        self.robot.set_position_moteurs(2, self.robot.get_position_moteurs()[1])

        vit = 10
        if (self.angle > 0):
            self.robot.set_vitesse_roue(1 , -vit)
            self.robot.set_vitesse_roue(2 , vit)
        else:
            self.robot.set_vitesse_roue(1 , vit)
            self.robot.set_vitesse_roue(2 , -vit)

    def etape(self):
        """Effectue une étape de la rotation en déplaçant le robot en fonction de la vitesse de rotation
        et du nombre de rafraichissement, tant que l'angle n'est pas atteint."""

        if self.stop():
            self.robot.set_position_moteurs(1, self.robot.get_position_moteurs()[0])
            self.robot.set_position_moteurs(2, self.robot.get_position_moteurs()[1])
            return
        
        self.angle_parcouru = self.robot.calcule_avancer_tourner()[1]

        logging.info(f"Angle parcouru: {self.angle_parcouru}")

    def stop(self):
        """Vérifie si la rotation doit s'arrêter"""
        return abs(self.angle) <= self.angle_parcouru #or self.angle_parcouru >= abs(self.angle) - 2
        

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
        """Démarre l'exécution de la liste de stratégies"""
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
        print("DEBUT WHILE")

    def etape(self):        
        """Effectue une étape de la stratégie en vérifiant la condition à chaque tour de boucle"""
        if self.stop():
            print("FIN WHILE")
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
    """
    Crée une séquence d'instructions pour faire avancer le robot en dessinant un carré vers la droite.
    
    Paramètres :
    - Robot: instance du robot
    - distance: distance à parcourir à chaque étape
    - vitesse: vitesse du robot
    - fps: frames par seconde
    - angle: angle de rotation à chaque coin du carré
   """
    strat_av = AvancerRobot(Robot, distance, vitesse, fps)
    strat_td = TournerRobot(Robot, -angle, fps)
    carreD = [strat_av, strat_td, strat_av, strat_td,\
             strat_av, strat_td, strat_av, strat_td]
    return Sequence(carreD)

def getStrat_seq_carreG(Robot,distance,vitesse,fps,angle):
    """Crée une séquence d'instructions pour faire avancer le robot en dessinant un carré vers la gauche."""
    strat_av = AvancerRobot(Robot, distance, vitesse, fps)
    strat_tg = TournerRobot(Robot, angle, fps)
    carreG = [strat_av, strat_tg, strat_av, strat_tg,\
             strat_av, strat_tg, strat_av, strat_tg]
    return Sequence(carreG)

def getStrat_dessine_n_carre(nombre,Robot,distance,vitesse,fps,angle, direction):
    """Crée une séquence d'instructions pour faire dessiner n carrés au robot.
    
    Paramètres :
    - nombre: nombre de carrés à dessiner
    - Robot: instance du robot
    - distance: distance à parcourir à chaque étape
    - vitesse: vitesse du robot
    - fps: frames par seconde
    - angle: angle de rotation  à chaque coin du carré
    - direction: direction dans laquelle dessiner les carrés(1 pour gauche,sinon droite)
    """
    if direction == 1:
        stratCarre = getStrat_seq_carreG(Robot,distance,vitesse,fps,angle)
    else:
        stratCarre = getStrat_seq_carreD(Robot,distance,vitesse,fps,angle)
    carres = []
    for i in range(nombre):
        carres.append(stratCarre)
    return Sequence(carres)

def getStrat_CarresFor(Robot,distance,vitesse,fps,angle):
    """Crée une séquence d'instructions pour faire dessiner trois carrés au robot.
    
    Paramètres :
    - Robot: instance du robot
    - distance: distance à parcourir à chaque étape
    - vitesse: vitesse du robot
    - fps: frames par seconde
    - angle: angle de rotationà chaque coin du carré
    """
    strat_av =AvancerRobot(Robot, distance, vitesse, fps)
    strat_CarreD = getStrat_seq_carreD(Robot,distance,vitesse,fps,angle)
    return Strat_for(3, [strat_CarreD, strat_av])

def getStrat_CarreCondition(Robot,distance,vitesse,fps,angle,long,larg):
    """Crée une séquence d'instructions pour faire dessiner des carrés au robot en fonction d'une condition.
    
    Paramètres :
    - Robot: instance du robot
    - distance: distance à parcourir à chaque étape
    - vitesse: vitesse du robot
    - fps: frames par seconde
    - angle: angle de rotation à chaque coin du carré
    - long,larg: dimensions de la simulation
    """
    dist_sup= CompareDistance(Robot, 100, long, larg)
    stratAvancer =AvancerRobot(Robot, distance, vitesse, fps)
    stratTournerDroite = TournerRobot(Robot, -angle, fps)
    cote_condition = Strat_if(dist_sup, [stratAvancer, stratTournerDroite])
    return Sequence([cote_condition, cote_condition, cote_condition, cote_condition])

def getStrat_AvancerViteMur(Robot,distance,vitesse,fps,long,larg):
    """Crée une séquence d'instructions pour faire avancer rapidement le robot vers un mur.
    
    Paramètres :
    - Robot: instance du robot
    - distance: distance à parcourir à chaque étape
    - vitesse: vitesse du robot
    - fps: frames par seconde
    - long,larg: dimensions de la simulation
    """
    avancerPeu = AvancerRobot(Robot, 5, vitesse, fps)
    dist_sup = CompareDistance(Robot, distance, long, larg)
    return Strat_while(dist_sup, [avancerPeu])