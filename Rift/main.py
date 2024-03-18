import Dexturret.turret as turret
from time import time, sleep
import Dexturret.interface
import logging
import Dexturret.controller.adaptateur as controller
from Dexturret.controller import TracerCarre, AvancerViteMur

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
    print("5 : Tracer un carré")
    print("6 : Avancer rapidement vers un mur")

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

controller_choisi = None 
tab = [(robot1.x,robot1.y)]
tailleMax = 500

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
    
    elif choix_ut == 5:
        print("Entrez la taille d'un coté du carré:")
        taille = int(input())        
        vitesse = int(input("Entrez la vitesse du robot : "))
        if not (isinstance(taille, int)):
            print("Entrée invalide, veuillez recommencer depuis le début (l'entrée doit être un entier)")
        else:
            controller_choisi = controller.TracerCarre(robot1, taille, vitesse)
            controller_choisi.start()
            while simu.awake and not controller_choisi.stop():
                #Mise a jour tous les 1/temps
                sleep(1/simu.fps)

                controller_choisi.etape()
                simu.rafraichir()
                if (robot1.x,robot1.y) != tab[-1]:
                    if len(tab) > tailleMax:
                        tab.pop(0)
                    tab.append((robot1.x,robot1.y))
                for elem in range(1,len(tab)):
                    x,y = tab[elem-1]
                    x1,y1 = tab[elem]

            #Affichage d'une fenêtre pop-up en cas de collision
            if not simu.awake:
                logging.info(f'Le Robot est entré en collision avec un obstacle')

    elif choix_ut == 6:
        vitesse= int(input("Entrez la vitesse du robot : "))
        controller_choisi = controller.AvancerViteMur(robot1, simu, vitesse)
        controller_choisi.start()
        while simu.awake and not controller_choisi.stop():
            #Mise a jour tous les 1/temps
            sleep(1/simu.fps)

            controller_choisi.etape()
            simu.rafraichir()
            if (robot1.x,robot1.y) != tab[-1]:
                if len(tab) > tailleMax:
                    tab.pop(0)
                tab.append((robot1.x,robot1.y))
            for elem in range(1,len(tab)):
                x,y = tab[elem-1]
                x1,y1 = tab[elem]

        #Affichage d'une fenêtre pop-up en cas de collision
        if not simu.awake:
            logging.info(f'Le Robot est entré en collision avec un obstacle')