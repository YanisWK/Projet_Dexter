from tkinter import IntVar,Button,Label
import Dexturret.interface as interface
import Dexturret.turret as turret
import Dexturret.controller as controller
from time import sleep, time
import logging

larg = 700
long = 1000
robotSim = turret.Robot(1, 50, 25, 5, long/2, larg/2, time())
robotSimu = controller.adaptateurSimu(robotSim)

def q11():
    obs1=turret.Obstacle(500,200,25)
    obs2=turret.Obstacle(700,200,25)
    obs3=turret.Obstacle(300,250,25)
    obs4=turret.Obstacle(325,455,25)
    obs5=turret.Obstacle(745,445,25)
    obstacles=[obs1,obs2,obs2,obs3,obs4,obs5]
    simu = turret.Simulation(1, robotSim, larg, long, 60, obstacles)
    window, couleur, canvas, frame, obstacles, text_distance = interface.creer_graphique(robotSim,simu,obstacles)
    while simu.awake:
        sleep(1/simu.fps)
        simu.rafraichir()
        interface.rafraichir_graphique(simu, canvas,obstacles)
        canvas.update()
        interface.affichage_distance(text_distance,robotSim,simu.longueur,simu.largeur)
    interface.popup_collision(window)
    window.mainloop()