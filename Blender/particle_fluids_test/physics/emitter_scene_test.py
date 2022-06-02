import unittest
from physics.emitter_scene import EmitterScene
import CrystalPLI
from scene.particle_system_scene import *

class EmitterSceneTest(unittest.TestCase):
    def __create_test_particle_system(self, scene) :
        positions = Vector3ddVector()
        positions.add(Vector3dd(1.0, 2.0, 3.0))
        positions.add(Vector3dd(4.0, 5.0, 6.0))
        color = ColorRGBAf()
        particle_system = ParticleSystemScene(scene)
        particle_system.create(positions, "", 1.0, color)
        return particle_system

    def test_create(self):
        world = World()
        scene = Scene(world)
        fluid = EmitterScene(scene)
        fluid.create()
        ps = self.__create_test_particle_system(scene)
        fluid.source_particle_system_id = ps.id
        fluid.send()
        p = fluid.get_positions()
        #print( p.values[0].x )
        
