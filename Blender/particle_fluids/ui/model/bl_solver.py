# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
import os

from physics.solver_scene import SolverScene
from ui.model.bl_fluid import BLFluid
from ui.model.bl_boundary import BLBoundary
from ui.model.bl_triangle_mesh import BLTriangleMesh
from physics.volume_scene import VolumeScene
from physics.surface_builder import SurfaceBuilder
from scene.triangle_mesh_scene import TriangleMeshScene
from CrystalPLI import Vector3df
from scene.file_io import FileIO
import threading

class BLSolver :
    def __init__(self) :
        self.__solver = None
        self.__running = False
        self.__bl_fluids = []
        self.__bl_emitters = []
        self.__bl_boundaries = []
        self.__external_force = Vector3df(0.0, 0.0, -9.8)
        self.__buoyancy = Vector3df(0.0, 0.0, 0.1)
        self.__time_step = 0.01
        self.__export_dir_path = "tmp_txt"
        self.__iteration = 1
        self.__current_frame = 0
        self.__volume = 0

    def get_current_frame(self) :
        return self.__current_frame

    def build(self, scene):
        if self.__solver != None :
            return

        self.__solver = SolverScene(scene)
        self.__solver.create()
        self.__volume = VolumeScene(scene)
        self.__volume.create()
        self.volBuilder = SurfaceBuilder(scene)
        
    def add_fluid(self, bl_fluid) :
        self.__bl_fluids.append(bl_fluid)

    def add_emitter(self, bl_emitter) :
        self.__bl_emitters.append(bl_emitter)

    def add_boundary(self, bl_boundary) :
        self.__bl_boundaries.append(bl_boundary)

    def set_export_path(self, dir_path) :
        self.__export_dir_path = dir_path

    def set_effect_length(self, effect_radius) :
        self.__solver.effect_length = effect_radius

    def set_external_force(self, f) :
        self.__external_force = Vector3df( f[0], f[1], f[2] )

    def set_buoyancy(self, b) :
        self.__buoyancy = Vector3df( b[0], b[1], b[2] )

    def send(self) :
        fluids = []
        for bl_fluid in self.__bl_fluids :
            fluids.append( bl_fluid.get_fluid() )
        self.__solver.fluids = fluids

        emitters = []
        for bl_emitter in self.__bl_emitters :
            emitters.append( bl_emitter.get_emitter() )
        self.__solver.emitters = emitters

        boundaries = []
        for bl_boundary in self.__bl_boundaries :
            boundaries.append( bl_boundary.get_boundary() )
        self.__solver.boundaries = boundaries

        self.__solver.external_force = self.__external_force
        self.__solver.buoyancy = self.__buoyancy
        self.__solver.time_step = self.__time_step
        self.__solver.send()

    def start(self):
        self.__current_frame = self.start_frame
        self.__running = True
        thread = threading.Thread(target=self.run)
        thread.start()

    def pause(self):
        self.__running = False

    def resume(self):
        thread = threading.Thread(target=self.run)
        thread.start()
        self.__running = True

    def stop(self):
        self.__running = False
        self.__current_frame = 0

    def set_start_frame(self, frame) :
        self.start_frame = frame

    def set_end_frame(self, frame):
        self.end_frame = frame

    def set_iteration(self, iter) :
        self.__iteration = iter

    def run(self) :
        for i in range(self.__current_frame, self.end_frame) :
            if(self.__running) :
                print("runnning frame" + str(i))
                self.step(i)
                self.__current_frame = i

    def step(self, frame):
        for i in range(0, self.__iteration) :
            self.__solver.simulate()

        for fluid in self.__bl_fluids :
            fluid.send_shader()

        for emitter in self.__bl_emitters :
            emitter.send_shader()

        dir_path = bpy.path.abspath(self.__export_dir_path)
        
        macro_file_path = os.path.join(dir_path, "macro" + str(frame) + ".ply")
        self.__solver.export_pcd(macro_file_path, True)

        #for fluid in self.__bl_fluids :
        #    self.volBuilder.build_isotorpic(fluid.get_fluid().id, self.__volume.id, 1.0, 0.5)
        #volume_file_path = os.path.join(dir_path, "volume" + str(frame) + ".ply")
        #self.__volume.export(volume_file_path)

    def is_running(self):
        return self.__running

    def reset(self):
#        for bl_fluid in self.__bl_fluids :
#            bl_fluid.reset()
        self.__bl_fluids.clear()
        self.__bl_emitters.clear()
        self.__bl_boundaries.clear()

    def render(self, point_shader):
        for bl_fluid in self.__bl_fluids :
            bl_fluid.render(point_shader)
        for bl_emitter in self.__bl_emitters :
            bl_emitter.render(point_shader)
        for bl_boundary in self.__bl_boundaries :
            bl_boundary.render()
