import turret.robot
import controller.adaptateur 

class AvancerRobotSimu():
    def __init__(self, robot, distance, vitesse):
        self.robot = robot
        self.distance = distance
        self.vitesse = vitesse

    def start(self):
        self.parcouru = 0
        self.robot_x = self.robot.x
        self.robot_y = self.robot.y

    def etape(self):
        self.robot.vitesse_lineaire_roue_gauche = self.vitesse
        self.robot.vitesse_lineaire_roue_droite = self.vitesse

        self.parcouru += sqrt((self.robot.x - self.robot_x)**2 + (self.robot.y - self.robot_y)**2)
        self.robot_x = self.robot.x
        self.robot_y = self.robot.y

        if self.stop() :
            self.robot.vitesse_lineaire_roue_gauche = 0
            self.robot.vitesse_lineaire_roue_droite = 0
            return
        
    def stop(self):
        return self.parcouru >= self.distance
    

class TournerRobotSimu():
    def __init__(self, robot, angle, vitesse):
        self.robot = robot
        self.angle = angle
        self.vitesse = vitesse

    def start(self):
        self.angle_parcouru = 0
        self.robot_direction = self.robot.direction

    def etape(self):
        self.robot.vitesse_lineaire_roue_gauche = 10
        self.robot.vitesse_lineaire_roue_droite = -10

        if (abs(self.robot_direction - self.robot.direction) > 180):
            self.angle_parcouru += 360 - abs(self.robot_direction - self.robot.direction)
        else:
            self.angle_parcouru += abs(self.robot_direction - self.robot.direction)

        self.robot_direction = self.robot.direction


        self.robot_direction = self.robot.direction

        if self.stop():
            self.robot.vitesse_lineaire_roue_gauche = 0
            self.robot.vitesse_lineaire_roue_droite = 0
            return

    def stop(self):
        print(self.angle_parcouru)
        print(self.robot.direction)
        return self.angle <= self.angle_parcouru #or self.angle - self.angle_parcouru <= 1
    

class AvancerViteRobotSimu():
    def __init__(self, robot, simu, vitesse):
        self.robot = robot
        self.simu = simu
        self.vitesse = vitesse

    def start(self):
        self.robot.vitesse_lineaire_roue_gauche = self.vitesse
        self.robot.vitesse_lineaire_roue_droite = self.vitesse

    def etape(self):
        if self.stop():
            self.robot.vitesse_lineaire_roue_gauche = 0
            self.robot.vitesse_lineaire_roue_droite = 0
            return

    def stop(self):
        return self.robot.detect_distance(self.simu.longueur, self.simu.largeur) <= self.robot.largeur



class TracerCarre():
    def __init__(self, robot, tailleCote, vitesse):
        result=isinstance(robot,turret.Robot)
        if(result):
            instanceSimu=controller.adaptateur.RobotSimu(robot)
            stratAvancer = instanceSimu.creerAvancer(tailleCote,vitesse)
            stratTourner = instanceSimu.creerTourner(90, vitesse)
        else:
            instanceIRL=controller.adaptateur.RobotIRL(robot)
            stratAvancer = instanceIRL.creerAvancer(tailleCote, vitesse)
            stratTourner = instanceIRL.creerTourner(90, vitesse)
         #Besoin de savoir a chaque fois qu'on tourne de combien de degrès il faut tourner.

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

class AvancerViteMur():
    def __init__(self, robot, simu, vitesse):
        result=isinstance(robot,turret.Robot)
        if(result):
            instanceSimu=controller.adaptateur.RobotSimu(robot)
            StratAvancerVite = instanceSimu.creerAvancerVite(vitesse,simu)
        else:
            instanceIRL=controller.adaptateur.RobotIRL(robot)
            StratAvancerVite = instanceIRL.creerAvancerVite()
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