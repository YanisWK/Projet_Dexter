import Dexturret.turret.robot
import Dexturret.turret.simulation
import Dexturret.turret.ballon

def main():
   
    ballon = Ballon(10, 20, 5)

    # Afficher la position initiale du ballon
    print(ballon.afficher_position())

    # Bouger le ballon et afficher sa nouvelle position
    ballon.bouger()
    print(ballon.afficher_position())

    # Modifier la vitesse du ballon et bouger le ballon à nouveau
    ballon.vitesse = 10
    ballon.bouger()
    print(ballon.afficher_position())

if __name__ == "__main__":
    main()