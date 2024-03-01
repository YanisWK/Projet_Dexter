import turret
from time import time

def affichage(robot):
    """
    Permet à l'utilisateur de choisir une action afin de contrôler le robot. Le temps n'est pas continu et c'est à l'utilisateur de choisir de combien de tick le robot avance
    """
    print("\n")
    print(robot)
    print("Pour pouvoir faire bouger le robot, veuillez taper le numéro de l'action :\n")
    print("0 : Sortir du programme")
    print("1 : Avancer d'une certaine durée")
    print("2 : Choisir la vitesse de la roue gauche")
    print("3 : Choisir la vitesse de la roue droite")
    print("4 : Obtenir la distance avec le mur le plus proche à l'avant du robot")
    while True:
        try:
            choix = int(input("Entrez un chiffre : "))
            if (choix >= 0 and choix <= 4):
                break
            else:
                print("Veuillez choisir un chiffre entre 0 et 4\n")
                continue
        except ValueError:
            print("Veuillez entrer un chiffre \n")

    print("\n")
    return choix

larg = 700
long = 1000
robot1 = turret.Robot(1, 50, 25, 10, long/2, larg/2, time.time())
simu = turret.Simulation(1,robot1,larg,long,120)
simu.robot.pret = True

vrd = 0
vrg = 0
while True:
    choix_ut = affichage(robot1)
    if choix_ut == 0:
        print("Le programme s'arrête\n")
        break

    elif choix_ut == 1:
        while True:
            try:
                choix_d = int(input("Veuillez écrire la durée que vous voulez faire : "))
                break
            except ValueError:
                print("Veuillez entrer un chiffre \n")
        for loop in range(choix_d):
            simu.rafraichir(vrg,vrd)

    elif choix_ut == 2:
        print(f"Vitesse de la roue gauche actuelle : {vrg}\n")
        while True:
            try:
                vrg = int(input("Veuillez écrire la vitesse de la roue gauche que vous voulez avoir (-100 à 100 inclus) : "))
                if (vrg >= -100 and vrg <= 100):
                    break
                else:
                    print("Veuillez choisir un chiffre entre -100 et 100\n")
                    continue
            except ValueError:
                print("Veuillez entrer un chiffre \n")
        robot1.vitesse_lineaire_roue_gauche = vrg
        print(f"Vitesse de la roue gauche initialisé à : {vrg} !!!\n")
        print("\n")

    elif choix_ut == 3:
        print(f"Vitesse de la roue droite actuelle : {vrd}\n")
        while True:
            try:
                vrd = int(input("Veuillez écrire la vitesse de la roue gauche que vous voulez avoir (-100 à 100 inclus) : "))
                if (vrd >= -100 and vrd <= 100):
                    break
                else:
                    print("Veuillez choisir un chiffre entre -100 et 100\n")
                    continue
            except ValueError:
                print("Veuillez entrer un chiffre \n")
        robot1.vitesse_lineaire_roue_droite = vrd
        print(f"Vitesse de la roue droite initialisé à : {vrd} !!!\n")
        print("\n")

    elif choix_ut == 4:
        distance_r_m = robot1.detect_distance(simu.longueur,simu.largeur)
        print(f"Le distance entre le robot et le mur est de : {distance_r_m} \n")
    
        
