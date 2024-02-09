from time import sleep
from tkinter import Canvas, Toplevel, Button, Label, Tk, Frame, StringVar, IntVar, Scale, RIGHT, LEFT, HORIZONTAL, BOTH, BOTTOM
from Turret.simulation import Simulation
from Turret.robot import Robot
from math import cos,radians,sin

"""Documentation : 
    - configure de l'interface graphique
    - affiche l'environnement à l'aide d'un canvas (fond gris)
    - affiche les échelles de la distance, la vitesse et l'angle pour l'utilisateur
    - affiche le robot sous forme de rectangle
    - configure la touche activant/désactivant la simulation
    - affiche une ligne rouge pointant vers le point centre du robot

"""




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
def creer_fenetre(simu_longueur, simu_largeur):
    window = Tk()
    window.title("Simulation")
    window.geometry(f"{simu_longueur+250}x{simu_largeur+5}")
    window.resizable(height=False, width=False)
    return window

#Première frame/boîte
def creer_frame(window):
    frame = Frame(window,borderwidth=5, relief="raise")
    frame.pack(fill = BOTH,side = RIGHT)
    return frame

#Canvas où sera simulé l'environnement du robot et ses déplacements
def creer_canvas(window, simu_longueur, simu_largeur):
    canvas = Canvas(window, bg='#cccccc', width=simu_longueur, height=simu_largeur)
    canvas.place(x='0',y='0')
    return canvas

#Pour le scale de la roue gauche
def creer_scale(frame, texte, var, min, max):
    texte_vit_gauche = StringVar()
    texte_vit_gauche.set(texte)
    label = Label(frame, textvariable=texte_vit_gauche, font=("Helvetica", 16))
    label.pack()
    scale = Scale(frame, from_=min, to=max, length=240,variable=var, orient=HORIZONTAL)
    scale.pack()
    return scale

espace(frame)

#Pour le scale de la roue gauche
texte_vit_droite = StringVar()
texte_vit_droite.set("Vitesse Roue Droite")
label = Label(frame, textvariable=texte_vit_droite, font=("Helvetica", 16))
label.pack()
vit_droite = IntVar()
scale2 = Scale(frame, from_=-100, to=100, length=240,variable=vit_droite, orient=HORIZONTAL)
scale2.pack()

espace(frame)

#Implementation du robot dans l'environnement
def affiche_robot(simu, canvas):
    canvas.create_polygon(simu.robot.coordRobot)
    canvas.pack()

def creer_couleur(frame):
    couleur = Canvas(frame, bg='red', width=100, height=50)
    couleur.pack(side=BOTTOM)
    return couleur

def change_color(activation, couleur):
    """
    Change la couleur du bouton d'activation de la simulation

    Paramètre :
    - activation : booléen (true si la simulation est active, false sinon)

    """
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


def popup_collision(window):
    """
    Crée un pop-up permettant de feemer la simulation lorsque le robot rencontre un obstacle
    
    """
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


def rafraichir(simu, canvas):
    canvas.delete("all")
    affiche_robot(simu, canvas)

    #Creer la ligne qui montre la direction du robot
    demi_longueur_robot = simu.robot.longueur / 2
    demi_largeur_robot = simu.robot.largeur / 2
    canvas.create_line(simu.robot.x, simu.robot.y, simu.robot.x + demi_longueur_robot * cos(radians(simu.robot.direction)), simu.robot.y - demi_largeur_robot * (sin(radians(simu.robot.direction))), fill = "red")
    
    canvas.pack()
    canvas.update()

#Boucle qui permet de rafraichir l'interface mais ça bouffe TROP DE RESSOURCES
while True:
    if (simu.awake):
        #Mise a jour tous les 1/temps
        sleep(1/simu.fps)

        #On efface tout et on redessine le robot
        rec_base.delete("all")
        simu.rafraichir(vit_gauche.get(), vit_droite.get())
        rec_base.create_polygon(simu.robot.coordRobot)

        #Affichage de la ligne rouge pour la direction du robot

        rec_base.pack()
        rec_base.update()
    else:
        break
popup_collision()


#boutton_moins_distance = Button(frame, text="-10",font =("verdana", 13), fg='black', bg='white')
#boutton_moins_distance.pack(side = LEFT)