import unittest
from scene.particle_system_scene import *
from scene.triangle_mesh_scene import *
from physics.surface_builder import *

class SurfaceBuilderTest(unittest.TestCase):
    def test_build(self):
        scene = Scene(World())

        particle_system = ParticleSystemScene(scene)
        particle_system.create_empty("")

        triangle_mesh = TriangleMeshScene(scene)
        triangle_mesh.create_empty("")

        builder = SurfaceBuilder(scene)
        builder.build_isotorpic(particle_system.id, triangle_mesh.id, 1.0, 1.0)

    #def test_build_mvp(self):
    #    scene = Scene(World())

    #    volume_particle_system = ParticleSystemScene(scene)
    #    volume_particle_system.create_empty("")

    #    mass_particle_system = ParticleSystemScene(scene)
    #    mass_particle_system.create_empty("")

    #    triangle_mesh = TriangleMeshScene(scene)
    #    triangle_mesh.create_empty("")

    #    builder = SurfaceBuilder(scene)
    #    builder.build_mvp_surface(volume_particle_system.id, mass_particle_system.id, triangle_mesh.id, 1.0, 1.0)


if __name__ == '__main__':
    unittest.main()
