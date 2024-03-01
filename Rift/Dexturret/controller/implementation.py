import controller.strat

class RobotSimu():
    def __init__(self,robot):
        self.robot=robot

    def creerAvancer(self,distance, vitesse):
        return controller.strat.AvancerRobotSimu(self.robot,distance,vitesse)

    def creerTourner(self,angle,vitesse):
        return controller.strat.TournerRobotSimu(self.robot,angle,vitesse)
    
    def creerAvancerVite(self,vitesse,simu):
        return controller.strat.AvancerViteRobotSimu(self.robot,simu,vitesse)
    



class RobotIRL():
    def __init__(self,robot):
        self.robot=robot

    def creerAvancer():
        pass
    def creerTourner():
        pass
    def creerAvancerVite():
        pass
     
    
        