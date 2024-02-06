from time import sleep
from tkinter import Canvas, Toplevel, Button, Label, Tk, Frame, StringVar, IntVar, Scale, RIGHT, LEFT, HORIZONTAL, BOTH, BOTTOM
from src.simulation import Simulation
from src.robot import Robot
from math import cos,radians,sin

"""Documentation : 
    - initialise les paramètres de la simulation
    - configure de l'interface graphique
    - affiche l'environnement à l'aide d'un canvas (fond gris)
    - affiche les échelles de la distance, la vitesse et l'angle pour l'utilisateur
    - affiche le robot sous forme de rectangle
    - configure les touches du clavier permettant de faire avancer/reculer/tourner le robot
    - affiche une ligne rouge pointant vers le point centre du robot

"""


larg = 700
long = 1000
robot1 = Robot(1,50,25,long/2,larg/2)
simu = Simulation(1,robot1,larg,long,60)



def espace (f):
    ''' 
    Ajoute un espace entre les éléments d'une frame

    Paramètres : 
    - f : frame

    '''
    espace = Label(f, text="", font=("Helvetica", 16))
    espace.pack()
    espace = Label(f, text="", font=("Helvetica", 16))
    espace.pack()

#Spécificité de notre interface graphique
window = Tk()
window.title("Simulation")
window.geometry(f"{simu.longueur+250}x{simu.largeur+5}")
window.resizable(height=False, width=False)

#Première frame/boîte
frame = Frame(window,borderwidth=5, relief="raise")
frame.pack(fill = BOTH,side = RIGHT)

#Canvas où sera simulé l'environnement du robot et ses déplacements
rec_base = Canvas(window, bg='#cccccc', width=simu.longueur, height=simu.largeur)
rec_base.place(x='0',y='0')

#Pour le scale de la roue droite
texte_vit_gauche = StringVar()
texte_vit_gauche.set("Vitesse Roue Droite")
label = Label(frame, textvariable=texte_vit_gauche, font=("Helvetica", 16))
label.pack()
vit_gauche = IntVar()
scale = Scale(frame, from_=-100, to=100, length=240,variable=vit_gauche, orient=HORIZONTAL)
scale.pack()

espace(frame)

#Pour le scale de la roue gauche
texte_vit_droite = StringVar()
texte_vit_droite.set("Vitesse Roue Gauche")
label = Label(frame, textvariable=texte_vit_droite, font=("Helvetica", 16))
label.pack()
vit_droite = IntVar()
scale2 = Scale(frame, from_=-100, to=100, length=240,variable=vit_droite, orient=HORIZONTAL)
scale2.pack()

espace(frame)

#Implementation du robot dans l'environnement
coord = simu.robot.coordRobot
rec_base.create_polygon(coord[0][0],coord[0][1],coord[1][0],coord[1][1],coord[2][0],coord[2][1],coord[3][0],coord[3][1])
rec_base.pack()

couleur = Canvas(frame, bg='red', width=100, height=50)
couleur.pack(side=BOTTOM)

def change_color(activation):
    if activation:
        couleur.configure(bg='green')
    else:
        couleur.configure(bg='red')

# def onKeyPress(event):
#     """
#     Choisit les fonctions à executer en fonction des touches directionnelles

#     Paramètres :
#     - event : événement de clavier dans l'interface utilisateur, crée quand une touche est pressée
#     """
#     if event.keysym == "Right":
#         simu.robot.rotationRobot(-angle.get(), vitesse.get(), simu.temps)
#     elif event.keysym == "Left":
#         simu.robot.rotationRobot(angle.get(), vitesse.get(), simu.temps)
#     elif event.keysym == "Up":
#         simu.robot.deplacementRobot(distance.get(), vitesse.get(), simu.temps)
#     elif event.keysym == "Down":
#         simu.robot.deplacementRobot(-distance.get(), vitesse.get(), simu.temps)
def onKeyPress(event):
    if event.keysym == "space":
        if (robot1.pret) :
            robot1.pret = False
            change_color(robot1.pret)
        else:
            robot1.pret = True
            change_color(robot1.pret)

def popup_collision():
    win = Toplevel()
    win.wm_title("CRASH")

    l = Label(win, text="Le robot est entré en collision avec un obstacle")
    l.grid(row=0, column=0)

    b = Button(win, text="Fermer la simulation", command=window.destroy)
    b.grid(row=1, column=0)

    #Calculer x et y pour positionner la popup au milieu de l'interface
    x = window.winfo_rootx() + window.winfo_width() // 2 - win.winfo_reqwidth() // 2
    y = window.winfo_rooty() + window.winfo_height() // 2 - win.winfo_reqheight() // 2

    # Définition de la position du Toplevel
    win.geometry("+{}+{}".format(x, y))


#Sert a utiliser la fonction onKeyPress lorsque on clique sur une touche du clavier
window.bind('<KeyPress>', onKeyPress)

#Boucle qui permet de rafraichir l'interface mais ça bouffe TROP DE RESSOURCES
while True:
    if (simu.awake):
        #Mise a jour tous les 1/temps
        sleep(1/simu.temps)

        #On efface tout et on redessine le robot
        rec_base.delete("all")
        simu.rafraichir(vit_gauche.get(), vit_droite.get())
        rec_base.create_polygon(simu.robot.coordRobot)

        #Affichage de la ligne rouge pour la direction du robot
        x = robot1.x
        y = robot1.y
        L = robot1.longueur / 2
        l = robot1.largeur / 2
        x1 = x + L*cos(radians(robot1.direction))
        y1 = y - L*sin(radians(robot1.direction))
        rec_base.create_line(x, y, x1, y1, fill="red")

        rec_base.pack()
        rec_base.update()
    else:
        break
popup_collision()

window.mainloop()







#boutton_moins_distance = Button(frame, text="-10",font =("verdana", 13), fg='black', bg='white')
#boutton_moins_distance.pack(side = LEFT)