import CrystalPLI
from scene import *
from physics_command import *

world = World()
scene = Scene(world)
physics = SolverScene(scene)
newId = physics.create()
print(newId)