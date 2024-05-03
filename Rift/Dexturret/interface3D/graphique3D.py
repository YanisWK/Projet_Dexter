from direct.showbase.ShowBase import ShowBase
from panda3d.core import Geom, GeomTriangles, GeomVertexWriter, GeomVertexFormat, GeomVertexData, GeomNode

class VueRobot(ShowBase):
    def __init__(self):
        super().__init__()

        # Coordonnées des sommets du premier rectangle 3D
        vertices1 = [
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
        vertices2 = [
            (-10, -10, -1),  # sommet 0
            (10, -10, -1),   # sommet 1
            (10, 10, -1),    # sommet 2
            (-10, 10, -1),   # sommet 3
        ]

        # Normales des sommets des rectangles 3D
        normals = [
            (-1, -1, -1),  # normal du sommet 0
            (1, -1, -1),   # normal du sommet 1
            (1, 1, -1),    # normal du sommet 2
            (-1, 1, -1),   # normal du sommet 3
            (-1, -1, 1),   # normal du sommet 4
            (1, -1, 1),    # normal du sommet 5
            (1, 1, 1),     # normal du sommet 6
            (-1, 1, 1),    # normal du sommet 7
        ]

        normals2 = [
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
        indices1 = [
            (0, 1, 2), (0, 2, 3),  # face avant
            (4, 5, 6), (4, 6, 7),  # face arrière
            (0, 1, 5), (0, 5, 4),  # face bas
            (2, 3, 7), (2, 7, 6),  # face haut
            (0, 3, 7), (0, 7, 4),  # face gauche
            (1, 2, 6), (1, 6, 5),  # face droite
        ]

        # Indices des triangles du deuxième rectangle 3D
        indices2 = [
            (0, 1, 2), (0, 2, 3),  # face avant
        ]

        # Créer le format des vertices
        format = GeomVertexFormat.getV3n3c4()  # 3D vertices, normals, and colors

        # Créer le GeomVertexData pour le premier rectangle
        vdata1 = GeomVertexData('vertices1', format, Geom.UHStatic)

        # Créer les writers pour le premier rectangle
        vertex1 = GeomVertexWriter(vdata1, 'vertex')
        normal1 = GeomVertexWriter(vdata1, 'normal')
        color1 = GeomVertexWriter(vdata1, 'color')

        # Ajouter les vertices, normales et couleurs du premier rectangle
        for i in range(8):
            vertex1.addData3f(vertices1[i])
            normal1.addData3f(normals[i])
            color1.addData4f(colors[i])

        # Créer le GeomTriangles pour le premier rectangle
        triangles1 = GeomTriangles(Geom.UHStatic)

        # Ajouter les triangles du premier rectangle
        for i in range(12):
            triangles1.addVertices(*indices1[i])
            triangles1.closePrimitive()

        # Créer le Geom pour le premier rectangle
        geom1 = Geom(vdata1)
        geom1.addPrimitive(triangles1)

        # Créer le GeomNode pour le premier rectangle
        node1 = GeomNode('rectangle1')
        node1.addGeom(geom1)

        # Créer le NodePath pour le premier rectangle et l'attacher à la scène
        rectangle1_node = self.render.attachNewNode(node1)
        rectangle1_node.setTwoSided(True)
        rectangle1_node.setColor(0, 0, 1, 1)

        # Créer le GeomVertexData pour le deuxième rectangle
        vdata2 = GeomVertexData('vertices2', format, Geom.UHStatic)

        # Créer les writers pour le deuxième rectangle
        vertex2 = GeomVertexWriter(vdata2, 'vertex')
        normal2 = GeomVertexWriter(vdata2, 'normal')
        color2 = GeomVertexWriter(vdata2, 'color')

        # Ajouter les vertices, normales et couleurs du deuxième rectangle
        for i in range(4):
            vertex2.addData3f(vertices2[i])
            normal2.addData3f(normals2[i])
            color2.addData4f(colors[i])

        triangles2 = GeomTriangles(Geom.UHStatic)
        # Ajouter les triangles du premier rectangle
        for i in range(2):
            triangles2.addVertices(*indices2[i])
            triangles2.closePrimitive()
         # Créer le Geom pour le premier rectangle
        geom2 = Geom(vdata2)
        geom2.addPrimitive(triangles2)

        # Créer le GeomNode pour le premier rectangle
        node2 = GeomNode('rectangle2')
        node2.addGeom(geom2)

        # Créer le NodePath pour le premier rectangle et l'attacher à la scène
        rectangle2_node = self.render.attachNewNode(node2)
        rectangle2_node.setTwoSided(True)
        rectangle2_node.setColor(1, 0, 1, 1)
        
        # Déplacer la caméra pour qu'elle pointe vers le rectangle 3D
        self.camera.lookAt(rectangle1_node)

        
            
app=VueRobot()
app.run()