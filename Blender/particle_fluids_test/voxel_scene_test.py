import unittest
import CrystalPLI
from scene.triangle_mesh_scene import *
from space.voxel_scene import *

class VoxelSceneTest(unittest.TestCase):
    def test_create_voxel(self):
        scene = Scene(World())
        voxel = VoxelScene(scene)
        resolution = [2,2,2]
        bb = Box3dd()
        voxel.create_voxel("", resolution,bb)
        self.assertEqual(1, voxel.id)
        data = voxel.get_values()
        print(data.bb.min.x)
        print(len(data.values))

    def test_set_values(self):
        scene = Scene(World())
        voxel = VoxelScene(scene)
        voxel.create_empty_voxel("")
        data = GridData()
        data.bb = Box3dd()
        data.res = [1,1,1]
        data.values = [False]
        voxel.set_values(data)

    def test_voxelizer(self):
        scene = Scene(World())
        mesh = TriangleMeshScene(scene)
        mesh.create(Triangle3ddVector(), "")
        voxel = VoxelScene(scene)
        voxel.create_empty_voxel("")
        voxelizer = Voxelizer(scene)
        voxelizer.voxelize(mesh.id, voxel.id, 1.0)
