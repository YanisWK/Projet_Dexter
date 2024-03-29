from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self) #initialise la fenetre de la scène

        self.disableMouse() #désactive les controles de la caméra

    
        self.scene = self.loader.loadModel("models/box") #charge l'environnement

        self.obstacle = self.loader.loadModel("models/box") #crée l'obstacle
        self.obstacle.reparentTo(self.render)
        self.obstacle.setScale(1, 1, 1)  #ajuste la taille de l'obstacle
        self.obstacle.setPos(0, 0, 0)  #positionne l'obstacle

        self.scene.reparentTo(self.render) #attache l'objet représentant la scène à l'arbre de la scène principale

        #echelle et positionnement de l'environnement
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask") #fait tourner la caméra


        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"}) #crée le panda qui marche
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render) #attache l'objet représentant la scène à l'arbre de la scène principale

        self.pandaActor.loop("walk") #répète l'animation on loop


        #initialise la caméra avec un angle de 3/4 par rapport au panda
        self.camera.setPos(0, -20, 6)  #déplacer la caméra derrière le panda
        self.camera.lookAt(self.pandaActor)  #oriente la caméra vers le panda

        #définition des intervalles de déplacement et de rotation du panda
        
        posInterval1 = self.pandaActor.posInterval(13,
                                                   Point3(0, -10, 0),
                                                   startPos=Point3(0, 10, 0))
        posInterval2 = self.pandaActor.posInterval(13,
                                                   Point3(0, 10, 0),
                                                   startPos=Point3(0, -10, 0))
        hprInterval1 = self.pandaActor.hprInterval(3,
                                                   Point3(180, 0, 0),
                                                   startHpr=Point3(0, 0, 0))
        hprInterval2 = self.pandaActor.hprInterval(3,
                                                   Point3(0, 0, 0),
                                                   startHpr=Point3(180, 0, 0))

        #puis les organisent dans une séquence à jouer
        self.pandaPace = Sequence(posInterval1, hprInterval1,
                                  posInterval2, hprInterval2,
                                  name="pandaPace")
        self.pandaPace.loop()

    def spinCameraTask(self, task):
        """
        - Calcule l'angle de rotation en fonction du temps
        - Positionne et oriente la caméra en fonction de l'angle

        Paramètre :
        - task : infos sur la tâche à effectuer
        """
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        #met à jour la position de la caméra pour suivre le panda
        self.camera.setPos(self.pandaActor, 5000, 5000, 5000)  #1e param= de près ou de loin, 2e param=depuis la gauche ou la droite, 3e param=vue d'en haut ou d'en bas
        self.camera.lookAt(self.pandaActor)
        return Task.cont


app = MyApp() #crée l'instance
app.run() #démarre l'application