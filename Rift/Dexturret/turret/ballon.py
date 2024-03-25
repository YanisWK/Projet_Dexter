from math import cos, sin, radians, degrees, sqrt
import logging
from time import time

class Ballon():
    def __init__(self, x, y, taille, dernier_rafraichissement):
        self.x = x
        self.y = y
        self.taille = taille
        self.dernier_rafraichissement = dernier_rafraichissement
        self.vitesse = 0
        self.direction = 0
        self.temps_ajustement = 0

    @property
    def coordCoins(self):
        largeur = self.taille/2
        c1 = (self.x - largeur, self.y - largeur)
        c2 = (self.x + largeur, self.y - largeur)
        c3 = (self.x + largeur, self.y + largeur)
        c4 = (self.x - largeur, self.y + largeur)
        return (c1, c2, c3, c4)
    
    def toucher(self, vitesse_RG, vitesse_RD, direction):
        self.direction = direction
        vitesse_robot = (vitesse_RG + vitesse_RD) / 2
        self.vitesse = 2 * vitesse_robot + self.vitesse

        print("TOUCHE")
        print(self.vitesse)

    def rafraichir(self):
        print("Vitesse de la balle: ", self.vitesse)
        temps_passe = time() - self.dernier_rafraichissement
        self.vitesse = max(0, self.vitesse - temps_passe * ((1 * self.vitesse**2) - (6 * self.vitesse)))

        vt = self.vitesse * temps_passe
        self.x += vt * cos(radians(self.direction))
        self.y -= vt * sin(radians(self.direction))

        """
        vt_dt = max(0, vt - temps_passe * ((0.01 * vt**2) - (0.06 * vt)) )
        self.vitesse = temps_passe / vt_dt
        """

        #print(self.vitesse)