from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Geom,GeomTriangles,GeomVertexWriter,GeomVertexFormat,GeomVertexData,TransparencyAttrib,Point3,Vec4

from panda3d.core import Geom, GeomTriangles, GeomVertexWriter, GeomVertexFormat, GeomVertexData, NodePath, GeomNode, GeomVertexReader

from panda3d.bullet import BulletWorld
from panda3d.core import Vec3
from panda3d.bullet import BulletWorld
from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletBoxShape
from panda3d.bullet import ZUp


from math import pi, sin, cos

class VueRobot(ShowBase):
    def __init__(self):
        super().__init__()
        world = BulletWorld()
        world.setGravity(Vec3(0, 0, -9.81))

        # Coordonnées des sommets du premier rectangle 3D
        verticesRect = [
            (-1, -1, -1),  # sommet 0
            (1, -1, -1),   # sommet 1
            (1, 1, -1),    # sommet 2
            (-1, 1, -1),   # sommet 3
            (-1, -1, 1),   # sommet 4
            (1, -1, 1),    # sommet 5
            (1, 1, 1),     # sommet 6
            (-1, 1, 1),    # sommet 7
        ]

        # Coordonnées des sommets du deuxième rectangle 3D
        verticesPlat = [
            (-100, -100, -1),  # sommet 0
            (100, -100, -1),   # sommet 1
            (100, 100, -1),    # sommet 2
            (-100, 100, -1),   # sommet 3
        ]

        # Normales des sommets des rectangles 3D
        normalsRobot = [
            (-1, -1, -1),  # normal du sommet 0
            (1, -1, -1),   # normal du sommet 1
            (1, 1, -1),    # normal du sommet 2
            (-1, 1, -1),   # normal du sommet 3
            (-1, -1, 1),   # normal du sommet 4
            (1, -1, 1),    # normal du sommet 5
            (1, 1, 1),     # normal du sommet 6
            (-1, 1, 1),    # normal du sommet 7
        ]

        normalsPlat = [
            (-10, -10, -1),  # normal du sommet 0
            (10, -10, -1),   # normal du sommet 1
            (10, 10, -1),    # normal du sommet 2
            (-10, 10, -1),   # normal du sommet 3
        ]

        # Couleurs des sommets des rectangles 3D
        colors = [
            (1, 0, 0, 1),  # rouge
            (0, 1, 0, 1),  # vert
            (0, 0, 1, 1),  # bleu
            (1, 1, 0, 1),  # jaune
            (1, 0, 1, 1),  # magenta
            (0, 1, 1, 1),  # cyan
            (1, 1, 1, 1),  # blanc
            (0, 0, 0, 1),  # noir
        ]

        # Indices des triangles du premier rectangle 3D
        indicesRobot = [
            (0, 1, 2), (0, 2, 3),  # face avant
            (4, 5, 6), (4, 6, 7),  # face arrière
            (0, 1, 5), (0, 5, 4),  # face bas
            (2, 3, 7), (2, 7, 6),  # face haut
            (0, 3, 7), (0, 7, 4),  # face gauche
            (1, 2, 6), (1, 6, 5),  # face droite
        ]

        # Indices des triangles du deuxième rectangle 3D
        indicesPlat = [
            (0, 1, 2), (0, 2, 3),  # face avant
        ]

        # Créer le format des vertices
        format = GeomVertexFormat.getV3n3c4()  # 3D vertices, normals, and colors

        # Créer le GeomVertexData pour le premier rectangle
        vdataRobot = GeomVertexData('verticesRect', format, Geom.UHStatic)

        # Créer les writers pour le premier rectangle
        vertexRobot = GeomVertexWriter(vdataRobot, 'vertex')
        normalRobot = GeomVertexWriter(vdataRobot, 'normal')
        colorRobot = GeomVertexWriter(vdataRobot, 'color')

        # Ajouter les vertices, normales et couleurs du premier rectangle
        for i in range(8):
            vertexRobot.addData3f(verticesRect[i])
            normalRobot.addData3f(normalsRobot[i])
            colorRobot.addData4f(colors[i])

        # Créer le GeomTriangles pour le premier rectangle
        trianglesRobot = GeomTriangles(Geom.UHStatic)

        # Ajouter les triangles du premier rectangle
        for i in range(12):
            trianglesRobot.addVertices(*indicesRobot[i])
            trianglesRobot.closePrimitive()

        # Créer le Geom pour le premier rectangle
        geomRobot = Geom(vdataRobot)
        geomRobot.addPrimitive(trianglesRobot)

        # Créer le GeomNode pour le premier rectangle
        nodeRobot = GeomNode('Robot')
        nodeRobot.addGeom(geomRobot)
        
        robotShape = BulletBoxShape(Vec3(0.5, 0.5, 0.5))
        nodeRobot_phys = BulletRigidBodyNode('Robot_Physics')
        nodeRobot_phys.setMass(1.0)
        nodeRobot_phys.addShape(robotShape)
        Robot_phys_pos = self.render.attachNewNode(nodeRobot_phys)
        Robot_phys_pos.setPos(2,2,2)
        world.attachRigidBody(nodeRobot_phys)
        
        
        
        # Créer le NodePath et ajouter le GeomNode et le relie a sa physique
        Robot_pos = self.render.attachNewNode(nodeRobot)
        Robot_pos.setPos(2,2,2)
        Robot_pos.setTwoSided(True)
        Robot_pos.setColor(0,0,1,1)
        Robot_pos.reparentTo(Robot_phys_pos)


        

        # Créer le GeomVertexData pour le deuxième rectangle
        vdataPlat = GeomVertexData('verticesPlat', format, Geom.UHStatic)

        # Créer les writers pour le deuxième rectangle
        vertexPlat = GeomVertexWriter(vdataPlat, 'vertex')
        normalPlat = GeomVertexWriter(vdataPlat, 'normal')
        colorPlat = GeomVertexWriter(vdataPlat, 'color')

        # Ajouter les vertices, normales et couleurs du deuxième rectangle
        for i in range(4):
            vertexPlat.addData3f(verticesPlat[i])
            normalPlat.addData3f(normalsPlat[i])
            colorPlat.addData4f(colors[i])

        trianglesPlat = GeomTriangles(Geom.UHStatic)


        for i in range(2):
            trianglesPlat.addVertices(*indicesPlat[i])
            trianglesPlat.closePrimitive()

        geomPlat = Geom(vdataPlat)
        geomPlat.addPrimitive(trianglesPlat)

        nodePlat = GeomNode('Platefrome')
        nodePlat.addGeom(geomPlat)

        # Créer le NodePath pour le premier rectangle et l'attacher à la scène
        platPos = self.render.attachNewNode(nodePlat)
        platPos.setPos(0,0,0)
        platPos.setTwoSided(True)
        platPos.setColor(1, 0, 1, 1)
        
        
        platShape = BulletPlaneShape(Vec3(0, 0, 1), 1)
        nodePlat_phys = BulletRigidBodyNode('Ground')
        nodePlat_phys.addShape(platShape)
        plat_phys_pos = self.render.attachNewNode(nodePlat_phys)
        plat_phys_pos.setPos(0, 3, 0)
        world.attachRigidBody(nodePlat_phys)



        platPos.reparentTo(plat_phys_pos)
        # Déplacer la caméra pour qu'elle pointe vers le rectangle 3D
        
        base.disableMouse()
        base.camera.setPos(0,30,10)
        base.camera.setHpr(60)
        base.camera.lookAt(Robot_pos)
        #base.camLens.setFov(40)

        # Update
        def update(task):
            dt = globalClock.getDt()
            world.doPhysics(dt)
            return task.cont

        self.taskMgr.add(update, 'update')
        

        
            
app=VueRobot()
app.run()