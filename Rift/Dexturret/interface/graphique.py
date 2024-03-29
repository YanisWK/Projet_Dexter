from time import sleep
from tkinter import Canvas, Toplevel, Button, Label, Tk, Frame, StringVar, IntVar, Scale, RIGHT, LEFT, HORIZONTAL, BOTH, BOTTOM, CENTER
import Dexturret.simu as turret
from math import cos,radians,sin

"""Documentation : 
    - creer_fenetre, creer_frame, creer_canvas, creer_scale, configure l'interface graphique
    - creer_graphique, rafraichir_graphique : affiche l'environnement à l'aide d'un canvas (fond gris)
    - affichage_distance : affiche les échelles de la distance et la vitesse des roues pour l'utilisateur
    - affiche_robot : affiche le robot sous forme de rectangle et affiche une ligne rouge pointant vers le point centre du robot
    - OnKeyPress : configure la touche activant/désactivant la simulation
    - dessiner : affiche le tracé du robot 
    - popup_collision : affiche un pop-up lorsque le robot rencontre une collision

"""

def creer_fenetre(simu_longueur, simu_largeur):
    """
    Crée et configure la fenêtre principale de l'interface graphique

    Paramètres :
    - simu_longueur : longueur de la simulation
    - simu_largeur : largeur de la simulation

    Retourne :
    - window : fenêtre principale
    
    """
    window = Tk()
    window.title("Simulation")
    window.geometry(f"{simu_longueur+250}x{simu_largeur+5}")
    window.resizable(height=False, width=False)
    return window

def creer_frame(window):
    """
    Crée et configure une frame 

    Paramètre :
    - window : fenêtre principale

    Retourne :
    - frame : fenêtre pour les échelles de vitesse des roues
    """
    frame = Frame(window,borderwidth=5, relief="raise")
    frame.pack(fill = BOTH,side = RIGHT)
    return frame

def creer_canvas(window, simu_longueur, simu_largeur):
    """
    Crée et configure un canvas pour la simulation

    Paramètres :
    - window : fenêtre principale
    - simu_longueur : longueur de la simulation
    - simu_largeur : largeur de la simulation

    Retourne :
    - canvas : canvas représentant l'environnement dans lequel se déplace le robot

    """
    canvas = Canvas(window, bg='#cccccc', width=simu_longueur, height=simu_largeur)
    canvas.place(x='0',y='0')
    return canvas

def creer_scale(frame, texte, var, min, max):
    """
    Crée et configure un scale (curseur) dans une frame.

    Paramètres :
    - frame : fenêtre pour les outils nécessaires au fonctionnement de la simulation
    - texte : texte à afficher à côté du scale
    - var : variable associée au scale
    - min : valeur minimale du scale
    - max : valeur maximale du scale

    Retourne :
    - scale : échelle qui servira à varier la vitesse d'une roue
    
    """
    texte_vit = StringVar()
    texte_vit.set(texte)
    label = Label(frame, textvariable=texte_vit, font=("Helvetica", 16))
    label.pack()
    scale = Scale(frame, from_=min, to=max, length=240, variable=var, orient=HORIZONTAL)
    scale.pack()
    return scale

def affiche_robot(simu, canvas):
    """
    Affiche le robot et la ligne pointant vers sa direction dans le canvas.

    Paramètres :
    - simu : simulation
    - canvas : canvas/environnement de la simulation

    """
    canvas.create_polygon(simu.robot.coordRobot)

    #Creer la ligne qui montre la direction du robot
    demi_longueur_robot = simu.robot.longueur / 2
    demi_largeur_robot = simu.robot.largeur / 2
    canvas.create_line(simu.robot.x, simu.robot.y, simu.robot.x + demi_longueur_robot * cos(radians(simu.robot.direction)), simu.robot.y - demi_longueur_robot * (sin(radians(simu.robot.direction))), fill = "red")
    
    canvas.pack()

def creer_couleur(frame):
    """
    Crée et configure une couleur.

    Paramètre :
    - frame : fenêtre concernée par la couleur

    Retourne :
    - couleur : élément graphique contenant la couleur 

    """
    couleur = Canvas(frame, bg='red', width=100, height=50)
    couleur.pack(side=BOTTOM)
    return couleur

def change_color(activation, couleur):
    """
    Configure la couleur du bouton d'activation de la simulation

    Paramètre :
    - activation : booléen (true si la simulation est active, false sinon)
    - couleur : couleur créée à partir de creer_couleur pour le bouton de simulation

    """
    if activation:
        couleur.configure(bg='green')
    else:
        couleur.configure(bg='red')

def popup_collision(window):
    """
    Crée un pop-up permettant de fermer la simulation lorsque le robot rencontre un obstacle

    Paramètre :
    - window : fenêtre principale
    
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


def rafraichir_graphique(simu, canvas):
    """
    Rafraîchit le graphique en effaçant le canvas et en réaffichant le robot avec les nouvelles positions, 
    et met à jour le canvas avec les changements effectués

    Paramètres :
    - simu : simulation
    - canvas : canvas/environnement de la simulation

    """
    canvas.delete("all")
    affiche_robot(simu, canvas)
    
    canvas.pack()
    canvas.update()


def creer_graphique(simu):
    """
    Assemble les éléments de la fenetre (frame, canvas, affichage de la distance)

    Paramètre :
    - simu : simulation dans lequel le robot se déplace 

    """
    #Création de la fenêtre principale, de la frame et du canvas pour la simulation
    window = creer_fenetre(simu.longueur, simu.largeur)

    frame = creer_frame(window)

    canvas = creer_canvas(window, simu.longueur, simu.largeur)

    text_distance = Label(frame, text="Distance : 0.0", font=("Helvetica", 16))
    text_distance.pack(ipady=10)
    #Création d'une couleur 
    couleur = creer_couleur(frame)
    return window, couleur, canvas, frame, text_distance


def affichage_distance(text_distance,robot,long,larg):
    """affiche la distance séparant le robot et la bordure vers lequel il se dirige"""
    text_distance.config(text = f"Distance : {round(robot.detect_distance(long,larg),1)}")

def onKeyPress(robot,couleur,event):
    """
    Gère l'événement lorsqu'une touche du clavier est pressée.

    Paramètre :
    - robot : robot à manipuler
    - couleur : couleur du bouton permettant l'activation ou la désactivation de la simu
    - event : évènement crée lorsqu'une touche du clavier est pressée

    """
    if event.keysym == "space":
        robot.pret = not robot.pret
        change_color(robot.pret, couleur)

def dessiner(robot,simu,canvas,text_distance):
    """
    Affichage du tracé qui suit le robot.

    Paramètre :
    - robot : robot à manipuler
    - canvas : canvas sur lequel le tracé du robot se fait

    """
    rafraichir_graphique(simu, canvas)
    #Affichage de la ligne rouge pour la direction du robot
    canvas.pack()
    if (len(robot.trace) == 0) or (robot.x,robot.y) != robot.trace[-1]:
        if len(robot.trace) > 500:
            robot.trace.pop(0)
        robot.trace.append((robot.x,robot.y))
    for elem in range(1,len(robot.trace)):
        x,y = robot.trace[elem-1]
        x1,y1 = robot.trace[elem]
        canvas.create_line(x, y, x1, y1, fill="black")
        canvas.pack()
    canvas.update()
    affichage_distance(text_distance,robot,simu.longueur,simu.largeur)