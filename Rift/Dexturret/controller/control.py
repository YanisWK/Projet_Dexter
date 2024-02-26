import Turret
update_time=60


class Avancer():
    def __init__(self, robot, distance, vitesse):
        self.robot = robot
        self.distance = distance
        self.vitesse = vitesse

    def start(self):
        self.parcouru=0

    def etape(self):
        self.robot.vitesse_lineaire_roue_gauche = self.vitesse
        self.robot.vitesse_lineaire_roue_droite = self.vitesse
        self.parcouru+=self.distance #Comment obtenir la relle distance parcourue?
        if self.stop() :
            self.robot.vitesse_lineaire_roue_gauche = 0
            self.robot.vitesse_lineaire_roue_droite = 0
            return
        
    def stop(self):
        return self.parcouru >= self.distance
    

class Tourner():
    def __init__(self, robot, angle, vitesse):
        self.robot = robot
        self.angle=angle
        self.vitesse = vitesse

    def start(self):
        self.angle_parcouru = 0

    def etape(self):
        self.robot.vitesse_lineaire_roue_gauche = self.vitesse
        self.robot.vitesse_lineaire_roue_droite = -self.vitesse
        self.angle_parcouru += self.angle #Comment obtenir l'angle que le robot a reellement parcouru?

        if self.stop():
            self.robot.vitesse_lineaire_roue_gauche = 0
            self.robot.vitesse_lineaire_roue_droite = 0
            return

    def stop(self):
        return self.angle_parcouru >= self.angle
    

class TracerCarre():
    def __init__(self,tailleCote):
        stratAvancer = Avancer(tailleCote)
        stratTourner = Tourner(90) #Besoin de savoir a chaque fois qu'on tourne de combien de degrès il faut tourner.

        self.strats = [stratAvancer,stratTourner,stratAvancer,stratTourner,stratAvancer,stratTourner,stratAvancer,stratTourner]
        self.tailleCote=tailleCote
        self.current = -1

    def start(self):
        self.current = -1

    def etape(self):
        if self.stop():
            return
        if self.current < 0 or self.strats[self.current].stop():
            self.current += 1
            self.strats[self.current].start()
        self.strats[self.current].etape()

    def stop(self):
        return self.current == len(self.strats)-1 and self.strats[self.current].stop()
