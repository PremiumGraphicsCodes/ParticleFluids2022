import unittest
import CrystalPLI
from scene.polygon_mesh_scene import *

class PolygonMeshSceneTest(unittest.TestCase) :
    def test_create_empty_polygon_mesh_scene(self):
        scene = Scene(World())
        mesh = PolygonMeshScene(scene)
        mesh.create_empty_polygon_mesh_scene("",1)
        self.assertEqual(1, mesh.id)

    def test_create_polygon_mesh_scene(self):
        scene = Scene(World())
        mesh = PolygonMeshScene(scene)
        positions = Vector3ddVector()
        normals = Vector3ddVector()
        texcoords = []
        mesh.create_polygon_mesh_scene("", positions, normals, texcoords, 1)
        self.assertEqual(1, mesh.id)

    def test_import_obj(self):
        scene = Scene(World())
        mesh = PolygonMeshScene(scene)
        mesh.import_obj_file("test_read.obj")