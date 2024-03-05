import turret.robot
import controller.adaptateur 
from math import sqrt, degrees


class AvancerRobot():
    def __init__(self, robot, distance, vitesse, fps):
        self.robot = robot
        self.distance = distance
        self.vitesse = vitesse
        self.fps = fps

    def start(self):
        self.parcouru = 0

    def etape(self):
        self.robot.set_vitesse_roue(3,self.vitesse)

        vitesse_deplacement = (self.vitesse + self.vitesse) / 2
        deplacement_par_rafraichissement = vitesse_deplacement / self.fps

        self.parcouru += deplacement_par_rafraichissement

        print("Parcour: ", deplacement_par_rafraichissement)

        if self.stop() :
            self.robot.set_vitesse_roue(3,0)
            return
        
    def stop(self):
        return self.parcouru >= self.distance
    

class TournerRobot():
    def __init__(self, robot, angle, fps):
        self.robot = robot
        self.angle = angle
        self.fps = fps

    def start(self):
        self.angle_parcouru = 0
        self.robot_direction = self.robot.direction

    def etape(self):
        vit = 10
        self.robot.set_vitesse_roue(1,vit)
        self.robot.set_vitesse_roue(2,-vit)

        vit_rot_RG = vit / self.robot.rayon_des_roues
        vit_rot_RD = -vit / self.robot.rayon_des_roues

        vitesse_rotation = ( self.robot.rayon_des_roues * (vit_rot_RD - vit_rot_RG)) / self.robot.largeur
        rotation_par_rafraichissement = vitesse_rotation / self.fps

        self.angle_parcouru += abs(degrees(rotation_par_rafraichissement))
        print("rot/raf ", degrees(rotation_par_rafraichissement))

        if self.stop():
            self.robot.set_vitesse_roue(3,0)
            return

    def stop(self):
        print(self.angle_parcouru)
        print(self.robot.direction)
        return self.angle <= self.angle_parcouru #or self.angle - self.angle_parcouru <= 1
    

class AvancerViteRobot():
    def __init__(self, robot, simu, vitesse):
        self.robot = robot
        self.simu = simu
        self.vitesse = vitesse

    def start(self):
        self.robot.set_vitesse_roue(3,self.vitesse)

    def etape(self):
        if self.stop():
            self.robot.vitesse_lineaire_roue_gauche = 0
            self.robot.vitesse_lineaire_roue_droite = 0
            return

    def stop(self):
        return self.robot.detect_distance(self.simu.longueur, self.simu.largeur) <= self.robot.largeur



class TracerCarre():
    def __init__(self, robot, tailleCote, vitesse, fps):
        self.robot = robot
        self.tailleCote = tailleCote
        self.vitesse = vitesse
        stratAvancer = AvancerRobot(self.robot, self.tailleCote, self.vitesse, fps)
        stratTourner = TournerRobot(self.robot, 90, fps)
         #Besoin de savoir a chaque fois qu'on tourne de combien de degrès il faut tourner.

        self.strats = [stratAvancer,stratTourner,stratAvancer,stratTourner,stratAvancer,stratTourner,stratAvancer,stratTourner]
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

class AvancerViteMur():
    def __init__(self, robot, simu, vitesse, fps):
        self.robot = robot
        self.simu = simu
        self.vitesse = vitesse
        StratAvancerVite = AvancerViteRobot(self.robot, self.simu, self.vitesse, fps)
        self.strats = [StratAvancerVite]
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