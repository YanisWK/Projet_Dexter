from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Geom,GeomTriangles,GeomVertexWriter,GeomVertexFormat,GeomVertexData,TransparencyAttrib,NodePath,CardMaker,Point3,Vec4

def create_colored_rect(x,z,width,height,colors=None):
    _format=GeomVertexFormat.getV3c4()

class VueRobot(ShowBase):
    def __init__(self):
        super().__init__()

        # Créer un CardMaker
        card_maker = CardMaker('card_maker')

        # Définir les dimensions du rectangle
        card_maker.setFrame(-1, 1, -1, 1)  # left, right, bottom, top

        # Créer le rectangle
        rectangle_node = NodePath(card_maker.generate())

        # Ajouter le rectangle à la scène
        rectangle_node.reparentTo(self.render)
            
app=VueRobot()
app.run()