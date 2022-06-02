import unittest
from scene.particle_system_scene import *
from scene.triangle_mesh_scene import *
from physics.volume_scene import *

class VolumeSceneTest(unittest.TestCase):
    def test_build(self):
        scene = Scene(World())

        volume = VolumeScene(scene)
        volume.create()

        volume.export("FluidVolumeTest.ply")