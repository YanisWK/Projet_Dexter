from direct.showbase.ShowBase import ShowBase

class VueRobot(ShowBase):
    def __init__(self):
        super().__init__()

app = VueRobot()

app.run()