from Turret.robot import Robot
from Turret.simulation import Simulation
from main_interface2D import main

Robot = Robot("Dexter", 50, 25, 0, 0)
print(Robot)

larg = 700
long = 1000
robot1 = Robot(1,50,25,long/2,larg/2)
simu = Simulation(1,robot1,larg,long,60)

#permet de relier les main de l'interface et de la simulation
if __name__ == "__main__":
    main()