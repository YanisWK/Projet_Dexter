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
        self.building.setPos(0,5,0)        
        self.building.reparentTo(render)

        self.scene = self.loader.loadModel("models/environment") #charge l'environnement
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

app = test()
app.run()