from time import sleep, time
import Dexturret.turret as turret
import Dexturret.interface as interface

# Exercice 2 :

# 2.1
class Ballon:
    def __init__(self, x, y, vitesse, dernier_rafraichissement):
        self.x = x
        self.y = y
        self.vitesse = vitesse
        self.dernier_rafraichissement = 0

    def bouger_ballon(self):
        self.x += self.vitesse
        self.y += self.vitesse

    def afficher_position_ballon(self):
        return f"Position du ballon: ({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Ballon(x={self.x}, y={self.y}, vitesse={self.vitesse})"
