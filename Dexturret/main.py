from Turret.robot import Robot
from Turret.simulation import Simulation
from main_interface2D import main

Robot = Robot("Dexter", 50, 25, 0, 0)

def affichage():
    print(Robot)
    print("Pour pouvoir faire bouger le robot, veuillez taper le numéro de l'action :\n")
    print("1 : Avancer\n")
    print("2 : Tourner\n")
    print("3 : Tracer un carré\n")
    while True:
        try:
            choix = int(input("Entrez un chiffre : "))
            if (choix > 0 and choix < 4):
                break
            else:
                print("Veuillez choisir un chiffre entre 1 à 3\n")
                continue
        except ValueError:
            print("Veuillez écrire un chiffre\n")

    print("\n")
    return choix

larg = 700
long = 1000
robot1 = Robot(1,50,25,long/2,larg/2)
simu = Simulation(1,robot1,larg,long,60)

#permet de relier les main de l'interface et de la simulation
if __name__ == "__main__":
    main()

while True:
    affichage()