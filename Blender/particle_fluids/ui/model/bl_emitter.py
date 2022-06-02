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
import gpu

from physics.emitter_scene import EmitterScene
from scene.particle_system_scene import ParticleSystemScene
from CrystalPLI import Vector3dd, Vector3ddVector
from bpy.props import FloatProperty, FloatVectorProperty
from gpu_extras.batch import batch_for_shader

from CrystalPLI import World
from scene.scene import Scene

class BLEmitter :
    def __init__(self, scene):
        self.__source_ps = None
        self.__emitter = None
        self.__coords = []
        self.__colors = []

    def get_emitter(self):
        return self.__emitter

    def clear(self) :
        del self.__shader

    def build(self, scene) :
        self.__emitter = EmitterScene(scene)
        self.__source_ps = ParticleSystemScene(scene)
        self.__source_ps.create_empty("")

        self.__emitter.create()
        self.__emitter.set_source_ps_id( self.__source_ps.id )
        self.__emitter.send()

    def convert_from_polygon_mesh(self, obj) :
        mesh = obj.to_mesh()
        matrix_world = obj.matrix_world
        print('---matrix_world---')
        print(matrix_world)

        positions = Vector3ddVector()
        print("num of vertices:", len(mesh.vertices))
        for vt in mesh.vertices:
#            print("vertex index:{0:2} co:{1} normal:{2}".format(vt.index, vt.co, vt.normal))
            vvv = matrix_world @ vt.co
            p = Vector3dd(vvv[0], vvv[1], vvv[2])
            positions.add(p)
        self.__source_ps.set_positions(positions)
        self.__emitter.send()
#        self.me = mesh

    def send_shader(self):
        positions = self.__emitter.get_positions()
        self.__coords = []
        self.__colors = []
        for p in positions.values :
            self.__coords.append( (p.x, p.y, p.z))
            self.__colors.append( (1.0, 1.0, 1.0, 1.0))
        
    def render(self, shader):
        batch = batch_for_shader(shader, 'POINTS', {"pos" : self.__coords, "color" : self.__colors})

        shader.bind()
        matrix = bpy.context.region_data.perspective_matrix
        shader.uniform_float("MVPMatrix", matrix)#        shader.uniform_float("color", color)
        batch.draw(shader)

    def reset(self, prop):
        self.__emitter.set_particle_radius( prop.particle_radius_prop )
        self.__emitter.set_stiffness( prop.stiffness_prop )
        self.__emitter.set_viscosity( prop.viscosity_prop )
        self.__emitter.set_start_step( prop.start_step_prop )
        self.__emitter.set_end_step( prop.end_step_prop )
        self.__emitter.set_interval( prop.interval_prop )
        self.__emitter.set_initial_velocity( prop.initial_velocity_prop )
        self.__emitter.set_temperature( prop.temperature_prop )
        self.__emitter.set_heat_diffuse( prop.heat_diffuse_prop )
        self.__emitter.set_drag_force( prop.drag_force_prop )
        self.__emitter.set_drag_heat( prop.drag_heat_prop )
        self.__emitter.set_lifetime( prop.lifetime_prop )
        self.__emitter.send()