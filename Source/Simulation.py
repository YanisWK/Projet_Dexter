class Simulation:
    def __init__(self, id, robot, environnement, temps):
        self.id = id
        self.robot = robot                  #Le robot
        self.environnement = environnement  #L'environnement
        self.temps = temps                  #Le nombre de rafraichissement par seconde
        self.vitesse = 100                  #La vitesse à laquelle le robot se déplace
        self.distance = 100                 #La distance que le robot va parcourir