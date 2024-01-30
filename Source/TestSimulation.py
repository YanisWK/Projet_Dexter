from Simulation import *
from Environnement import *
from Robot import *

Environnement_test = Environnement(1,1000,700)
Robot1 = Robot(1,100,50,Environnement_test.getLo()/2,Environnement_test.getLa()/2)
Simu = Simulation(1,Robot1,Environnement_test,10)


print(Simu.coordRobot)
Simu.vitesse = 100
Simu.distance = 200
Simu.angle = 90

Simu.deplacementRobot()

print(Simu.velociteD)

Simu.rafraichir()

print(Simu.velociteD)

Simu.rotationRobot()

print(Simu.velociteR)