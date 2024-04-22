from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Geom,GeomTriangles,GeomVertexWriter,GeomVertexFormat,GeomVertexData,TransparencyAttrib


def create_colored_rect(x,z,width,height,colors=None):
    _format=GeomVertexFormat.getV3c4()

class VueRobot(ShowBase):
    def __init__(self):
        super().__init__()


            
app=VueRobot()
app.run()