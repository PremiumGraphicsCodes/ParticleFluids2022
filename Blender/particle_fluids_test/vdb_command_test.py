import CrystalPLI
import unittest
import os
import scene_labels
import space_labels
import physics_labels
import vdb_command
import vdb_command_test

from vdb_command import *
from CrystalPLI import *


class VDBCommandTest(unittest.TestCase):
    def setUp(self):
        world = World()
        scene = Scene(world)
        self.vdb = VDBCommand(scene)
        self.vdb.init()

    def test_create_vdb_points(self):
        newId = self.vdb.create_vdb_empty_points("test_vdb_points")
        self.assertEqual(1, newId)

        p = Vector3ddVector()
        p.add(Vector3dd(1.0, 2.0, 3.0))
        p.add(Vector3dd(4.0, 5.0, 6.0))
        newId = self.vdb.create_vdb_points(p, "test_vdb_points_2")
        self.assertEqual(2, newId)

    def test_create_vdb_mesh(self):
        newId = self.vdb.create_vdb_mesh("test_vdb_mesh")
        self.assertEqual(1, newId)

    def test_create_vdb_volume(self):
        newId = self.vdb.create_vdb_volume("test_vdb_volume")
        self.assertEqual(1, newId)

    def test_read_vdb_file(self):
        newIds = self.vdb.read_vdb_file("./source_river.vdb")
        self.assertEqual([1], newIds)
#        print(newIds)
        self.vdb.write_vdb_file("test_write.vdb", newIds, [])
#        self.assertEqual(1, newId)

    def test_read_obj_file(self):
        newId = self.vdb.read_obj_file("./quad.obj")
        self.assertEqual(1, newId)
        self.vdb.write_obj_file(newId, "./test_write.obj")

    def test_convert_ps_to_volume(self):
        ps_id = self.vdb.create_vdb_empty_points("")
        volume_id = self.vdb.create_vdb_volume("")
        self.vdb.convert_ps_to_volume(ps_id, volume_id, 1.0)

if __name__ == '__main__':
    unittest.main()
