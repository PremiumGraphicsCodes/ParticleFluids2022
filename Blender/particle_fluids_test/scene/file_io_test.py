import unittest
from CrystalPLI import * #World, Vector3dd, Vector3ddVector
from scene.particle_system_scene import ParticleSystemScene
from scene.file_io import FileIO
#from scene.wire_frame_scene import *
from scene.scene import Scene

class FileIOTest(unittest.TestCase):
    def test_export_txt(self) :
        scene = Scene(World())
        ps = self.__create_test_particle_system(scene)
        ids = []
        ids.append(ps.id)
        FileIO.export_txt(scene, ids, "TXTExportTest.txt")

    def test_import_txt(self) :
        scene = Scene(World())
        ps = ParticleSystemScene(scene)
        ps.create_empty("")
        FileIO.import_txt(scene, ps.id, "TXTExportTest.txt")

    def test_import_pcd(self):
        scene = Scene(World())
        ps = ParticleSystemScene(scene)
        ps.create_empty("")
        #FileIO.import_pcd(scene, ps.id, "macro2.pcd")
        FileIO.import_pcd(scene, ps.id, "PCDBinaryFile.pcd")

    def __create_test_particle_system(self, scene) :
        positions = Vector3ddVector()
        positions.add(Vector3dd(1.0, 2.0, 3.0))
        positions.add(Vector3dd(4.0, 5.0, 6.0))
        color = ColorRGBAf()
        particle_system = ParticleSystemScene(scene)
        particle_system.create(positions, "", 1.0, color)
        return particle_system
