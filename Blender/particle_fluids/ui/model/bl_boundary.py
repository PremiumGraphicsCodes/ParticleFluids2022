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
import bmesh
from CrystalPLI import Vector3dd, Vector3ddVector, Box3dd
from physics.csg_boundary_scene import CSGBoundaryScene
import gpu
from gpu_extras.batch import batch_for_shader
from CrystalPLI import World
from scene.scene import Scene


def get_position(box, u, v, w) :
    lx = box.max.x - box.min.x
    ly = box.max.y - box.min.y
    lz = box.max.z - box.min.z
    x = lx * u + box.min.x
    y = ly * v + box.min.y
    z = lz * w + box.min.z
    return Vector3dd(x,y,z)

class BLBoundary :
    def __init__(self, scene) :
        self.__boundary = None

    def build(self, scene) :
        self.__boundary = CSGBoundaryScene(scene)
        self.__boundary.create()
        self.__boundary.bounding_box = Box3dd(Vector3dd(0,0,0), Vector3dd(10,10,10))
        self.__boundary.send()

    def set_box(self, box) :
        self.__boundary.bounding_box = box

    def get_boundary(self) :
        return self.__boundary

    def send(self) :
        self.__boundary.send()

    def render(self):
        shader = gpu.shader.from_builtin('3D_UNIFORM_COLOR')
        shader.bind()
        shader.uniform_float("color", (1, 1, 0, 1))

        box = self.__boundary.bounding_box

        positions = Vector3ddVector()
        positions.add(get_position(box, 0.0, 0.0, 0.0))
        positions.add(get_position(box, 1.0, 0.0, 0.0))
        positions.add(get_position(box, 1.0, 1.0, 0.0))
        positions.add(get_position(box, 0.0, 1.0, 0.0))
        positions.add(get_position(box, 0.0, 0.0, 1.0))
        positions.add(get_position(box, 1.0, 0.0, 1.0))
        positions.add(get_position(box, 1.0, 1.0, 1.0))
        positions.add(get_position(box, 0.0, 1.0, 1.0))

        edges = []
        edges.append((0,1))
        edges.append((1,2))
        edges.append((2,3))
        edges.append((3,0))

        edges.append((4,5))
        edges.append((5,6))
        edges.append((6,7))
        edges.append((7,4))

        edges.append((0,4))
        edges.append((1,5))
        edges.append((2,6))
        edges.append((3,7))

        coords = []
        for p in positions.values :
            coords.append( (p.x, p.y, p.z))

        batch = batch_for_shader(shader, 'LINES', {"pos": coords}, indices=edges)
        batch.draw(shader)
