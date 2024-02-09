from tkinter import Tk
#from Interface.graphique import window
from Turret import Robot
from Turret import Simulation

larg = 700
long = 1000
robot1 = Robot(1,50,25,long/2,larg/2)
simu = Simulation(1,robot1,larg,long,60)

def onKeyPress(event):
    """
    Paramètre :
    - event : évènement crée lorsqu'une touche du clavier est pressée

    """
    if event.keysym == "space":
        if (robot1.pret) :
            #fait bouger le robot si le robot est prêt et qu'on appuie sur espace
            robot1.pret = False
            change_color(robot1.pret)
        else:
            #stoppe le robot si le robot n'est pas prêt et qu'on appuie sur espace
            robot1.pret = True
            change_color(robot1.pret)
            
window.bind('<KeyPress>', onKeyPress)

#window.mainloop()