from direct.showbase.ShowBase import ShowBase

class VueRobot(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.scene = self.loader.loadModel("models/robot")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.5, 0.5, 0.5)
        self.scene.setPos(8, 42, 0)

VueRobot().run()