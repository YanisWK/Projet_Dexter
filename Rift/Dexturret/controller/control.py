import turret.robot
import implementation
class TracerCarre():
    def __init__(self, robot, tailleCote, vitesse):
        result=isinstance(robot,turret.Robot)
        if(result):
            stratAvancer = implementation.RobotSimu.creerAvancer(robot, tailleCote, vitesse)
            stratTourner = implementation.RobotSimu.creerTourner(robot, 90, vitesse)
        else:
            stratAvancer = implementation.RobotIRL.creerAvancer(robot, tailleCote, vitesse)
            stratTourner = implementation.RobotIRL.creerTourner(robot, 90, vitesse)
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
            StratAvancerVite = implementation.RobotSimu.creerAvancerVite(robot, simu, vitesse,simu)
        else:
            StratAvancerVite = implementation.RobotIRL.creerAvancerVite()
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