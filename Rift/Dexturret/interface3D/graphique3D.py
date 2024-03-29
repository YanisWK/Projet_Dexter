from panda3d.core import loadPrcFile
loadPrcFile("config/conf.prc")
from direct.showbase.ShowBase import ShowBase

class VueRobot(ShowBase):
    def __init__(self):
        super().__init__()

class test(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.building = loader.loadModel("test.glb")
        self.building.setPos(0,50,0)
        self.building.reparentTo(render)

app = test()
 
print(__builtins__.base)

app.run()