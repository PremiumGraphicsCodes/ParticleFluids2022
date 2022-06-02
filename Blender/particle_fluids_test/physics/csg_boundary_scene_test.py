import unittest
from physics.csg_boundary_scene import *

class CSGBoundarySceneTest(unittest.TestCase):
    def test_create(self):
        world = World()
        scene = Scene(world)
        boundary = CSGBoundaryScene(scene)
        boundary.create()
        boundary.send()
        boundary.delete()

if __name__ == '__main__':
    unittest.main()

