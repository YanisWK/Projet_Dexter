import direct.directbase.DirectStart
from panda3d.core import Vec3
from panda3d.bullet import BulletWorld
from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletBoxShape
from panda3d.bullet import ZUp
from panda3d.bullet import BulletCylinderShape





# World
world = BulletWorld()
world.setGravity(Vec3(0, 0, -9.81))


base.cam.setPos(0, -10, 0)
base.cam.lookAt(0, 0, 0)





# Plane
shape = BulletPlaneShape(Vec3(0, 0, 1), 1)
node = BulletRigidBodyNode('Ground')
node.addShape(shape)
np = render.attachNewNode(node)
np.setPos(0, 0, -2)
world.attachRigidBody(node)



# radius = 0.4
# height = 2.4
# shape1 = BulletCylinderShape(radius, height, ZUp)
# shape2 = BulletCylinderShape(Vec3(radius, 0, 0.5 * height), ZUp)
# node = BulletRigidBodyNode('Cylinder')
# node.setMass(1.0)
# node.addShape(shape1)
# node.addShape(shape2)
# np = render.attachNewNode(node)
# np.setPos(0, 0, 8)
# world.attachRigidBody(node)




# Box
shape = BulletBoxShape(Vec3(0.5, 0.5, 0.5))
node = BulletRigidBodyNode('Box')
node.setMass(1.0)
node.addShape(shape)
np = render.attachNewNode(node)
np.setPos(0, 0, 2)
world.attachRigidBody(node)
model = loader.loadModel('models/box.egg')
model.flattenLight()
model.reparentTo(np)

# Update
def update(task):
    dt = globalClock.getDt()
    world.doPhysics(dt)
    return task.cont

taskMgr.add(update, 'update')
base.run()