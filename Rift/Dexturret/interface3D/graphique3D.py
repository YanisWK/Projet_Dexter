from panda3d.core import loadPrcFile
loadPrcFile("config/conf.prc")

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3

class VueRobot(ShowBase):
    def __init__(self):
        super().__init__()
       

        self.robot = Actor("test.glb")
        self.robot.setScale(0.01, 0.01, 0.01)
        self.scene.setPos(-8, 58, 0)
        self.robot.reparentTo(self.render)

        self.building = loader.loadModel("test.glb")
        self.building.setPos(0,5,0)        
        self.building.reparentTo(render)

        self.scene = self.loader.loadModel("models/environment") #charge l'environnement
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

app = test()
app.run()