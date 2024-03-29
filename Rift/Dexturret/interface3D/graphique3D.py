from panda3d.core import loadPrcFile
loadPrcFile("config/conf.prc")
from direct.showbase.ShowBase import ShowBase

class VueRobot(ShowBase):
    def __init__(self):
        super().__init__()


app = VueRobot()
 
print(__builtins__.base)

app.run()