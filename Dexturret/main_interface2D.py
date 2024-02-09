from tkinter import Tk
#from Interface.graphique import window
from Turret import Robot
from Turret import Simulation

larg = 700
long = 1000
robot1 = Robot(1,50,25,long/2,larg/2)
simu = Simulation(1,robot1,larg,long,60)


#window.mainloop()