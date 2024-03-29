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
        self.scene = self.loader.loadModel("models/environment")
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(0,50,0)
        self.scene.reparentTo(self.render)

        self.robot = Actor("test.glb")
        self.robot.setScale(0.01, 0.01, 0.01)
        self.scene.setPos(-8, 58, 0)
        self.robot.reparentTo(self.render)


app = VueRobot()
 
print(__builtins__.base)

app.run()