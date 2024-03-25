import Dexturret.turret as turret
import Dexturret.interface as interface

def main():
   
    ballon = turret.Ballon(10, 20, 5, 0)

    # Afficher la position initiale du ballon
    print(ballon.afficher_position_ballon())

    # Bouger le ballon et afficher sa nouvelle position
    ballon.bouger_ballon()
    print(ballon.afficher_position_ballon())

    # Modifier la vitesse du ballon et bouger le ballon à nouveau
    ballon.vitesse = 10
    ballon.bouger_ballon()
    print(ballon.afficher_position_ballon())


if __name__ == "__main__":
    main()