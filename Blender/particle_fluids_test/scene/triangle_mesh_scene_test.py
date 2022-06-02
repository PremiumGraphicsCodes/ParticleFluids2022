import unittest
import CrystalPLI
from scene.triangle_mesh_scene import *

class TriangleMeshSceneTest(unittest.TestCase) :
    def test_create_triangle_mesh_scene(self):
        scene = Scene(World())
        mesh = TriangleMeshScene(scene)

        v0 = Vector3dd(0.0, 0.0, 0.0)
        v1 = Vector3dd(1.0, 0.0, 0.0)
        v2 = Vector3dd(1.0, 1.0, 0.0)
        triangles = Triangle3ddVector()
        triangles.add(Triangle3dd(v0, v1, v2))
        mesh.create(triangles, "test")
        self.assertEqual(1, mesh.id)

        triangles = mesh.get_triangles()
        self.assertEqual(1, (len(triangles.values)))

    def test_create_empty(self):
        scene = Scene(World())
        mesh = TriangleMeshScene(scene)
        mesh.create_empty("")
        self.assertEqual(1, mesh.id)

    def test_set_triangles(self):
        scene = Scene(World())
        mesh = TriangleMeshScene(scene)
        mesh.create_empty("")
        v0 = Vector3dd(0.0, 0.0, 0.0)
        v1 = Vector3dd(1.0, 0.0, 0.0)
        v2 = Vector3dd(1.0, 1.0, 0.0)
        triangles = Triangle3ddVector()
        triangles.add(Triangle3dd(v0, v1, v2))
        mesh.set_triangles(triangles)

    def test_export_stl(self):
        scene = Scene(World())
        mesh = TriangleMeshScene(scene)
        mesh.create_empty("")
        v0 = Vector3dd(0.0, 0.0, 0.0)
        v1 = Vector3dd(1.0, 0.0, 0.0)
        v2 = Vector3dd(1.0, 1.0, 0.0)
        triangles = Triangle3ddVector()
        triangles.add(Triangle3dd(v0, v1, v2))
        mesh.set_triangles(triangles)
        mesh.export_stl("test_export.stl")

    def test_import_stl(self):
        scene = Scene(World())
        mesh = TriangleMeshScene(scene)
        mesh.create_empty("")
        mesh.import_stl("test1.stl")
        triangles = mesh.get_triangles()
        print("num of triangles")
        print(len(triangles.values))