import Dexturret.interface as interface
import Dexturret.turret as turret
from time import sleep, time
from tkinter import IntVar


class q2:
    def __init__(self):
        self.balle = turret.Ballon(100, 100, 10, time())
        self.balle.vitesse = 10
        larg = 700
        long = 1000

        self.fps = 60

        self.robot = turret.Robot(1, 50, 25, 0.05, long/2, larg/2, time())
        self.simu = turret.Simulation(1, self.robot, larg, long, self.fps, self.balle)
        
        self.window, self.couleur, self.canvas, self.frame, self.text_distance = interface.creer_graphique(self.robot, self.simu)
        
        self.vitesse_roue_gauche = IntVar()
        self.scale_roue_gauche = interface.creer_scale(self.frame, "Vitesse roue gauche", self.vitesse_roue_gauche, -100, 100)
        self.scale_roue_gauche.pack(ipady=20)

        self.vitesse_roue_droite = IntVar()
        self.scale_roue_droite = interface.creer_scale(self.frame, "Vitesse roue droite", self.vitesse_roue_droite, -100, 100)
        self.scale_roue_droite.pack(ipady=20)


    def e1(self):
        while self.simu.awake:
            sleep(1/self.fps)
            self.simu.rafraichir()
            interface.rafraichir_graphique(self.simu, self.canvas)


"""
Q2.5
Une strategie pour que le robot marque un but est que le robot se positionne de pour etre alignee au ballon et au but,
tourne pour faire face au but (et donc a la balle), puis avance tout droit
"""

q = q2()
q.e1()