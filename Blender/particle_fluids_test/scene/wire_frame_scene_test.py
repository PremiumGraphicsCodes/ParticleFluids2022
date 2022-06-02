import unittest
import CrystalPLI
from scene.wire_frame_scene import *
from scene.scene import *

class WireFrameSceneTest(unittest.TestCase):
    def test_create_wire_frame_scene(self):
        scene = Scene(World())
        color = ColorRGBAf()
        wire_frame = WireFrameScene(scene)
        wire_frame.create_empty_wire_frame_scene("", 1.0,color,1)
        self.assertEqual(1, wire_frame.id)
