import unittest
from scene.particle_system_scene import *
from physics.fluid_scene import *
from physics.emitter_scene import EmitterScene
from physics.solver_scene import *
from physics.csg_boundary_scene import CSGBoundaryScene
from CrystalPLI import Vector3df

class SolverSceneTest(unittest.TestCase):
    def __create_test_particle_system(self, scene) :
        positions = Vector3ddVector()
        positions.add(Vector3dd(1.0, 2.0, 3.0))
        positions.add(Vector3dd(4.0, 5.0, 6.0))
        color = ColorRGBAf()
        particle_system = ParticleSystemScene(scene)
        particle_system.create(positions, "", 1.0, color)
        return particle_system

    def test(self):
        world = World()
        scene = Scene(world)
        solver = SolverScene(scene)
        solver.create()
        self.assertEqual(1, solver.id)

        #ps = ParticleSystemScene(scene)
        ps = self.__create_test_particle_system(scene)

        #ps.create_empty("")

        fluids = []
        fluid = FluidScene(scene)
        fluid.create()
        fluid.source_particle_system_id = ps.id
        fluid.send()
        fluids.append(fluid)

        ps2 = self.__create_test_particle_system(scene)

        emitters = []
        emitter = EmitterScene(scene)
        emitter.create()
        emitter.source_particle_system_id = ps2.id
        emitter.send()
        emitters.append(emitter)

        boundaries = []
        boundary = CSGBoundaryScene(scene)
        boundary.create()
        boundary.send()
        boundaries.append(boundary)

        solver.fluids = fluids
        solver.emitters = emitters
        solver.boundaries = boundaries
        solver.external_force = Vector3df(0.0, 0.0, -9.8)
        solver.send()
        solver.simulate()

        solver.export_pcd("export_macro.pcd", False)
        solver.export_pcd("export_micro.pcd", True)
