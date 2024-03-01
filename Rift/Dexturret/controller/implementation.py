import strat

class RobotSimu():
    def __init__(self,robot):
        self.robot=robot

    def creerAvancer(self,distance, vitesse):
        return strat.AvancerRobotSimu(self.robot,distance,vitesse)

    def creerTourner(self,angle,vitesse):
        return strat.TournerRobotSimu(self.robot,angle,vitesse)
    
    def creerAvancerVite(self,vitesse,simu):
        return strat.AvancerViteRobotSimu(self.robot,simu)
    



class RobotIRL():
    def __init__(self,robot):
        self.robot=robot

    def creerAvancer():
        pass
    def creerTourner():
        pass
    def creerAvancerVite():
        pass
     
    
        